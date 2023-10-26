"""
SDcard slot pinout:
3.3V
CS
MOSI
CLK
MISO
GND


"""
import machine
import sdcard
import os


print("assigning CS pin")
CS = machine.Pin(5, machine.Pin.OUT)
print("assigning spi")
spi = machine.SPI(1,baudrate=1000000,polarity=0,phase=0,bits=8,firstbit=machine.SPI.MSB,sck=machine.Pin(10),mosi=machine.Pin(11),miso=machine.Pin(8))
print("spi initialized")
sd = sdcard.SDCard(spi,CS)
print("spi passed to SDcard")
vfs = os.VfsFat(sd)
print("file system created")
os.mount(vfs, "/sd")
print("sd card mounted to the filesystem")
# Create a file and write something to it
with open("/sd/data.txt", "w") as file:
    print("Writing to data.txt...")
    file.write("Welcome to microcontrollerslab!\r\n")
    file.write("This is a test\r\n")

# Open the file we just created and read from it
with open("/sd/data.txt", "r") as file:
    print("Reading data.txt...")
    data = file.read()
    print(data)