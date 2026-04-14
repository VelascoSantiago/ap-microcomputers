from machine import ADC, Pin # Importa las clases necesarias para hardware
import time                  # Importa la librería para retardos

Sensor = ADC(4)              # Inicializa el canal ADC4 (sensor de temperatura interno)

while True:                  # Inicia un bucle de ejecución infinita
    
    # Lee el valor crudo de 16 bits (0-65535) y lo convierte a un voltaje (0 a 3.3V)
    Valor = Sensor.read_u16() * (3.3 / 65535) 
    
    # Calcula la temperatura en °C usando la ecuación específica del sensor de la Pico
    Temp = 27 - (Valor - 0.706) / 0.001721    
    
    print(Temp)              # Imprime el valor de la temperatura en la consola
    # (Nota: Faltaría un time.sleep() para no saturar la consola)