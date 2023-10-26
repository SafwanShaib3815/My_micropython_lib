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

# Define the duty cycles for each note
duty_cycles = [15000, 20000, 25000, 30000, 25000, 20000, 15000, 20000, 25000, 30000]

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for idx, note_name in enumerate(phrase):
            # Get the frequency and duty cycle of the current note
            freq = notes[note_name]
            duty_cycle = duty_cycles[idx]
            # Play the note for 0.25 seconds with the given duty cycle
            speaker.freq(freq)
            speaker.duty_u16(duty_cycle)
            sleep(0.25)
        # Pause for 0.25 seconds between phrases
        sleep(0.25)

# Turn off the PWM object
speaker.duty_u16(0)
