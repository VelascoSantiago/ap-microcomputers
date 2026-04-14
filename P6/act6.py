from machine import Pin, PWM
import time

pwm0 = PWM(Pin(0))
pwm1 = PWM(Pin(1))

pwm0.freq(1000)
pwm1.freq(1000)

while True:
    # Ciclo de incremento (Sube GPIO0, Baja GPIO1)
    for duty in range(0, 65535, 500):
        pwm0.duty_u16(duty)
        pwm1.duty_u16(65535 - duty) # Refleja el valor inverso
        time.sleep(0.01)

    # Ciclo de decremento (Baja GPIO0, Sube GPIO1)
    for duty in range(65535, 0, -500):
        pwm0.duty_u16(duty)
        pwm1.duty_u16(65535 - duty) # Refleja el valor inverso
        time.sleep(0.01)