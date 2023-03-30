import RPi.GPIO as GPIO
import time

servoOUT = 19
tempOUT = 26


def open_door():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 19 for PWM with 50Hz
    p.start(2.5) # Initialization


    try:
        p.ChangeDutyCycle(2)
        time.sleep(3)
        p.ChangeDutyCycle(9)
        time.sleep(0.7)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

def close_door():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoOUT, GPIO.OUT)
        GPIO.setup(tempOUT, GPIO.OUT)
        GPIO.output(tempOUT, GPIO.HIGH)
        p = GPIO.PWM(servoOUT, 50)  #GPIO 13 for PWM with 50Hz
        p.start(0) # Initialization
        p.ChangeDutyCycle(12.6) #close the door
        time.sleep(0.7)
        p.ChangeDutyCycle(1.6) #open the door
        time.sleep(0.7)
    except KeyboardInterrupt:
        p.stop()
    GPIO.cleanup()

        
    
