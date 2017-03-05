#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep
from random import randint
import random
import sys


sense = SenseHat()

x=0
y=0
while True:
	try:
        	sense.clear()
        	r1 = randint(0,255)
        	r2=randint(0,255)
		x=randint(0,7)
		y=randint(0,7)
        	sense.set_pixel(x,y,[r1,r2,127])
        	r1= randint(0,255)
        	r2=randint(0,255)
		x=randint(0,7)
        	y=randint(0,7)
		r1 = randint(0,255)
        	r2=randint(0,255)
        	sense.set_pixel(x,y,[r2,r1,255])
	except KeyboardInterrupt:
        	sense.clear()
		sys.exit()

 

