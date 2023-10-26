from machine import Pin, PWM
from utime import sleep

# Define the pins and create a PWM object
SPEAKER_PIN = 16
speaker = PWM(Pin(SPEAKER_PIN))

# Define the notes in the C major scale
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

# Define the phrases of the melody
phrases = [
    ['C4', 'D4', 'E4', 'C4', 'E4', 'D4', 'C4', 'E4', 'D4', 'C4'],
    ['G4', 'A4', 'B4', 'G4', 'B4', 'A4', 'G4', 'B4', 'A4', 'G4'],
    ['F4', 'G4', 'A4', 'F4', 'A4', 'G4', 'F4', 'A4', 'G4', 'F4']
]

# Define the duty cycle patterns for different notes
duty_patterns = {
    'C4': [0, 32767, 0, 0],
    'D4': [0, 8192, 32767, 8192, 0, 0],
    'E4': [0, 8192, 16384, 32767, 16384, 8192, 0, 0],
    'F4': [0, 4096, 8192, 16384, 32767, 16384, 8192, 4096, 0, 0],
    'G4': [0, 4096, 8192, 16384, 24576, 32767, 24576, 16384, 8192, 4096, 0, 0],
    'A4': [0, 2048, 4096, 8192, 16384, 24576, 32767, 24576, 16384, 8192, 4096, 2048, 0, 0],
    'B4': [0, 2048, 4096, 8192, 12288, 16384, 24576, 32767, 24576, 16384, 8192, 4096, 2048, 0, 0],
    'C5': [0, 1024, 2048, 4096, 8192, 12288, 16384, 24576, 32767, 24576, 16384, 8192, 4096, 2048, 1024, 0]
}

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for note_name in phrase:
            # Get the frequency and duty cycle pattern of the current note
            freq = notes[note_name]
            duty_pattern = duty_patterns[note_name]
            # Play the note for the specified duration and duty cycle pattern
            for duty_cycle in duty_pattern:
                speaker.freq(freq)
                speaker.duty_u16(duty_cycle)
                sleep(0.02)
