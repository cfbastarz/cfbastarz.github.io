"""Render a local PDF for the presentation viewer.
Usage: python scripts/prepare_presentation.py path/to/talk.pdf
Requires Poppler (pdfinfo, pdftoppm, pdftotext) and Pillow.
"""
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from PIL import Image

source = Path(sys.argv[1]).resolve()
output = source.with_name(source.stem + '-slides')
info = subprocess.check_output(['pdfinfo', str(source)], text=True)
count = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
output.mkdir(exist_ok=True)
slides = []
with tempfile.TemporaryDirectory() as temp:
    subprocess.run(['pdftoppm', '-scale-to', '1800', '-png', str(source), str(Path(temp)/'slide')], check=True)
    for index in range(1, count+1):
        name = f'slide-{index:03d}.webp'
        png = next(Path(temp).glob(f'slide-{index:0{len(str(count))}d}.png'))
        with Image.open(png) as image:
            image.save(output/name, 'WEBP', quality=88, method=6)
            width, height = image.size
        text = subprocess.check_output(['pdftotext', '-f', str(index), '-l', str(index), str(source), '-'], text=True).replace('\f','').strip()
        slides.append({'image':name, 'text':text, 'width':width, 'height':height})
(output/'manifest.json').write_text(json.dumps({'slides':slides}, ensure_ascii=False, indent=2)+'\n')
print(f'{count} slides written to {output}')
