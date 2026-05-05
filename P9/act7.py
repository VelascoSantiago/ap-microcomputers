import dht
from machine import Pin
import time

# Se define la instancia del DHT11 conectada al pin de entrada/salida 21
sensor = dht.DHT11(Pin(21))

while True:
    try:
        # Petición de lectura física al sensor
        sensor.measure()
        # Asignación de variables desde los búferes del objeto
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print("Temperatura: {} °C".format(temp))
        print("Humedad: {} %".format(hum))
    except OSError as e:
        print("Error en la comunicación con el DHT11.")
        
    # El DHT11 tiene una tasa de muestreo máxima de 1Hz, un retraso de 2s garantiza estabilidad
    time.sleep(2)