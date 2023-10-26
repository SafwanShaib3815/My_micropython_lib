import machine
import time

# Define the GPIO pin connected to the DIN (data input) pin of the LED matrix panel
din_pin = machine.Pin(10, machine.Pin.OUT)

# Define the LED matrix pattern for the letter 'S'
letter_S = [
    0x00,
    0x00,
    0x00,
    0x00,

]

# Function to send a single bit of data to the LED matrix panel
def send_bit(bit):
    din_pin.value(bit)
    din_pin.on()
    din_pin.off()

# Function to send a byte of data to the LED matrix panel
def send_byte(byte):
    for _ in range(8):
        send_bit(byte & 0x01)
        byte <<= 1

# Function to display the letter 'S' on the LED matrix panel
def display_letter_S():
    for row in letter_S:
        send_byte(row)
        time.sleep(0.1)  # Adjust delay as needed

# Display the letter 'S' on the LED matrix panel
display_letter_S()
