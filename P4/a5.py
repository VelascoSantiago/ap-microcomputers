from machine import Pin, PWM
import time

# --- Configuración de Entradas ---
s2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
s1 = Pin(11, Pin.IN, Pin.PULL_UP)
sw1_1 = Pin(10, Pin.IN)
sw1_2 = Pin(9, Pin.IN)
sw1_3 = Pin(8, Pin.IN)

# --- Configuración de Salidas ---
# LEDs del GPIO 0 al 7
leds = [Pin(i, Pin.OUT) for i in range(8)]

# El buzzer ahora se configura con PWM para poder generar tonos musicales
buzzer_pwm = PWM(Pin(22))
buzzer_pwm.duty_u16(0) # Inicia silenciado (Ciclo de trabajo en 0)

# --- Variables de control ---
paso = 0       
contador = 0   

def leer_estado():
    return (s2.value(), s1.value(), sw1_1.value(), sw1_2.value(), sw1_3.value())

def set_leds(valor_byte):
    for i in range(8):
        leds[i].value((valor_byte >> i) & 1)

def set_contador_4bits(valor):
    leds[3].value((valor >> 0) & 1)
    leds[4].value((valor >> 1) & 1)
    leds[5].value((valor >> 2) & 1)
    leds[6].value((valor >> 3) & 1)

def reproducir_cancion():
    # Frecuencias estándar para la Marcha Imperial (Octava normal)
    LA4 = 440
    FA4 = 349
    DO5 = 523
    
    # Secuencia de la canción: (Frecuencia, Duración en segundos)
    notas_cancion = [
        (LA4, 0.4), (LA4, 0.4), (LA4, 0.4), 
        (FA4, 0.3), (DO5, 0.1), 
        (LA4, 0.4), (FA4, 0.3), (DO5, 0.1), 
        (LA4, 0.8)  # Nota final larga
    ]
    
    set_leds(0) # Apagamos los LEDs 
    print("Reproduciendo: Marcha Imperial (A todo volumen)...")
    
    for frecuencia, duracion in notas_cancion:
        buzzer_pwm.freq(frecuencia)  
        # Potencia al 50% (32768) para sacar el máximo volumen posible del PWM
        buzzer_pwm.duty_u16(32768)    
        time.sleep(duracion)         
        buzzer_pwm.duty_u16(0)       # Silencio
        time.sleep(0.05)             # Pausa muy breve para separar las notas

while True:
    estado = leer_estado()
    
    # Asegurarnos de que el buzzer esté en silencio si no es la opción de la canción
    if estado != (1, 0, 1, 1, 1):
        buzzer_pwm.duty_u16(0)
        
    if estado == (0, 0, 0, 0, 0):
        set_leds(0x00) 
        
    elif estado == (0, 1, 0, 0, 1):
        set_leds(0xFF) 
        
    elif estado == (0, 1, 0, 1, 0):
        set_leds(0xAA if paso % 2 == 0 else 0x55)
        
    elif estado == (0, 1, 0, 1, 1):
        set_leds(0x55 if paso % 2 == 0 else 0xAA)
        
    elif estado == (0, 1, 1, 0, 0):
        set_leds(1 << (7 - (paso % 8)))
        
    elif estado == (0, 1, 1, 0, 1):
        set_leds(1 << (paso % 8))
        
    elif estado == (0, 1, 1, 1, 0):
        sec_adentro = [0x81, 0x42, 0x24, 0x18] 
        set_leds(sec_adentro[paso % 4])
        
    elif estado == (0, 1, 1, 1, 1):
        sec_afuera = [0x18, 0x24, 0x42, 0x81]
        set_leds(sec_afuera[paso % 4])
        
    elif estado == (0, 0, 1, 1, 1):
        set_leds(0) 
        set_contador_4bits(contador)
        contador = (contador + 1) % 10 
        
    elif estado == (1, 1, 1, 1, 1):
        set_leds(0)
        set_contador_4bits(contador)
        contador = 9 if contador == 0 else contador - 1
        
    elif estado == (1, 0, 1, 1, 1):
        # Llama a la función de la canción (Esto detendrá el monitoreo hasta que acabe la melodía)
        reproducir_cancion()
        
    else:
        set_leds(0)

    paso += 1
    time.sleep(0.3)