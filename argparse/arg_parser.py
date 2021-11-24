#!/usr/bin/env python3
import argparse
import os
import sys

def parserFunc():
    parser=argparse.ArgumentParser(prog='cloc_component.py',
        usage='%(prog)s [-h] [--dry] -d DISTRO -b BRANCH -n BUILD_NO',
        epilog='simple usage: %(prog)s --distro webos --branch master --build_no 1927')
    parser.add_argument("--dry", help="Dry run script for specific target", action="store_true")
    group2=parser.add_argument_group('mandatory option')
    group2.add_argument("-d", "--distro", help="Pass Distro")
    group2.add_argument("-b", "--branch", help="Pass Branch Name")
    group2.add_argument("-n", "--build_no", help="Pass Build Number")
    args=parser.parse_args()
    print(args.dry)

if __name__ == '__main__':
    parserFunc()