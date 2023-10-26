import machine
import time

# define trigger and echo pins
TRIGGER_PIN = 4
ECHO_PIN = 5

# set trigger pin as output and echo pin as input
trigger = machine.Pin(TRIGGER_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# function to calculate distance in cm
def distance():
    # send a 10us pulse to trigger pin
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    # measure pulse duration on echo pin
    pulse_time = machine.time_pulse_us(echo, 1, 1000000)
    
    # calculate distance in cm
    distance_cm = pulse_time / 58
    
    return distance_cm

# example usage
while True:
    dist = distance()
    print("Distance: {} cm".format(dist))
    time.sleep(1)
