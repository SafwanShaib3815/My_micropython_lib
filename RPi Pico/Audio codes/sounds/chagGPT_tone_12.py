from machine import Pin, PWM
from utime import sleep

SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))

# define the notes with their frequencies for a C major scale
C4 = 261
D4 = 294
E4 = 329
F4 = 349
G4 = 392
A4 = 440
B4 = 493
C5 = 523

# define the notes with their frequencies for a C minor scale
Cm4 = 261
Dm4 = 293
Eb4 = 311
Fm4 = 349
Gm4 = 391
Ab4 = 415
Bb4 = 466
Cm5 = 523

# define the corresponding duration for each note
# (in seconds)
duration = 0.5

# define the duty cycle values for the volume modulation
duty_cycles = [5000, 7000, 9000, 11000, 13000, 15000, 17000, 19000]

# play the diatonic major scale
for i, note in enumerate([C4, D4, E4, F4, G4, A4, B4, C5]):
    speaker.freq(note)
    speaker.duty_u16(duty_cycles[i % len(duty_cycles)])
    sleep(duration)
    speaker.duty_u16(0)
    sleep(0.05)

# pause briefly between scales
sleep(0.5)

# play the diatonic minor scale
for i, note in enumerate([Cm4, Dm4, Eb4, Fm4, Gm4, Ab4, Bb4, Cm5]):
    speaker.freq(note)
    speaker.duty_u16(duty_cycles[i % len(duty_cycles)])
    sleep(duration)
    speaker.duty_u16(0)
    sleep(0.05)
