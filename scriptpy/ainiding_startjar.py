#!/usr/local/python3
#-*- coding: utf-8 -*-
#
# Scripty for start some jar process of ainiding
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

def Start(arg2):
    ps = os.popen("""ps -ef | grep ainiding | grep java | awk -F " " '{print $10}'""").read()
    if(arg2 in ps):
        print("The process of %s is running! Please check it!" %arg2)
        os._exit()
    else:
        os.chdir(jar_package[arg2][0])
        os.system("nohup java -jar %s &" %jar_package[arg2][1])

def Stop(arg2):
    ps = os.popen("""ps -ef | grep ainiding | grep java | awk -F " " '{print $10}'""").read()
    if(arg2 in ps):
        os.system("ps -ef | grep " + arg2 + """ | grep java |  awk -F " " '{print $2}' | xargs kill -9 """)
    else:
        print("This process is already stopped!")

def Help():
    print("python3 start_jar.py start manager-service")
    print("python3 start_jar.py stop phone-service")

if __name__ == "__main__":
    if((len(sys.argv) == 3) and (sys.argv[1]) == 'start'):
        Start(sys.argv[2])
        print(sys.argv[2])
    elif((len(sys.argv) == 3) and (sys.argv[1] == 'stop')):
        Stop(sys.argv[2])
    elif((len(sys.argv) == 3) and (sys.argv[1] == "--help")):
        Help()
    else:
        Help()
