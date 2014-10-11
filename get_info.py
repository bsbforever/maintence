#!/usr/bin/env python
# -*_ coding:utf-8 -*-
import os,sys,urllib,urllib2
def get_cpu():
    a=os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2]
    cpus=a.split()[1].split('u')[0]
    return cpus
def get_mem():
     mem = {}
     f = open("/proc/meminfo")
     lines = f.readlines()
     f.close()
     for line in lines:
         if len(line) < 2:
             continue
         name = line.split(':')[0]
         var = line.split(':')[1].split()[0]
         mem[name] = long(var) * 1024.0
     mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
     return mem
def main():
    cpu=get_cpu()
    mem=get_mem();
    mem_u=round(mem['MemUsed']/1024/1024,2)
    mem_f=round(mem['MemFree']/1024/1024,2)
    values={}
    values['cpu']=str(cpu)
    values['memu']=str(mem_u)
    values['memf']=str(mem_f)
    url='http://192.168.173.50/ins.php?ins=info'
    data = urllib.urlencode(values)
    print data
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page

if __name__=='__main__':
    main()
