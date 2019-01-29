#!/usr/local/python
#-*- coding: utf-8 -*-
#
# This python script is aim at mounting www directory to NAS automatically.
#

import os

# Get the mount content.
mou = os.popen("df -h | awk '{print $1}'")
pmou = mou.read()
pmou = pmou.split("\n")

naskeylist = ["202:/mnt/pic/b2b", "203:/mnt/html", "202:/mnt/pic/user"]
moucmddict = {
             "202:/mnt/pic/b2b":"mount 172.20.28.202:/mnt/pic/b2b   /www/pic",
             "202:/mnt/pic/user":"mount 172.20.28.202:/mnt/pic/user   /www/user-pic",
             "203:/mnt/html":"mount 172.20.28.203:/mnt/html      /www/cms-publish"
             }

# Judge some directory mounted or not,if mount return 1, else return 0
def judge_mount(naskey,  listmou):
    for itemmou in listmou:
        if naskey in itemmou:
            return 1
    return 0

# If the judge_mount function return 0, than excute mount command
for naskey in naskeylist:
    if(judge_mount(naskey, pmou)):
        continue
    else:
        os.system(moucmddict[naskey])