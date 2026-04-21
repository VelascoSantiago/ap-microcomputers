import select
import sys
import time
from machine import Pin

# Configuración del LED integrado de la Raspberry Pi Pico
led = Pin(25, Pin.OUT)

poll_obj = select.poll()
poll_obj.register(sys.stdin, 1)

print("Control de LED vía consola. Ingresa '1' para ON o '0' para OFF:")

while True:
    if poll_obj.poll(0):
        ch = sys.stdin.read(1)
        
        # Lógica de la Tabla 7-2
        if ch == '1':
            led.value(1)
            print("GPIO25 = ON")
        elif ch == '0':
            led.value(0)
            print("GPIO25 = OFF")
            
    time.sleep(0.1)