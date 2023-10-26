# Example using PWM to fade an LED.

import time
from machine import Pin, PWM

# Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(5))

# Set the PWM frequency.
pwm.freq(1000)

# Fade the LED in and out a few times.
def fade_led(blink):
    duty = 0
    direction = 1
    while True:
    #for _ in range(8 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
if __name__ == "__main__":
    fade_led(1)