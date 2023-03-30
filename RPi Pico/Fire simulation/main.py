#This program is a fire simulation led circuit, using two effects (fade & flame random blink) uses 10 GP pins
#Author: Safwan Shaib
#Date: SEP 7  2022

from time import sleep
from machine import Pin
from random import randint
from machine import PWM
from time import sleep
import _thread
lock = _thread.allocate_lock()

flame_leds = [5,10,13,14,21,18]
fade_leds = [6,7,8]
switch_counter = Pin(20, Pin.IN, Pin.PULL_UP)
indicator = Pin(25, Pin.OUT)
white_led = Pin(22, Pin.OUT)


def setServoCycle (position):
    led_pwm.duty_u16(position)
    sleep(0.0029)


def fade(pins_lst):
    duty = 0
    direction = 1
    while True:
        for pin in pins_lst:
            pwm = PWM(Pin(pin))
            # Set the PWM frequency.
            pwm.freq(1000)
            duty += direction
            if duty > 255:
                duty = 255
                direction = -1
            elif duty < 0:
                duty = 0
                direction = 1
            pwm.duty_u16(duty * duty)
            sleep(0.01)
    

def rand_flame(speed):
    while True:
        for led in flame_leds:
            led_pwm = PWM(Pin(led))
            led_pwm.freq(50)
            # Set the PWM frequency.
            led_pwm.freq(1000)
            led_pwm.duty_u16(randint(0,200)*1000)
            sleep(speed)
            if switch_counter.value() == 0:
                return

def main():
    indicator.high()
    white_led.high()
    _thread.start_new_thread(fade, (fade_leds,))
    counter = 1
    while True:
        if switch_counter.value() == 0:
            indicator.low()
            sleep(0.15)
            indicator.high()
            counter +=1

        if counter > 5:
            counter = 1
        
        if counter == 1:
            
            rand_flame(0.1)
        elif counter == 2:
            rand_flame(0.2)
        elif counter ==3:
            rand_flame(0.3)
        elif counter == 4:
            rand_flame(0.4)
        else:
            rand_flame(0.5)
            
if __name__ == "__main__":
    main()