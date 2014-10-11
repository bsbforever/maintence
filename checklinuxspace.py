#!/usr/bin/python
#coding=gbk
#coding=utf-8
import re
import os
import smtplib
from email.MIMEText import MIMEText
mailto_list=["ezio_shi@adata.com.cn"]
mail_host="192.168.170.170"  #设置服务器
mail_user="ezio_shi"    #用户名
#mail_pass="296701298a!"   #口令
mail_postfix="adata.com.cn"  #发件箱的后缀

def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="LinuxSpace Warnning"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        #s.set_debuglevel(1)
        s.ehlo()
        #s.starttls()
        #s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

def checkspace(ipaddress,alert):
    #fp=os.popen('ssh '+ipaddress +  ' \'df -h |awk \'{if ($1==$NF){a=$1;printf $a}else{print $0}}\'\'')
    fp=os.popen('ssh '+ipaddress +  ' df -h |awk \'{if ($1==$NF){printf $1}else{print $0}}\'')
    k=1
    #print ipaddress+'\n'+fp.read()
    for i in fp:
        j=i.split()
        if k>1:
            #print j[4]
            if int(j[4][:-1])> 80:
               alertcontent='The Space of '+j[0]+' on '+ipaddress+' is '+j[4]+' Used!'
               alert=alert+alertcontent
               #print alert
               k+k+1
        else:
            k=k+1
    return alert

if __name__ == '__main__':
    alert=''
    ip=open(r'/root/linuxip.txt','r')
    for ipaddress in ip:
        ipaddress=ipaddress.strip()
        alert=checkspace(ipaddress,alert)
    #print alert
    if alert != '':
        send_mail(mailto_list,"LinixSpace Warnning",alert)
