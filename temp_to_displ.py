import time
import machine
import bme280
import ssd1306

i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

i2c_sensor = machine.I2C(scl=machine.Pin(0), sda=machine.Pin(2))
bme = bme280.BME280(i2c=i2c_sensor)

while True:
    temp, pres, hum = bme.values
    oled.fill(0)
    oled.text(u'Temp: %s' % temp, 0, 0)
    oled.text(u'Humi: %s' % hum, 0, 10)
    oled.text(u'Pres: %s' % pres, 0, 20)
    oled.show()
    time.sleep(1)