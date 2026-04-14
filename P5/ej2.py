from machine import Pin
import utime

# --- CONFIGURACIÓN DE HARDWARE ---
# Pines de las bobinas (A, B, C, D) según Tabla 5-1 [cite: 196, 201]
pins = [Pin(7, Pin.OUT), Pin(6, Pin.OUT), Pin(5, Pin.OUT), Pin(4, Pin.OUT)]

# Pines de Switches (MSB a LSB) [cite: 200, 366]
sw_pins = [Pin(10, Pin.IN, Pin.PULL_DOWN), Pin(9, Pin.IN, Pin.PULL_DOWN), Pin(8, Pin.IN, Pin.PULL_DOWN)]

# Pin del Zumbador [cite: 472]
buzzer = Pin(22, Pin.OUT)

# --- PARÁMETROS DEL MOTOR ---
STEPS_PER_REV = 2048  # Pasos para una vuelta completa (ajustar según motor)
# Secuencia de Pasos Completos de la Figura 5-4 [cite: 125]
secuencia = [
    [1, 1, 0, 0], # Paso 1: Bobina A y B ON
    [0, 1, 1, 0], # Paso 2: Bobina B y C ON
    [0, 0, 1, 1], # Paso 3: Bobina C y D ON
    [1, 0, 0, 1]  # Paso 4: Bobina D y A ON
]

# Variable global para mantener la posición de la secuencia
estado_paso = 0

def obtener_combinacion():
    """Lee los pines y retorna el valor decimal (0-7) y su cadena binaria."""
    bit2 = sw_pins[0].value() # Peso 4 (SW1_1) [cite: 366]
    bit1 = sw_pins[1].value() # Peso 2 (SW1_2) [cite: 366]
    bit0 = sw_pins[2].value() # Peso 1 (SW1_3) [cite: 366]
    valor = (bit2 << 2) | (bit1 << 1) | bit0
    binario = f"{bit2}{bit1}{bit0}"
    return valor, binario

def mover_un_paso(direccion):
    """Ejecuta un solo paso físico en la dirección indicada."""
    global estado_paso
    # direccion: 1 para Horario, -1 para Antihorario
    estado_paso = (estado_paso + direccion) % 4
    
    for i in range(4):
        pins[i].value(secuencia[estado_paso][i])
    utime.sleep_ms(2) # Tiempo mínimo para que el motor responda

def ejecutar_movimiento(pasos_totales, direccion, con_buzzer=False):
    """
    Mueve el motor n pasos, pero revisa constantemente si la combinación cambió.
    Si cambias el switch a PARO (000), el motor se detiene inmediatamente.
    """
    for p in range(pasos_totales):
        # Punto de control: Si el usuario cambia el switch, rompemos el bucle
        actual, _ = obtener_combinacion()
        if actual == 0: 
            return False # Indica que se abortó el movimiento

        mover_un_paso(direccion)
        
        # Lógica del buzzer por revolución [cite: 472]
        if con_buzzer and (p + 1) % STEPS_PER_REV == 0:
            buzzer.value(1)
            utime.sleep_ms(300)
            buzzer.value(0)
    return True

# --- LOOP PRINCIPAL ---
print("--- Sistema de Control de Motor a Pasos Iniciado ---")

while True:
    val, bin_str = obtener_combinacion()
    
    # Imprime en terminal la lectura actual para monitoreo
    print(f"Lectura actual: [{bin_str}] | Acción: ", end="")

    if val == 0: # 000 - PARO [cite: 365, 466]
        print("Motor Detenido")
        for p in pins: p.value(0)
        utime.sleep_ms(100) # Pequeña pausa para no saturar la terminal

    elif val == 1: # 001 - GIRA HORARIO [cite: 365, 467]
        print("Giro Horario Continuo")
        mover_un_paso(1)

    elif val == 2: # 010 - GIRA ANTIHORARIO [cite: 365, 468]
        print("Giro Antihorario Continuo")
        mover_un_paso(-1)

    elif val == 3: # 011 - 90° HORARIO cada 2 seg [cite: 365, 469]
        print("90° Horario")
        if ejecutar_movimiento(STEPS_PER_REV // 4, 1):
            utime.sleep(2)

    elif val == 4: # 100 - 180° ANTIHORARIO cada 3 seg [cite: 365, 469]
        print("180° Antihorario")
        if ejecutar_movimiento(STEPS_PER_REV // 2, -1):
            utime.sleep(3)

    elif val == 5: # 101 - 360° HORARIO cada 4 seg [cite: 365, 469]
        print("360° Horario + Buzzer")
        if ejecutar_movimiento(STEPS_PER_REV, 1, con_buzzer=True):
            utime.sleep(4)

    elif val == 6: # 110 - 5 REVOLUCIONES HORARIO [cite: 365, 469]
        print("5 Revoluciones Horario")
        ejecutar_movimiento(STEPS_PER_REV * 5, 1, con_buzzer=True)

    elif val == 7: # 111 - 10 REVOLUCIONES ANTIHORARIO 
        print("10 Revoluciones Antihorario")
        ejecutar_movimiento(STEPS_PER_REV * 10, -1, con_buzzer=True)