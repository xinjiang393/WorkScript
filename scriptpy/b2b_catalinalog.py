#!/usr/local/python
#-*- coding: utf-8 -*-
#
# Partition /opt/tomcat-kmb2b/log/catalina.out by days and delete log files 7-days ago
#

import os
import datetime
import time

# Get derictory of partition log to store it
catalinabaklog_Dir="/opt/tomcat-kmb2b/logs/catalina_logDir"
# Get derictory of catalina.out
catalina_logDir="/opt/tomcat-kmb2b/logs/"
# Get the local current time 
date_current = os.popen("date +%Y-%m-%d").read().strip()
# Get the local half a month ago
date_halfAmonth_ago = os.popen("date -d '(date +%Y%m%d) -7 days' +%Y-%m-%d").read().strip()

# Transfort date to structure date
halfdate_str = time.strptime(date_halfAmonth_ago, '%Y-%m-%d')
halfdate_str = datetime.datetime(*halfdate_str[:3])

# Get into derictory of cataliana.out and empty the file of catalina.out
os.chdir(catalina_logDir)
os.system("cp catalina.out %s/catalina.%s.out" %(catalinabaklog_Dir,date_current))
os.system("echo '' > catalina.out")

# Get into backup derictory of catalina.out and delete the back file half a month ago
os.chdir(catalinabaklog_Dir)
for filename in os.listdir(os.getcwd()):
    file_time = os.popen("stat %s|sed -n '7p'|awk '{print $2}'" %filename).read().strip()
    Tfile_time = time.strptime(file_time, '%Y-%m-%d')
    Tfile_time = datetime.datetime(*Tfile_time[:3])
    if Tfile_time > halfdate_str:
         print "The %s is used in recent half a month,can`t delete it!" %filename
    else:
         print "The %s is not changed beyond half a month, delete it!" %filename
         os.system("rm -f %s" %filename)
