from machine import Pin, PWM
from utime import sleep

# lower right corner with USB connector on top
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

# play a C major chord
speaker.freq(262) # C4
speaker.duty_u16(15000)
sleep(0.5)
speaker.freq(330) # E4
sleep(0.5)
speaker.freq(392) # G4
sleep(0.5)

# fade out the chord
for i in range(15000, 0, -1000):
    speaker.duty_u16(i)
    sleep(0.01)

# turn off the PWM 
speaker.duty_u16(0)
