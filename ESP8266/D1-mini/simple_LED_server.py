# Code taken from https://www.cnx-software.com/2022/07/03/getting-started-with-wifi-on-raspberry-pi-pico-w-board/
import network
import socket
import time
import secrets

from machine import Pin

# Select the onboard LED
led = Pin(2, Pin.OUT)


stateis = "LED is OFF"

html = """<!DOCTYPE html>
<html>
   <head>
     <title>Web Server On D1 Mini </title>
   </head>
  <body>
      <h1 style= color:blue; text-align: center;">D1 Mini Wireless Web Server</h1>
      <div style="text-align: center;">
      <p style="font-size: 36px;">%s</p>
      <a style="font-size: 48px;" href="/light/on">Turn On&nbsp;&nbsp;&nbsp;</a>
      <a style="font-size: 48px;" href="/light/off">&nbsp;Turn Off</a>
      </div>
  </body>
</html>
"""

# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
print('addr:', addr)
s = socket.socket()
#if not addr:
s.bind(addr)
s.listen(1)

print('listening on', addr)

# Listen for connections
while True:
  try:
    cl, addr = s.accept()
    print('client connected from', addr)
    request = cl.recv(1024)
    print(request)
    request = str(request)
    led_on = request.find('/light/on')
    led_off = request.find('/light/off')
    print( 'led on = ' + str(led_on))
    print( 'led off = ' + str(led_off))

    if led_on == 6:
      print("led on")
      led.value(0)
      stateis = "LED is ON"

    if led_off == 6:
      print("led off")
      led.value(1)
      stateis = "LED is OFF"
    # generate the web page with the stateis as a parameter
    response = html % stateis
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
#     cl.close()

  except OSError as e:
    cl.close()
    print('connection closed')

