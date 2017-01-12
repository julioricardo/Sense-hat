#!/usr/bin/python





import time
import sys
from sense_hat import SenseHat 
 
sense = SenseHat() 




sense = SenseHat() 

sense.clear()

v=[199,21,133]
gd=[1,128,128]
g=[173,255,47]
e = [0,0,0]
image = [e,e,e,e,e,e,e,e,
v,e,e,e,e,e,e,e,
e,v,e,e,v,e,v,e,
e,v,gd,gd,v,g,g,e,
e,gd,gd,gd,g,e,g,gd,
e,gd,gd,gd,gd,g,g,e, 
e,e,gd,e,gd,e,e,e,
e,e,e,e,e,e,e,e] 
sense.set_pixels(image) 

while True:
	try:
		time.sleep(1)
		sense.flip_h()
		time.sleep(1)
		sense.flip_v()
	except KeyboardInterrupt:
		sense.clear()
		sys.exit() 





