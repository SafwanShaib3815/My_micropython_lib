from machine import Pin, PWM
from utime import sleep

SPEAKER_PIN = 16
SPEAKER_PIN1 = 17

# create a Pulse Width Modulation Object on this pin
speaker = PWM(Pin(SPEAKER_PIN))
speaker1 = PWM(Pin(SPEAKER_PIN1))


# define the notes with their frequencies
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

# define a list of notes for a simple melody
melody = [C4, C4, G4, G4, A4, A4, G4]

# define the corresponding duration for each note
# (in seconds)
duration = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 1]

# define the duty cycle values for the volume modulation
duty_cycles = [3000, 6000, 9000, 12000, 15000, 18000, 21000]

# play the melody
for i, note in enumerate(melody):
    speaker.freq(note)
    speaker.duty_u16(duty_cycles[i % len(duty_cycles)])
    sleep(duration[i])
    speaker.duty_u16(0)
    speaker1.duty_u16(0)
    sleep(0.05)
