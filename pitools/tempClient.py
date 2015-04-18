#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-01 23:52:22
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-16 19:05:15

import psycopg2
from w1thermsensor import W1ThermSensor
from datetime import datetime
sensor = W1ThermSensor()
temp_in_c = sensor.get_temperature()
temp_in_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)

conn = psycopg2.connect(database="pihome",user="pihome",password="pihome",host="t400-serv")
SQL = "INSERT INTO temp (temp,date_time,room_id,pi_id) VALUES (%s, %s, %s, %s);"
data = (round(temp_in_c,1),datetime.now(), 1, 1)

cur = conn.cursor()
cur.execute(SQL,data)
conn.commit()
conn.close()
