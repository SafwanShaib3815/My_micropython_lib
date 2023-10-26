"""ILI9341 demo (simple touch demo)."""
from ili9341 import Display, color565
from xpt2046 import Touch
from machine import idle, Pin, SPI  # type: ignore

# SPI0 pins configuration
spi_bus0=0
sck0=Pin(2)
mosi0=Pin(3)
baudrate0=40000000

# SPI1 pins configuration
spi_bus1=1
sck1=Pin(10)
mosi1=Pin(15)
miso1=Pin(8)
baudrate1=1000000
T_cs=Pin(9)
T_int_pin=Pin(5)

# Display pins configuration
dc=Pin(11)
cs=Pin(22)
rst=Pin(20)

class Demo(object):
    """Touchscreen simple demo."""
    CYAN = color565(0, 255, 255)
    PURPLE = color565(255, 0, 255)
    WHITE = color565(255, 255, 255)

    def __init__(self, display, spi1):
        """Initialize box.

        Args:
            display (ILI9341): display object
            spi1 (SPI): SPI bus
        """
        self.display = display
        self.touch = Touch(spi1, cs=T_cs, int_pin=T_int_pin,
                           int_handler=self.touchscreen_press)
        # Display initial message
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "TOUCH ME",
                                  self.WHITE,
                                  background=self.PURPLE)

        # A small 5x5 sprite for the dot
        self.dot = bytearray(b'\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00')

    def touchscreen_press(self, x, y):
        """Process touchscreen press events."""
        # Y needs to be flipped
        y = (self.display.height - 1) - y
        # Display coordinates
        self.display.draw_text8x8(self.display.width // 2 - 32,
                                  self.display.height - 9,
                                  "{0:03d}, {1:03d}".format(x, y),
                                  self.CYAN)
        # Draw dot
        self.display.draw_sprite(self.dot, x - 2, y - 2, 5, 5)


def test():
    """Test code."""
    spi0 = SPI(spi_bus0, baudrate=baudrate0, sck=sck0, mosi=mosi0)
    display = Display(spi0, dc=dc, cs=cs, rst=rst)
    spi1 = SPI(spi_bus1, baudrate=baudrate1, sck=sck1, mosi=mosi1, miso=miso1)

    Demo(display, spi1)

    try:
        while True:
            idle()

    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        display.cleanup()


test()
