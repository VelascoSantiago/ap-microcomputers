from machine import Pin
import time

# Configuración de Entradas (Interruptores)
sw1_1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw1_2 = Pin(9, Pin.IN, Pin.PULL_DOWN)
sw1_3 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Configuración Motor 1
m1_dir1 = Pin(0, Pin.OUT)
m1_dir2 = Pin(1, Pin.OUT)
m1_en = Pin(20, Pin.OUT)
m1_en.value(1) # Habilitar Motor 1

# Configuración Motor 2
m2_dir1 = Pin(2, Pin.OUT)
m2_dir2 = Pin(3, Pin.OUT)
m2_en = Pin(19, Pin.OUT)
m2_en.value(1) # Habilitar Motor 2

def control_motor(motor, estado):
    """Controla el giro: 'PARO', 'HORARIO', 'ANTIHORARIO'"""
    if motor == 1:
        d1, d2 = m1_dir1, m1_dir2
    else:
        d1, d2 = m2_dir1, m2_dir2
        
    if estado == 'PARO':
        d1.value(0); d2.value(0)
    elif estado == 'HORARIO':
        d1.value(1); d2.value(0)
    elif estado == 'ANTIHORARIO':
        d1.value(0); d2.value(1)

while True:
    # Leer el estado de los interruptores (formato binario: ej. 101)
    estado = (sw1_1.value() << 2) | (sw1_2.value() << 1) | sw1_3.value()
    
    if estado == 0b000: # 0
        control_motor(1, 'PARO'); control_motor(2, 'PARO')
    elif estado == 0b001: # 1
        control_motor(1, 'HORARIO'); control_motor(2, 'PARO')
    elif estado == 0b010: # 2
        control_motor(1, 'PARO'); control_motor(2, 'HORARIO')
    elif estado == 0b011: # 3
        control_motor(1, 'HORARIO'); control_motor(2, 'HORARIO')
    elif estado == 0b100: # 4
        control_motor(1, 'ANTIHORARIO'); control_motor(2, 'HORARIO')
    elif estado == 0b101: # 5
        control_motor(1, 'HORARIO'); control_motor(2, 'ANTIHORARIO')
    elif estado == 0b110: # 6
        control_motor(1, 'ANTIHORARIO'); control_motor(2, 'ANTIHORARIO')
    elif estado == 0b111: # 7
        control_motor(1, 'PARO'); control_motor(2, 'PARO')
        
    time.sleep(0.1)