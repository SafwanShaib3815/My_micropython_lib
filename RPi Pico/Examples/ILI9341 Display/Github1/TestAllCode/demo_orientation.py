"""ILI9341 demo (orientation).

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
VCC		>>>>>	3.3V"""

from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont

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
    print('Loading Espresso Dolce font...')
    espresso_dolce = XglcdFont('fonts/EspressoDolce18x24.c', 18, 24)
    print('Font loaded.')
    # Baud rate of 40000000 seems about the max
    spi = SPI(spi_bus, baudrate=baudrate, sck=sck, mosi=mosi)
    
    display = Display(spi, dc=dc, cs=cs, rst=rst,
					  width=240, height=320, rotation=0)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 0), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=dc, cs=cs, rst=rst,
					  width=320, height=240, rotation=90)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 255))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 255, 255), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=dc, cs=cs, rst=rst,
					  width=240, height=320, rotation=180)
    display.draw_text(0, 0, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 0, 255))
    display.draw_text(0, 319, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(255, 0, 0), landscape=True)
    sleep(5)
    
    display = Display(spi, dc=dc, cs=cs, rst=rst,
					  width=320, height=240, rotation=270)
    display.draw_text(0, 215, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(225, 0, 128))
    display.draw_text(295, 239, 'Espresso Dolce 18x24', espresso_dolce,
                      color565(0, 255, 0), landscape=True)
    sleep(5)
    display.cleanup()




