from machine import Pin, SPI
import time
import max7219_8digit
import max7219
from ST7735 import TFT
from sysfont import sysfont

# --- 1. CONFIGURACIÓN DEL BUS SPI COMPARTIDO ---
# Mantenemos 5MHz para evitar ruido electromagnético en la tarjeta
spi = SPI(0, baudrate=5000000, polarity=0, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(4))

# --- 2. CONFIGURACIÓN DE PINES CHIP SELECT (CS) ---
cs_8dig = Pin(5, Pin.OUT)
cs_mat  = Pin(6, Pin.OUT)
# ¡Usa el pin CS que te funcionó en la act 6 para el TFT! Asumiremos el 7.
cs_tft  = Pin(7, Pin.OUT) 

# Por seguridad, ponemos todos los CS en ALTO (inactivos) antes de inicializar
cs_8dig.value(1)
cs_mat.value(1)
cs_tft.value(1)

# --- 3. INICIALIZACIÓN DE LOS 3 DISPLAYS ---
# Display 8 Dígitos
disp_8 = max7219_8digit.Display(spi, cs_8dig)

# Matriz 8x8 (Asumiendo módulo cuádruple de 4 elementos)
disp_mat = max7219.Matrix8x8(spi, cs_mat, 4)

# Display TFT -> ¡REEMPLAZA LOS PINES CON LOS QUE DESCUBRISTE!
# Ejemplo: tft = TFT(spi, 14, 15, 7) o tft = TFT(spi, 15, 14, 7)
tft = TFT(spi, 15, 14, 7) 
tft.initg()
tft.rgb(True)
tft.rotation(2)
tft.fill(TFT.BLACK)

# --- 4. CONFIGURACIÓN DE BOTONES (PULL-UP) ---
# Según la tabla 8-3, la acción es al estar "Cerrado", lo que manda un 0 lógico.
btn_start_rst = Pin(12, Pin.IN, Pin.PULL_UP)
btn_stop      = Pin(13, Pin.IN, Pin.PULL_UP)

# Variables de control
contador = 0
corriendo = False
ultimo_tiempo = time.ticks_ms()

# Despliegue estático en TFT
tft.text((5, 10), "Contador:", TFT.YELLOW, sysfont, 2)

while True:
    # --- LÓGICA DE BOTONES ---
    if btn_start_rst.value() == 0:
        time.sleep_ms(30) # Antirrebote
        if btn_start_rst.value() == 0:
            if corriendo:
                contador = 0 # Reinicia si ya estaba corriendo
            else:
                corriendo = True # Inicia
            # Pausa para evitar que lea el botón múltiple veces si lo mantienes apretado
            while btn_start_rst.value() == 0: pass 
                
    if btn_stop.value() == 0:
        time.sleep_ms(30) 
        if btn_stop.value() == 0:
            corriendo = False # Detiene
            while btn_stop.value() == 0: pass

    # --- INCREMENTO DEL CONTADOR ---
    tiempo_actual = time.ticks_ms()
    if corriendo and time.ticks_diff(tiempo_actual, ultimo_tiempo) >= 1000: # 1 segundo
        contador += 1
        ultimo_tiempo = tiempo_actual

    # --- 5. ACTUALIZACIÓN SIMULTÁNEA DE DISPLAYS ---
    
    # 1. Display 8 dígitos (Formato de 8 espacios alineado a la derecha)
    disp_8.write_to_buffer("{:8d}".format(contador))
    disp_8.display()

    # 2. Matriz 8x8
    disp_mat.fill(0)
    # Centramos un poco el texto, ajusta '0, 1' si quieres que salga más a la derecha
    disp_mat.text(str(contador), 0, 1, 1) 
    disp_mat.show()

    # 3. Display TFT 
    # Dibujamos un rectángulo negro SOLO sobre los números viejos para borrarlos.
    # Si usamos tft.fill(TFT.BLACK), la pantalla parpadeará horrible en cada ciclo.
    tft.fillrect((5, 50), (120, 40), TFT.BLACK)
    tft.text((5, 50), str(contador), TFT.WHITE, sysfont, 4)

    time.sleep_ms(50) # Retardo mínimo para no saturar el bus SPI