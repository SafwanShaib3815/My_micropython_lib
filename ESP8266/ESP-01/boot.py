# This file is executed on every boot (including wake-boot from deepsleep)

import machine
import network
import secrets
from time import sleep
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()

#setting up UART bus
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)
print("UART is set up!! Connecting...\n")
led_pin = machine.Pin(2, machine.Pin.OUT)  # set GPIO2 as output pin
# Connect to WiFi network
sta_if = network.WLAN(network.STA_IF)

# def connect():
sta_if.disconnect()
while not sta_if.isconnected():
    led_pin.value(0)  # turn on the LED
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(secrets.ssid, secrets.password)
    sleep(0.5)
    while not sta_if.isconnected():
        pass
    if sta_if.isconnected(): #break whenever it's connected
        print("WiFi connected!")
        print('network config:', sta_if.ifconfig())
        print("IP address:", sta_if.ifconfig()[0])
        uart.write(str(sta_if.ifconfig()[0]).encode())
        for i in range(8):
            led_pin.value(0)  # turn on the LED
            sleep(0.1)  # wait for 1 second
            led_pin.value(1)  # turn off the LED
            sleep(0.1)  # wait for 1 second
        break 
# connect()        
gc.collect()



