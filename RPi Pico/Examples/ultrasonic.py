#Source: Electrocredible.com, Language: MicroPython
from machine import Pin
import time
trigger_pin=4
echo_pin=5
trigger=Pin(trigger_pin, Pin.OUT)
echo=Pin(echo_pin, Pin.IN)

while True:
    trigger.high()
    time.sleep_us(11)
    trigger.low()
    while (echo.value()==0):
        pass #wait for echo
    lastreadtime=time.ticks_us() # record the time when signal went HIGH
    while (echo.value()==1):
        pass #wait for echo to finish
    echotime=time.ticks_us()-lastreadtime
    if echotime>37000:
        print("No obstacle detected")
    else:
        distance = (echotime * 0.034) / 2
        print("Obstace distance= {}cm".format(distance))
    time.sleep(0.5)