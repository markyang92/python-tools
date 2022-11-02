#!/usr/bin/env python3

def renamer(s):
    """Make sure s name are legitimate strings"""
    import re

    def fixutf(m):
        cp = m.group(1)
        if cp:
            return('\\u%s' % cp).encode('latin-1').decode('unicode_escape')
    
    # Handle unicode codepoints encoded as <U0123>, as in glibc locale files.
    s = re.sub(r'<U([0-9A-Fa-f]{1,4})>', fixutf, s)

    # Remaining package name validity fixes
    return s.lower().replace('_', '-').replace('@', '+').replace(',', '+').replace('/', '-')

if __name__ == '__main__':
    s = "package_1.24.@git,/hub.deb"
    print(renamer(s))
