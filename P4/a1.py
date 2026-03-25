from machine import Pin  # Importa la clase Pin del módulo machine para controlar los pines GPIO
import time              # Importa el módulo time para manejar las pausas (retardos)

sw1_1 = Pin(8, Pin.IN)   # Configura el pin GPIO 8 como una entrada digital (conectado al interruptor)

while True:              # Inicia un bucle infinito para leer continuamente el estado del pin
    if sw1_1.value() == 1:                     # Evalúa si el valor leído en el pin 8 es un 1 lógico (3.3V)
        print("Interruptor cerrado, '1'")      # Imprime en consola que el interruptor está cerrado
        time.sleep(0.5)                        # Espera 0.5 segundos antes de la siguiente lectura
    else:                                      # Si el valor leído no es 1 (es decir, es 0 lógico o 0V)
        print("Interruptor abierto, '0'")      # Imprime en consola que el interruptor está abierto
        time.sleep(0.5)                        # Espera 0.5 segundos antes de la siguiente lectura