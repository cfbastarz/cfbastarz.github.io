"""Date archives and tag pages for the existing blog URLs (MkDocs 1.6+)."""
from collections import defaultdict
from datetime import date
from html import escape
from pathlib import PurePosixPath
import hashlib
import re

from mkdocs.plugins import event_priority
from mkdocs.structure.files import File
from mkdocs.structure.nav import Section
from mkdocs.utils.meta import get_data


def tag_path(tag):
    return 'blog/tags/' + hashlib.sha256(tag.encode()).hexdigest()[:16] + '.md'


def posts(files):
    result = []
    for file in files.documentation_pages():
        match = re.fullmatch(r'blog/(\d{4})/(\d{2})/(\d{2})/[^/]+\.md', file.src_uri)
        if not match:
            continue
        published = date(*map(int, match.groups()))
        body, meta = get_data(file.content_string)
        heading = re.search(r'^#\s+(.+)', body, re.M)
        title = str(meta.get('title') or (heading.group(1) if heading else PurePosixPath(file.src_uri).stem))
        tags = meta.get('tags', [])
        if not isinstance(tags, list) or any(not isinstance(tag, str) or not tag.strip() for tag in tags):
            raise ValueError(f'{file.src_uri}: tags must be a list of nonempty strings')
        result.append((published, title, file, sorted(set(tags))))
    return sorted(result, key=lambda post: (-post[0].toordinal(), post[1].casefold(), post[2].src_uri))


def link(title, target, source):
    import posixpath
    return '[' + escape(title).replace('[', '&#91;').replace(']', '&#93;') + '](<' + posixpath.relpath(target, posixpath.dirname(source)) + '>)'


def listing(items, source):
    return '\n'.join(f'- {published:%d/%m/%Y} — {link(title, file.src_uri, source)}' for published, title, file, tags in items)


def on_files(files, config):
    items = posts(files)
    by_tag = defaultdict(list)
    groups = defaultdict(list)
    for post in items:
        groups[post[0].year].append(post)
        for tag in post[3]:
            by_tag[tag].append(post)
    archive = '# Blog\n\nPosts organizados por ano, mês e dia.\n\n[Explorar tags](tags/index.md)\n'
    for year, entries in groups.items():
        archive += f'\n## {year}\n'
        months = defaultdict(list)
        for post in entries:
            months[post[0].month].append(post)
        for month, entries in months.items():
            archive += f'\n### {month:02d}/{year}\n\n' + listing(entries, 'blog/index.md') + '\n'
    generated = {'blog/index.md': archive}
    tags_index = '# Tags\n\n'
    for tag in sorted(by_tag, key=str.casefold):
        target = tag_path(tag)
        tags_index += f'- {link(tag, target, "blog/tags/index.md")} ({len(by_tag[tag])})\n'
        generated[target] = '# ' + escape(tag) + '\n\n' + listing(by_tag[tag], target) + '\n'
    generated['blog/tags/index.md'] = tags_index if by_tag else tags_index + 'Nenhuma tag publicada ainda.\n'
    for path, content in generated.items():
        if files.get_file_from_path(path):
            raise ValueError(f'Reserved generated blog page: {path}')
        files.append(File.generated(config, path, content=content))
    return files


@event_priority(-100)
def on_nav(nav, config, files):
    items = posts(files)
    years = {}
    for published, title, file, tags in items:
        months = years.setdefault(str(published.year), {})
        days = months.setdefault(f'{published.month:02d}', {})
        days.setdefault(f'{published.day:02d}', []).append(file.page)
    children = [files.get_file_from_path('blog/index.md').page,
                files.get_file_from_path('blog/tags/index.md').page]
    children += [Section(year, [Section(month, [Section(day, pages) for day, pages in days.items()])
                                for month, days in months.items()]) for year, months in years.items()]
    blog = Section('Blog', children)
    for index, item in enumerate(nav.items):
        if isinstance(item, Section) and any(page.file.src_uri.startswith('blog/') for page in nav.pages if is_descendant(page, item)):
            nav.items[index] = blog
            break
    else:
        nav.items.append(blog)
    def parents(section):
        for child in section.children:
            child.parent = section
            if isinstance(child, Section):
                parents(child)
    parents(blog)
    return nav


def is_descendant(page, section):
    parent = page.parent
    while parent:
        if parent is section:
            return True
        parent = parent.parent
    return False


def on_page_markdown(markdown, page, config, files):
    if re.fullmatch(r'blog/\d{4}/\d{2}/\d{2}/[^/]+\.md', page.file.src_uri):
        tags = page.meta.get('tags', [])
        if tags:
            markdown += '\n\nTags: ' + ' · '.join(link(tag, tag_path(tag), page.file.src_uri) for tag in tags) + '\n'
    return markdown
