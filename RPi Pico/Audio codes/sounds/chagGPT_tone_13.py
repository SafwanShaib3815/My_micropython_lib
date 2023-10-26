import math
from machine import Pin, PWM
from utime import sleep

# Define the pins for the speakers
BEAT_PIN = 16
MELODY_PIN = 17

# Define the diatonic major scale
major_scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Define the frequencies for each note in the scale
major_freqs = [261, 294, 329, 349, 392, 440, 494]

# Define the length of each note in milliseconds
note_length = 500

# Create PWM objects for each speaker
beat_speaker = PWM(Pin(BEAT_PIN))
melody_speaker = PWM(Pin(MELODY_PIN))

# Loop through each note in the scale and play a beat on the beat_speaker
for i in range(len(major_scale)):
    # Play a low frequency tone on the beat_speaker every other note
    if i % 2 == 0:
        freq = 100
        duty_cycle = int(math.pow(2, 16) / 2 - 1)
    else:
        freq = 10
        duty_cycle = 0
    
    beat_speaker.freq(freq)
    beat_speaker.duty_u16(duty_cycle)
    
    # Play the melody note on the melody_speaker
    freq = major_freqs[i]
    period = int(1 / freq * 1000000)
    duty_cycle = int(math.pow(2, 16) / 2 - 1)
    
    melody_speaker.freq(freq)
    melody_speaker.duty_u16(duty_cycle)
    
    # Wait for the note to play
    sleep(note_length / 1000)
    
    # Stop the PWM objects
    beat_speaker.duty_u16(0)
    melody_speaker.duty_u16(0)
    
    sleep(0.1) # Pause between notes
