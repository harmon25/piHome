#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sin, radians
from time import sleep

COMMON_ANODE=True

if COMMON_ANODE == True:
	MAX_BRIGHTNESS = 0
	MIN_BRIGHTNESS = 255
	OFF = 1
else:
	MAX_BRIGHTNESS = 255
	MIN_BRIGHTNESS = 0
	OFF = 0

PosSinWave = lambda amp, ang, freq: amp + (amp * sin(radians(ang) * freq))

def pulse_off(pi, pins):
	dutyList = []
	for p in pins:
		dutyList.append(int(pi.get_PWM_dutycycle(p)))
	avg = sum(dutyList)/len(dutyList)
	for i in range(int(avg), MIN_BRIGHTNESS, 5):
		for p in pins:
			pi.set_PWM_dutycycle(p, i)
		sleep(0.03)
	return

def pulse_on(pi, pins, c=2):
	for i in range(0, c*360, 5):
		for p in pins:
			pi.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
		sleep(0.05)
	return

def rgb(pi, pins, c=3):
	freq = [0.5,1,2]
	for i in range(0, c*360, 5):
		for idx, p in enumerate(pins):
			pi.set_PWM_dutycycle(p, int(PosSinWave(125, i, freq[idx])))
		sleep(0.05)
	return

def pulser(pi,pins,queue):
	qu = queue  
	r, g, b = [pins[0]], [pins[1]] , [pins[2]] 	#1,#2, #3
	v, y, c = [pins[0],pins[2]], [pins[0],pins[1]], [pins[1],pins[2]] #4,#5,#6
	while True:
		if qu.empty():
			pulse_on(pi, pins)
		else:
			pulse_off(pi, pins)
			e = qu.get()
			if e == 1:	
				pulse_on(pi, r)
			elif e == 2:
				pulse_on(pi, g)
			elif e == 3:
				pulse_on(pi, b)
			elif e == 4:
				pulse_on(pi, v)
			elif e == 5:
				pulse_on(pi, y)
			elif e == 6:
				pulse_on(pi, c)
			elif e == 0:
				pulse_off(pi, pins)
				break
			else:
				rgb(pi, pins)

def set_pins(r=22, g=23, b=24):
		if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
			print("One of those is not an integer...")
			return False
		else:
			return [r,g,b]