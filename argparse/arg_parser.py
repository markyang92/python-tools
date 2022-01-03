#!/usr/bin/env python3
import argparse
import os
import sys

# ======================= BEGIN: Usage =================================== #
PROG=os.path.normpath(sys.argv[0])
usage=f'{PROG} [-h]  -d DISTRO -b BRANCH -n <BUILD_NO | latest> -i IMAGE -m MACHINE\n\n\
simple usage:\n\
  {PROG} --distro \n\
Support DISTRO:\n\
  hello world!'
# ======================= END: Usage ===================================== #

def parserFunc():
    global usage
    parser = argparse.ArgumentParser(
        usage = usage)
    group2 = parser.add_argument_group('required option')
    group2.add_argument("-d", "--distro", help="Pass Distro. You can specify 'git repository url'", required=True)
    group2.add_argument("-b", "--branch", help="Pass Branch Name", required=True)
    group2.add_argument("-n", "--build-no", help="Pass Build Number If you wan\'t to build latest build, Just pass 'latest'", required=True)
    group2.add_argument("-i", "--image", help="Pass Build Image.", required=True)
    group2.add_argument("-m", "--machine", help="Pass Build Machine", required=True)
    args = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_usage()
        exit(1)

if __name__ == '__main__':
    parserFunc()
