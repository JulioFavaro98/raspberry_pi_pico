import machine
import utime
led = machine.Pin(1, machine.Pin.OUT)
button = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.toggle()
        utime.sleep(0.1)
