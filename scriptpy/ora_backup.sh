#!/bin/bash

# 以上代码为Oracle数据库运行账号oracle的系统环境变量设置，必须添加，否则crontab任务计划不能执行。
# /home/oracle/.bash_profile
export ORACLE_SID=kmb2b
export TERM=vt100
export ORACLE_BASE=/u01/app/oracle/rdbms
export NLS_DATE_FORMAT="yyyy-mm-dd hh24:mi:ss"
export ORACLE_DOC=$ORACLE_BASE/doc
export TMP=/tmp
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0
export PATH=$ORACLE_HOME/bin:$PATH
export NLS_LANG='SIMPLIFIED CHINESE_CHINA.AL32UTF8'

dateTime=$(date +%Y-%m-%d)
days=7
orsid=127.0.0.1:1521/kmb2b
orowner=kmdata
backuser=kmdata
backpass=kmDATA_ora
backdir=/u01/backfile_ora/backup
backdata=$orowner"_"$dateTime.dmp
backlog=$orowner"_"$dateTime.log
ordatafile=$orowner"_"$dateTime.tar.gz
remotedir=/backup/oracle_data_backup/

cd $backdir
#su - oracle
exp $backuser/$backpass@$orsid grants=y owner=$orowner file=$backdir/$backdata log=$backdir/logs/$backlog
cd $backdir
tar -zcvf $ordatafile $backdata $backlog

find $backdir/ -type f -name "*.log" | xargs rm -f
find $backdir/ -type f -name "*.dmp" | xargs rm -f
find $backdir/ -type f -name "*.tar.gz" -mtime +$days | xargs rm -rf  

scp $backdir/$ordatafile 172.20.28.34:$remotedir
