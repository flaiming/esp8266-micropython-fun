import sys
import network
import time
import socket
import machine
import bme280

def do_connect(wlan):
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('____', 'naseHesloJeJednaDlouhaVeta')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()


def log(text, exception=None):
    with open('log.txt', 'w+') as f:
        f.write("[%s] %s: %s\n" % (time.ticks_ms(), text, exception))
        if exception:
            sys.print_exception(exception, f)


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)
wlan = network.WLAN(network.STA_IF)

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

try:
    do_connect(wlan)
    if wlan.isconnected():
        temp, pres, hum = bme.values
        #print("Temp:", temp)
        #print("Humi:", hum)
        #print()
        http_get("https://api.thingspeak.com/update?api_key=7HYDO7KRHIJNKX2S&field1={}&field2={}&field3={}&field4={}&field5={}".format(
            temp[:-1],
            temp[:-1],
            hum[:-1],
            hum[:-1],
            pres
        ))
    wlan.active(False)
    # set RTC.ALARM0 to fire after 60 min (waking the device)
    rtc.alarm(rtc.ALARM0, 60000)

    # put the device to sleep
    machine.deepsleep()
except Exception as e:
    log("Some exception", e)

