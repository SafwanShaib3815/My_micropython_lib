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
    ['F4', 'G4', 'A4', 'F4', 'A4', 'G4', 'F4', 'A4', 'G4', 'F4'],
    ['C4', 'E4', 'G4', 'C4', 'G4', 'E4', 'C4', 'G4', 'E4', 'C4'],
    ['D4', 'F4', 'A4', 'D4', 'A4', 'F4', 'D4', 'A4', 'F4', 'D4'],
    ['G4', 'B4', 'D5', 'G4', 'D5', 'B4', 'G4', 'D5', 'B4', 'G4']
]

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for j, note_name in enumerate(phrase):
            # Get the frequency of the current note
            freq = notes[note_name]
            # Set the duty cycle based on the note's position in the phrase
            if j % 4 == 0:
                duty = 32000
            elif j % 4 == 2:
                duty = 20000
            else:
                duty = 15000
            # Play the note for 0.5 seconds
            speaker.freq(freq)
            speaker.duty_u16(duty)
            sleep(0.5)
            speaker.duty_u16(0)
        # Pause for 0.5 seconds between phrases
        sleep(0.5)

# Turn off the PWM object
speaker.duty_u16(0)
