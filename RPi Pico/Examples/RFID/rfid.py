from mfrc522 import MFRC522
import utime
from machine import Pin

interrupt_flag=0

# Set up the interrupt and reset pins
IRQ_PIN = 16
RST_PIN = 17
irq_pin = Pin(IRQ_PIN, Pin.IN, Pin.PULL_UP)
rst_pin = Pin(RST_PIN, Pin.OUT)

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=RST_PIN)

print("Bring TAG closer...")


# def handle_interrupt(irq_pin):
#     print("occured")
#     global interrupt_flag
#     interrupt_flag=1
#     reader.init()
#     (stat, tag_type) = reader.request(reader.REQIDL)
#     if stat == reader.OK:
#         (stat, uid) = reader.SelectTagSN()
#         if stat == reader.OK:
#             card = int.from_bytes(bytes(uid),"little",False)
#             print("CARD ID: "+str(card))
#     utime.sleep_ms(500)
# 
#     
# 
# #Attach the callback function to the interrupt pin
# irq_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=handle_interrupt)
# while True:
#     utime.sleep_ms(100)
#     if interrupt_flag is 1:
#         print("Interrupt has occured")
#         interrupt_flag=0
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
    utime.sleep_ms(500)
