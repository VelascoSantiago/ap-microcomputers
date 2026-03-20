import machine

leds = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

for led in leds:
    led.value(0)
