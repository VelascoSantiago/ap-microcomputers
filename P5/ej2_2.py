from machine import Pin
import utime

# --- CONFIGURACIÓN DE PINES (Tabla 5-1) ---
# Motor: A=7, B=6, C=5, D=4
pins = [Pin(7, Pin.OUT), Pin(6, Pin.OUT), Pin(5, Pin.OUT), Pin(4, Pin.OUT)]
# Switches: 10 (MSB), 9, 8 (LSB)
sw_pins = [Pin(10, Pin.IN, Pin.PULL_DOWN), Pin(9, Pin.IN, Pin.PULL_DOWN), Pin(8, Pin.IN, Pin.PULL_DOWN)]
buzzer = Pin(22, Pin.OUT)

# --- PARÁMETROS ---
STEPS_PER_REV = 2048 
RETARDO_PASO = 2  # <--- Este es el retardo fijo para TODAS las combinaciones
# Secuencia de Pasos Completos (Figura 5-4)
secuencia = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]]

# Variables de estado
estado_paso = 0
ultimo_valor = -1
pasos_pendientes = 0
direccion_actual = 1
espera_ms = 0
tiempo_ultima_accion = 0

def leer_switches():
    """Retorna el valor decimal de la combinación actual[cite: 366, 462]."""
    return (sw_pins[0].value() << 2) | (sw_pins[1].value() << 1) | sw_pins[2].value()

def mover_un_paso(direccion):
    """Ejecuta un solo paso físico[cite: 97]."""
    global estado_paso
    estado_paso = (estado_paso + direccion) % 4
    for i in range(4):
        pins[i].value(secuencia[estado_paso][i])
    utime.sleep_ms(RETARDO_PASO)

# --- LOOP PRINCIPAL ---
print("Sistema Iniciado. Todas las acciones a 2ms por paso.")

while True:
    actual = leer_switches()
    tiempo_ahora = utime.ticks_ms()

    # Si cambias el switch, reseteamos la tarea actual inmediatamente
    if actual != ultimo_valor:
        print(f"Cambio detectado: {bin(actual)[2:].zfill(3)}")
        ultimo_valor = actual
        pasos_pendientes = 0
        espera_ms = 0
        for p in pins: p.value(0) # Paro preventivo

    # --- LÓGICA DE ACCIONES (Tabla 5-2 / 5-3) ---
    if actual == 0: # PARO
        pass 

    elif actual == 1: # GIRA HORARIO CONTINUO
        mover_un_paso(1)

    elif actual == 2: # GIRA ANTIHORARIO CONTINUO
        mover_un_paso(-1)

    elif actual == 3: # 90° HORARIO cada 2 seg [cite: 469]
        if pasos_pendientes <= 0 and utime.ticks_diff(tiempo_ahora, tiempo_ultima_accion) > 2000:
            pasos_pendientes = STEPS_PER_REV // 4
            direccion_actual = 1
        
    elif actual == 4: # 180° ANTIHORARIO cada 3 seg [cite: 469]
        if pasos_pendientes <= 0 and utime.ticks_diff(tiempo_ahora, tiempo_ultima_accion) > 3000:
            pasos_pendientes = STEPS_PER_REV // 2
            direccion_actual = -1

    elif actual == 5: # 360° HORARIO cada 4 seg + Buzzer [cite: 469, 472]
        if pasos_pendientes <= 0 and utime.ticks_diff(tiempo_ahora, tiempo_ultima_accion) > 4000:
            pasos_pendientes = STEPS_PER_REV
            direccion_actual = 1

    elif actual == 6: # 5 REVOLUCIONES HORARIO [cite: 469]
        if pasos_pendientes <= 0:
            pasos_pendientes = STEPS_PER_REV * 5
            direccion_actual = 1

    elif actual == 7: # 10 REVOLUCIONES ANTIHORARIO [cite: 470]
        if pasos_pendientes <= 0:
            pasos_pendientes = STEPS_PER_REV * 10
            direccion_actual = -1

    # --- EJECUTOR DE PASOS PENDIENTES ---
    if pasos_pendientes > 0:
        mover_un_paso(direccion_actual)
        pasos_pendientes -= 1
        
        # Lógica del Buzzer: suena cada que termina una revolución completa (paso % 2048 == 0)
        if (pasos_pendientes % STEPS_PER_REV == 0) and actual >= 5:
            buzzer.value(1)
            utime.sleep_ms(10) # Sonido corto para no bloquear
            buzzer.value(0)
            
        if pasos_pendientes == 0:
            tiempo_ultima_accion = utime.ticks_ms()

    utime.sleep_ms(1) # Respiro para el procesador