from machine import Pin
import time

sw1_1 = Pin(8, Pin.IN)      # Pin 8 configurado como entrada (Interruptor)
led_verde = Pin(0, Pin.OUT) # Pin 0 configurado como salida (LED Verde)

while True:
    if sw1_1.value() == 1:
        led_verde.value(1)  # Envía un 1 lógico (3.3V) para encender el LED
        print("Interruptor cerrado, '1'")
        print("LED VERDE en GPIO0 encendido")
        time.sleep(0.5)
    else:
        led_verde.value(0)  # Envía un 0 lógico (0V) para apagar el LED
        print("Interruptor abierto, '0'")
        print("LED VERDE en GPIO0 apagado")
        time.sleep(0.5)