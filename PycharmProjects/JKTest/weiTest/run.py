#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import data
import  mysql
import  time
#
db = pymysql.connect(host="192.168.16.31", port=9001, user="dev", password="jmdevcd", db="jls")
#
cursor = db.cursor()
err_number=0
for i in range(100):
    # print  iE00000001379515
    sql = mysql.resql()

    print sql
    try:




        cursor.execute(sql)


        
        if cursor.rowcount == 0:

            print("ERR")

        '''     
    
        while True:
        
        
            data = cursor.fetchone()
            if data == None:        
                break;
            print(data)
        '''
        db.commit()
        alist = cursor.fetchall()
        for vo in alist:
            print(vo)

    except Exception as err:
        err_number +=1
        print("Err", err)

    i = i+1
    time.sleep(1)
print err_number
db.close()