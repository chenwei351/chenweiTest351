#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import time


def db_reject(sql):
    db1 = pymysql.connect(host="192.168.16.31", port=9001, user="dev", password="jmdevcd", db="jls")
    #
    cursor = db1.cursor()

    cursor.execute(sql)
    db1.commit()
    alist1 = cursor.fetchall()
    for ve in alist1:
        print(ve)
    time.sleep(1)

    db1.close()