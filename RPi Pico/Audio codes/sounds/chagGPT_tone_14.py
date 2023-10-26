import math
from machine import Pin, PWM
from utime import sleep

# Define the pin for the speakers
SPEAKER_PIN_1 = 16
SPEAKER_PIN_2 = 17

# Define the frequencies for the beat and melody notes
beat_freq = 200
melody_freqs = [261, 294, 329, 349, 392, 440, 494]

# Define the length of each note in milliseconds
beat_length = 250
melody_length = 500

# Create PWM objects on the speaker pins
beat_speaker = PWM(Pin(SPEAKER_PIN_1))
melody_speaker = PWM(Pin(SPEAKER_PIN_2))

# Define the beat pattern
beat_pattern = [1, 0, 1, 0, 1, 0, 1, 1]

# Loop through each note in the melody
for i in range(len(melody_freqs)):
    # Get the frequency of the melody note
    melody_freq = melody_freqs[i]
    
    # Calculate the period and duty cycle for the melody note
    melody_period = int(1 / melody_freq * 1000000)
    melody_duty_cycle = int(math.pow(2, 16) / 2 - 1)
    
    # Set the frequency and duty cycle of the melody PWM object
    melody_speaker.freq(melody_freq)
    melody_speaker.duty_u16(melody_duty_cycle)
    
    # Play the beat pattern
    for beat in beat_pattern:
        # Calculate the duty cycle for the beat note
        beat_duty_cycle = int(beat * math.pow(2, 16) / 2 - 1)
        
        # Set the duty cycle of the beat PWM object
        beat_speaker.duty_u16(beat_duty_cycle)
        
        # Wait for the beat note to play
        sleep(beat_length / 1000)
    
    # Stop the beat PWM object
    beat_speaker.duty_u16(0)
    
    # Wait for the melody note to play
    sleep(melody_length / 1000)
    
    # Stop the melody PWM object
    melody_speaker.duty_u16(0)
    
    # Pause between notes
    sleep(0.1)
