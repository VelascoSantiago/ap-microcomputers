from machine import Pin, UART, ADC, PWM
import time

# Inicialización UART0
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))
uart.init(bits=8, parity=None, stop=1)

# Configuración de Periféricos
pot = ADC(Pin(26))       # Potenciómetro en ADC0
ldr = ADC(Pin(27))       # Foto-resistencia en ADC1
tmp36 = ADC(Pin(28))     # Sensor de temp en ADC2
buzzer = PWM(Pin(15))    # Zumbador
leds = [Pin(i, Pin.OUT) for i in range(8)] # Lista de LEDs en GPIO 0 a 7

def apagar_leds():
    for led in leds: led.value(0)

apagar_leds()
uart.write("Sistema Listo. Ingresa un comando (1-7):\n")

while True:
    if uart.any() > 0:
        # Leemos el dato, decodificamos a string y eliminamos espacios extra
        comando = uart.read(1).decode('utf-8').strip()

        if comando == '1':
            voltaje = (pot.read_u16() * 3.3) / 65535
            uart.write(f"Voltaje Pot: {voltaje:.2f} V\n")

        elif comando == '2':
            val_ldr = ldr.read_u16()
            uart.write(f"ADC LDR Hex: {hex(val_ldr)}\n")

        elif comando == '3':
            voltaje_tmp = (tmp36.read_u16() * 3.3) / 65535
            temp_c = (voltaje_tmp - 0.5) * 100
            temp_f = (temp_c * 9/5) + 32
            temp_k = temp_c + 273.15
            uart.write(f"Temp: {temp_c:.1f}C, {temp_f:.1f}F, {temp_k:.1f}K\n")

        elif comando == '4':
            uart.write("Reproduciendo Nota DO...\n")
            buzzer.freq(261) # Frecuencia aproximada de DO (C4)
            buzzer.duty_u16(32768) # 50% ciclo de trabajo
            time.sleep(0.5)
            buzzer.duty_u16(0) # Silenciar

        elif comando == '5':
            uart.write("Parpadeando GPIO0 y GPIO7...\n")
            for _ in range(5):
                leds[0].value(1); leds[7].value(1)
                time.sleep(0.2)
                leds[0].value(0); leds[7].value(0)
                time.sleep(0.2)

        elif comando == '6':
            uart.write("Corrimiento a la derecha...\n")
            apagar_leds()
            for i in range(7, -1, -1): # Cuenta regresiva de 7 a 0
                leds[i].value(1)
                time.sleep(0.2)
                leds[i].value(0)

        elif comando == '7':
            uart.write("Corrimiento a la izquierda...\n")
            apagar_leds()
            for i in range(8): # Cuenta progresiva de 0 a 7
                leds[i].value(1)
                time.sleep(0.2)
                leds[i].value(0)