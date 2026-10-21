import json,re
from pathlib import Path
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup
import yaml
r=Path(__file__).resolve().parents[1]; report=json.loads((r/'wordpress-migration.json').read_text()); site=(r/'site').resolve()
assert len(report['posts']) == report['published_posts']
assert len(list((r/'docs/assets/wordpress').rglob('*.*'))) == report['copied_media']
broken=[]; rendered=0; images=0
for p in report['posts']:
 src=r/'docs'/p['path']; raw=src.read_text(); meta=yaml.safe_load(raw.split('---',2)[1]); assert meta['wordpress_id']==p['id']; assert not re.search(r'WORDPRESS(?:BLOCK|PARAGRAPH)|\[(?:caption|gallery|sourcecode|youtube|audio)\b|\$latex',raw)
 target=site/Path(p['path']).with_suffix('')/'index.html'; assert target.exists(),target
 soup=BeautifulSoup(target.read_text(),'html.parser'); rendered+=1
 for tag in soup.select('[role=main] a[href], [role=main] img[src], [role=main] audio[src]'):
  href=tag.get('href',tag.get('src')); url=urlsplit(href)
  if tag.name=='img': images+=1
  if url.scheme or url.netloc or not url.path: continue
  dest=(target.parent/unquote(url.path)).resolve()
  if dest.is_dir(): dest=dest/'index.html'
  if not dest.exists():broken.append((p['id'],href))
print('Rendered posts:',rendered,'Images:',images,'Broken local links:',broken)
assert not broken
math=(site/'blog/2013/11/14/derivacao-da-equacao-de-analise-a-partir-da-funcao-custo-variacional-tridimensional-wp-2155/index.html').read_text();assert 'class="arithmatex"' in math
print('Math markup verified. All published post IDs, metadata, shortcode conversion and local links verified.')
