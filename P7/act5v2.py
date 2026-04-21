from machine import Pin, UART, ADC, PWM
import time

# 1. Configuración Bluetooth (Sigue escuchando en los Pines 16 y 17)
bt = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# 2. Configuración de Sensores
pot = ADC(Pin(26))       
ldr = ADC(Pin(27))       
tmp36 = ADC(Pin(28))     

# 3. Configuración de Actuadores
buzzer = PWM(Pin(22))    
led_0 = Pin(0, Pin.OUT)  
led_7 = Pin(7, Pin.OUT)  

def apagar_leds():
    led_0.value(0)
    led_7.value(0)

apagar_leds()

# ¡CAMBIO AQUÍ! Usamos print() para que salga en Thonny
print("Sistema Listo. Envia un numero (1-5) desde tu app de celular:")

while True:
    if bt.any() > 0:
        comando = bt.read(1).decode('utf-8').strip()
        
        # También imprimimos qué comando recibimos para llevar un registro
        print(f"-> Recibí el comando: {comando}")

        if comando == 'A':
            voltaje = (pot.read_u16() * 3.3) / 65535
            print(f"Voltaje Potenciometro: {voltaje:.2f} V") # Sale en Thonny

        elif comando == 'D':
            val_ldr = ldr.read_u16()
            print(f"ADC LDR Hexadecimal: {hex(val_ldr)}")

        elif comando == 'T':
            voltaje_tmp = (tmp36.read_u16() * 3.3) / 65535
            temp_c = (voltaje_tmp - 0.5) * 100
            temp_f = (temp_c * 9/5) + 32
            temp_k = temp_c + 273.15
            print(f"Temperatura: {temp_c:.1f}°C, {temp_f:.1f}°F, {temp_k:.1f}K")

        elif comando == 'I':
            print("Reproduciendo Nota DO...")
            buzzer.freq(261)       
            buzzer.duty_u16(32768) 
            time.sleep(0.5)        
            buzzer.duty_u16(0)     

        elif comando == 'S':
            print("Parpadeando GPIO0 y GPIO7...")
            for _ in range(5):     
                led_0.value(1); led_7.value(1)
                time.sleep(0.2)
                led_0.value(0); led_7.value(0)
                time.sleep(0.2)
                
        else:
            print("Comando no válido. Ingresa A, D, T, I, S.")