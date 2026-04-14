from machine import ADC, Pin
import time

fotoresistencia = ADC(27)  
gpio7 = Pin(7, Pin.OUT)    

VREF = 1.5 

print("Iniciando sistema de control de iluminación...")
print("Leyendo voltaje del sistema...")

while True:
    lectura_u16 = fotoresistencia.read_u16()
    voltaje = lectura_u16 * (3.3 / 65535)
    
    print("Voltaje actual: {:.2f} V".format(voltaje))
    
  
    if voltaje < VREF:
        gpio7.value(1)  
    else:
        gpio7.value(0)  
        
    time.sleep(0.5)  