from machine import Pin
import time

# Configura S1 en GPIO 11 con resistencia Pull-Up interna (1 lógico por defecto)
s1 = Pin(11, Pin.IN, Pin.PULL_UP)

# Configura los pines de los LEDs y el Zumbador como salidas
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)
led6 = Pin(6, Pin.OUT)
led7 = Pin(7, Pin.OUT)
buzzer = Pin(22, Pin.OUT)

while True:
    # Como tiene Pull-Up, si el botón NO está presionado, lee 1
    if s1.value() == 1:
        # Apaga todas las salidas
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        buzzer.value(0)
        print("Push button S1 liberado, '1'")
        print("Salidas en bajo")
    else:
        # Si se presiona, aterriza a GND y lee 0. Enciende todas las salidas.
        led4.value(1)
        led5.value(1)
        led6.value(1)
        led7.value(1)
        buzzer.value(1)
        print("Push button S1 presionado, '0'")
        print("Salidas en alto")
        
    time.sleep(0.2) # Retardo corto para estabilidad