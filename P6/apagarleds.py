from machine import Pin

# Definimos los pines que usaste para los LEDs en las prácticas
led_gpio0 = Pin(0, Pin.OUT)
led_gpio1 = Pin(1, Pin.OUT)
led_gpio7 = Pin(7, Pin.OUT)

# Apagamos todos los LEDs enviando un 0 (LOW)
led_gpio0.value(0)
led_gpio1.value(0)
led_gpio7.value(0)

print("¡Todos los LEDs han sido apagados exitosamente!")