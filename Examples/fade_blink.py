from machine import Pin, Timer, PWM
from time import sleep
from utime import sleep_us

led = Pin(25, Pin.OUT)

def fade(timer):
    # Construct PWM object, with LED on Pin(25).
    pwm = PWM(led)

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
        sleep(0.001)
#     tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

def fade2(speed):
    pwm = PWM(led)
    # Set the PWM frequency.
    pwm.freq(1000)
    while True:
        # Fade in
        for duty_cycle in range(0, 255*255, 4):
            pwm.duty_u16(duty_cycle)
            sleep_us(speed)  # Adjust the delay for desired fade-in speed

        # Fade out
        for duty_cycle in range(255*255, -1, -4):
            pwm.duty_u16(duty_cycle)
            sleep_us(speed)  # Adjust the delay for desired fade-out speed

led = Pin(25, Pin.OUT)
def blink(blink):
    led = Pin(25, Pin.OUT)
    while True:
        led.high()
        sleep(0.45)
        led.low()
        sleep(0.1)
        led.high()
        sleep(0.1)
        led.low()
        sleep(0.1)
        led.high()
        sleep(0.05)
        led.low()
        sleep(0.05)
    


if __name__ == "__main__":
    fade(1)
    blink(1)