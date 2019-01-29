- 拉去项目
    * mkdir Project
    * cd Project
    * git init
    * git clone repository

- 配置ssh
    * 进入\~路径下，必须保证当前路径在\~路径下, 在git命令行敲击 ssh-keygen -t  rsa -C 385832410@qq.com
    * 把 ~/.ssh/id_rsa.pub文件的内容放入到github上的`SSH & GPG key`条目下
    * git config --global user.name arthur
    * git config --global user.email 385832410@qq.com
```
arthur@learnning:~/.ssh$ git config --global user.name arthur
arthur@learnning:~/.ssh$ git config --global user.email 385832410@qq.com
arthur@learnning:~/.ssh$ ssh -T git@github.com
The authenticity of host 'github.com (13.229.188.59)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known hosts.
Hi xinjiang393! You've successfully authenticated, but GitHub does not provide shell access.
```
- git add filename
```
arthur@learnning:~/Project/WorkScript$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

    new file:   auto_mountNAS.py

```
- git commit -m "Mount Nas dis automatic"
- git push
```
arthur@learnning:~/Project/WorkScript$ git push
Username for 'https://github.com': xinjiang393
Password for 'https://xinjiang393@github.com': Pur
```
