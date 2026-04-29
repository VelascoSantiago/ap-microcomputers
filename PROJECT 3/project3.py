from machine import Pin, Timer
import time

# Equipo 8
# Microcomputadoras

# Configuración de Pines para Segmentos (A-G + DP)
segments = [Pin(i, Pin.OUT) for i in range(2, 10)]

# Configuración de Pines para Dígitos (NUEVOS PINES: GP18 a GP21 para los transistores)
digits = [Pin(i, Pin.OUT) for i in range(18, 22)]

# Pines para Botones (Pull-up externo físico + interno de seguridad)
btn_start = Pin(14, Pin.IN, Pin.PULL_UP)
btn_reset = Pin(15, Pin.IN, Pin.PULL_UP)

# Mapas de bits para los números (7 segmentos: A,B,C,D,E,F,G)
# 0 = apagado, 1 = encendido (Cátodo Común, Lógica Directa)
num_map = {
    '0': [1,1,1,1,1,1,0],
    '1': [0,1,1,0,0,0,0],
    '2': [1,1,0,1,1,0,1],
    '3': [1,1,1,1,0,0,1],
    '4': [0,1,1,0,0,1,1],
    '5': [1,0,1,1,0,1,1],
    '6': [1,0,1,1,1,1,1],
    '7': [1,1,1,0,0,0,0],
    '8': [1,1,1,1,1,1,1],
    '9': [1,1,1,1,0,1,1],
    'off': [0,0,0,0,0,0,0]
}

# Variables de estado
seconds = 0
minutes = 0
running = False
last_ticks = 0

def display_digit(digit_idx, value, show_dp=False):
    # 1. APAGAR todos los transistores mandando 0 (LOW)
    for d in digits: 
        d.value(0)
    
    # 2. Configurar segmentos
    pattern = num_map[value]
    for i in range(7):
        segments[i].value(pattern[i])
    
    # 3. Punto decimal (DP es el pin GP9, índice 7)
    segments[7].value(1 if show_dp else 0)
    
    # 4. ENCENDER el transistor actual mandando 1 (HIGH) a su base
    digits[digit_idx].value(1)
    time.sleep_ms(4) # Tiempo de refresco

def handle_start(pin):
    global running
    # Debounce simple
    time.sleep_ms(50)
    if pin.value() == 0:
        running = not running

def handle_reset(pin):
    global seconds, minutes, running
    # Debounce simple
    time.sleep_ms(50)
    if pin.value() == 0:
        running = False
        seconds = 0
        minutes = 0

# Configuración de Interrupciones (Lógica Inversa: detecta cuando cae a 0)
btn_start.irq(trigger=Pin.IRQ_FALLING, handler=handle_start)
btn_reset.irq(trigger=Pin.IRQ_FALLING, handler=handle_reset)

last_time = time.ticks_ms()

while True:
    # Lógica del cronómetro
    if running:
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_time) >= 1000:
            seconds += 1
            if seconds >= 60:
                seconds = 0
                minutes += 1
            if minutes >= 100: # Límite del display 99:59
                minutes = 0
            last_time = current_time

    # Preparar strings para el display (formato 00)
    s_min = "{:02d}".format(minutes)
    s_sec = "{:02d}".format(seconds)
    display_str = s_min + s_sec

    # Renderizar cada dígito (Multiplexación)
    for i in range(4):
        # En el segundo dígito activamos el punto para separar Min:Seg
        display_digit(i, display_str[i], show_dp=(i == 1))