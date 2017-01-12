#!/usr/bin/python
from sense_hat import SenseHat



sense=SenseHat()
sense.show_message("HELLO WORLD...")

sense.show_message("HOLA MUNDO..",scroll_speed=0.09, text_colour=[255,255,0],back_colour=[0,0,255])
sense.clear()
