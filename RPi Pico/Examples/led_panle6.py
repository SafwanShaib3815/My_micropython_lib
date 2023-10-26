import machine, neopixel, time
import random
import math
pin = machine.Pin(10, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 8*32)


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

def is_odd(number):
    # Check if the number is odd
    if number % 2 != 0:
        return True
    else:
        return False

def is_even(number):
    # Check if the number is even
    if number % 2 == 0:
        return True
    else:
        return False

def color(r,g,b):
    for i in range(256):
        r=random.randint(0, 255)
        g=random.randint(0, 255)
        b=random.randint(0, 255)
    return (r,g,b)


def slide(color):
    color = color(0,0,0)
    for i in index_array:
        np[i] = color
        np.write()
    np.fill((0,0,0))
    np.write()
    for i in range(len(index_array) - 1, -1, -1):
        np[i] = color
        np.write()
    np.fill((0,0,0))
    np.write()


def odd_even(color):
    color1 = color(0,0,0)
    color2 = color(0,0,0)
    num = random.randint(0,1)
    for i in index_array:
        if is_odd(i):
            np[i] = color1
            np.write()
        else:
            np[i]=(0,0,0)
            np.write()
    for i in range(len(index_array) - 1, -1, -1):
        if is_odd(i):
            if num:
                np[i] = (0,0,0)
                np.write()
            else:
                pass
        else:
            np[i]=color2
            np.write()
    time.sleep(1)
    np.fill((0,0,0))
    np.write()
    
    
def random_blink():
    np.fill((0, 0, 0))  # Clear all LEDs
    np.write()

    for _ in range(10):
        np.fill(color(0,0,0))  # Randomly fill all LEDs with a color
        np.write()
        time.sleep(0.2)  # Adjust the delay for the desired speed



def color_fade(start_color, end_color, duration):
    np.fill(start_color)  # Set initial color
    np.write()

    steps = 50  # Number of steps for the color fade
    delay = duration / steps

    r_step = (end_color[0] - start_color[0]) / steps
    g_step = (end_color[1] - start_color[1]) / steps
    b_step = (end_color[2] - start_color[2]) / steps

    for step in range(steps):
        r = start_color[0] + int(r_step * step)
        g = start_color[1] + int(g_step * step)
        b = start_color[2] + int(b_step * step)

        np.fill((r, g, b))  # Set intermediate color
        np.write()
        time.sleep(delay)  # Adjust the delay for the desired speed

    np.fill(end_color)  # Set final color
    np.write()










for _ in range(10):
    slide(color)
    odd_even(color)
    random_blink()
    color_fade((255, 0, 0), (0, 255, 0), 1)
