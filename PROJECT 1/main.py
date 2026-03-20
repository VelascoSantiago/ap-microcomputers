from machine import Pin
import time

# -------------------------
# Configuración LEDs (Actualizado a GP6-GP13)
# -------------------------
leds = [Pin(i, Pin.OUT) for i in range(6, 14)]

# -------------------------
# Configuración DIP
# -------------------------
dip0 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip1 = Pin(5, Pin.IN, Pin.PULL_DOWN)

# -------------------------
# Funciones auxiliares
# -------------------------
def leer_dip():
    return (dip1.value() << 1) | dip0.value()

def apagar_todos():
    for led in leds:
        led.off()

# -------------------------
# SECUENCIA 0
# Todos parpadean
# -------------------------
def secuencia_0():
    apagar_todos()
    for led in leds:
        led.on()
    time.sleep(1)
    apagar_todos()
    time.sleep(1)

# -------------------------
# SECUENCIA 1
# Corrimiento ida y vuelta
# -------------------------
def secuencia_1():
    for i in range(8):
        apagar_todos()
        leds[i].on()
        time.sleep(0.5)

    for i in range(6, -1, -1):
        apagar_todos()
        leds[i].on()
        time.sleep(0.5)

# -------------------------
# SECUENCIA 2
# Centro hacia extremos
# -------------------------
def secuencia_2():
    apagar_todos()

    for i in range(4):
        leds[3 - i].on()
        leds[4 + i].on()
        time.sleep(0.5)

    for i in range(3, -1, -1):
        leds[3 - i].off()
        leds[4 + i].off()
        time.sleep(0.5)

# -------------------------
# SECUENCIA 3
# Corrimiento acumulativo de dos LEDs
# -------------------------
def secuencia_3():
    apagar_todos()

    # Encender acumulativamente hacia la derecha
    for i in range(0, 8, 2):
        leds[i].on()
        if i + 1 < 8:
            leds[i + 1].on()
        time.sleep(0.5)

    # Apagar acumulativamente hacia la izquierda
    for i in range(6, -2, -2):
        if i >= 0:
            leds[i].off()
        if i + 1 < 8 and i + 1 >= 0:
            leds[i + 1].off()
        time.sleep(0.5)

# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
while True:
    modo = leer_dip()

    if modo == 0:
        secuencia_0()
    elif modo == 1:
        secuencia_1()
    elif modo == 2:
        secuencia_2()
    elif modo == 3:
        secuencia_3()
    else:
        apagar_todos()