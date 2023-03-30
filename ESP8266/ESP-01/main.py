from machine import UART
import time

#initializing the UART protocol
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

ctr = 0
while True:
    message = str(ctr)+"Hello pico pico it's ESP8266-01s here!\n"
    uart.write(message.encode('utf-8'))
    time.sleep(1)
    ctr+=1
    if uart.any():
        data = uart.read()
        print(data.decode())
        time.sleep(1)
#     else:
#         print("trying in 3 seconds...")
#         time.sleep(3)
# 
# 

