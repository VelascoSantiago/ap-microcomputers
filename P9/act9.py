import machine, onewire, ds18x20, time, dht, tm1637
from neopixel import Neopixel
from machine import Pin

# --- 1. Configuración de Neopixel (Semáforos) ---
# OJO: La tabla indica que ahora se usa el GPIO4
pixels = Neopixel(8, 0, 4, "GRB")

verde = (0, 255, 0)
amarillo = (255, 255, 0)
rojo = (255, 0, 0)
negro = (0, 0, 0)

# --- 2. Configuración Displays TM1637 ---
# Display 1 (DS18B20): CLK en GPIO0, DIO en GPIO1
tm_ds = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
# Display 2 (DHT11): CLK en GPIO10, DIO en GPIO11
tm_dht = tm1637.TM1637(clk=Pin(10), dio=Pin(11))

# --- 3. Configuración Sensores Térmicos ---
# DS18B20 en GPIO16
ds_pin = Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()

# DHT11 en GPIO21
dht_sensor = dht.DHT11(Pin(21))

def apagar_semaforos():
    for i in range(8):
        pixels.set_pixel(i, negro)
    pixels.show()

while True:
    # ---------------------------------------------------------
    # FASE A: Secuencia de Semáforos
    # ---------------------------------------------------------
    apagar_semaforos()
    
    # Estado 1: S1 en Verde (LED 0), S2 en Rojo (LED 7)
    pixels.set_pixel(0, verde)
    pixels.set_pixel(7, rojo)
    pixels.show()
    time.sleep(3)
    
    # Estado 2: S1 en Amarillo (LED 1), S2 en Rojo (LED 7)
    pixels.set_pixel(0, negro)
    pixels.set_pixel(1, amarillo)
    pixels.show()
    time.sleep(1)
    
    # Estado 3: S1 en Rojo (LED 2), S2 en Verde (LED 5)
    pixels.set_pixel(1, negro)
    pixels.set_pixel(2, rojo)
    pixels.set_pixel(7, negro)
    pixels.set_pixel(5, verde)
    pixels.show()
    time.sleep(3)
    
    # Estado 4: S1 en Rojo (LED 2), S2 en Amarillo (LED 6)
    pixels.set_pixel(5, negro)
    pixels.set_pixel(6, amarillo)
    pixels.show()
    time.sleep(1)
    
    apagar_semaforos()

    # ---------------------------------------------------------
    # FASE B: Lectura y muestra de temperaturas
    # ---------------------------------------------------------
    
    # Lectura del DS18B20
    temp_ds_val = 0
    if roms:
        ds_sensor.convert_temp()
        time.sleep_ms(750) # Tiempo de conversión requerido
        temp_ds_val = int(ds_sensor.read_temp(roms[0]))
        
    # Lectura del DHT11
    temp_dht_val = 0
    try:
        dht_sensor.measure()
        temp_dht_val = dht_sensor.temperature()
    except OSError:
        pass # Si falla, mantendrá el valor 0
    
    # Visualización en los displays. 
    # Al enviarlo como tm.numbers(0, valor), se mostrará en la forma "00:XX"
    tm_ds.numbers(0, temp_ds_val, colon=False)
    tm_dht.numbers(0, temp_dht_val, colon=False)
    
    # Mantenemos las temperaturas en pantalla 3 segundos antes de iniciar 
    # la secuencia de los semáforos otra vez.
    time.sleep(3)