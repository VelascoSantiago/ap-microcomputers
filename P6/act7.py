from machine import ADC, Pin, PWM
import time

potenciometro = ADC(26) # Entrada analógica en GPIO26 (ADC0)

pwm0 = PWM(Pin(0))      # Salida PWM directa
pwm1 = PWM(Pin(1))      # Salida PWM inversa

pwm0.freq(1000)
pwm1.freq(1000)

while True:
    # El valor del ADC mapea perfectamente con el duty_u16 ya que ambos son de 16 bits (0-65535)
    lectura = potenciometro.read_u16() 
    
    pwm0.duty_u16(lectura)            # Asigna la lectura directa
    pwm1.duty_u16(65535 - lectura)    # Asigna la lectura inversa
    
    time.sleep(0.05) # Pequeño retardo para estabilizar la lectura y evitar parpadeos