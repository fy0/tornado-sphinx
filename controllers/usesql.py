
# coding:utf-8

import time
import MySQLdb as mdb

conn = mdb.connect('localhost','root','','focuscrawl_data')

cur = conn.cursor()

#cur.execute('select * from items')
# ,('url','title','body',int(time.time()),'ext')
#cur.execute('replace into items values(null,%s,%s,%s,%s,%s)',('url','''tit"`'"le''','body',int(time.time()),'ext'))
#conn.commit()

def getDataById(docid):
    cur.execute('select * from items where id=%s',str(docid))
    return cur.fetchall()

