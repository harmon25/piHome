#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmoN
# @Date:   2015-04-04 02:25:29
# @Last Modified by:   harmoN
# @Last Modified time: 2015-04-06 00:36:40
from time import sleep

class PulserPi(object):
	'''
	Notification Light
	'''
	def __init__(self, pi):
		self.PI=pi
		self.PINS=[22, 23, 24]
	def set_pins(self, red=22, green=23, blue=24):
		if not isinstance(red, int) or not isinstance(green, int) or not isinstance(blue, int):
			print("One of those is not an integer...")
			return
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
	def pulse(self, colour="w"):
		from math import sin, radians
		def PosSinWave(amplitude, angle, frequency):
			return amplitude + (amplitude * sin(radians(angle)*frequency) )
		setup = self.check_setup()
		CYCLES=1
		#white
		if not setup[0]:
			return print(setup[1])
		else:
			if colour == "w":
				for i in range(0, CYCLES*360, 5):
					for p in self.PINS:
						self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, 1)))
						sleep(0.05)
				for p in self.PINS:
					for x in range(self.PI.get_PWM_dutycycle(p), 255 ,5):
						print(x)
						self.PI.set_PWM_dutycycle(p,x)
						sleep(0.05)
			#red
			elif colour == "r":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[0], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[0], 1)
			#blue
			elif colour == "b":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[2], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[2], 1)
			#green
			elif colour == "g":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[1], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[1], 1)
			#cyan
			elif colour == "c":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[1], int(PosSinWave(125, i, 1)))
					self.PI.set_PWM_dutycycle(self.PINS[2], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[1], 1)
				self.PI.write(self.PINS[2], 1)
			#violet
			elif colour == "v":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[0], int(PosSinWave(125, i, 1)))
					self.PI.set_PWM_dutycycle(self.PINS[2], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[0], 1)
				self.PI.write(self.PINS[2], 1)
			#yellow
			elif colour == "y":
				for i in range(0, CYCLES*360, 5):
					self.PI.set_PWM_dutycycle(self.PINS[0], int(PosSinWave(125, i, 1)))
					self.PI.set_PWM_dutycycle(self.PINS[1], int(PosSinWave(125, i, 1)))
					sleep(0.05)
				self.PI.write(self.PINS[0], 1)
				self.PI.write(self.PINS[1], 1)
			#rgb tripp
			elif colour == "rgb":
				freq = [0.5,1,2]
				for i in range(0, CYCLES*360, 5):
					for idx, p in enumerate(self.PINS):
						self.PI.set_PWM_dutycycle(p, int(PosSinWave(125, i, freq[idx])))
					sleep(0.05)
				for pin in self.PINS:
					self.PI.write(pin, 1)