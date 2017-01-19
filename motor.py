from machine import Pin, PWM

pin1 = Pin(5, Pin.OUT)
pin2 = Pin(4, Pin.OUT)
pin3 = Pin(0, Pin.OUT)
pin4 = Pin(2, Pin.OUT)

forw = Pin(14, Pin.IN, Pin.PULL_UP)
back = Pin(12, Pin.IN, Pin.PULL_UP)

def go(a, b):
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
    
while True:
    if not forw.value():
        go(1, 1)
    elif not back.value():
        go(-1, -1)
    else:
        go(0, 0)
    
