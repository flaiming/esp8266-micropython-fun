import time
import machine
import ssd1306


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

try:
    adc = machine.ADC(0)

    while True:
        oled.fill(0)
        val = 63 - int(adc.read() / 1023 * 63)
        for i in range(127):
            oled.pixel(i, val, 1)
        #oled.text(u"%s" % val, 0, 0)
        oled.show()

except Exception as e:
    oled.fill(0)
    oled.text(u'Error:', 0, 0)
    oled.text(u'%s' % e, 0, 10)
    oled.show()

