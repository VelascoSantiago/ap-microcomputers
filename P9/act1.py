import time
from neopixel import Neopixel

# Inicializa la tira Neopixel: 8 LEDs, máquina de estado 0, pin GP0, formato de color GRB
pixels = Neopixel(8, 0, 4, "GRB") 
brightness = 0.1 # Nivel de brillo global (aunque no se aplica directamente en este snippet básico)

# Definición de tuplas de colores en formato (Rojo, Verde, Azul)
red = (255, 0, 0)
black = (0, 0, 0)

while True:
    pixels.set_pixel(0, red)   # Asigna el color rojo al primer LED (índice 0)
    pixels.show()              # Envía la trama de datos para actualizar el estado físico del LED
    time.sleep(1)              # Pausa la ejecución 1 segundo
    pixels.set_pixel(0, black) # Asigna el color negro (apagado) al primer LED
    pixels.show()              # Actualiza la tira para apagar el LED
    time.sleep(1)              # Pausa de 1 segundo antes de repetir el ciclo