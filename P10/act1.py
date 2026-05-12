from machine import Pin, I2C

# Configuración de pines para I2C0
sda = Pin(8)
scl = Pin(9)
# Inicializa el bus I2C con los pines definidos
i2c = I2C(0, scl=scl, sda=sda)

# Escanea el bus en busca de dispositivos conectados
devices = i2c.scan()

if devices:
    for d in devices:
        # Imprime la dirección de cada dispositivo encontrado en formato hexadecimal
        print(hex(d))