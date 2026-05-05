import tm1637
from machine import Pin
from utime import sleep

# Instancia el controlador del display definiendo los pines de reloj y datos
tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
Sec = 0
Min = 0

while True:
    # Muestra los valores actuales y enciende los dos puntos centrales
    tm.numbers(Min, Sec, colon=True)
    sleep(0.5)
    # Mantiene los mismos valores pero apaga los dos puntos
    tm.numbers(Min, Sec, colon=False)
    sleep(0.5)
    
    Sec = Sec + 1 # Incrementa el valor de los segundos
    
    # Lógica de desbordamiento para el reloj
    if Sec == 60:
        Min = Min + 1
        Sec = 0
        if Min == 60:
            Min = 0