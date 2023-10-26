"""ILI9341 demo (fonts 8x8).

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
from ili9341 import Display, color565
from machine import Pin, SPI  # type: ignore

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
    spi = SPI(spi_bus, baudrate=baudrate, sck=sck, mosi=mosi)
    display = Display(spi, dc=dc, cs=cs, rst=rst)

    x_center = display.width // 2
    y_center = display.height // 2

    display.draw_text8x8(0, 0, 'Built-in', color565(255, 0, 255))
    display.draw_text8x8(16, 16, 'MicroPython', color565(255, 255, 0))
    display.draw_text8x8(32, 32, '8x8 Font', color565(0, 0, 255))
    
    display.draw_text8x8(x_center - 40, 120, "Rotate = 0",
                         color565(0, 255, 0))
    display.draw_text8x8(0, y_center - 44, "Rotate = 90",
                         color565(255, 0, 0), rotate=90)
    display.draw_text8x8(x_center - 48, display.height - 9, "Rotate = 180",
                         color565(0, 255, 255), rotate=180)
    display.draw_text8x8(display.width - 9, y_center - 48, "Rotate = 270",
                         color565(255, 255, 255), rotate=270)

    display.draw_text8x8(x_center - 40, 140, "Rotate = 0",
                         color565(0, 255, 0), background=color565(255, 0, 0))
    display.draw_text8x8(20, y_center - 44, "Rotate = 90", color565(255, 0, 0),
                         rotate=90, background=color565(0, 255, 0))
    display.draw_text8x8(x_center - 48, display.height - 29, "Rotate = 180",
                         color565(0, 255, 255), rotate=180,
                         background=color565(0, 0, 255))
    display.draw_text8x8(display.width - 29, y_center - 48, "Rotate = 270",
                         color565(255, 255, 255), rotate=270,
                         background=color565(255, 0, 255))

    sleep(15)
    display.cleanup()


test()
