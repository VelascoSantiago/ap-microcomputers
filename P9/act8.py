import dht
from machine import Pin
import time

# Configuración de pines según la Tabla 9-1
sensor = dht.DHT11(Pin(21))
led = Pin(20, Pin.OUT)
zumbador = Pin(17, Pin.OUT)

# Aseguramos que las alarmas inicien apagadas
led.value(0)
zumbador.value(0)

# Pausa inicial para permitir que el sensor DHT11 se estabilice
time.sleep(2)

print("Tomando temperatura de referencia...")
try:
    sensor.measure()
    temp_ref = sensor.temperature()
    print(f"Temperatura de Referencia: {temp_ref}°C")
except OSError as e:
    print("Error al leer el sensor DHT11 en el inicio.")
    temp_ref = 25 # Valor de respaldo en caso de error

while True:
    try:
        # Petición de lectura actual
        sensor.measure()
        temp_actual = sensor.temperature()
        print(f"Temperatura actual: {temp_actual}°C")
        
        # Lógica de control según la tabla 9-1
        if temp_actual >= (temp_ref + 1):
            # Condición de alarma activada
            led.value(1)
            zumbador.value(1)
        else:
            # Condición segura
            led.value(0)
            zumbador.value(0)
            
    except OSError as e:
        print("Error en la comunicación con el DHT11.")
        
    time.sleep(2) # Frecuencia de muestreo permitida para el DHT11