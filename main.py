import machine, utime
led = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(0.1)
    led.value(0)
    utime.sleep(0.1)
    
    led2.value(1)
    utime.sleep(0.1)
    led2.value(0)
    utime.sleep(0.1)
