import machine
import utime

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

while True:
    for count in range(256):
        for i in range(8):
            bit_value = (count >> i) & 1
            leds[i].value(bit_value)
        utime.sleep_ms(50)