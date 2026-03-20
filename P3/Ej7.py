import machine
import utime

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    for i in range(8):
        for j in range(8):
            if i == j:
                leds[j].value(1)
            else:
                leds[j].value(0)
        utime.sleep_ms(100)