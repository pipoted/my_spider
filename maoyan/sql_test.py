#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='xzx199110',
    database='spider',
    port=3306,
)

cursor = conn.cursor()
sql = """
create table if not exists sql_test (
id varchar(255) not null,
name varchar(255) not null,
age int not null,
primary key(id))
"""
cursor.execute(sql)
conn.close()

