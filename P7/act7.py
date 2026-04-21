from machine import Pin, UART
import time

# 1. Configuración de UART para Bluetooth (Pines 16 y 17)
bt = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# 2. Configuración Motor 1
m1_dir1 = Pin(0, Pin.OUT)
m1_dir2 = Pin(1, Pin.OUT)
m1_en = Pin(20, Pin.OUT)
m1_en.value(1) # Habilitar Motor 1

# 3. Configuración Motor 2
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

# Iniciar con los motores apagados por seguridad
control_motor(1, 'PARO')
control_motor(2, 'PARO')

while True:
    # 4. Esperar comandos desde la app Bluetooth
    if bt.any() > 0:
        comando = bt.read(1).decode('utf-8').strip().upper()
        
        # 5. Lógica de movimiento según la letra recibida
        if comando == 'S': # Stop / Paro total
            control_motor(1, 'PARO')
            control_motor(2, 'PARO')
            
        elif comando == 'A': # Adelante
            control_motor(1, 'HORARIO')
            control_motor(2, 'HORARIO')
            
        elif comando == 'T': # aTrás / Reversa
            control_motor(1, 'ANTIHORARIO')
            control_motor(2, 'ANTIHORARIO')
            
        elif comando == 'D': # Derecha (M1 Horario, M2 Antihorario)
            control_motor(1, 'HORARIO')
            control_motor(2, 'ANTIHORARIO')
            
        elif comando == 'I': # Izquierda (M1 Antihorario, M2 Horario)
            control_motor(1, 'ANTIHORARIO')
            control_motor(2, 'HORARIO')