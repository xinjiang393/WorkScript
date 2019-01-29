#!/usr/local/python3
#-*- coding: utf-8 -*-
#
# Scripty for check jar process of ainiding
#
# Time: 2019-01-17
# User: Arthur
#

import sys
import os


jar_package = {"manage-service": ["/opt/ainiding_jar/ainiding_manage/","ainiding-manage-service.jar"],
               "manage-web":["/opt/ainiding_jar/ainiding_manage/","ainiding-manage-web.war"],
               "phone-api":["/opt/ainiding_jar/ainiding_phone/","ainiding-phone-api.jar"],
               "phone-service":["/opt/ainiding_jar/ainiding_phone/","ainiding-phone-service.jar"],
               "phone-wx":["/opt/ainiding_jar/ainiding_phone/","ainiding-phone-wx.war"],
               "store-api":["/opt/ainiding_jar/ainiding_store/","ainiding-store-api.jar"],
               "store-service":["/opt/ainiding_jar/ainiding_store/","ainiding-store-service.jar"]
              }

def Check():
    ps = os.popen("""ps -ef | grep ainiding | grep java | awk -F " " '{print $10}'""").read()
    for k in jar_package.keys():
        if(k in ps):
            print("The process of %s is running! Please check it!" %k)
            continue
        else:
            os.chdir(jar_package[k][0])
            os.system("nohup java -jar %s &" %jar_package[k][1])

if __name__ == "__main__":
    Check()