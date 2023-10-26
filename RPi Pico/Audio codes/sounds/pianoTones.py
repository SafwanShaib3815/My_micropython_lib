from machine import Pin, PWM
from time import sleep

# Pin assignments
SPEAKER_PIN = 16
BUTTON_PIN = 5

# Piano key frequencies
KEY_FREQUENCIES = {
"G#0/Ab0": 251,
    "A0": 265,
    "A#0/Bb0": 281,
    "B0": 298,
    "C1": 316,
    "C#1/Db1": 335,
    "D1": 355,
    "D#1/Eb1": 376,
    "E1": 398,
    "F1": 422,
    "F#1/Gb1": 447,
    "G1": 474,
    "G#1/Ab1": 502,
    "A1": 532,
    "A#1/Bb1": 563,
    "B1": 596,
    "C2": 631,
    "C#2/Db2": 668,
    "D2": 708,
    "D#2/Eb2": 750,
    "E2": 795,
    "F2": 842,
    "F#2/Gb2": 893,
    "G2": 947,
    "G#2/Ab2": 1004,
    "A2": 1064,
    "A#2/Bb2": 1127,
    "B2": 1194,
    "C3": 1264,
    "C#3/Db3": 1337,
    "D3": 1415,
    "D#3/Eb3": 1500,
    "E3": 1591,
    "F3": 1685,
    "F#3/Gb3": 1786,
    "G3": 1893,
    "G#3/Ab3": 2007,
    "A3": 2129,
    "A#3/Bb3": 2255,
    "B3": 2389,
    "C4": 2531,
    "C#4/Db4": 2681,
    "D4": 2839,
    "D#4/Eb4": 3006,
    "E4": 3181,
    "F4": 3363,
    "F#4/Gb4": 3562,
    "G4": 3780,
    "G#4/Ab4": 4015,
    "A4": 4267,
    "A#4/Bb4": 4535,
    "B4": 4819,
    "C5": 5062,
    "C#5/Db5": 5363,
    "D5": 5680,
    "D#5/Eb5": 6013,
    "E5": 6363,
    "F5": 6732,
    "F#5/Gb5": 7125,
    "G5": 7548,
    "G#5/Ab5": 8008,
    "A5": 8513,
    "A#5/Bb5": 9069,
    "B5": 9659,
    "C6": 10124,
    "C#6/Db6": 10727,
    "D6": 11360,
    "D#6/Eb6": 12027,
    "E6": 12727,
    "F6": 13464,
    "F#6/Gb6": 14250,
    "G6": 15096,
    "G#6/Ab6": 160,
    "A6": 16961,
    "A#6/Bb6": 17981,
    "B6": 19054,
    "C7": 20182,
    "C#7/Db7": 21368,
    "D7": 22614,
    "D#7/Eb7": 23923,
    "E7": 25300,
    "F7": 26748,
    "F#7/Gb7": 28270,
    "G7": 29867,
    "G#7/Ab7": 31543,
    "A7": 33302,
    "A#7/Bb7": 35146,
    "B7": 37077,
    "C8": 38163
}

# Set up PWM on the speaker pin
speaker = PWM(Pin(SPEAKER_PIN))

# Set up button on the button pin
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_DOWN)

# Loop through each piano key frequency and play it when the button is pressed
for key, frequency in KEY_FREQUENCIES.items():
    while True:
        if button.value() == 1:
            # Button is pressed, play the key
            speaker.duty_u16(32768)  # 50% duty cycle
            speaker.freq(int(frequency))
            sleep(0.5)
            speaker.duty_u16(0)
            sleep(0.1)
            break  # Exit the loop and wait for the next button press
        else:
            # Button is not pressed, wait for it to be pressed
            sleep(0.1)
