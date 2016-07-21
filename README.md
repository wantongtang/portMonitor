# 端口监控
# mysql支持

## 1 导入mysql表，mb.sql
## 2 配置修改mysql_conf.py 文件配置,你的mysql用户名，密码这些，我的如下:
        #mysql_conf.py 
        host='172.17.21.156'
        user='root'
        password='*****'
        port=3306
        database='mb'

## 3 运行 python myscan.py start  开始之后会一直监控
## 4 停止：python myscan.py stop
### (after started it will create a daemon,do not need to stop it normally)

## TODO
### 创建web展示，目前我是直接在数据库里面直接看

### 最后，运行一段时间之后可以去数据库查看运行结果
### 欢迎加入 交流QQ群：214550530

