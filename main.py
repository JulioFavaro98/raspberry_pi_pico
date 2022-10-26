from machine import Pin
import utime

led = Pin(15, Pin.OUT)
botao = Pin(5, Pin.IN, Pin.PULL_DOWN)

while True:
    if botao.value() == 1:
        led.toggle()
        utime.sleep(0.5)
