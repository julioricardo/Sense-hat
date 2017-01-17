#!/usr/bin/python

#Este ejercicio escribe UCLM en color rojo

from sense_hat import SenseHat
from time import sleep
import sys



sense=SenseHat()
sense.clear()

sense.show_letter("U",text_colour=[255,0,0])
sleep(1)
sense.show_letter("C",text_colour=[0,0,255])
sleep(1)
sense.show_letter("L",text_colour=[0,255,0])
sleep(1)
sense.show_letter("M",text_colour=[0,0,0],back_colour=[255,255,255])
sleep(1)
sense.clear()

