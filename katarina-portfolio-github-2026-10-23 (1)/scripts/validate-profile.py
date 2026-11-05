#!/usr/bin/env python3
"""Validate FMK profile data and local image references. No dependencies."""
import json
from pathlib import Path
import re
import struct
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT if (ROOT / 'index.html').is_file() else ROOT / 'dist'
KEYS = ['schemaVersion', 'name', 'studyProgram', 'bio', 'countryCode',
        'portfolioUrl', 'photoOriginal', 'photoStamp']


def validate():
    data = json.loads((PUBLIC / 'portfolio.json').read_text(encoding='utf-8'))
    assert set(data) == set(KEYS), 'portfolio.json must contain exactly the eight FMK fields'
    assert type(data['schemaVersion']) is int and data['schemaVersion'] == 1
    for key in ['name', 'studyProgram', 'bio']:
        assert isinstance(data[key], str) and data[key].strip(), key + ' is required'
    assert len(data['bio']) <= 180, 'bio exceeds 180 characters'
    assert data['countryCode'] is None or re.fullmatch(r'[A-Z]{2}', data['countryCode'])
    public_url = data['portfolioUrl']
    if public_url is not None:
        url = urlsplit(public_url)
        assert url.scheme == 'https' and url.netloc and not url.username and not url.password
        assert url.hostname not in ['localhost', '127.0.0.1', '::1']
        assert not url.query and not url.fragment, 'Use the clean public portfolio base URL'
    else:
        print('Pending: portfolioUrl must be filled after the public site is published.')
    for key in ['photoOriginal', 'photoStamp']:
        value = data[key]
        if value is None:
            print('Pending:', key)
            continue
        assert isinstance(value, str) and value, key + ' must be a path or null'
        if value.startswith('https://'):
            print(key + ': remote image, not checked offline')
            continue
        assert not value.startswith('/') and not urlsplit(value).scheme and '\\' not in value
        path = (PUBLIC / value).resolve()
        assert path.is_relative_to(PUBLIC.resolve()) and path.is_file(), key + ' does not exist'
        assert path.stat().st_size > 0, key + ' is empty'
        if key == 'photoStamp':
            header = path.read_bytes()[:33]
            assert header[:8] == b'\x89PNG\r\n\x1a\n', 'Stamp must be PNG'
            width, height = struct.unpack('>II', header[16:24])
            assert header[25] in (4, 6), 'Stamp must have an alpha channel'
            print('Stamp:', str(width) + ' × ' + str(height), 'px, PNG with alpha')
            if width * 5 != height * 4:
                print('Note: generated canvas is approximately 4:5, not pixel-exact 4:5.')
    print('FMK profile valid; bio:', len(data['bio']), 'characters; local images exist.')


if __name__ == '__main__':
    validate()
