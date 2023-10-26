import machine
import neopixel
import utime

# Define the number of pixels in the LED panel
num_pixels = 8 * 32

# Configure the DIN pin connected to the LED panel
din_pin = machine.Pin(10, machine.Pin.OUT)  # Replace with the actual pin number you have connected

# Create a NeoPixel object with the number of pixels and the DIN pin
pixels = neopixel.NeoPixel(din_pin, num_pixels)

CHARS = {
    'H': (255, 0, 0),  # Red
    'e': (0, 255, 0),  # Green
    'l': (0, 0, 255),  # Blue
    'o': (255, 255, 255)  # White
}

# Clear the LED panel
pixels.fill((0, 0, 0))
pixels.write()

# Example animation: Scrolling text
message = "He"  # Replace with your desired message
color = (100, 255, 155)  # Replace with your desired color

while True:
    # Scroll the text from right to left
    for i in range(num_pixels + len(message) * 8):
        pixels.fill((0, 0, 0))
        for j in range(len(message)):
            # Calculate the starting pixel index for the current character
            start_index = i - j * 8
            if start_index >= -8 and start_index < num_pixels:
                # Display each character
                for k in range(8):
                    if start_index + k >= 0 and start_index + k < num_pixels:
                        pixels[start_index + k] = color
        pixels.write()
        utime.sleep_us(100000)