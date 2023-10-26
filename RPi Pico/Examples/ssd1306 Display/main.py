from machine import Pin, SoftSPI
from time import sleep
import ssd1306
import shapes

spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))



dc = Pin(7)   # data/command
rst = Pin(8)  # reset
cs = Pin(5)  # chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)



# # Draw a line
# display.line(0, 0, 127, 0, 1)
# display.show()
# sleep(2)
# # Draw a rectangle
# display.rect(10, 10, 50, 50, 1)
# display.show()
# sleep(2)

# while True:
#     for name, bitmap in shapes.bitmaps.items():
#         shapes.draw_bitmap(bitmap, display, 10, 20)
#         sleep(3)
#         display.fill(0)
while True:
    for width in range(-55, 90, 10):
        for hieght in range(64, 0, -11):
            shapes.draw_bitmap(shapes.bitmaps['heart'], display, width, hieght)
        

