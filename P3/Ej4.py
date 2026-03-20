import machine
import utime

led1 = machine.Pin(2, machine.Pin.OUT)
led2 = machine.Pin(3, machine.Pin.OUT)

while True:
    led1.value(1)
    led2.value(0)
    utime.sleep_ms(85)
    
    led1.value(0)
    led2.value(1)
    utime.sleep_ms(85)