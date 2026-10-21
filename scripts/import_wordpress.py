"""Import published WXR posts and only referenced media. Run from repository root.

python scripts/import_wordpress.py EXPORT.xml MEDIA.tar
Dependencies: beautifulsoup4, markdownify, PyYAML
"""
import collections
import html
import json
import posixpath
from pathlib import Path, PurePosixPath
import re
import sys
import tarfile
from urllib.parse import urlsplit, unquote, parse_qs, quote
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify
import yaml

NS = {'wp': 'http://wordpress.org/export/1.2/', 'content': 'http://purl.org/rss/1.0/modules/content/'}

def field(item, name):
    return item.findtext(name, '', NS)

def main(xml_path, tar_path):
    items = ET.parse(xml_path).findall('./channel/item')
    published = [i for i in items if field(i, 'wp:post_type') == 'post' and field(i, 'wp:status') == 'publish']
    attachments = {field(i, 'wp:post_id'): i for i in items if field(i, 'wp:post_type') == 'attachment'}
    paths = {}
    urls = {}
    for item in published:
        stamp = field(item, 'wp:post_date')[:10]
        from datetime import date
        date.fromisoformat(stamp)
        slug = unquote(field(item, 'wp:post_name'))
        slug = re.sub(r'[^\w-]+', '-', slug).strip('-') or 'post'
        target = f'blog/{stamp.replace("-", "/")}/{slug}-wp-{field(item, "wp:post_id")}.md'
        paths[field(item, 'wp:post_id')] = target
        urls[unquote(urlsplit(field(item, 'link')).path).rstrip('/')] = target
    archive = tarfile.open(tar_path)
    members = {m.name: m for m in archive.getmembers() if m.isfile() and not m.issym() and '..' not in PurePosixPath(m.name).parts and not m.name.startswith('/')}
    used = set()
    missing = collections.defaultdict(set)
    external_media = collections.defaultdict(set)
    mapping = []
    for item in published:
        post_id = field(item, 'wp:post_id')
        source = paths[post_id]
        def local(url):
            url = html.unescape(url.strip())
            parsed = urlsplit(url)
            host = (parsed.hostname or '').lower()
            path = unquote(parsed.path)
            own = host in {'craftmind.wordpress.com', 'craftmind.files.wordpress.com', 'alephzero.wordpress.com', 'alephzero.files.wordpress.com'}
            if not own:
                return url
            media = None
            if '/wp-content/uploads/' in path:
                media = path.split('/wp-content/uploads/', 1)[1]
            elif '.files.wordpress.com' in host:
                media = path.lstrip('/')
            if media:
                candidate = media
                if candidate not in members:
                    candidate = re.sub(r'-\d+x\d+(?=\.[^.]+$)', '', media)
                if candidate in members:
                    used.add(candidate)
                    target = 'assets/wordpress/' + candidate
                    return quote(posixpath.relpath(target, posixpath.dirname(source)), safe='/.-_') + ('#' + parsed.fragment if parsed.fragment else '')
                missing[url].add(post_id)
                return url
            linked = urls.get(path.rstrip('/'))
            if not linked:
                linked = paths.get(parse_qs(parsed.query).get('p', [''])[0])
            if linked:
                return quote(posixpath.relpath(linked, posixpath.dirname(source)), safe='/.-_') + ('#' + parsed.fragment if parsed.fragment else '')
            return url
        body = field(item, 'content:encoded')
        protected = {}
        def protect(content, block=True):
            key = f'WORDPRESSBLOCK{len(protected)}TOKEN'
            protected[key] = content
            return '\n\n' + key + '\n\n' if block else key
        def code(match):
            language = re.search(r'language=["\']?([\w+-]+)', match.group(2))
            text = html.unescape(match.group(3)).strip('\n')
            fence = '`' * max(3, max([len(s) + 1 for s in re.findall(r'`+', text)] or [3]))
            return protect(f'{fence}{language.group(1) if language else ""}\n{text}\n{fence}')
        body = re.sub(r'\[(sourcecode|code)([^\]]*)\](.*?)\[/\1\]', code, body, flags=re.S|re.I)
        body = re.sub(r'\$latex\s+(.*?)\$', lambda m: protect('$' + html.unescape(m.group(1)).strip() + '$', block=False), body, flags=re.S)
        def caption(match):
            attr, inner = match.groups()
            legacy = re.search(r'\bcaption="([^"]*)"', attr)
            if legacy:
                inner += '<p><em>' + html.escape(html.unescape(legacy.group(1))) + '</em></p>'
            return '\n\n' + inner + '\n\n'
        body = re.sub(r'\[caption([^\]]*)\](.*?)\[/caption\]', caption, body, flags=re.S|re.I)
        def gallery(match):
            ids = re.search(r'ids="([\d,]+)"', match.group(1))
            if not ids:
                raise ValueError('Gallery without explicit IDs')
            output = []
            for aid in ids.group(1).split(','):
                attachment = attachments[aid]
                url = field(attachment, 'wp:attachment_url')
                output.append('<p><img src="' + html.escape(url, quote=True) + '" alt="' + html.escape(field(attachment, 'title'), quote=True) + '"></p>')
                caption_text = field(attachment, 'content:encoded')
                if caption_text: output.append('<p>' + caption_text + '</p>')
            return '\n'.join(output)
        body = re.sub(r'\[gallery([^\]]*)\]', gallery, body)
        def youtube(match):
            url = html.unescape(match.group(1)).strip()
            return '<p><a href="' + html.escape(url, quote=True) + '">Assistir ao vídeo no YouTube</a></p>'
        body = re.sub(r'\[youtube(?:=|\s+)([^\]]+)\]', youtube, body, flags=re.I)
        def audio(match):
            url = match.group(1).strip()
            src = local(url)
            if urlsplit(src).scheme: external_media[url].add(post_id)
            return protect('<audio controls preload="none" src="' + html.escape(src, quote=True) + '"></audio>\n\n[Ouvir / baixar áudio](<' + src + '>)')
        body = re.sub(r'\[audio\s+([^\]]+)\]', audio, body, flags=re.I)
        body = re.sub(r'\[soundcloud\s+url="([^"]+)"[^\]]*\]', lambda m: '<p><a href="' + html.escape(html.unescape(m.group(1)),quote=True) + '">Ouvir no SoundCloud</a></p>', body, flags=re.S|re.I)
        soup = BeautifulSoup(body, 'html.parser')
        for pre in soup.find_all('pre'):
            # WordPress code blocks are literal, including shell commands and brackets.
            token = protect('```\n' + pre.get_text().strip('\n') + '\n```')
            pre.replace_with(token)
        for node in soup.find_all(['script', 'style']): node.decompose()
        for node in soup.find_all(True):
            for attr in list(node.attrs):
                if attr.lower().startswith('on'): del node[attr]
            for attr in ['src', 'href']:
                if node.get(attr):
                    original = node[attr]
                    node[attr] = local(original)
                    if node.name == 'img' and attr == 'src' and urlsplit(node[attr]).scheme:
                        external_media[original].add(post_id)
            if node.has_attr('srcset'): del node['srcset']
        for text_node in list(soup.find_all(string=True)):
            if '\n\n' in str(text_node):
                text_node.replace_with(NavigableString(re.sub(r'\n[ \t]*\n+', 'WORDPRESSPARAGRAPHTOKEN', str(text_node))))
        converted = markdownify(str(soup), heading_style='ATX', bullets='-', escape_underscores=False, escape_asterisks=False)
        converted = converted.replace('WORDPRESSPARAGRAPHTOKEN', '\n\n')
        for key, value in protected.items(): converted = converted.replace(key, value)
        converted = re.sub(r'^\$([^$\n]+)\$[ \t]*$', lambda m: '\n\n$$\n' + m.group(1) + '\n$$\n\n', converted, flags=re.M)
        categories = sorted({c.text for c in item.findall('category') if c.get('domain') == 'category'})
        tags = sorted({c.text for c in item.findall('category') if c.get('domain') == 'post_tag'} | set(categories))
        meta = {'title': html.unescape(field(item, 'title')), 'date': field(item, 'wp:post_date'), 'tags': tags, 'categories': categories, 'wordpress_id': int(post_id), 'original_url': field(item, 'link')}
        dest = Path('docs') / source
        dest.parent.mkdir(parents=True, exist_ok=True)
        output = '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n# ' + html.escape(meta['title']) + '\n\n' + converted.strip() + '\n'
        if dest.exists() and dest.read_text() != output:
            raise ValueError(f'Refusing to overwrite changed post: {dest}')
        dest.write_text(output)
        mapping.append({'id': int(post_id), 'title': meta['title'], 'original_url': meta['original_url'], 'path': source})
    for name in sorted(used):
        dest = Path('docs/assets/wordpress') / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(archive.extractfile(members[name]).read())
    report = {'published_posts': len(published), 'draft_posts_excluded': sum(field(i, 'wp:post_type')=='post' and field(i, 'wp:status')=='draft' for i in items), 'copied_media': len(used), 'copied_bytes': sum(members[n].size for n in used), 'missing_export_media': {k: sorted(v) for k,v in sorted(missing.items())}, 'external_media': {k:sorted(v) for k,v in sorted(external_media.items())}, 'posts': mapping}
    Path('wordpress-migration.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'posts','missing_export_media','external_media'}},indent=2))
    print('Missing export media:',len(missing),'External media:',len(external_media))

if __name__ == '__main__':
    main(*sys.argv[1:])
