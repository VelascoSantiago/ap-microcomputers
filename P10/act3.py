import pcf8574
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8))
pcf = pcf8574.PCF8574(i2c, 0x39)

# Secuencia basada en la Tabla 10-1 de image_4.png
secuencia = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20]

while True:
    for valor in secuencia:
        pcf.port = valor
        time.sleep(0.5)