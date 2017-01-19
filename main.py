import time
import machine
from machine import Pin
import ssd1306


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


adc = machine.ADC(0)

def read_x():
    pinx = Pin(0, Pin.IN)
    piny = Pin(2, Pin.OUT)
    piny.low()
    return adc.read()

def read_y():
    pinx = Pin(0, Pin.OUT)
    piny = Pin(2, Pin.IN)
    pinx.low()
    return adc.read()

try:

    while True:
        oled.fill(0)
        #x = int(read_x() / 1023 * 63)
        #y = int(read_y() / 1023 * 63)
        x = read_x()
        time.sleep_ms(50)
        y = read_y()
        time.sleep_ms(50)
        oled.text(u"%s" % x, 0, 0)
        oled.text(u"%s" % y, 0, 10)
        #val = 63 - int(adc.read() / 1023 * 63)
        oled.pixel(x, y, 1)
        oled.show()

except Exception as e:
    oled.fill(0)
    oled.text(u'Error:', 0, 0)
    oled.text(u'%s' % e, 0, 10)
    oled.show()

