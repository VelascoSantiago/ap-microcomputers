from imu import MPU6050
from machine import Pin, I2C
import utime

# Configuración de periféricos
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
imu = MPU6050(i2c)

# Definición de pines para la alarma según la Tabla 10-2
led = Pin(18, Pin.OUT)
buzzer = Pin(17, Pin.OUT)

while True:
    ax_angle = imu.accel.x * 90 # Conversión aproximada a grados para la lógica de la tabla
    
    # Aplicación de las condiciones de la Tabla 10-2
    if -45 <= ax_angle <= 45:
        # Condición 1: Inclinación estable
        led.value(0) # LED (GPIO18) = OFF
        buzzer.value(0) # BUZZER (GPIO17) = OFF
    else:
        # Condición 2: Inclinación crítica (ax <= -46 o ax >= 46)
        led.value(1) # LED (GPIO18) = ON
        buzzer.value(1) # BUZZER (GPIO17) = ON
        
    utime.sleep_ms(200)