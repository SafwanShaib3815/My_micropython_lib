from machine import Pin, PWM
import time

trigger_pin = 4
echo_pin = 5
buzzer_pin = 11  # Replace with your buzzer pin number
trigger = Pin(trigger_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)
buzzer = PWM(Pin(buzzer_pin))

while True:
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    while echo.value() == 0:
        pass # wait for echo
    start = time.ticks_us() # record the time when signal went HIGH
    while echo.value() == 1:
        pass # wait for echo to finish
    duration = time.ticks_us() - start
    distance = duration / 58
    print("Distance: {:.2f} cm".format(distance))
    frequency = 50 + (distance - 10) * 10
    if frequency < 50:
        frequency = 50
    elif frequency > 1000:
        frequency = 1000
    print("Frequency: {:.0f} Hz".format(frequency))
    buzzer.freq(int(frequency))
    buzzer.duty_u16(1000)
    time.sleep(0.01)
