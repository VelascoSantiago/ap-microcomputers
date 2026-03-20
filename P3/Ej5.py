import machine
import utime

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    for led in leds:
        led.value(1)
    utime.sleep_ms(500)
    
    for led in leds:
        led.value(0)
    utime.sleep_ms(500)