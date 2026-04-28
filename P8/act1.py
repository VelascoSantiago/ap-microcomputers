from machine import Pin, SPI
import max7219_8digit
import time

# Configuración del bus SPI0
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
# Configuración del pin Chip Select (CS/SS)
ss = Pin(5, Pin.OUT)

# Inicialización del display
display = max7219_8digit.Display(spi, ss)

# Despliega en el buffer
display.write_to_buffer("01234567")
# Despliega en el display
display.display()
time.sleep(1)