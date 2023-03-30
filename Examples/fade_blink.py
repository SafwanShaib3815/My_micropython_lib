from machine import Pin, Timer, PWM
import time

def fade(timer):
    # Construct PWM object, with LED on Pin(25).
    pwm = PWM(Pin(25))

    # Set the PWM frequency.
    pwm.freq(1000)

#     tim = Timer()
    duty = 0
    direction = 1
    while True:
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
#     tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

led = Pin(25, Pin.OUT)

    
def blink(blink):
    led = Pin(25, Pin.OUT)
    while True:
        led.high()
        time.sleep(0.45)
        led.low()
        time.sleep(0.1)
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)
        led.high()
        time.sleep(0.05)
        led.low()
        time.sleep(0.05)
    


if __name__ == "__main__":
    fade(1)
    blink(1)