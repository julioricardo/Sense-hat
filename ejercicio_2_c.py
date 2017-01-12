#!/usr/bin/python

from sense_hat import SenseHat 
from time import sleep 
from random import randint 
import random
import sys
import time

sense = SenseHat() 
tecla=""

while tecla!="s":
	sense.clear()
	r1 = randint(0,255)
	r2=randint(0,255)
	
	sense.show_letter("U", text_colour=[r1, 125, r2])
	sleep(1) 

	r1= randint(0,255)
	r2=randint(0,255)
	
	sense.show_letter("C", text_colour=[123, r2, r1]) 
	sleep(1) 

	r1 = randint(0,255) 
	r2=randint(0,255)

	
	sense.show_letter("L", text_colour=[r1, r2, 255]) 
	sleep(1) 
	sense.show_letter("M", text_colour=[r2, r1, 0], back_colour=[r1, 255, 255]) 
	sleep(1) 
	tecla=sys.stdin.read(1)
sense.clear()
