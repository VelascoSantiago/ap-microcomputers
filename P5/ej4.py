from machine import Pin, PWM
import time

servo = PWM(Pin(21))
servo.freq(50)

# Límites de pulso en nanosegundos
PULSO_MIN = 500_000  # 0°
PULSO_MAX = 2_500_000 # 180°
PASO_NS = 20_000      # Tamaño del salto para suavidad

print("Iniciando Actividad 4 - Servomotor Automático")

while True:
    # Barrido de 0° a 180°
    for pulso in range(PULSO_MIN, PULSO_MAX + 1, PASO_NS):
        servo.duty_ns(pulso)
        time.sleep_ms(10)
        
    time.sleep(0.5) # Pausa en 180°
    
    # Barrido de 180° a 0°
    for pulso in range(PULSO_MAX, PULSO_MIN - 1, -PASO_NS):
        servo.duty_ns(pulso)
        time.sleep_ms(10)
        
    time.sleep(0.5) # Pausa en 0°