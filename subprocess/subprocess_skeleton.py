#!/usr/bin/env python3
import subprocess

def BASH_CMD(cmd: str):
    proc=subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    ret=proc.communicate()
    if not proc.returncode:
        return (0,ret[0])
    else:
        return (proc.returncode,ret[1])


if __name__ == '__main__':
    ret=BASH_CMD('curl --max-time 3 -I wrongDNS.com')
    print (ret)
