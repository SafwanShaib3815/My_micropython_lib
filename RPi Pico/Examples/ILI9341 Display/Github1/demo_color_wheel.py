"""ILI9341 demo (color wheel).

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

s"""
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from math import cos, pi, sin

HALF_WIDTH = const(120)
HALF_HEIGHT = const(160)
CENTER_X = const(119)
CENTER_Y = const(159)
ANGLE_STEP_SIZE = 0.05  # Decrease step size for higher resolution
PI2 = pi * 2

# SPI pins configuration
spi_bus=0
sck=Pin(2)
mosi=Pin(3)
baudrate=40000000

# Display pins configuration
dc=Pin(11)
cs=Pin(22)
rst=Pin(20)

def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB (based on colorsys.py).

        Args:
            h (float): Hue 0 to 1.
            s (float): Saturation 0 to 1.
            v (float): Value 0 to 1 (Brightness).
    """
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    v = int(v * 255)
    t = int(t * 255)
    p = int(p * 255)
    q = int(q * 255)

    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    spi = SPI(spi_bus, baudrate=baudrate, sck=sck, mosi=mosi)
    display = Display(spi, dc=dc, cs=cs, rst=rst)

    x, y = 0, 0
    angle = 0.0
    #  Loop all angles from 0 to 2 * PI radians
    while angle < PI2:
        # Calculate x, y from a vector with known length and angle
        x = int(CENTER_X * sin(angle) + HALF_WIDTH)
        y = int(CENTER_Y * cos(angle) + HALF_HEIGHT)
        color = color565(*hsv_to_rgb(angle / PI2, 1, 1))
        display.draw_line(x, y, CENTER_X, CENTER_Y, color)
        angle += ANGLE_STEP_SIZE

    sleep(5)

    for r in range(CENTER_X, 0, -1):
        color = color565(*hsv_to_rgb(r / HALF_WIDTH, 1, 1))
        display.fill_circle(CENTER_X, CENTER_Y, r, color)

    sleep(9)
    display.cleanup()


test()
