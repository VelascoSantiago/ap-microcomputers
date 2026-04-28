from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

# El TFT requiere el pin MISO (GP4) aunque no envíe datos
spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# Pines: a0/dc=14, rst=15, cs=5 (según fig 8-7)
tft = TFT(spi, 15, 14, 7) 
tft.initg()
tft.rgb(True)
tft.rotation(2)

tft.fill(TFT.WHITE)
tft.text((10, 10), "MICROS", TFT.RED, sysfont, 2, nowrap=True)
tft.text((25, 30), "FI", TFT.GREEN, sysfont, 2, nowrap=True)