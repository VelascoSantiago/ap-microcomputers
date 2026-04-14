from machine import Pin, PWM
import time

# Interruptores
s2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
s1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw1_1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw1_2 = Pin(9, Pin.IN, Pin.PULL_DOWN)
sw1_3 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Servomotor
servo = PWM(Pin(21))
servo.freq(50) # Frecuencia de 50Hz (20ms)

def set_angulo(angulo):
    # 0.5ms = 1638 (0 grados), 2.5ms = 8192 (180 grados) en escala 0-65535
    duty = int(1638 + (angulo / 180) * (8192 - 1638))
    servo.duty_u16(duty)

while True:
    # Construir un valor binario de 5 bits con todos los switches
    # (S2, S1, SW1_1, SW1_2, SW1_3)
    estado = (s2.value() << 4) | (s1.value() << 3) | (sw1_1.value() << 2) | (sw1_2.value() << 1) | sw1_3.value()
    
    if estado == 0b01000:
        servo.duty_u16(0) # PARO (desactiva pulso PWM)
    elif estado == 0b01001:
        set_angulo(0)
    elif estado == 0b01010:
        set_angulo(45)
    elif estado == 0b01100:
        set_angulo(90)
    elif estado == 0b00000:
        set_angulo(135)
    elif estado == 0b11000:
        set_angulo(180)
        
    time.sleep(0.1)