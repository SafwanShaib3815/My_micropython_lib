#Blinks a led continuesly, provide GPIO pin number as an argument
import sys
import time
import RPi.GPIO as GPIO


def blink_led(argv):
    #if len(sys.argv) < 2:
    if argv == None: 
        #print("Provide a GPIO pin number based on the BCM mode")
        #exit(0)
        exit(1) 
    #pin=int(sys.argv[1])
    pin=int(argv)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    try:
        while 1:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.05)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.95)
    except KeyboardInterrupt:
        #exit(0)
        return
    GPIO.cleanup()
if __name__ == "__blink_led__":
    blink_led() 
