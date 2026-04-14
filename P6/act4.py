from machine import ADC
import time

sensor_interno = ADC(4)
sensor_tmp36 = ADC(28) # Canal ADC2

while True:
    # --- Lectura Sensor Interno ---
    val_int = sensor_interno.read_u16() * (3.3 / 65535)
    temp_int_c = 27 - (val_int - 0.706) / 0.001721
    temp_int_f = (temp_int_c * 9/5) + 32

    # --- Lectura Sensor TMP36 ---
    val_tmp = sensor_tmp36.read_u16() * (3.3 / 65535)
    temp_tmp_c = (val_tmp - 0.5) * 100
    temp_tmp_f = (temp_tmp_c * 9/5) + 32

    # --- Impresión en consola ---
    print("Temperatura interna = {:.0f}°C; {:.0f}°F".format(temp_int_c, temp_int_f))
    print("Temperatura externa TMP36 = {:.0f}°C; {:.0f}°F".format(temp_tmp_c, temp_tmp_f))

    if temp_tmp_c > temp_int_c:
        print("El sensor TMP36 tiene el valor mayor de temperatura")
    elif temp_int_c > temp_tmp_c:
        print("El sensor interno tiene el valor mayor de temperatura")
    else:
        print("Ambos sensores son iguales")
        
    print("-" * 40)
    time.sleep(2)