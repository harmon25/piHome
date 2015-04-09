#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-04 02:25:29
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-06 00:36:40
from time import sleep
from math import sin, radians
from multiprocessing import Process, Queue

import pigpio

COMMON_ANODE=True
PosSinWave = lambda amp, ang, freq: amp + (amp * sin(radians(ang) * freq))
CYCLES=2

if COMMON_ANODE == True:
	MAX_BRIGHTNESS = 0
	MIN_BRIGHTNESS = 255
	OFF = 1
else:
	MAX_BRIGHTNESS = 255
	MIN_BRIGHTNESS = 0
	OFF = 0

def pulse_off(pi, pins=[]):
	if isinstance(pins,int):
		pins = [pins]
	dutyList = []
	for p in pins:
		dutyList.append(int(pi.get_PWM_dutycycle(p)))
	avg = sum(dutyList)/len(dutyList)
	for i in range(int(avg), MIN_BRIGHTNESS, 5):
		for p in pins:
			pi.set_PWM_dutycycle(p, i)
		sleep(0.04)
	for p in pins:
		pi.write(p, OFF)

def pulse_on(pi, pins=[], c=2):
	if isinstance(pins,int):
		pins = [pins]
	for i in range(0, c*360, 5):
		for p in pins:
			pi.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
		sleep(0.05)

def rgb(pi, pins, c=3):
	freq = [0.5,1,2]
	for i in range(0, c*360, 5):
		for idx, p in enumerate(pins):
			pi.set_PWM_dutycycle(p, int(PosSinWave(125, i, freq[idx])))
		sleep(0.05)

def pulser(pi,pins,queue):
	qu = queue
	w = pins    #111
	r = w[0] 		#100
	g = w[1] 		#010
	b = w[2] 		#001
	v, y, c = [r,b], [r,g], [g,b] # 101,110, 011
	while True:
		if qu.empty():
			pulse_on(pi, w)
		else:
			e = qu.get()
			if e == "r":
				pulse_off(pi, w)
				pulse_on(pi, r)
			elif e == "g":
				pulse_off(pi, w)
				pulse_on(pi, g)
			elif e == "b":
				pulse_off(pi, w)
				pulse_on(pi, b)
			elif e == "v":
				pulse_off(pi, w)
				pulse_on(pi, v)
			elif e == "y":
				pulse_off(pi, w)
				pulse_on(pi, y)
			elif e == "c":
				pulse_off(pi, w)
				pulse_on(pi, c)
			elif e == "0":
				pulse_off(pi, w)
				break
			else:
				rgb(pi, w)
				pulse_off(pi, w)

def set_pins(r=22, g=23, b=24):
		if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
			print("One of those is not an integer...")
		else:
			return [r,g,b]

class notifyLight:
	'''
	Notification Light
	'''
	def __init__(self, pi=""):
		p = set_pins()
		self.RGB = p
		self.pi =  pigpio.pi(pi)
		self.queue = Queue()
	
	def change_pins(self,r, g, b):
		self.RGB = set_pins(r,g,b)

	def event(self, e=None):
		self.queue.put(e)

	def stop(self):
		self.queue.put("000")

	def run(self):
		p = Process(target=pulser, args=(self.pi,self.RGB,self.queue,), daemon=True)
		p.start()

		
		
		


