#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-02 11:06:12
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-03 01:36:00
from __future__ import print_function
import time
import os.path

RED_PIN = 22
GREEN_PIN = 23
BLUE_PIN = 24

PI_BLASTER_PATH = "/dev/pi-blaster"

class RGB_LED:
	'''
	LED Object
	STATUS[0] = ON
	STATUS[1] = PULSING
	'''
	state = {
			"PINS":{
			 		"RED":[RED_PIN, 0],
			 		"GREEN":[GREEN_PIN, 0],
			 		"BLUE":[BLUE_PIN, 0]
			 		},
	 		"STATUS":[False, False]
	 		}
	def led_sleep(self,rate):
		if rate == 1:
			time.sleep(0.005)
		elif rate == 2:
			time.sleep(0.0005)
		elif rate == 3:
			time.sleep(0.00005)
		else:
			time.sleep(0)
	def set_intensity(self, colour, intensity, rate=2):
		with open(PI_BLASTER_PATH, 'w') as f:
			while intensity != self.state.get("PINS").get(colour)[1]:
				if self.state.get("PINS").get(colour)[1] > intensity:
					print("{}={}".format(self.state.get("PINS").get(colour)[0], self.state.get("PINS").get(colour)[1]/255), file=f)
					self.led_sleep(rate)
					self.state.get("PINS").get(colour)[1]-=1
				else:
					print("{}={}".format(self.state.get("PINS").get(colour)[0], self.state.get("PINS").get(colour)[1]/255), file=f)
					self.led_sleep(rate)
					self.state.get("PINS").get(colour)[1]+=1
	def all_on(self):
		'''Change every LED pin state to 255'''
		self.set_intensity("RED", 255)
		self.set_intensity("GREEN", 255)
		self.set_intensity("BLUE", 255)
		self.state.get("STATUS")[0] = True
	def all_off(self):
		'''Change every LED pin state to 0'''
		self.state.get("STATUS")[0] = False
		if self.state.get("PINS").get("RED")[1] == 0 and self.state.get("PINS").get("GREEN")[1] == 0 and self.state.get("PINS").get("BLUE")[1] == 0:
			with open(PI_BLASTER_PATH, 'w') as f:
				for c,s in self.state.get("PINS").items():
					print("{}={}".format(s[0], 0), file=f)
		else:
			self.set_intensity("RED", 0)
			self.set_intensity("GREEN", 0)
			self.set_intensity("BLUE", 0)
	def rgb_cycle(self):
		self.state.get("STATUS")[0] = True
		self.state.get("STATUS")[1] = True
		try:
			while self.state.get("STATUS")[1] == True:
				self.set_intensity("BLUE", 255)
				self.set_intensity("RED", 255)
				self.set_intensity("BLUE", 0)
				self.set_intensity("RED", 255)
				self.set_intensity("GREEN", 255)
				self.set_intensity("RED", 0)
				self.set_intensity("GREEN", 0)
		except(KeyboardInterrupt):
			self.state.get("STATUS")[1] = False
	'''
	def pulse(self, scale=50):
		self.set_intensity("GREEN", 0, 4)
		self.set_intensity("BLUE", 0, 4)
		while self.pulsing == True:
			self.set_intensity("RED", 255, 1)
			self.set_intensity("RED", 0, 1)
	'''

