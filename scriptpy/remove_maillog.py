#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Remove files 7 days ago which directory is /var/spool/postfix/maildrop/
#

import os
import datetime
import time

# Get the upper directory of the file that needs to delete
delete_dir = "/var/spool/postfix/maildrop"

# Get local time on last week
date = os.popen("date -d '(date +%Y%m%d) -7 days' +%Y-%m-%d").read().strip()
# Transfort date to structure date
t2 = time.strptime(date, '%Y-%m-%d')
t2 = datetime.datetime(*t2[:3])

# Get list of file name
dir_name = []

# get in directory of delete file
os.chdir(delete_dir)

for filename in os.listdir(os.getcwd()):
    file_time = os.popen("stat  %s|sed -n '7p'|awk '{print $2}'" %filename).read().strip()
    t1 = time.strptime(file_time, '%Y-%m-%d')
    t1 = datetime.datetime(*t1[:3])
    if t1 > t2:
        print "The %s is used in recent week,can`t delete it!" %filename
    elif t2 > t1:
        print "The %s is changed beyond one week, delete it!" %filename
        os.system("rm -rf %s" %filename)