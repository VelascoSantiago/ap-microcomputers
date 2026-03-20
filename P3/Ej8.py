import machine
import utime

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    for led in leds:
        led.value(0)
        
    for i in range(8):
        leds[i].value(1)
        utime.sleep_ms(100)