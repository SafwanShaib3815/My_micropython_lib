# Pico Wifi Module
# Pico Companion code

from machine import UART
uart = UART(1,baudrate=115200) #setting uart channel 1 on rpi pico pins 6 and 7
uart.init(115200, bits=8, parity=None, stop=1)

print("hello World from pico")
uart.write("hello")
while True:
    if uart.any() > 0:
        try:
            msg = str(uart.read(),'utf-8','ignore')
            print(msg)
        except:
            pass
        