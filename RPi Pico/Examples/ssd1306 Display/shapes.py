bitmaps = {
    'heart': [
        0b011110000011110,
        0b111111000111111,
        0b111111101111111,
        0b111111111111111,
        0b011111111111110,
        0b001111111111100,
        0b000111111111000,
        0b000011111110000,
        0b000001111100000,
        0b000000111000000,
        0b000000010000000,
    ],
    'circle': [
        0b0000000111111111110000000,
        0b0000001111111111111000000,
        0b0000111111111111111110000,
        0b0001111111111111111111000,
        0b0011111111111111111111100,
        0b0011111111111111111111100,
        0b0111111111111111111111110,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b1111111111111111111111111,
        0b0111111111111111111111110,
        0b0011111111111111111111100,
        0b0011111111111111111111100,
        0b0001111111111111111111000,
        0b0000111111111111111110000,
        0b0000001111111111111000000,
        0b0000000111111111110000000,
    ],
    'square': [
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
        0b11111111111110,
    ],
    'bird': [
        0b00000000000000000000000011000000000000000000000000,
        0b00000000000000000000000011000000000000000000000000,
        0b00000000000000000000000111100000000000000000000000,
        0b00000000000000000000000111100000000000000000000000,
        0b00000000000000000000001111110000000000000000000000,
        0b00000000000000000000001111110000000000000000000000,
        0b11111111100000000000011111111000000000000111111111,
        0b11111111111111111000011111111000011111111111111111,
        0b11111111111111111111111111111111111111111111111111,
        0b11111111111111111111111111111111111111111111111111,
        0b11111111111111111111111111111111111111111111111111,
        0b11111111111111111111111111111111111111111111111111,
        0b11111111111111111111111111111111111111111111111111,
        0b01111111111111111111111111111111111111111111111110,
        0b00111111111100011111111111111111111000111111111100,
        0b00011111111000001111111111111111110000011111111000,
        0b00001111110000000011111111111111000000001111110000,
        0b00000111100000000000111111111100000000000111100000,
        0b00000011000000000000011111111000000000000011000000,
        0b00000000000000000000011111111000000000000000000000,
        0b00000000000000000000001111110000000000000000000000,
        0b00000000000000000000001111110000000000000000000000,
        0b00000000000000000000000111100000000000000000000000,
        0b00000000000000000000000011100000000000000000000000,
        0b00000000000000000000000011000000000000000000000000,
        0b00000000000000000000000011000000000000000000000000,
        0b00000000000000000000000111100000000000000000000000,
        0b00000000000000000000001111110000000000000000000000,
        0b00000000000000000000011111111000000000000000000000,
        0b00000000000000000000111111111100000000000000000000,
        0b00000000000000000001111111111110000000000000000000,
        0b00000000000000000011111111111111000000000000000000,
        0b00000000000000000011111111111111000000000000000000,
        ],
    'star': [
        0b0000000000000000000110000000000000000000,
        0b0000000000000000000110000000000000000000,
        0b0000000000000000000110000000000000000000,
        0b0000000000000000001111000000000000000000,
        0b0000000000000000001111000000000000000000,
        0b0000000000000000001111100000000000000000,
        0b0000000000000000011111100000000000000000,
        0b0000000000000000011111100000000000000000,
        0b0000000000000000011111110000000000000000,
        0b0000000000000000111111110000000000000000,
        0b0000000000000000111111110000000000000000,
        0b0000000000000001111111111000000000000000,
        0b1111111111111111111111111111111111111111,
        0b1111111111111111111111111111111111111111,
        0b0011111111111111111111111111111111111110,
        0b0001111111111111111111111111111111111000,
        0b0000011111111111111111111111111111110000,
        0b0000001111111111111111111111111111000000,
        0b0000000011111111111111111111111100000000,
        0b0000000001111111111111111111111000000000,
        0b0000000000011111111111111111100000000000,
        0b0000000000001111111111111111000000000000,
        0b0000000000011111111111111111100000000000,
        0b0000000000011111111111111111100000000000,
        0b0000000000011111111111111111100000000000,
        0b0000000000111111111111111111110000000000,
        0b0000000000111111111111111111110000000000,
        0b0000000000111111111000111111110000000000,
        0b0000000001111111100000011111111000000000,
        0b0000000001111110000000000111111000000000,
        0b0000000001111100000000000011111100000000,
        0b0000000011110000000000000000111100000000,
        0b0000000011100000000000000000001100000000,
        0b0000000010000000000000000000000100000000,
        ],
}

def draw_bitmap(bitmap, display, x, y):
    width = 60
    height = len(bitmap)
    
    for row in range(height):
        row_data = bitmap[row]
        for col in range(width):
            pixel_value = (row_data >> (width - 1 - col)) & 1
            display.pixel(x + col, y + row, pixel_value)
    display.show()
