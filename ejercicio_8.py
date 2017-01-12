#!/usr/bin/python





import time
import sys
from sense_hat import SenseHat 
 
sense = SenseHat() 




 

sense.clear()
 

while True:
	try:
		orientation=sense.get_orientation()
		pitch=orientation['pitch']
		roll=orientation['roll']
		yaw=orientation['yaw']
		print("Pitch={0},Roll={1},Yaw={2}".format(pitch,yaw,roll))
		time.sleep(1)
	except KeyboardInterrupt:
		sense.clear()
		sys.exit() 





