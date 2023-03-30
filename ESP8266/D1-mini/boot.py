# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import uos, machine
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

# Connect to WiFi network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    while not sta_if.isconnected(): 
        print('connecting to network...')
        sta_if.active(True)
        sta_if.hostname("ESP01sNO1_95438D")
        sta_if.connect(secrets.ssid, secrets.password)
        sleep(0.5)
        while not sta_if.isconnected():
            pass
    conn_info = sta_if.ifconfig()
    print("WiFi connected!")
    print('network config:', conn_info)
    print("IP address:", sta_if.ifconfig()[0])
    uart.write(str(conn_info).encode())
        
do_connect()

gc.collect()

