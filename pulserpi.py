#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-04 02:25:29
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-06 00:36:40
from time import sleep
from math import sin, radians

PosSinWave = lambda amp, ang, freq: amp + (amp * sin(radians(ang) * freq))

class PulserPi(object):
	'''
	Notification Light
	'''
	def __init__(self, pi):
		self.HOST = ''
		self.PORT0 = 5011
		self.AUTHKEY = b'authkey'
		self.PI = pi
		self.PINS = [22, 23, 24]
		self.ON = False
		self.CYCLES = 2
	def QueueClient(HOST, PORT, AUTHKEY):
		from multiprocessing.managers import SyncManager
		class QueueManager(SyncManager):
			pass
		QueueManager.register('get_queue')
		QueueManager.register('get_name')
		QueueManager.register('get_description')
		manager = QueueManager(address = (HOST, PORT), authkey = AUTHKEY)
		manager.connect() # This starts the connected client

		return manager
	def set_pins(self, red=22, green=23, blue=24):
		if not isinstance(red, int) or not isinstance(green, int) or not isinstance(blue, int):
			print("One of those is not an integer...")
		else:
			self.PINS[0]=red
			self.PINS[1]=green
			self.PINS[2]=blue
			print("Red pin set to: {}\nGreen pin set to: {}\nBlue pin set to: {}".format(red,green,blue))
	def check_setup(self):
		from pigpio import pi
		if None in self.PINS:
			msg = "Must first set_pins"
			return [False, msg]
		elif not isinstance(self.PI, pi):
			msg = "Set PIGPIO object as PiLight.PI - pi = pigpio.pi()\nPiLightClass.PI = pi"
			return [False, msg]
		else:
			msg = "Setup!"
			return [True, msg]
	def white(self):
		for i in range(0, self.CYCLES*360, 5):
			for p in self.PINS:
				self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for p in self.PINS:
			for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
				self.PI.set_PWM_dutycycle(p,x)
		sleep(0.05)
	def red(self):
		for i in range(0, self.CYCLES*360, 5):
			self.PI.set_PWM_dutycycle(self.PINS[0], int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(self.PINS[0]), 255 ,5):
			self.PI.set_PWM_dutycycle(self.PINS[0],x)
		sleep(0.05)
	def blue(self):
		for i in range(0, self.CYCLES*360, 5):
			self.PI.set_PWM_dutycycle(self.PINS[2], int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(self.PINS[2]), 255 ,5):
			self.PI.set_PWM_dutycycle(self.PINS[2],x)
			sleep(0.05)
	def green(self):
		for i in range(0, self.CYCLES*360, 5):
			self.PI.set_PWM_dutycycle(self.PINS[1], int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(self.PINS[1]), 255 ,5):
			self.PI.set_PWM_dutycycle(self.PINS[1],x)
			sleep(0.05)
	def cyan(self):
		CPINS = [self.PINS[1],self.PINS[2]]
		for i in range(0, self.CYCLES*360, 5):
			for p in CPINS:
				self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
			for p in CPINS:
				self.PI.set_PWM_dutycycle(p,x)
		sleep(0.05)
	def violet(self):
		VPINS = [self.PINS[0],self.PINS[2]]
		for i in range(0, self.CYCLES*360, 5):
			for p in VPINS:
				self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
			for p in VPINS:
				self.PI.set_PWM_dutycycle(p,x)
		sleep(0.05)
	def yellow(self):
		YPINS = [self.PINS[0],self.PINS[1]]
		for i in range(0, self.CYCLES*360, 5):
			for p in YPINS:
				self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
			for p in YPINS:
				self.PI.set_PWM_dutycycle(p,x)
		sleep(0.05)
	def rgb(self):
		freq = [0.5,1,2]
		for i in range(0, self.CYCLES*360, 5):
			for idx, p in enumerate(self.PINS):
				self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, freq[idx])))
			sleep(0.05)
		for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
			for p in self.PINS:
				self.PI.set_PWM_dutycycle(p,x)
		sleep(0.05)

	def main(self):
		self.white()
		self.red()
		self.green()
		self.blue()
		self.cyan()
		self.violet()
		self.yellow()
		self.rgb()

	if __name__ == '__main__':
		main()