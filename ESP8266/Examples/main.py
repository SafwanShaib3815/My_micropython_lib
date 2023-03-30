from machine import UART, Pin
import time


uart = UART(1, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

while True:
    if uart.any():
        data = uart.read()
        print(data.decode())
        time.sleep(1)
    else:
        print("trying in 3 seconds...")
        time.sleep(3)


