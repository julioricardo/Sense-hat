#!/usr/bin/python

#Este ejercicio muestra un mensaje en matriz de leds y se puede cambiar la velocidad del texto
#con la funcin scroll_speed. Adems, el color de fondo y del texto con las funciones back_colour y text_colour.
#pulsar s para salir

from sense_hat import SenseHat
import sys

sense=SenseHat()
sense.clear()
tecla=""
while True:
	if tecla=="s":
                sense.clear()
                break
	else:
		sense.show_message("Taller Raspberry Pi 3",scroll_speed=0.05,text_colour=[255,255,0],back_colour=[0,0,255])
	tecla=sys.stdin.read(1)

