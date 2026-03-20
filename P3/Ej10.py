import machine
import utime

v1 = machine.Pin(0, machine.Pin.OUT)
a1 = machine.Pin(1, machine.Pin.OUT)
r1 = machine.Pin(2, machine.Pin.OUT)

v2 = machine.Pin(7, machine.Pin.OUT)
a2 = machine.Pin(6, machine.Pin.OUT)
r2 = machine.Pin(5, machine.Pin.OUT)

def apagar_todos():
    v1.value(0); a1.value(0); r1.value(0)
    v2.value(0); a2.value(0); r2.value(0)

while True:
    apagar_todos()
    # Estado 1: V1, R2 5 segundos
    v1.value(1)
    r2.value(1)
    utime.sleep(5)
    
    # Estado 2: V1 intermitente, R2 fijo
    v1.value(0)
    for _ in range(5):
        v1.value(1)
        utime.sleep_ms(200)
        v1.value(0)
        utime.sleep_ms(200)
        
    apagar_todos()
    # Estado 3: A1, R2 3 segundos
    a1.value(1)
    r2.value(1)
    utime.sleep(3)
    
    apagar_todos()
    # Estado 4: R1, V2 5 segundos
    r1.value(1)
    v2.value(1)
    utime.sleep(5)
    
    # Estado 5: R1 fijo, V2 intermitente
    v2.value(0)
    for _ in range(5):
        v2.value(1)
        utime.sleep_ms(200)
        v2.value(0)
        utime.sleep_ms(200)
        
    apagar_todos()
    # Estado 6: R1, A2 3 segundos
    r1.value(1)
    a2.value(1)
    utime.sleep(3)