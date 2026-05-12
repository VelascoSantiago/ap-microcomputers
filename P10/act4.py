import pcf8574
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
pcf = pcf8574.PCF8574(i2c, 0x39)

ON = 0
OFF = 1
pcf.port = 0x3F
pcf.pin(6, 1) # Configura P6 como entrada

print("iniciamos")
while True:
    if pcf.pin(6) == 0: # Si se detecta un pulso bajo (botón presionado)
        pcf.pin(0, ON)
        print("Alto")
    else:
        pcf.pin(0, OFF)
        print("bajo")
    pcf.pin(6, 1) # Mantiene el pull-up/estado de lectura