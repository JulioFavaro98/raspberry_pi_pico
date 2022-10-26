from machine import Pin
import utime

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)

while True:
    led1.value(1)
    led2.value(0)
    led3.value(0)
    utime.sleep(3)
    led1.value(0)
    led2.value(1)
    led3.value(0)
    utime.sleep(3)
    led1.value(0)
    led2.value(0)
    led3.value(1)
    utime.sleep(3)