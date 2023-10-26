#GPIO  2 & 3  pin 4 and 5 are the output
#Need to use Micropython v1.19 for the wavePlayer class to work

import os as uos
import wavePlayer
from utime import sleep_us
player = wavePlayer.wavePlayer()
from machine import PWM, Pin
import _thread

flag=None
led = Pin(20, Pin.OUT, Pin.PULL_DOWN)
motion = Pin(21, Pin.IN)
amplifier_sd = Pin(14, Pin.OUT, Pin.PULL_DOWN) # Shutdown amplifier
          
def slow_fade():
    pwm = PWM(led)
    # Set the PWM frequency.
    pwm.freq(1000)
    while True:
        # Fade in
        sleep_us(200000)
        for duty_cycle in range(0, 255*255, 6):
            pwm.duty_u16(duty_cycle)
            sleep_us(250)  # Adjust the delay for desired fade-in speed
            if motion.value(): #break and release when no motion detected
                return
        # Fade out
        for duty_cycle in range(255*255, -1, -6):
            pwm.duty_u16(duty_cycle)
            sleep_us(180)  # Adjust the delay for desired fade-out speed
            if motion.value(): #break and release when no motion detected
#                 sLock.release() #release resources used
                return
            
def fast_fade():
    pwm = PWM(led)
    # Set the PWM frequency.
    pwm.freq(1000)
    for i in range(4):
        global flag
        # Fade in
        for duty_cycle in range(0, 255*255, 6):
            pwm.duty_u16(duty_cycle)
            sleep_us(48)  # Adjust the delay for desired fade-in speed
        # Fade out
        for duty_cycle in range(255*255, -1, -6):
            pwm.duty_u16(duty_cycle)
            sleep_us(48)  # Adjust the delay for desired fade-out speed
    led_blink = Pin(20, Pin.OUT, Pin.PULL_DOWN)
    
    for i in range(11):
        led_blink.on()
        sleep_us(199990)
        led_blink.off()
        sleep_us(200000)
    for i in range(19):
        led_blink.on()
        sleep_us(70000)
        led_blink.off()
        sleep_us(50000)
    while True:
        if flag:
            return           
            
def play_sound():
    # run this on core 1
    try:
        global flag
        flag = 0
        amplifier_sd.value(1) #Turn on amplifier
        player.play("sounds/Martian War Machine.wav")
        flag=1
        amplifier_sd.value(0) #shutdown amplifier
    except KeyboardInterrupt:
        player.stop()
        print("wave player terminated")
       

def main():
    while not motion.value():
        slow_fade()
        if motion.value():
            _thread.start_new_thread(play_sound, ())
            fast_fade()
        
if __name__ == "__main__":
    main()

