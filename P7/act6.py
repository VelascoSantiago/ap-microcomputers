from machine import Pin, UART

# Asumiendo que conectas el HC-05/HC-06 en los mismos pines UART0 (TX 16, RX 17)
bt = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

leds = [Pin(0, Pin.OUT), Pin(1, Pin.OUT), Pin(2, Pin.OUT), Pin(3, Pin.OUT)]

def apagar_todos():
    for led in leds: led.value(0)

apagar_todos()

while True:
    if bt.any() > 0:
        dato = bt.read(1).decode('utf-8').strip().upper() # .upper() para no distinguir entre 'a' y 'A'

        if dato == 'A':
            leds[0].value(1)
        elif dato == 'T':
            leds[1].value(1)
        elif dato == 'D':
            leds[2].value(1)
        elif dato == 'I':
            leds[3].value(1)
        elif dato == 'S':
            apagar_todos()