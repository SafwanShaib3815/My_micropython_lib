#a mouse trap code
import RPi.GPIO as GPIO
import time
import sys

import Blink
import Servo
from threading import Thread 


#sys.path.insert(0,'/home/pi/Desktop/Servo')#adding the servo.py path to the sys
GPIO.setwarnings(False)#disable warnings

motionIN=29
indicatorLedOut=37
stop_threads=False

def runfun(stop):
    while 1:
        GPIO.output(indicatorLedOut, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(indicatorLedOut, GPIO.LOW)
        time.sleep(0.95)
        if stop(): 
            break
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motionIN, GPIO.IN)#Read output from PIR motion sensor
GPIO.setup(indicatorLedOut, GPIO.OUT)#LED pin set to out

blink_thread = Thread(target=runfun, args=(lambda : stop_threads, ))#instenciating a thread for the blink task
blink_thread.start() #starting the thread


while True:
    i= GPIO.input(motionIN)
    if i == 0: #When output from motion sensor is LOW
        print ("Door is open, waiting for a mouse ",GPIO.input(motionIN))
        while True:
            time.sleep(0.01)
            if GPIO.input(motionIN) !=0:
                break
    elif i == 1:#When output from motion sensor is HIGH
        stop_threads=True
        blink_thread.join()
        print ("CLOSING DOOR IMEDEATELY!!",GPIO.input(motionIN))
        GPIO.output(indicatorLedOut, 1)  #Turn ON LED
        #from servo import close_door#importing the close_door function from servo.py script
        Servo.close_door()
        time.sleep(1)
        print("check for a mouse in the trap")
        break

GPIO.cleanup()
