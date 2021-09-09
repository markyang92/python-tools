#!/usr/bin/env python3
import os

# ============================= User Define ================================= #
WORKDIR     = os.getcwd()+'/' # Default: Now Directory
PARSE_FILE  = "installed-packages_raspberrypi4.txt"    
PARSE_FILE  = WORKDIR+PARSE_FILE


class Package():
    def __init__(self, file:str):
        self.file=file
    
    def parsePackage(self):
        f=open(file=self.file,encoding='utf-8',mode='r')
        fw=open(self.file.split('.')[0]+'.csv','w')
        fw.write("idx,package,version,arch\n")
        idx=1
        while True:
            line=f.readline().strip()
            if not line:
                break
            # find arch
            packagename_version_arch=line[0:line.rfind('.')]
            arch=packagename_version_arch.split('_')[-1]
            package_name=packagename_version_arch.split('_')[0]
            version=(packagename_version_arch.lstrip(package_name).lstrip('_')).rstrip(arch).rstrip('_')
            fw.write('%d,%s,%s,%s\n' % (idx,package_name,version,arch))
            idx+=1

        f.close()
        fw.close()



if __name__=='__main__':
    WORKDIR=os.getcwd()
    packages1=Package(PARSE_FILE)
    packages1.parsePackage()
    
