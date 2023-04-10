'''
Brief: This program is a fire simulation led circuit, using two effects (random fade & flicker) uses 10 GP pins
Date: SEP 7  2022
Author: Safwan Shaib
Email: sh5safwan@hotmail.com
Detailed: This program employes the Raspberry pi pico's two cores to simulate fire by a group of 10 GPIO pins.
for that purpose two effects are used, fade and flicker, these effects work simultainously together on each core using threading
and randomly pick led's to fade or flicker.
Features: The program has 3 speeds and two modes, in de


'''

from time import sleep
from machine import Pin
from random import randint
from machine import PWM
from time import sleep
import time
import _thread

sLock = _thread.allocate_lock()

#based on gpio numbers
outer_leds = [5,10,13,14,21,18] 
inner_leds = [6,7,8]
speed = 0.09 #initial flickering speed
counter = 1 #used to change flickering speed

mode_button = Pin(20, Pin.IN, Pin.PULL_UP) # create a machine.Pin object for the button
indicator = Pin(25, Pin.OUT)
washer_leds = Pin(22, Pin.OUT)
fade_thread_running = True
flicker_running = True

#fades provided leds in and out
def rand_fade(leds):
    sLock.acquire()
    duty = 0
    direction = 1
    while True:
        random_led = randint(0,len(leds)-1) #pick a random index number based on the length of fade_leds list as a limit
        fade_limit = 0
        while True:
            pwm = PWM(Pin(leds[random_led])) #use obtained index to pick an LED from the list
            pwm.freq(1000)# Set the PWM frequency
            duty += direction 
            if duty > 255: # when duty reaches 256
                duty = 255 # don't allow it to exceed 255
                direction = -1 #this will make duty count backwards allowing it to start to fade out
                fade_limit += 1 # fade_limit is 1
            elif duty < 0: # when duty reaches -1
                duty = 0 # don't allow it to go below zero
                direction = 1 #this will make duty count forwards allowing it to start to fade in
                fade_limit += 1 #fade_limit is 2
            pwm.duty_u16(duty * duty)
            sleep(0.005)
            if fade_limit == 2: #When fade_limits becomes 2 (fade in and out once)
                break #break loop to pick another led to fade
        if not fade_thread_running: # When this flag is false
            sLock.release() #release resources used and return to main
            return 
# flickers a group of leds based on provided flickering speed 
def rand_flicker(speed,leds):
    while True:
        indicator.high()
        for led in leds: #loop throgh leds
            led_pwm = PWM(Pin(led))
            led_pwm.freq(1000) # Set the PWM frequency
            led_pwm.duty_u16(randint(0,25)*8000)
            sleep(speed) #sleep by provided speed (using the on-board mode button)
            indicator.low()
            if mode_button.value() == 0 or not flicker_running: #when mode button is clicked, return to update function parameter with a different speed
                return
        

def main():
    while True:
        #tuggle on the on-board green indicator 
        for _ in range(3):
            indicator.low()
            sleep(0.08)
            indicator.high()
            sleep(0.02)
            
        global speed
        global counter
        global fade_thread_running, flicker_running # define as globl variables
        fade_thread_running = False  # stop thread
        flicker_running = False # return from flicker function
        sleep(3) # allow time for thread to stop and function to return
        
        # Global variable flags to allow fade/flicker functions to run
        fade_thread_running = True 
        flicker_running = True
        
        washer_leds.high() #these are three leds that stay on all the time
        
        _thread.start_new_thread(rand_fade, (inner_leds,))
        rand_flicker(speed, outer_leds) 
        #stay here until the button is pressed
        
        
        ####button settings####
        print("returning from flicker, speed was:", speed)
        print("counter now is:", counter)
        
        while True:
            indicator.low() 
            start_time = time.time() # record the start time of the button press
            while mode_button.value() == 0: # wait for the button to be released
                sleep(0.1)
            press_duration = time.time() - start_time # calculate the duration of the button press
            indicator.high()
            
            if press_duration >= 2: #if long press on button
                
                for _ in range(10):
                    indicator.low()
                    sleep(0.02)
                    indicator.high()
                    sleep(0.08)
                    
                global fade_thread_running, flicker_running # define as globl variables
                fade_thread_running = False  # stop thread
                flicker_running = False # return from flicker function
                sleep(3) # allow time for thread to stop and function to return
                #flip led lists to opposite
                outer_leds_fade = [5,10,13,14,21,18] 
                inner_leds_flicker = [6,7,8]
                # Global variable flags to allow fade/flicker functions to run
                fade_thread_running = True 
                flicker_running = True
                print("\n\n\nEntering second mode with flickering speed:", speed, "\n\n\n")
                _thread.start_new_thread(rand_fade, (outer_leds_fade,))
                rand_flicker(speed, inner_leds_flicker)

            else:
                counter +=1 #next mode
                print("counter after incrementing:", counter)
                if   counter == 1: #fastest flickering speed setting
                     speed = 0.09
                     print("First speed option, speed now is:", speed, "\n\n\n")
                     
                elif counter == 2: #medium flickering speed setting
                    speed = 0.17
                    print("Second speed option, speed now is:", speed, "\n\n\n")

                elif counter ==3:  #slowest flickering speed setting
                    speed = 0.33
                    print("Third speed option, speed now is:", speed, "\n\n\n")

                    counter = 0
                    print("Counter has been reset", counter, "\n\n\n")

            break
if __name__ == "__main__":
    main()
