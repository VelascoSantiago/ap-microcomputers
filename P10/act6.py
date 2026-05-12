from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0) # Limpia pantalla
oled.text("Microcomputadoras", 1, 6, 1)
oled.text("Practica I2C", 3, 30, 1)
oled.show()
print("UNAM FI")