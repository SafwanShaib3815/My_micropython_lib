import neopixel
import machine
import time
# Define the number of LEDs in the matrix
NUM_LEDS = 256

# Define the pin number to which the LED matrix is connected
PIN = machine.Pin(10, machine.Pin.OUT)

# Initialize the neopixel object
np = neopixel.NeoPixel(PIN, NUM_LEDS)

# Function to set the color of a specific LED
def set_led_color(led_index, color):
    np[led_index] = color
    np.write()

# Example usage:
# Send a byte of data to specific LEDs
def send_byte_to_leds(data):
    for i in range(8):
        for j in range(32):
            led_index = i * 32
            if i % 2 == 1:
                led_index += 31 - j
            else:
                led_index += j
            if data & (1 << (i * 32 + j)):
                # Set the LED color to ON (e.g., white)
                set_led_color(led_index, (255, 255, 255))
#             else:
#                 # Set the LED color to OFF (e.g., black)
#                 set_led_color(led_index, (0, 0, 0))

# Example usage:
# Send the byte 0xAA (10101010 in binary) to the LEDs

# Define the letter 'S' pattern
letter_S = [
    0x7E,
    0x0100,
    0x800000,
    0x01000000,
    0x7E00000000,
    0x400000000000,
    0x41000000000000,
    0x3E00000000000000,
]

# for byte in letter_S:
send_byte_to_leds(letter_S[1])
send_byte_to_leds(letter_S[0])

#     time.sleep(.1)
# send_byte_to_leds(0x7E)
# send_byte_to_leds(0x8100)
# send_byte_to_leds(0x010000)
# send_byte_to_leds(0x80000000)
# send_byte_to_leds(0x7E00000000)
# send_byte_to_leds(0x010000000000)
# send_byte_to_leds(0x80000000000000)
# send_byte_to_leds(0x8100000000000000)
# send_byte_to_leds(0x7E0000000000000000)
np.fill((0,0,0))
time.sleep(1)
np.write()
