#!/usr/bin/env python3
import subprocess
import threading
import os

class AppRunner(threading.Thread):
    def __init__(self, cmd: str):
        threading.Thread.__init__(self)
        self.cmd=cmd

    def run(self):
        print(self.cmd)
        self.proc=subprocess.Popen(self.cmd, shell=True, executable='bash',stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        try:
            out,err = self.proc.communicate()
        except subprocess.TimeoutExpired:
            print("[ERROR]: rsync timeout expired")
        else:
            if out != '':
                print(out)
            


if __name__=='__main__':
    rsync_cmd="rsync -aq $HOME/workspace/ffmpeg/ $HOME/workspace/dummy"
    rsync1=AppRunner(rsync_cmd)
    rsync1.start()
    rsync1.join()
    if rsync1.proc.returncode != 0:
        print("[Error]: {:s} return {}".format(rsync1.cmd,rsync1.proc.returncode))
    elif rsync1.proc.returncode == 0:
        print("[INFO]: {:s} return {}".format(rsync1.cmd,rsync1.proc.returncode))
    

