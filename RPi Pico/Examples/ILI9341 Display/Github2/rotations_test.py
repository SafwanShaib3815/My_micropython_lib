from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import tt14, tt24, tt32

text = 'Safwan'
spi = SPI(0, baudrate=20000000, miso=Pin(0),mosi=Pin(3), sck=Pin(2))
display = ILI9341(spi, cs=Pin(22), dc=Pin(11), rst=Pin(20), w=320, h=240, r=0)
display.erase()
display.set_font(tt32)
display.set_pos(0,0)
display.print(text)
display.set_pos(0,50)
display.print(text)
display.set_pos(80,50)
display.print(text)

