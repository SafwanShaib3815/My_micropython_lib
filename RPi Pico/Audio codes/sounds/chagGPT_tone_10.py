from machine import Pin, PWM
import math
from utime import sleep

# Define the pins and create a PWM object
SPEAKER_PIN = 16
speaker = PWM(Pin(SPEAKER_PIN))

# Define the notes in the C major scale and their frequencies
notes = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}

# Define the phrases of the melody
phrases = [
    ['C4', 'E4', 'G4', 'C5'],
    ['B4', 'D4', 'G4', 'B4'],
    ['A4', 'C4', 'E4', 'A4'],
    ['G4', 'B4', 'D4', 'G4']
]

# Define the duration of each note in seconds
note_duration = 0.5

# Define the number of cycles to play for each note
cycles_per_note = 50

# Define the duty cycle values for the melody
duty_cycle_values = [32767 * math.sin(2 * math.pi * x / 255) for x in range(256)]

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for note_name in phrase:
            # Get the frequency of the current note
            freq = notes[note_name]
            # Get the duty cycle value for the current note
            duty_cycle = [duty_cycle_values[int((x / cycles_per_note) * 255)] for x in range(cycles_per_note)]
            # Play the note for the specified duration
            for j in range(int(note_duration * cycles_per_note)):
                for dc in duty_cycle:
                    speaker.freq(int(freq))
                    speaker.duty_u16(int(dc))
                    sleep(1 / (freq * cycles_per_note))
            # Pause briefly between notes
            sleep(0.1)

# Turn off the PWM object
speaker.duty_u16(0)
