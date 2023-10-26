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

# Define the duty cycle values for the melody
duty_cycle_values = [10000, 14000, 18000, 20000, 24000, 27000, 31000, 35000]

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for note_name in phrase:
            # Get the frequency of the current note
            freq = notes[note_name]
            # Get the duty cycle value for the current note
            duty_cycle = duty_cycle_values[list(notes.keys()).index(note_name) % len(duty_cycle_values)]
            # Play the note for 0.25 seconds with varying duty cycle
            speaker.freq(freq)
            for j in range(4):
                speaker.duty_u16(duty_cycle)
                sleep(0.0625)
                speaker.duty_u16(0)
                sleep(0.0625)
        # Pause for 0.25 seconds between phrases
        sleep(0.25)

# Turn off the PWM object
speaker.duty_u16(0)
