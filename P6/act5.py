from machine import Pin, PWM # Importa los módulos para control de pines y PWM
import time                  # Módulo para el control del tiempo

pwm = PWM(Pin(1))            # Asigna el control PWM al GPIO1
pwm.freq(1000)               # Fija la frecuencia de la señal PWM a 1000 Hz (1kHz)

while True:                  # Bucle infinito
    # Recorre valores de duty cycle desde 0 hasta 65535 en saltos de 500
    for duty in range(0, 65535, 500):
        pwm.duty_u16(duty)   # Actualiza el ancho de pulso (aumenta el brillo)
        time.sleep(0.05)     # Pausa de 50 milisegundos entre cada incremento
        
    pwm.duty_u16(0)          # Apaga el PWM (duty cycle = 0%) de golpe
    time.sleep(2)            # Mantiene el pin apagado por 2 segundos antes de reiniciar