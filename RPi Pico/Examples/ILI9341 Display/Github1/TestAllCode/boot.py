"""ILI9341 demo (bouncing boxes).

Display	>>>>>	PICO

T_IRQ	>>>>>	GP 8
T_DO	>>>>>	GP 9
T_DIN	>>>>>	GP 5
T_CS	>>>>>	GP 17
T_CLK	>>>>>	GP 16

MISO	>>>>>	GP 1
LED	>>>>>	3.3V
SCK	>>>>> 	GP 2
MOSI	>>>>> 	GP 3
DC	>>>>>	GP 11
REST	>>>>>	GP 20	
CS	>>>>>	GP 22
GND	>>>>>	GND
VCC	>>>>>	3.3V

"""

# import demo_bouncing_boxes.py
# import demo_clear
# import demo_color_palette
# import demo_color_wheel
# import demo_colored_squares
# import demo_fonts
# import demo_fonts8x8
# import demo_images
# import demo_orientation
# import demo_scrolling_marquee
# import demo_shapes

import time

# Button pin number
BUTTON_PIN = 17

# Module names
module_names = ['demo_clear', 'demo_color_palette', 'demo_color_wheel',
                'demo_colored_squares', 'demo_fonts', 'demo_fonts8x8', 'demo_images',
                'demo_orientation', 'demo_scrolling_marquee', 'demo_shapes', 'demo_bouncing_boxes']

# Create button object

# Helper function to call test() on each module
def call_test_functions(modules):
    for module_name in modules:
        try:
            module = __import__(module_name)
            timeout = time.time() + 10  # Set a timeout of 10 seconds
            while time.time() < timeout:
                module.test()
                time.sleep_ms(100)  # Small delay between test iterations
        except ImportError:
            print(f"Error importing module: {module_name}")
        except AttributeError:
            print(f"Error calling test() function in module: {module_name}")

# Main loop
while True:
    call_test_functions(module_names)
    time.sleep_ms(300)  # Debounce delay to avoid multiple rapid presses
