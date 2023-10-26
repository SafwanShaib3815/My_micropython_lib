import machine
import time
from neopixel import NeoPixel

# Define the number of LEDs in the strip
num_leds = 256

# Define the number of rows and columns in the LED panel
num_rows = 8
num_cols = 32

# Define the GPIO pin connected to the LED strip
pin = machine.Pin(10)

# Create a neopixel object
strip = NeoPixel(pin, num_leds)

# Define the RGB color values for the characters
CHARS = {
    'H': (55, 0, 0),  # Red
    'e': (0, 55, 0),  # Green
    'l': (0, 0, 55),  # Blue
    'o': (55, 55, 55)  # White
}

# Define the delay between displaying characters
delay = 0.2

# Define the LED panel layout mapping
layout = []
for row in range(num_rows):
    if row % 2 == 0:
        layout.extend(range(row * num_cols, (row + 1) * num_cols))
    else:
        layout.extend(range((row + 1) * num_cols - 1, row * num_cols - 1, -1))

# Display "Hello World"
def display_message(message):
    for char in message:
        if char in CHARS:
            color = CHARS[char]
            for led_index in layout:
                strip[led_index] = color
            strip.write()
            time.sleep(delay)
            for led_index in layout:
                strip[led_index] = (0, 0, 0)  # Turn off LEDs
            strip.write()
            time.sleep(delay)

# Display "Hello World"
display_message("Hello World")

# Turn off all LEDs
for led_index in layout:
    strip[led_index] = (0, 0, 0)
strip.write()
