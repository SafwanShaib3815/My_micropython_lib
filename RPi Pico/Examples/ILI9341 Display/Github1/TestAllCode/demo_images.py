"""ILI9341 demo (images).

Pin configuration:
Display	>>>>>	PICO

<"SPI1" interface>
T_IRQ	>>>>>	GP 5
T_DO	>>>>>	GP 15
T_DIN	>>>>>	GP 8
T_CS	>>>>>	GP 9
T_CLK	>>>>>	GP 10


<"SPI0" interface>
MISO	>>>>>	GP 0
LED		>>>>>	3.3V
SCK		>>>>> 	GP 2
MOSI	>>>>> 	GP 3
DC		>>>>>	GP 11
REST	>>>>>	GP 20	
CS		>>>>>	GP 22
GND		>>>>>	GND
VCC		>>>>>	3.3V
"""
from time import sleep
from ili9341 import Display
from machine import Pin, SPI

# SPI pins configuration
spi_bus=0
sck=Pin(2)
mosi=Pin(3)
baudrate=40000000

# Display pins configuration
dc=Pin(11)
cs=Pin(22)
rst=Pin(20)

def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    spi = SPI(spi_bus, baudrate=baudrate, sck=sck, mosi=mosi)
    display = Display(spi, dc=dc, cs=cs, rst=rst)

    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(2)

    display.draw_image('images/MicroPython128x128.raw', 0, 129, 128, 128)
    sleep(2)

    display.draw_image('images/Tabby128x128.raw', 112, 0, 128, 128)
    sleep(2)

    display.draw_image('images/Tortie128x128.raw', 112, 129, 128, 128)
    sleep(9)

    display.cleanup()


