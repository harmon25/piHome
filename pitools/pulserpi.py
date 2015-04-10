#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-04 02:25:29
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-06 00:36:40

from multiprocessing import Process, Queue
import pigpio
from pitools.pulserutils import *

class notifyLight(object):
	"""
	notify Light Object
	[R,G,B]: Pins to control each LED from RGB LED on a Pi BCM Pinout - default 22,23,24
	pigpioDict: {"pi hostname/ip":[[pigpio object],[R,G,B]], ...}  

	"""
	def __init__(self, pis):
		"""Initilize a new notifyLight class object, creates a new Queue used for passing events to child processes"""
		if not isinstance(pis,list):
			self.pis = [pis]
		self.ON = False
		self.pis = pis
		self.queue = Queue()
		self.pigpioDict = {}
		return

	def initLight(self):
		"""Initilize pigpio.pi objects for each host passed to the notifyLight class"""
		for pi in self.pis:
			self.pigpioDict[pi] = [pigpio.pi(pi) , set_pins()]
			print("{} Initilized!".format(pi))
		return 
	
	def changePins(self,r, g, b, pi):
		""" notifyLight.changePins(REDPIN,GREENPIN,BLUEPIN,pi_to_change)"""
		self.pigpioDict[pi][1] = set_pins(r,g,b)
		return print("Pins changed on {} to, R:{}, G:{}, B:{}".format(pi, r, g, b))

	def event(self, e=None):
		""" 
		notifyLight.event(0-7)
		1 = RED
		2 = GREEN
		3 = BLUE
		4 = VIOLET
		5 = YELLOW
		6 = CYAN
		7 = RGB Cycle
		0 = OFF
		"""
		if not isinstance(e, int):
			return print("invalid event")
		elif not self.ON:
			return print("Must run() before sending events")
		else:
			for pi in self.pis:
				self.queue.put(e)
			return

	def stop(self):
		""" notifyLight.stop()"""
		if self.ON:
			self.ON = False
			for pi in self.pis:
				self.queue.put(0)
			return print("Pulse Stopped")
		else:
			return print("I wasn't ON")
		
	def deinitLight(self):
		""" 
		notifyLight.deinitLight()
		Stops pigio.pi connections
		cleans dictionary - reinitialize to rerun
		"""
		pitoPop = []
		for pi, v in self.pigpioDict.items():
			v[0].stop()
			pitoPop.append(pi)
		for pi in pitoPop:
			self.pigpioDict.pop(pi,None)
			print("{} DeInitilized!".format(pi))
		return 

	def run(self):
		"""
		notifyLight.run()
		Start daemon processes awaiting on Queue for events 
		"""
		if not self.ON:	
			self.ON = True
			procList = []
			for k, v in self.pigpioDict.items():
				procList.append(Process(target=pulser, args=(v[0], v[1], self.queue,) , daemon=True))
			for p in procList:
				p.start()
			return
		else:
			return print("I am already ON")
		
		

		
		
		


