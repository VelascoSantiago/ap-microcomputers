import machine
import utime

# Configuración de Pines según tu diagrama
RS = machine.Pin(0, machine.Pin.OUT)
RW = machine.Pin(1, machine.Pin.OUT)
E  = machine.Pin(2, machine.Pin.OUT)
# Bus de datos de 8 bits (GP3 al GP10)
D = [machine.Pin(i, machine.Pin.OUT) for i in range(3, 11)]

# --- FUNCIONES DE BAJO NIVEL (Sin librerías) ---

def pulso_enable():
    E.value(1)
    utime.sleep_us(1)
    E.value(0)
    utime.sleep_ms(2)

def enviar(valor, modo):
    RS.value(modo) # 0 para comando, 1 para dato
    RW.value(0)    # Siempre escribir [cite: 23]

    for i in range(8):
        # Envía el bit correspondiente al bus de 8 bits [cite: 9]
        D[i].value((valor >> i) & 1)

    pulso_enable()

def comando(cmd):
    enviar(cmd, 0)

def dato(d):
    enviar(d, 1)

# --- CONFIGURACIÓN DEL LCD ---

def lcd_init():
    utime.sleep_ms(50)
    comando(0x38) # Modo 8 bits, 2 líneas [cite: 18]
    comando(0x0C) # Display ON, Cursor OFF
    comando(0x06) # Incremento del cursor
    comando(0x01) # Limpiar pantalla
    utime.sleep_ms(5)

def lcd_clear():
    comando(0x01)
    utime.sleep_ms(5)

def cursor(fila, col):
    direccion = 0x80 + (0x40 * fila) + col
    comando(direccion)

def escribir(texto):
    for c in texto:
        dato(ord(c))

# --- MEMORIA CGRAM (Animación personalizada) ---

# Pac-Man Boca Abierta
pac1 = [0x0E, 0x1D, 0x1E, 0x1C, 0x1E, 0x1F, 0x0E, 0x00]
# Pac-Man Boca Cerrada
pac2 = [0x0E, 0x1D, 0x1F, 0x1F, 0x1F, 0x1F, 0x0E, 0x00]

def cargar_chars():
    comando(0x40) # Inicio de la CGRAM 
    for x in pac1: dato(x) # Carácter 0
    for x in pac2: dato(x) # Carácter 1

# --- EFECTOS Y LÓGICA DEL PROYECTO ---

def desplazar_nombre(texto):
    # Desplazamiento hacia la izquierda [cite: 5]
    texto_aux = texto + " " * 16
    for i in range(len(texto_aux) - 15):
        cursor(0, 0)
        escribir(texto_aux[i:i+16])
        utime.sleep_ms(250)

def animacion_pacman():
    # Animación continua desplazándose a la derecha 
    while True:
        for i in range(16):
            cursor(1, i)
            # Alterna entre boca abierta y cerrada
            if i % 2 == 0:
                dato(0) 
            else:
                dato(1)
            
            utime.sleep_ms(250)
            
            # Borrar rastro
            cursor(1, i)
            escribir(" ")

# --- PROGRAMA PRINCIPAL ---

def main():
    lcd_init()
    cargar_chars()

    # Fase 1: Mostrar información del equipo [cite: 3]
    mensaje = "Equipo 10 - Diego, Gael, Santiago, Charchi"
    desplazar_nombre(mensaje)
    
    # Fase 2: Pausa de dos segundos después de mostrar la info 
    lcd_clear()
    cursor(0, 3)
    escribir("EQUIPO 10")
    utime.sleep(2) # <--- Los 2 segundos obligatorios del PDF
    
    # Fase 3: Animación CGRAM continua a la derecha 
    lcd_clear()
    cursor(0, 0)
    escribir("Animacion CGRAM")
    animacion_pacman()

# Ejecución
main()