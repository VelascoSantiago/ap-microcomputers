import select
import sys
import time
import machine

# Crea un objeto 'poll' para monitorear eventos de entrada/salida
poll_obj = select.poll()
# Registra la entrada estándar (teclado/consola REPL) para monitorear lectura (evento 1)
poll_obj.register(sys.stdin, 1)

# Imprime un mensaje inicial sin salto de línea automático
sys.stdout.write("Esperando recepción de datos \n")
# Imprime una instrucción con salto de línea automático
print("Teclea un caracter y luego <enter>")

while True:
    # Revisa si hay datos listos en la consola (timeout 0 significa que no se bloquea esperando)
    if poll_obj.poll(0):
        ch = sys.stdin.read(1) # Lee 1 solo caracter de la consola
        sys.stdout.write("Dato recibido \n") # Confirma recepción
        print("Hola UNAM") # Imprime el mensaje solicitado
    time.sleep(0.1) # Pequeña pausa para no saturar el procesador