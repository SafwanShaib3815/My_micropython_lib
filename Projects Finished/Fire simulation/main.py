'''
Brief: This program is a fire simulation LED circuit, using two effects (random fade & flicker) uses 10 GP pins
Date: SEP 7  2022
Author: Safwan Shaib
Email: sh5safwan@hotmail.com
Detailed: This program employes the Raspberry pi pico's two cores to simulate fire by a group of 10 GPIO pins.
for that purpose two effects are used, fade and flicker, these effects work simultainously together on each core using threading
and randomly pick LED's to fade or flicker.

Features:
-The program has 2 modes and 3 speeds for each.
-First mode (always runs first as deafault) fades inner 3 LEDs in and out and flickers the outer 6 LEDs.
-Second mode is the opposite of that (inner LEDs flicker and outer ones fade).
-To toggle between speeds, short click on the button and wait 3 seconds (The speed can only be set while in the flicker mode).
-To set to the second mode, long click on the button (minimum of two seconds), then wait for 3 seconds.
-Short clicking while in the second mode will retrun back to the first mode.
-Thus the speed of the second mode flickering has to be set while in the first mode.
-Indicator LED indicates how fast the flickering is done, and blinks on changing mode or speed.
'''

from time import sleep
from machine import Pin
from random import randint
from machine import PWM
import time
import _thread

sLock = _thread.allocate_lock()

#Setting pins based on their GPIO numbers
outer_leds = [5,10,13,14,21,18] 
inner_leds = [6,7,8]
speed = 0.09 #Initial flickering speed
counter = 1 #Used to change flickering speed

mode_button = Pin(20, Pin.IN, Pin.PULL_UP) #create a machine.Pin object for the on-board button
indicator = Pin(25, Pin.OUT) #Create a machine.Pin object for the on-board green LED
washer_leds = Pin(22, Pin.OUT) #create a machine.Pin object for 3 LEDs that stay always ON
#Used to turn ON/OFF the fade and flicker affects
fade_thread_running = True
flicker_running = True

#Fades provided LEDs in and out
def rand_fade(leds):
    sLock.acquire() #Lock resources for this function
    duty = 0 #Used to set the duty-cycle of the LED
    direction = 1 #Used to control whether the led is fading in (1) or out (-1)
    #Repeats until stoped by fade_thread_running flag
    while True:
        random_led = randint(0,len(leds)-1) #Pick a random index number based on the length of fade_LEDs list as a limit
        fade_limit = 0 # Counts the number of fade-INs and fade-OUTs
        #Repeats on each fade-in and fade-out of an LED
        while True: 
            pwm = PWM(Pin(leds[random_led])) #use obtained index to pick an LED from the list
            pwm.freq(1000)# Set the PWM frequency
            duty += direction 
            if duty > 255: # When duty reaches 256
                duty = 255 # don't allow it to exceed 255
                direction = -1 #this will make duty count backwards allowing the LED to start to fade-OUT
                fade_limit += 1 # fade_limit becomes 1 here
            elif duty < 0: # when duty reaches -1
                duty = 0 # don't allow it to go below zero
                direction = 1 #this will make duty count forwards allowing the LED to start to Fade-IN
                fade_limit += 1 #fade_limit becomes 2 here
            pwm.duty_u16(duty * duty) #LEDs need big numbers to start to show light, this gives a good approximation
            sleep(0.005) #time between each duty cycle (controls how fast an LED fades IN or OUT
            if fade_limit == 2: #When fade_limits becomes 2 (when LED fades IN and OUT once)
                break #break loop to pick another LED to fade
        if not fade_thread_running: # When this flag is false
            sLock.release() #release resources used 
            return #exit thread (here this core will be available for another thread) 
        
# Flickers a given group of LEDs based on provided flickering speed 
def rand_flicker(speed,leds):
    #Repeats untill button press (long/short) or the flicker_flag is set to False
    while True:
        indicator.high() #Turns indicator ON during the flicker process
        for led in leds: #loop throgh LEDs
            led_pwm = PWM(Pin(led)) #Create a PWM object for the current led (no need to pick randomly since the brightness is changing randomly here)
            led_pwm.freq(1000) # Set the PWM frequency
            led_pwm.duty_u16(randint(0,25)*8000) #duty is random numbers between 0-2000k (25 possible numbers with a step of 80k (0,80k,160k,...))
            sleep(speed) #sleep by provided speed (using the on-board mode button)
            indicator.low() #Turns indicator OFF to indicate the flickering speed
            if mode_button.value() == 0 or not flicker_running: #when on-board button is clicked, or flicker_running flag is false 
                return #return to main (function parameters maybe updated)
        
#Main function
def main():
    print("\t\t\t\tSTARTING PROGRAM\n\n\n")
    #Repeats as long as the board is pluged in
    while True:
        print("Default mode start............\n\n") 
        #Toggle the on-board green indicator 3 times
        for _ in range(3):
            indicator.low()
            sleep(0.08)
            indicator.high()
            sleep(0.02)
        #Define the variables to be used globally    
        global speed 
        global counter 
        global fade_thread_running, flicker_running
        fade_thread_running = False  # stop the fade thread
        flicker_running = False # return from flicker function
        sleep(3) # allow time for thread to stop and function to return
        
        # Global variable flags to allow fade/flicker functions to run
        fade_thread_running = True 
        flicker_running = True
        
        washer_leds.high() # LEDs that stay on all the time
        
        _thread.start_new_thread(rand_fade, (inner_leds,)) #Start the default Fade affect
        rand_flicker(speed, outer_leds) #Start the default Flicker affect
        
        ################################################################################
        #stay here until the button is pressed
        ################################################################################
        
        ####Button Settings####
        print("Returning from flicker, speed was: ", speed, "and counter now is: ",counter)
        #Repeats whenever the button is clicked
        while True:
            indicator.low() #Indicator is OFF as long as the button is pressed
            start_time = time.time() # Record the start time of the button press
            while mode_button.value() == 0: # Wait for the button to be released
                sleep(0.1)
            press_duration = time.time() - start_time # Calculate the duration of the button press
            indicator.high() #Indicator is back ON after button release
            
            if press_duration >= 2: #If button was long-pressed
                #Toggle the on-board green indicator 10 times
                for _ in range(10):
                    indicator.low()
                    sleep(0.02)
                    indicator.high()
                    sleep(0.08)
                    
                global fade_thread_running, flicker_running # Define globl variables
                fade_thread_running = False  # Stop Fade function thread
                flicker_running = False # Return from flicker function
                sleep(3) # Allow time for thread to stop and function to return
                #Flip LED lists to opposite
                outer_leds_fade = [5,10,13,14,21,18] 
                inner_leds_flicker = [6,7,8]
                # Global variable flags to allow fade/flicker functions to run
                fade_thread_running = True 
                flicker_running = True
                print("\n\n\nSecond mode start with flickering speed: ", speed, "............\n\n")
                _thread.start_new_thread(rand_fade, (outer_leds_fade,)) #Start the second Fade affect
                rand_flicker(speed, inner_leds_flicker) #Start the second Flicker affect

            else:
                counter +=1 #Next speed
                if   counter == 1: #fastest flickering speed setting
                     speed = 0.09
                     print("First speed option, speed is changed to : ", speed, "\n\n\n")
                     
                elif counter == 2: #medium flickering speed setting
                    speed = 0.17
                    print("Second speed option, speed is changed to ", speed, "\n\n\n")

                elif counter ==3:  #slowest flickering speed setting
                    speed = 0.33
                    print("Third speed option, speed is changed to ", speed, "\n\n\n")

                    counter = 0
                    print("Counter has been reset to: ", counter, "\n\n\n")

            break
if __name__ == "__main__":
    main()
