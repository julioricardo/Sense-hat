#!/usr/bin/python

#Este ejercicio la letra J en color rojo

from sense_hat import SenseHat
import sys
tecla=""

sense=SenseHat()
sense.clear()
while tecla!="s":
	sense.show_letter("J",text_colour=[255,123,123])
	tecla=sys.stdin.read(1)
sense.clear()
