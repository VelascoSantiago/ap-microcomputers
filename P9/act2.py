import time
from neopixel import Neopixel

pixels = Neopixel(8, 0, 4, "GRB")

# Lista con tres colores distintos: Rojo, Verde y Azul
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
negro = (0, 0, 0)

while True:
    for color in colores:
        # Barrido de izquierda a derecha (0 al 7)
        for i in range(8):
            pixels.set_pixel(i, color)
            pixels.show()
            time.sleep(0.1)
            pixels.set_pixel(i, negro) # Apaga el LED actual para dar el efecto de movimiento
        
        # Barrido de derecha a izquierda (6 al 1, para no repetir los extremos)
        for i in range(6, 0, -1):
            pixels.set_pixel(i, color)
            pixels.show()
            time.sleep(0.1)
            pixels.set_pixel(i, negro)