#!/usr/bin/env python3
"""Refresh the offline profile snapshot and metadata from portfolio.json."""
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT if (ROOT / 'index.html').is_file() else ROOT / 'dist'


def sync():
    profile = json.loads((PUBLIC / 'portfolio.json').read_text(encoding='utf-8'))
    path = PUBLIC / 'index.html'
    markup = path.read_text(encoding='utf-8')
    snapshot = json.dumps(profile, ensure_ascii=False, indent=2).replace('<', '\\u003c')
    markup, count = re.subn(
        r'(<script type="application/json" id="portfolio-profile">).*?(</script>)',
        lambda match: match[1] + '\n' + snapshot + '\n' + match[2],
        markup, count=1, flags=re.S,
    )
    if count != 1:
        raise SystemExit('Missing portfolio-profile snapshot in index.html')
    name = html.escape(profile['name'], quote=True)
    markup = re.sub(r'<meta name="author" content="[^"]*">',
                    lambda _: '<meta name="author" content="' + name + '">', markup, count=1)
    markup = re.sub(r'<title>.*?</title>',
                    lambda _: '<title>' + name + ' · Retro TV portfolio</title>', markup, count=1)
    description = html.escape('The portfolio of ' + profile['name'] +
                             ', a student with a background in illustration and animation.', quote=True)
    markup = re.sub(r'<meta name="description" content="[^"]*">',
                    lambda _: '<meta name="description" content="' + description + '">', markup, count=1)
    markup = re.sub(r'(<span id="profile-first-name">).*?(</span>)',
                    lambda m: m[1] + html.escape(profile['name'].split()[0]) + m[2], markup, count=1)
    path.write_text(markup, encoding='utf-8')
    print('Profile snapshot and page metadata updated from portfolio.json.')


if __name__ == '__main__':
    sync()
