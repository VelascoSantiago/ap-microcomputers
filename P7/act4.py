from machine import Pin, UART
import time

# Crea la instancia UART0 a 9600 baudios, usando el Pin 16 para Transmisión (TX) y Pin 17 para Recepción (RX)
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
# Configura el frame de datos: 8 bits de datos, sin paridad, 1 bit de paro
uart.init(bits=8, parity=None, stop=1)

# Configura el LED integrado como salida
led = Pin(25, Pin.OUT)

# Envía un mensaje inicial hacia el monitor serie (ej. PuTTY)
uart.write('Inicia Comunicacion Serie\n')

while True:
    # Comprueba si existen bytes esperando en el buffer de recepción UART
    if uart.any() > 0:
        data = uart.read() # Lee todos los datos disponibles
        uart.write(data)   # Eco: Envía de vuelta exactamente lo que recibió
        led.toggle()       # Invierte el estado del LED (si estaba prendido se apaga y viceversa)
    time.sleep(1)