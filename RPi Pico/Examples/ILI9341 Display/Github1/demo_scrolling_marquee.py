"""ILI9341 demo (Scrolling Marquee)."""
from ili9341 import Display, color565
from time import sleep
from sys import implementation
from machine import Pin

# SPI pins configuration
spi_bus=0
sck=Pin(2)
mosi=Pin(3)
baudrate=40000000




def test():
    """Scrolling Marquee."""
    try:
        # Implementation dependant pin and SPI configuration
        if implementation.name == 'circuitpython':
            import board
            from busio import SPI
            from digitalio import DigitalInOut
            cs_pin = DigitalInOut(board.P0_15)
            dc_pin = DigitalInOut(board.P0_17)
            rst_pin = DigitalInOut(board.P0_20)
            spi = SPI(clock=board.P0_24, MOSI=board.P0_22)
        else:
            from machine import SPI
            # Display pins configuration
            cs_pin=Pin(22)
            dc_pin=Pin(11)
            rst_pin=Pin(20)
            # Baud rate of 40000000 seems about the max
            spi = SPI(spi_bus, baudrate=baudrate, sck=sck, mosi=mosi)

        # Create the ILI9341 display:
        display = Display(spi, dc=dc_pin, cs=cs_pin, rst=rst_pin)
        display.clear()

        # Draw non-moving circles
        display.fill_rectangle(0, 0, 239, 99, color565(27, 72, 156))
        display.fill_rectangle(0, 168, 239, 151, color565(220, 27, 72))

        # Load Marquee image
        display.draw_image('images/Rototron128x26.raw', 56, 120, 128, 26)

        # Set up scrolling
        display.set_scroll(top=152, bottom=100)

        spectrum = list(range(152, 221)) + list(reversed(range(152, 220)))
        while True:
            for y in spectrum:
                display.scroll(y)
                sleep(.1)

    except KeyboardInterrupt:
        display.cleanup()


test()
