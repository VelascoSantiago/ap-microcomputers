from ST7735 import TFT
from sysfont import sysfont
from machine import SPI, Pin

spi = SPI(0, baudrate=5000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# INTENTO 1: Usando CS=7, A0=15, RST=14
tft = TFT(spi, 15, 14, 7) 

tft.initg()
tft.rgb(True)
tft.rotation(2)
tft.fill(TFT.WHITE)


# Despliegue de información del equipo
tft.text((10, 10), "Mauricio", TFT.BLUE, sysfont, 2, nowrap=True)
tft.text((10, 35), "Tony", TFT.RED, sysfont, 2, nowrap=True)
tft.text((10, 70), "Santiago", TFT.PURPLE, sysfont, 2, nowrap=True)