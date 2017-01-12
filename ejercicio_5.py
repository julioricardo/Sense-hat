#!/usr/bin/python





import time
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

 
angles=[0,90,180,270,0,90,180,270,0]
for r in angles:
	sense.set_rotation(r)
	time.sleep(1)





