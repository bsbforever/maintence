#!/usr/bin/env python
# -*_ coding:utf-8 -*-
import urllib,os,urllib2,sys

def tijiao(m):
    values={}
    values['name']=m[0]
    values['total']=float(m[1])
    values['used']=float(m[2])
    values['free']=float(m[4])
    values['usage']=m[3]
    url='http://192.168.173.50/ins.php?ins=tab'
    data = urllib.urlencode(values)
    print data
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
def main():
    shfile=sys.path[0]+'/tab_spa.sh'
    #f=os.popen('/home/oracle/db_check/tab_spa.sh').readlines()
    f=os.popen('%s'%shfile).readlines()
    j=0
    for i in f:
        if j>2 and j<32:
            tmp=i.split()
            tijiao(tmp)
        j+=1
if __name__=='__main__':
    main()
