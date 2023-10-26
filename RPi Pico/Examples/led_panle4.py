import machine
import neopixel
import utime

pixel_num = 8*32

index_array = [
    7, 6, 5, 4, 3, 2, 1, 0,
    8, 9, 10, 11, 12, 13, 14, 15,
    23, 22, 21, 20, 19, 18, 17, 16,
    24, 25, 26, 27, 28, 29, 30, 31,
    39, 38, 37, 36, 35, 34, 33, 32,
    40, 41, 42, 43, 44, 45, 46, 47,
    55, 54, 53, 52, 51, 50, 49, 48,
    56, 57, 58, 59, 60, 61, 62, 63,
    71, 70, 69, 68, 67, 66, 65, 64,
    72, 73, 74, 75, 76, 77, 78, 79,
    87, 86, 85, 84, 83, 82, 81, 80,
    88, 89, 90, 91, 92, 93, 94, 95,
    103, 102, 101, 100, 99, 98, 97, 96,
    104, 105, 106, 107, 108, 109, 110, 111,
    119, 118, 117, 116, 115, 114, 113, 112,
    120, 121, 122, 123, 124, 125, 126, 127,
    135, 134, 133, 132, 131, 130, 129, 128,
    136, 137, 138, 139, 140, 141, 142, 143,
    151, 150, 149, 148, 147, 146, 145, 144,
    152, 153, 154, 155, 156, 157, 158, 159,
    167, 166, 165, 164, 163, 162, 161, 160,
    168, 169, 170, 171, 172, 173, 174, 175,
    183, 182, 181, 180, 179, 178, 177, 176,
    184, 185, 186, 187, 188, 189, 190, 191,
    199, 198, 197, 196, 195, 194, 193, 192,
    200, 201, 202, 203, 204, 205, 206, 207,
    215, 214, 213, 212, 211, 210, 209, 208,
    216, 217, 218, 219, 220, 221, 222, 223,
    231, 230, 229, 228, 227, 226, 225, 224,
    232, 233, 234, 235, 236, 237, 238, 239,
    247, 246, 245, 244, 243, 242, 241, 240,
    248, 249, 250, 251, 252, 253, 254, 255
]


# Define the letter 'S' pattern
letter_S = [
    0x7E,
    0x01,
    0x01,
    0x00,
    0x7E,
    0x01,
    0x00,
    0x01,
    0x7E
]
din_pin = machine.Pin(10, machine.Pin.OUT)  # Replace with the actual pin number you have connected

# Configure NeoPixel strip
np = neopixel.NeoPixel(din_pin, 8*32)

# Function to send a single bit of data to the LED matrix panel
def send_bit(bit):
    if bit:
        np[102]=(80,2,3)
    else:
        np[102]=(0,0,0)
# Function to send a byte of data to the LED matrix panel
def send_byte(byte):
    for _ in range(8):
        send_bit(byte & 0x80)
        byte <<= 1

# Function to display the letter 'S' on the LED matrix panel
def display_letter_S():
    for row in letter_S:
        send_byte(row)
        utime.sleep(0.1)  # Adjust delay as needed



# Function to display the letter 'S'
# def display_letter_S():
#     counter = 0
#     for row in letter_S:
#         for value in row:
#             if value:
#                 np[counter]=(0,2,1)
#                 np.write() # Update the LED strip
#             counter +=1
#             
#             utime.sleep(0.01)  # Adjust delay as needed

# Display the letter 'S' on the LED strip
display_letter_S()
