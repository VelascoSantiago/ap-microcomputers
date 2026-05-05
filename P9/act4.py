import tm1637
from machine import Pin
from utime import sleep

# Configuración del bus Two-wire para el display
tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
# Configuración del pin del zumbador como salida digital
buzzer = Pin(17, Pin.OUT)

sec = 5

while sec >= 0:
    # Mostramos los minutos en 0 y los segundos actuales, con los dos puntos fijos
    tm.numbers(0, sec, colon=True)
    sleep(1)
    
    if sec == 0:
        # Al llegar a cero, se dispara el zumbador enviando un estado alto
        buzzer.value(1)
        sleep(1) # El sonido dura exactamente un segundo
        buzzer.value(0)
        break # Termina el programa tras la alarma
    
    sec -= 1 # Decrementa el contador