# Fire Simulation LED Circuit for Raspberry Pi Pico

This program simulates a fire effect on an LED circuit using a Raspberry Pi Pico microcontroller. It utilizes ten GPIO pins to create a dynamic and realistic fire simulation by employing two effects: random fading and flickering.

**Author:** Safwan Shaib
**Email:** sh5safwan@hotmail.com
**Date:** September 7, 2022

## Description

This program harnesses the dual-core capabilities of the Raspberry Pi Pico microcontroller to simulate a fire effect. It controls a group of ten GPIO pins that represent LEDs. Two effects, fading and flickering, are applied simultaneously on separate cores using threading. These effects randomly select LEDs to either fade or flicker, creating a dynamic and realistic fire simulation.

## Features

- The program offers two modes and three speeds for each mode.
- The default mode fades the inner three LEDs in and out while flickering the outer six LEDs.
- The second mode reverses the behavior: the inner LEDs flicker, and the outer ones fade.
- To toggle between speeds, perform a short click on the button and wait for three seconds (speed adjustment is only possible in flicker mode).
- Switching to the second mode requires a long click on the button (at least two seconds), followed by a three-second wait.
- In the second mode, a short click will return to the first mode.
- Therefore, the speed of the second mode's flickering must be set while in the first mode.
- An indicator LED displays the flickering speed and blinks when changing modes or speed settings.

  [Watch the Simulator in Action](https://www.youtube.com/watch?v=yourvideoid)
  Diagram image:
![20230407_190640](https://github.com/SafwanShaib3815/My_micropython_lib/assets/73716969/1a4bad08-7a2c-4386-be58-9f37c8ad8baa)

