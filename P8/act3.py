import max7219
from machine import Pin, SPI
from time import sleep

num_display = 1 # Según el manual para la prueba inicial
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
cs_pin = Pin(6, Pin.OUT)

display = max7219.Matrix8x8(spi, cs_pin, num_display)

display.fill(0)
display.text('0', 0, 1, 1)
display.show()
sleep(3)