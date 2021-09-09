#!/usr/bin/env python3

import requests

class Curl():
    def __init__(self,url) -> None:
        self.url=url
        self.response=None
        self.device=None
        self.get()
    
    def get(self):
        self.response=requests.get(self.url)

    def show(self):
        print(self.response.text)
    
    def write(self):
        self.initPackages()
        filename='_'.join(self.url.split('/')[-5:-3])+'.csv'
        device=self.url.split('/')[-3]
        f=open(filename,mode='w',encoding='utf-8')
        f.write("package,version,arch\n")
        for idx,val in enumerate(self.packages):
            dev_idx=val.rfind(device)
            line=val[0:dev_idx]
            line=line.split('_',maxsplit=1)
            f.write('%s,%s,%s\n' % (line[0],line[1],device))
        f.close()

    def initPackages(self):
        self.response.encoding='utf-8'
        self.packages=self.response.text.strip().split('\n')
        self.packages_len=len(self.packages)
    

    
if __name__=='__main__':
    image1=Curl('URL')
    image1.write()
