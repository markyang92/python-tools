#!/usr/bin/env python3

import os
import codecs


def get_subpkgdata(pkg):
    pkgdata = {}

    def decode(str):
        c = codecs.getdecoder("unicode_escape")
        return c(str)[0]

    if os.access(pkg, os.R_OK):
        import re
        with open(pkg, 'r') as f:
            lines = f.readlines()
        r = re.compile(r"(^.+?):\s+(.*)")
        for l in lines:
            m = r.match(l)
            if m:
                pkgdata[m.group(1)] = decode(m.group(2))
    
    return pkgdata

if __name__=='__main__':
    pkg = 'which'
    print(get_subpkgdata(pkg))