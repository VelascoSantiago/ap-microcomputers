import max7219
from machine import Pin, SPI
from time import sleep

num_display = 4 # Matriz 8x8x4
spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
cs_pin = Pin(6, Pin.OUT)
display = max7219.Matrix8x8(spi, cs_pin, num_display)

mensajes = ["UNAM", "F I", "2026", "26-2", "AEV8"]

while True:
    for msg in mensajes:
        display.fill(0)
        display.text(msg, 0, 1, 1)
        display.show()
        sleep(2)