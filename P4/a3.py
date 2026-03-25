from machine import Pin  # Importa la clase Pin
import time              # Importa la clase time para retardos

LED = Pin(0, Pin.OUT)                            # Configura el pin GPIO 0 como salida digital para el LED
push_S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)         # Configura el pin GPIO 12 como entrada y activa la resistencia Pull-Down interna

while True:                                      # Bucle infinito
    if push_S2.value() == 0:                     # Si el botón no está presionado (Pull-Down mantiene el estado en 0)
        LED.value(0)                             # Apaga el LED
        print("Push Button S2 en espera; ... lectura: '0'") # Imprime estado de espera
        time.sleep(0.5)                          # Retardo de medio segundo
    else:                                        # Si el botón está presionado (conecta a 3.3V, cambiando a 1 lógico)
        LED.value(1)                             # Enciende el LED
        print("Push Button S2 presionado; ... lectura: '1'") # Imprime estado presionado
        time.sleep(0.5)                          # Retardo de medio segundo