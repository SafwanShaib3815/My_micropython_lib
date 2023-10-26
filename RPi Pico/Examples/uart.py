from machine import UART, Pin
import time

#initializing the UART protocol
uart = UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)

# initializing the PIR motion sensor's input pin
# pir=machine.Pin(16, machine.Pin.IN)
# 
# while True:
#     if pir.value() == 1:
#         uart.write("Motionnnn DDDDetected")
#         print("Motion Detected!")
#         time.sleep(1)
#     else:
#         print("No motion Detected")
#     time.sleep(0.5)  #Delay for 0.5 second
#     


#uncomment if you wanna read from uart
while True:
    if uart.any():
        data = uart.read()
        print(data.decode('utf-8'))
        time.sleep(1)
    else:
        print("trying in 3 seconds...")
        time.sleep(3)

