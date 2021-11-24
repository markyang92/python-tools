#!/usr/bin/env python3
import subprocess

def CMD(cmd: str):
	proc=subprocess.Popen(cmd, shell=True, executable="/usr/bin/bash", stdout=subprocess.PIPE, universal_newlines=True)
	try:
		ret = proc.communicate() # ret=(tuple)(stdout,stderr)
	except subprocess.TimeoutExpired:
		proc.kill()
		return 127
	else:
		if proc.returncode == 0:
			return(proc.returncode,ret[0]) # ret[1] == None
		else:
			return(proc.returncode,ret[1])

if __name__ == '__main__':
	CMD('echo Helloworld!')
