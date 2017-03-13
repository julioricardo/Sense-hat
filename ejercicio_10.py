#!/usr/bin/python

import time
import sys
from sense_hat import SenseHat 
 
sense = SenseHat() 
sense.clear()
 
sense.show_letter("A")
while True:
	try:
		acceleration=sense.get_accelerometer_raw()
		x=acceleration['x']
		y=acceleration['y']
		z=acceleration['z']
		x=round(x,0)
		y=round(y,0)
		z=round(z,0)
		if x == -1: 
			sense.set_rotation(180) 
		elif y == 1: 
			sense.set_rotation(90) 
		elif y == -1: 
			sense.set_rotation(270) 
		else: 
			sense.set_rotation(0) 
		
		print("X={0},Y={1},Z={2}".format(x,y,z))
		#time.sleep(1)
	except KeyboardInterrupt:
		sense.clear()
		sys.exit() 
