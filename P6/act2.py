from machine import ADC
import time

potenciometro = ADC(26) # Canal ADC0 según la Tabla 6-1

while True:
    valor_adc = potenciometro.read_u16()
    voltaje = valor_adc * (3.3 / 65535) # Conversión a voltaje real
    
    # Formato de impresión solicitado por el manual
    print("Conversión = {}; Voltaje = {:.2f} Volts".format(valor_adc, voltaje))
    
    time.sleep(1) # Actualiza cada segundo