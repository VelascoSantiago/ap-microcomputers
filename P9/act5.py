import machine, onewire, ds18x20, time

# Inicializa el bus 1-Wire en el pin GP16
ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

# Busca y almacena las direcciones de hardware únicas de los sensores conectados
roms = ds_sensor.scan()
print("Sensor detectado", roms)

while True:
    # Envía el comando global para que todos los sensores inicien la lectura térmica
    ds_sensor.convert_temp()
    time.sleep_ms(750) # Retardo crítico por la hoja de datos para la conversión de 12 bits
    
    for rom in roms:
        print(rom)
        # Recupera los datos calculados desde la memoria del sensor (Scratchpad)
        tempC = ds_sensor.read_temp(rom)
        print('temperatura (°C):', "{:.2f}".format(tempC))
        print()
    time.sleep(2)