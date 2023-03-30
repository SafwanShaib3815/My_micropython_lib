"""
Name: main.py
Description: This is the main script, it waits for motion sensor and closes the door on activation, clicking a button will loop back to open the door and wait again
Author: Safwan Shaib
Date: 1/29/2023


-----------------
WIRING:
-----------------
PIR Sensor		+		>> 3.3V
                -		>> Ground
                Out		>> D2
            
Servo Motor		+		>> 3.3V
                -		>> Ground
                Signal	>> D5

Indicator LED	+		>> D0
                -		>> Ground
-----------------
ESP8266 Pinout:
-----------------
The D0-D8 pins on the ESP8266 D1 Mini board correspond to the following GPIO (General Purpose Input/Output) numbers in MicroPython:

D0 = 16
D1 = 5
D2 = 4
D3 = 0
D4 = 2 (this is also the onboard led)
D5 = 14
D6 = 12
D7 = 13
D8 = 15
RST (this is not a gpio, but a pin connected with the onboard switch)
"""


# import time
# #setting up UART bus
# 
# while True:
#     if uart.any():
#         data = uart.read()
#         print(data.decode())
#         time.sleep(1)
#         
# #     uart.write("\nHello, PicoPico!")
# #     time.sleep(1)


from machine import Pin, PWM
import time
import urequests
import ocdoor #self_made script to open and close a door using a 90G servo motor

#initializing the PIR motion sensor and button input pins
pir=Pin(4, Pin.IN)
btn=Pin(5, Pin.IN)

#initializing the led outputs
onboard_led=Pin(2, Pin.OUT)
led=Pin(16, Pin.OUT)

#this is used to create fade effect for the blink operation while sensor is waiting movement
p2 =Pin(2)
pwm = PWM(p2)
pwm.freq(50)


def ambush():
    
    while True:
        if pir.value():
            print("Motion Detected!")
            ocdoor.closedoor()
            onboard_led.value(0) #Value of 0 is onboard_led-on
            led.value(1) #Turn Led ON
    #         response = urequests.get("https://maker.ifttt.com/trigger/trigger_event_activated/with/key/d91vdEAZFyW0Lgvt736gUl")
    #         print(response.text)
    #         response.close()
            return
        else: #pir sensor pulls to 1 when it detects motion
            print("No motion Detected")
            
            #make fade affect on the onboard LED while waiting
            for pos in range(0, 100, 2):
                pwm.duty(pos)
                time.sleep(0.002)
            led.value(0) #Turn led OFF
            for pos in range(1000, 0, -2):
                pwm.duty(pos)
                time.sleep(0.002)
            ocdoor.opendoor()


def main():
    while True:
        for i in range(0, 20, 1):
            onboard_led.value(0) #value of 0 is onboard_led-on
            time.sleep(0.05)
            onboard_led.value(1) #value of 1 is onboard_led-off
            time.sleep(0.05)
        ambush()
        while True:
            time.sleep(0.5)
            if btn.value()==0: #button value = 1 when not clicked
                break
if __name__ == "__main__":
    main()
    