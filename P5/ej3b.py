from machine import Pin, PWM
import time

# Configuración del Servo en GP21 a 50Hz (20ms periodo)
servo = PWM(Pin(21))
servo.freq(50)

# Entradas (Respetando pull-up/pull-down indicados en tabla 5-1 y 5-3)
s2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
s1 = Pin(11, Pin.IN, Pin.PULL_UP)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(9, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Tiempos en nanosegundos (1ms = 1,000,000 ns)
ANGULOS = {
    0: 500_000,    # 0.5 ms
    45: 1_000_000, # 1.0 ms
    90: 1_500_000, # 1.5 ms
    135: 2_000_000,# 2.0 ms
    180: 2_500_000 # 2.5 ms
}

print("Iniciando Actividad 3 - Servomotor Manual")

while True:
    estado = (s2.value(), s1.value(), sw1.value(), sw2.value(), sw3.value())
    
    # Tabla 5-3
    if estado == (0, 1, 0, 0, 0):
        servo.duty_ns(0) # PARO (Apaga la señal)
    elif estado == (0, 1, 0, 0, 1):
        servo.duty_ns(ANGULOS[0])
    elif estado == (0, 1, 0, 1, 0):
        servo.duty_ns(ANGULOS[45])
    elif estado == (0, 1, 1, 0, 0):
        servo.duty_ns(ANGULOS[90])
    elif estado == (0, 0, 0, 0, 0):
        servo.duty_ns(ANGULOS[135])
    elif estado == (1, 1, 0, 0, 0):
        servo.duty_ns(ANGULOS[180])
        
    time.sleep(0.1)