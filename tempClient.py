#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-01 23:52:22
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-01 23:53:39

from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

temp_in_c = sensor.get_temperature()
temp_in_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)