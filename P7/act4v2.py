from machine import Pin, UART
import time

# Configuración del UART0 para el Bluetooth (Pines 16 y 17)
bt = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# Configuración del LED integrado de la tarjeta
led = Pin(25, Pin.OUT)

# Mensaje de bienvenida directo en la consola de Thonny
print('Inicia Comunicación Bluetooth (Modo Monitor)')
print('Esperando a que envíes algo desde la app...')

while True:
    # Revisa si la tablet ha enviado algún mensaje
    if bt.any() > 0:
        data = bt.read() # Lee los datos recibidos (llegan en formato de 'bytes')
        
        # Intentamos decodificar los bytes a texto normal para leerlo en Thonny
        try:
            texto = data.decode('utf-8').strip()
            print(f"-> Recibido desde la app: {texto}")
        except:
            # Por si envías un caracter extraño que no se pueda decodificar
            print(f"-> Dato crudo recibido: {data}")

        # ECO: Enviamos el mismo dato de regreso a la app de la tablet
        bt.write(data)   
        
        # Cambia el estado del LED integrado
        led.toggle()     
        
    time.sleep(0.1)