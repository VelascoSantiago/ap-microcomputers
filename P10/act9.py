from imu import MPU6050
from machine import Pin, I2C
import utime

# Inicialización del bus I2C en los pines GP8 (SDA) y GP9 (SCL)
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
imu = MPU6050(i2c)

while True:
    # Captura el valor de aceleración en el eje X redondeado a 2 decimales
    ax = round(imu.accel.x, 2)
    print(ax)
    utime.sleep_ms(200)