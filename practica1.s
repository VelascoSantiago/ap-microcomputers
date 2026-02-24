/*
 * Actividad 4: Promedio de dos números de 8 bits
 * Basado en el código de ejemplo de la Actividad 1
 * Fórmula: Promedio = (DATO1 + DATO2) / 2
 */

.text
.global _start

_start:
    @ 1. Cargar los dos datos (números de 8 bits) en los registros r1 y r2
    mov r1, #0x19      @ DATO1 = 25 en decimal (0x19 en hexadecimal)
    mov r2, #53        @ DATO2 = 53 en decimal
    
    @ 2. Sumar DATO1 y DATO2
    add r3, r2, r1     @ r3 = r2 + r1 (r3 contendrá 53 + 25 = 78)
    
    @ 3. Dividir entre 2 para obtener el promedio
    @ En ensamblador ARM, una división entre 2 (potencia de 2) 
    @ se hace de manera muy eficiente con un desplazamiento a la derecha de 1 bit.
    lsr r4, r3, #1     @ r4 = r3 / 2 (Logical Shift Right de 1 bit) -> r4 = 39
    
    @ 4. Preparar la salida del programa
    mov r0, r4         @ Movemos el resultado final del promedio a r0
    mov r7, #1         @ Cargar el número de llamada al sistema para 'exit' (1)
    svc 0              @ Llamada al sistema (Supervisor Call) para terminar


/*
 * Actividad 5: Comentar código de ejemplo
 * Descripción: Este programa es un bucle infinito que cuenta hacia arriba
 * desde 0 hasta 9, y luego cuenta hacia abajo desde 9 hasta 0 repetidamente.
 */

.global main

main:   
    mov R0, #0       @ Inicializa el registro R0 con el valor 0 (actuará como contador)
    mov r1, #9       @ Inicializa el registro R1 con el valor 9 (límite superior)
    mov r2, #0       @ Inicializa el registro R2 con el valor 0 (límite inferior)

loop1:  
    add r0, r0, #1   @ Incrementa el contador: R0 = R0 + 1
    cmp r1, r0       @ Compara el límite superior (R1=9) con el contador actual (R0)
    bne loop1        @ Branch if Not Equal (Salta a 'loop1' si no son iguales).
                     @ Sigue iterando aquí hasta que R0 alcance el valor de 9.

loop2:  
    add r0, r0, #-1  @ Decrementa el contador sumando -1: R0 = R0 - 1
    cmp r2, r0       @ Compara el límite inferior (R2=0) con el contador actual (R0)
    beq loop1        @ Branch if Equal (Salta a 'loop1' si son iguales).
                     @ Si R0 llegó a 0, regresa a 'loop1' para volver a subir a 9.
    b loop2          @ Salto incondicional: Salta siempre a 'loop2'.
                     @ Si no ha llegado a 0, continúa restando en este mismo ciclo.


/*
 * Actividad 6: Recorrer un bit desde la posición menos significativa
 * hacia la más significativa (corrimiento de bits a la izquierda).
 */

.global main

main:
    mov r3, #1          @ Inicia con el bit menos significativo activado (0x00000001)
    
loop_shift:
    lsl r3, r3, #1      @ LSL (Logical Shift Left): Desplaza el bit 1 posición a la izquierda
    cmp r3, #0          @ Compara si el registro se volvió 0 (el bit fue empujado fuera del bit 31)
    beq main_act6       @ Si es 0, el ciclo terminó. Salta a 'main_act6' para reiniciar en 1.
    b loop_shift        @ Si el registro no es 0, repite el desplazamiento.


/*
 * Actividad 7: Suma de dos números de 32 bits y almacenar con acarreo.
 */
.global main_act7

main_act7:
    @ Cargar datos de ejemplo de 32 bits
    ldr r1, =0xFFFFFFFF  @ DATO1_32_BITS (Valor máximo para forzar un acarreo al sumar)
    ldr r2, =0x00000005  @ DATO2_32_BITS
    
    @ Realizar la suma y actualizar las banderas de estado (con la letra 's' en adds)
    adds r3, r1, r2      @ RESULTADO_32BITS = DATO1 + DATO2. Se actualiza la bandera C (Acarreo).
    
    @ Almacenar el resultado en la memoria
    ldr r4, =res_32      @ Cargar la dirección de memoria de res_32
    str r3, [r4]         @ Guardar el resultado en esa dirección
    
    @ Obtener y almacenar el estado del acarreo
    mov r5, #0           @ Inicializar un registro en 0
    adc r5, r5, #0       @ adc (Add with Carry): r5 = 0 + 0 + C (Bandera de acarreo)
    ldr r6, =carry_32    @ Cargar la dirección de memoria de carry_32
    str r5, [r6]         @ Guardar el estado del acarreo (0 o 1) en memoria


/*
 * Actividad 8: Suma de dos números de 64 bits y almacenar con acarreo.
 */
.global main_act8

main_act8:
    @ DATO1 de 64 bits = 0x00000001_FFFFFFFF
    mov r0, #0x00000001  @ DATO1_64_BITS_H (Parte alta)
    ldr r1, =0xFFFFFFFF  @ DATO1_64_BITS_L (Parte baja)
    
    @ DATO2 de 64 bits = 0x00000002_00000005
    mov r2, #0x00000002  @ DATO2_64_BITS_H (Parte alta)
    ldr r3, =0x00000005  @ DATO2_64_BITS_L (Parte baja)
    
    @ Sumar primero las partes bajas y actualizar banderas (adds)
    adds r4, r1, r3      @ r4 = L1 + L2. Si hay desbordamiento, la bandera de Acarreo (C) será 1.
    
    @ Sumar las partes altas incluyendo el acarreo anterior (adc) y actualizar banderas (adcs)
    adcs r5, r0, r2      @ r5 = H1 + H2 + Carry de la suma baja.
    
    @ Almacenar los resultados en memoria
    ldr r6, =res_64_L
    str r4, [r6]         @ Guardar RESULTADO_64_BITS_L
    ldr r7, =res_64_H
    str r5, [r7]         @ Guardar RESULTADO_64_BITS_H
    
    @ Almacenar el estado del acarreo final (de la suma de las partes altas)
    mov r8, #0
    adc r8, r8, #0       @ r8 = 0 + 0 + C (Carry final)
    ldr r9, =carry_64
    str r8, [r9]         @ Guardar ESTADO DEL ACARREO


/*
 * Actividad 9: Factorial de un número de 8 bits (Resultado = n!)
 */
.global main_act9

main_act9:
    mov r0, #5           @ n = 5 (Ejemplo: calcular factorial de 5 -> 5! = 120)
    mov r1, r0           @ r1 será el acumulador del resultado (inicia valiendo n)
    mov r2, r0           @ r2 será el decrementador (n)

    @ Verificar casos especiales (0! o 1!)
    cmp r0, #1
    ble caso_base_fact

loop_factorial:
    sub r2, r2, #1       @ Decrementar: n = n - 1
    cmp r2, #1           @ ¿Llegamos a 1?
    beq fin_factorial    @ Si llegamos a 1, terminamos las multiplicaciones
    
    mul r3, r1, r2       @ r3 = Acumulador * (n-1)
    mov r1, r3           @ Guardar el nuevo valor en el acumulador (r1)
    b loop_factorial     @ Repetir el ciclo de multiplicación

caso_base_fact:
    mov r1, #1           @ Si n = 0 o n = 1, el resultado del factorial es 1

fin_factorial:
    @ El resultado final (n!) queda almacenado en el registro r1.
    nop                  @ Fin de la actividad (Sin operación, útil para poner breakpoints)


/*
 * =================================================================
 * SECCIÓN DE DATOS (.data):
 * Aquí se reservan los espacios en memoria para guardar los resultados
 * =================================================================
 */
.data
    res_32:    .word 0      @ Actividad 7: Espacio para resultado de 32 bits
    carry_32:  .word 0      @ Actividad 7: Espacio para el acarreo
    
    res_64_L:  .word 0      @ Actividad 8: Espacio para el resultado bajo (L)
    res_64_H:  .word 0      @ Actividad 8: Espacio para el resultado alto (H)
    carry_64:  .word 0      @ Actividad 8: Espacio para el acarreo final


/*
 * Actividad 10: Implementar un ciclo for en ensamblador
 * Equivalente en C:
 * int j = 0;
 * for (i = 0; i <= 50; i++) { j = j + 2; }
 */
.global main_act10

main_act10:
    mov r1, #0           @ r1 será nuestra variable 'j', inicializada en 0 (int j = 0;)
    mov r0, #0           @ r0 será nuestra variable 'i', inicializada en 0 (i = 0;)

loop_for:
    cmp r0, #50          @ Compara 'i' (r0) con el límite 50
    bgt fin_for          @ Si 'i' es mayor que 50 (i > 50), salir del ciclo (Branch if Greater Than)
    
    add r1, r1, #2       @ Cuerpo del ciclo: j = j + 2
    add r0, r0, #1       @ Incremento del ciclo: i++
    b loop_for           @ Salto incondicional al inicio del ciclo para repetir

fin_for:
    @ Al terminar el ciclo, r1 (j) contendrá el valor final.
    nop                  @ Fin de la actividad 10


/*
 * =================================================================
 * SECCIÓN DE DATOS (.data):
 * Aquí se reservan los espacios en memoria para guardar los resultados
 * =================================================================
 */
.data
    res_32:    .word 0      @ Actividad 7: Espacio para resultado de 32 bits
    carry_32:  .word 0      @ Actividad 7: Espacio para el acarreo
    
    res_64_L:  .word 0      @ Actividad 8: Espacio para el resultado bajo (L)
    res_64_H:  .word 0      @ Actividad 8: Espacio para el resultado alto (H)
    carry_64:  .word 0      @ Actividad 8: Espacio para el acarreo final