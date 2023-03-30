"""
Name: ocdoor.py
Description: Open/Close door using a 90G servo motor, includes main function to allow for seperate testings
Author: Safwan Shaib
Date: 1/29/2023
""" 




from machine import Pin, PWM
import time
# create a PWM object on pin D5
p14 =Pin(14)
pwm = PWM(p14)
pwm.freq(50)


def closedoor():
    for pos in range(75,129,1): #min 0 max 130
        if pwm.duty() == 128: #don't open if it's already open
            break
        else:
            pwm.duty(pos)
            time.sleep(0.0029)


def opendoor():
    for pos in range(129,75,-1):
        if pwm.duty() == 76: #don't close if it's already closed
            break
        else:
            pwm.duty(pos)
            time.sleep(0.029)



def main():
    opendoor()
    print(pwm.duty())
    time.sleep(2)
    print("closing door")
    closedoor()
    print("door closed")
    print(pwm.duty())
    time.sleep(2)
if __name__ == "__main__":
    main()
    
