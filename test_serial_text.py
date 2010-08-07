#!/usr/bin/env python
# encoding: utf-8

import os
import serial

###
### Test PySerial Read -- reads text over serial from controller (serial_text.pde)
### 'PySerial Read Test'.
###

class TestSerialText:
	def __init__(self):
		self.serialPort = '/dev/tty.usbserial-A900cfoR' # machine specific
		self.testString = "arduino"
		self.serial = None
	
	def setUp(self):
		self.serial = serial.Serial(self.serialPort, 9600, timeout=10) 

	def tearDown(self):
		self.serial.close()
				
	def test_read(self):
		"""
		Testing PySerial read.
		"""
		for i in range(0, 9):		
			data = self.serial.readline()
			if data:
				assert(cmp(data,str(i) + self.testString))
			else:
				print "Looping."

if __name__ == "__main__":
	x = TestSerialText()
	x.setUp()
	x.test_read()
