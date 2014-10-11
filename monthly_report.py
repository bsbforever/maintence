#!/usr/bin/python
#coding=utf-8
import os
import re
import time
import datetime
# 获取日期：
today =datetime.date.today()    #获取今天日期
#daily_deltadays =datetime.timedelta(days=1)
#weekly_deltadays =datetime.timedelta(weeks=1)    #确定日期差额，如前天 days=2
monthly_deltadays=datetime.timedelta(days=30)
#daily_day=today-daily_deltadays
#weekly_day =today -weekly_deltadays    # 获取差额日期，一周前
monthly_day =today -monthly_deltadays     # 获取差额日期，一月前
# 格式化输出
ISOFORMAT='%d/%m/%Y' #设置输出格式
today= today.strftime(ISOFORMAT)
#daily_day= daily_day.strftime(ISOFORMAT)
#weekly_day= weekly_day.strftime(ISOFORMAT)
monthly_day= monthly_day.strftime(ISOFORMAT)
#daily_dir=r'/usr/local/squid/report/daily'
#weekly_dir=r'/usr/local/squid/report/weekly'
monthly_dir=r'/usr/local/squid/report/monthly'
result=os.popen('/usr/local/sarg/bin/sarg -o '+monthly_dir+ ' -d '+monthly_day+'-'+today )
print result.read()
