from time import sleep

from machine import Pin

from machine import PWM

pwm = PWM(Pin(10))

pwm.freq(50)

#Function to set an angle

#The position is expected as a parameter

def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.0029)

def closedoor():
    for pos in range(1000,8400,100):
        if pwm.duty_u16() == 8949: #don't open if it's already open
            break
        else:
            setServoCycle(pos)


def opendoor():
    for pos in range(9000,5000,-2):
        if pwm.duty_u16() == 1049: #don't close if it's already closed
            break
        else:
            setServoCycle(pos)


def main():
    opendoor()
    print(pwm.duty_u16())
    sleep(1)
    closedoor()
    print(pwm.duty_u16())
if __name__ == "__main__":
    main()
    
