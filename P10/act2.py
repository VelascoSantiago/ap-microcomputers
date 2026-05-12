import pcf8574
from machine import I2C, Pin
import time

# Inicialización de I2C y el expansor de puertos PCF8574 en la dirección 0x39
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
pcf = pcf8574.PCF8574(i2c, 0x39)

while True:
    # Escribe 0x3F al puerto (enciende/apaga según lógica de bits)
    pcf.port = 0x3F
    print(pcf.port)
    time.sleep(0.8)
    
    # Escribe 0x3E al puerto (cambia el estado del bit menos significativo)
    pcf.port = 0x3E
    print(pcf.port)
    time.sleep(0.8)