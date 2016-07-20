#!/usr/bin/env python
# -*-coding:UTF-8-*-
import sys,MySQLdb,traceback
import time
class mysql:
    def __init__ (self,
                  host   = '',
                  user   = '',
                  passwd = '',
                  db     = '',
                  port   = 3306,
                  charset= 'utf8'
                  ):
        self.host   = host
        self.user   = user
        self.passwd = passwd
        self.db     = db
        self.port   = port
        self.charset= charset
        self.conn   = None
        self._conn()

    def _conn (self):
        try:
            self.conn = MySQLdb.Connection(self.host, self.user, self.passwd, self.db, self.port , self.charset)
            return True
        except :
            return False

    def _reConn (self,num = 3,stime = 3): #重试连接总次数为1天,这里根据实际情况自己设置,如果服务器宕机1天都没发现就......
        _number = 0
        _status = True
        while _status and _number <= num:
            try:
                self.conn.ping()       #cping 校验连接是否异常
                _status = False
            except:
                if self._conn()==True: #重新连接,成功退出
                    _status = False
                    break
                _number +=1
                time.sleep(stime)      #连接不成功,休眠3秒钟,继续循环，知道成功或重试次数结束

    def select (self, sql = ''):
        try:
            self._reConn()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            self.cursor.execute (sql)
            result = self.cursor.fetchall()
            self.cursor.close ()
            return result
        except MySQLdb.Error,e:
            #print "Error %d: %s" % (e.args[0], e.args[1])
            return False

    def select_limit (self, sql ='',offset = 0, length = 20):
        sql = '%s limit %d , %d ;' % (sql, offset, length)
        return self.select(sql)

    def query (self, sql = ''):
        try:
            self._reConn()
            self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
            self.cursor.execute ("set names utf8") #utf8 字符集
            result = self.cursor.execute (sql)
            self.conn.commit()
            self.cursor.close ()
            return (True,result)
        except MySQLdb.Error, e:
            return False
    def insert(self,sql=''):
	try:
	    self._reConn()
	    self.cursor=self.conn.cursor(MySQLdb.cursors.DictCursor)
	    self.cursor.execute("set names utf8")
	    result = self.cursor.execute(sql)
	    if result:
		insert_id=self.conn.insert_id()
	    else:
		insert_id=None
	    self.conn.commit()
	    self.cursor.close()
	    return (True,result,insert_id)
	except MySQLdb.Error,e:
	    return False
    def close (self):
        self.conn.close()

#if __name__=='__main__':
    #my = mysql('172.17.21.156','root','wtt@564','fe_fireeye',3306)
    #print my.query('insert into fe_monitor_task values(0,"/outsource/unreadmsgnum","asdasdsdf",5,1,0000,1111)')
    #ccc= my.select_limit('select * from fe_monitor_task',0,1)
    #print type(my.select_limit('select * from fe_monitor_task',0,1))
    #my.close()  
