#!/usr/bin/python
#coding=gbk
#coding=utf-8
import smtplib
import os
import time
from email.MIMEText import MIMEText
mailto_list=["ezio_shi@adata.com.cn"]
mail_host="192.168.170.170"  #设置服务器
mail_user="ezio_shi"    #用户名
mail_postfix="adata.com.cn"  #发件箱的后缀

def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="OracleAlert"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        #s.set_debuglevel(1)
        s.helo()
        #s.starttls()
        #s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    result=os.popen('tail -n 1000 /oracle/admin/ADATAMES/bdump/alert_ADATAMES1.log | awk  \'/Error/\' || \'/failed/\' {print $0}').read()
    if result != '':
        send_mail(mailto_list,"OracleAlert",result)
    else:
	print ' there are  no  errors on oracle at '+ time.strftime("%d/%m/%Y %H:%M:%S")

