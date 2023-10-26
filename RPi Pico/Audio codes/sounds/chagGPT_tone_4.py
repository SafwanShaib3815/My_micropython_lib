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
    ['C4', 'E4', 'G4', 'C5', 'E4', 'C5', 'G4', 'E4', 'C4'],
    ['A4', 'C5', 'E4', 'A4', 'C5', 'E4', 'A4', 'C5', 'G4', 'E4'],
    ['F4', 'A4', 'C5', 'F4', 'C5', 'A4', 'F4', 'C5', 'A4', 'F4'],
    ['G4', 'B4', 'D4', 'G4', 'B4', 'D4', 'G4', 'B4', 'A4', 'F4']
]

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for note_name in phrase:
            # Get the frequency of the current note
            freq = notes[note_name]
            # Get the current index in the phrase
            note_index = phrase.index(note_name)
            # Determine the duty cycle based on the note index
            if note_index % 2 == 0:
                duty_cycle = 25000
            else:
                duty_cycle = 15000
            # Play the note for 0.25 seconds with the determined duty cycle
            speaker.freq(freq)
            speaker.duty_u16(duty_cycle)
            sleep(0.25)
            speaker.duty_u16(0)
        # Pause for 0.25 seconds between phrases
        sleep(0.25)

# Turn off the PWM object
speaker.duty_u16(0)
