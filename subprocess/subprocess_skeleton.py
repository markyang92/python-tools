#!/usr/bin/env python3
import subprocess
import sys

def BASH_CMD(cmd: str, STDIO_PIPE = False):
    """
    # ========================================================================= #
    # @brief                Execute Simple bash command and deal with it
    # @param cmd            Bash command : str
    # @param STDIO_PIPE     IF Caller need 'STDOUT' string, Then it set to True
    # @return (returncode, STDOUT | STDERR)
    # ========================================================================= #
    """
    if STDIO_PIPE:
        stdout = subprocess.PIPE
        stderr = subprocess.PIPE
    else:
        stdout = sys.stdout
        stderr = sys.stderr

    proc = subprocess.Popen(cmd, shell=True, executable="/bin/bash", \
        stdout = stdout, \
        stderr = stderr, \
        encoding = 'utf-8',
        text = True)
    ret = proc.communicate()
    if not proc.returncode:
        return (proc.returncode,ret[0]) # (returncode, STDOUT) : tuple
    else:
        return (proc.returncode,ret[1]) # (returncode, STDERR) : tuple


# Case 1. Don't Need STDOUT
ret = BASH_CMD('echo \"hello world\"')
if ret[0] != 0:
    print(ret[1], file=sys.stderr)
    exit(ret[0])

# Case 2. Need STDOUT
ret = BASH_CMD(f"find ./ -name \"file\"",STDIO_PIPE=True)
if ret[0] != 0:
    print(ret[1],file=sys.stderr)
    exit(ret[0])
res_stdout = ret[1].strip()