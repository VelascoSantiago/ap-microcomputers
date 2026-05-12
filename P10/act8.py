import utime
from machine import Pin, I2C
import ahtx0

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.2f C" % sensor.temperature)
    print("Humidity: %0.2f %%" % sensor.relative_humidity)
    utime.sleep(5)