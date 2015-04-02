#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-01 23:52:22
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-02 02:17:58

import pymysql.cursors
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
temp_in_c = sensor.get_temperature()
temp_in_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)

sensor_id = 1

connection = pymysql.connect(host='192.168.0.220',
                             user='piClient',
                             passwd='piPass',
                             db='piHome',
                             cursorclass=pymysql.cursors.DictCursor)

try:
	with connection.cursor() as cursor:
		cursor.execute("INSERT INTO `temp` (`timestamp`, `temp`,`sensor_id`) VALUES ({},{},{})".format('NOW()',temp_in_c, sensor_id))
	connection.commit()
finally:
    connection.close()