from machine import Pin, SPI
import max7219_8digit
import time

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
display = max7219_8digit.Display(spi, ss)

# Entradas de control
btn_up = Pin(12, Pin.IN, Pin.PULL_UP)
btn_down = Pin(13, Pin.IN, Pin.PULL_UP)

contador = 0

while True:
    if btn_up.value() == 0:
        contador += 1
        time.sleep(0.5)
    elif btn_down.value() == 0:
        contador -= 1
        time.sleep(0.5)
        
    # Formatear a 8 espacios para el display
    texto_contador = "{:8d}".format(contador)
    display.write_to_buffer(texto_contador)
    display.display()
    time.sleep(0.05)