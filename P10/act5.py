from machine import I2C, Pin
import time
from esp8266_i2c_lcd import I2cLcd

DEFAULT_I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

lcd.putstr("UNAM!\nFI")
time.sleep(3)
lcd.clear()

lcd.move_to(3, 0)
lcd.putstr("Laboratorio")
lcd.move_to(0, 1)
lcd.putstr("* M I C R O S *")
time.sleep(1)