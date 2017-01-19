import socket 
import machine
from machine import Pin


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center><h2>A simple webserver for turning HUZZAH Feather LED's on and off with Micropython</h2></center>
<center><h3>(for noobs to both the ESP8266 and Micropython)</h3></center>
<form>
LED0: 
<button name="LED" value="1" type="submit">GO</button>
<button name="LED" value="0" type="submit">STOP</button><br><br>
</form>
</html>
"""

pin1 = Pin(5, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
pin3 = Pin(0, Pin.OUT)
pin4 = Pin(2, Pin.OUT)

def move(a, b):
    if a < 0:
        pin1.low()
        pin2.high()
    elif a > 0:
        pin1.high()
        pin2.low()
    else:
        pin1.low()
        pin2.low()

    if b < 0:
        pin3.low()
        pin4.high()
    elif b > 0:
        pin3.high()
        pin4.low()
    else:
        pin3.low()
        pin4.low()
    print(pin1.value(), pin2.value())
    print(pin3.value(), pin4.value())

#Setup Socket WebServer
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    go = request.find('/?LED=1')
    stop = request.find('/?LED=0')
    print("Data: " + str(go))
    print("Data2: " + str(stop))
    if go == 6:
        print('TURN LED0 ON')
        move(1, 1)
    elif stop == 6:
        print('TURN LED0 OFF')
        move(0, 0)
    response = html
    conn.send(response)
    conn.close()