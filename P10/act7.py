from machine import Pin, I2C
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=100000)
addr = i2c.scan()
print("address is :" + str(addr))

for i in range(100):
    data = i2c.readfrom(0x48, 2) # Lee 2 bytes del sensor
    intdata = int.from_bytes(data, 'big')
    tmp = intdata >> 4 # Ajusta según resolución del sensor
    print(tmp * 0.0625) # Convierte a grados Celsius
    time.sleep(1)