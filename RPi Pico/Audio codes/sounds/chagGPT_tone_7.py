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

# Define the duty cycle values for each note
duty_cycles = {
    'C4': [10000, 15000, 20000],
    'D4': [12000, 17000, 22000],
    'E4': [14000, 19000, 24000],
    'F4': [16000, 21000, 26000],
    'G4': [18000, 23000, 28000],
    'A4': [20000, 25000, 30000],
    'B4': [22000, 27000, 32000],
    'C5': [24000, 29000, 32767]
}

# Play each phrase twice, with a brief pause in between
for i in range(2):
    for phrase in phrases:
        for note_name in phrase:
            # Get the frequency and duty cycle values of the current note
            freq = notes[note_name]
            duty = duty_cycles[note_name]
            # Play the note with three different duty cycle values, gradually decreasing
            # the duty cycle over time to create a "fade out" effect
            for d in duty:
                speaker.freq(freq)
                speaker.duty_u16(d)
                sleep(0.15)
            for d in reversed(duty):
                speaker.duty_u16(d)
                sleep(0.15)
            # Pause for a short time between notes
            sleep(0.1)

        # Pause for a short time between phrases
        sleep(0.25)

# Turn off the PWM object
speaker.duty_u16(0)
