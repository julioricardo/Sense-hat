#!/usr/bin/python





import time
import sys
from sense_hat import SenseHat 
 
sense = SenseHat() 




 

sense.clear()

 

while True:
	try:
		t=sense.get_temperature()
		p=sense.get_pressure()
		h=sense.get_humidity()
		t=round(t,1)
		p=round(p,1)
		h=round(h,1)
		msg="Temp={0},Pres={1},Hum={2}".format(t,p,h)
		sense.show_message(msg,scroll_speed=0.1)
	except KeyboardInterrupt:
		sense.clear()
		sys.exit() 




