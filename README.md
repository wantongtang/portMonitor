# 端口监控
# mysql支持
# 配置：
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
## example:
        git clone git@github.com:wantongtang/portMonitor.git 
        开启扫描服务
        python myscan.py start 
        我随便添加一个任务，数据库里面执行：
        INSERT INTO `polls_task` (`id`, `ipdir`, `state`, `white_port`, `create_time`) VALUES ('0', '172.17.21.156', '0', '80,443', '1122');
        过一会之后去数据库查看数据，得到扫描结果
        后台会一直运行，如需要停止扫描服务：
        python myscan.py stop
## TODO
        创建web接口添加扫描任务
        创建web展示平台

### 欢迎加入 交流QQ群：214550530

