/* =====================================================================
 * ACTIVIDAD 4: Promedio de dos números de 8 bits
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:
    @ 1. Cargar los dos datos
    mov r1, #0x19      @ DATO1 = 25
    mov r2, #53        @ DATO2 = 53
    
    @ 2. Sumar DATO1 y DATO2
    add r3, r2, r1     @ r3 = 53 + 25 = 78
    
    @ 3. Dividir entre 2 (Corrimiento a la derecha)
    lsr r4, r3, #1     @ r4 = 78 / 2 = 39 (0x27)
    
    @ 4. Salida
    mov r0, r4         
    mov r7, #1         @ exit
    svc 0              


/* =====================================================================
 * ACTIVIDAD 5: Comentar código de ejemplo (Contador ping-pong)
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:   
    mov r0, #0       @ Contador
    mov r1, #9       @ Límite superior
    mov r2, #0       @ Límite inferior

loop1:  
    add r0, r0, #1   @ Incrementa
    cmp r1, r0       
    bne loop1        @ Sube hasta 9

loop2:  
    add r0, r0, #-1  @ Decrementa
    cmp r2, r0       
    beq loop1        @ Baja hasta 0 y repite
    b loop2          


/* =====================================================================
 * ACTIVIDAD 6: Corrimiento de bit a la izquierda
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:
    mov r3, #1          @ Inicia en bit menos significativo
    
loop_shift:
    lsl r3, r3, #1      @ Desplaza a la izquierda
    cmp r3, #0          @ ¿Se salió del registro?
    beq _start          @ Si es 0, reinicia
    b loop_shift        @ Si no, sigue desplazando


/* =====================================================================
 * ACTIVIDAD 7: Suma de 32 bits con acarreo
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:
    ldr r1, =0xFFFFFFFF  @ DATO1_32_BITS (Fuerza acarreo)
    ldr r2, =0x00000005  @ DATO2_32_BITS
    
    adds r3, r1, r2      @ Suma y actualiza banderas
    
    ldr r4, =res_32      
    str r3, [r4]         @ Guarda resultado en memoria
    
    mov r5, #0           
    adc r5, r5, #0       @ Atrapa el acarreo (Carry)
    ldr r6, =carry_32    
    str r5, [r6]         @ Guarda acarreo en memoria
    
    mov r7, #1
    svc 0                @ Fin

.data
    res_32:    .word 0   
    carry_32:  .word 0   


/* =====================================================================
 * ACTIVIDAD 8: Suma de 64 bits con acarreo
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:
    mov r0, #0x00000001  @ DATO1_H (Alta)
    ldr r1, =0xFFFFFFFF  @ DATO1_L (Baja)
    
    mov r2, #0x00000002  @ DATO2_H (Alta)
    ldr r3, =0x00000005  @ DATO2_L (Baja)
    
    adds r4, r1, r3      @ Suma partes bajas (actualiza Carry)
    adcs r5, r0, r2      @ Suma partes altas + Carry previo
    
    ldr r6, =res_64_L
    str r4, [r6]         @ Guarda resultado bajo
    ldr r7, =res_64_H
    str r5, [r7]         @ Guarda resultado alto
    
    mov r8, #0
    adc r8, r8, #0       @ Atrapa el acarreo final
    ldr r9, =carry_64
    str r8, [r9]         @ Guarda acarreo final
    
    mov r7, #1
    svc 0                @ Fin

.data
    res_64_L:  .word 0   
    res_64_H:  .word 0   
    carry_64:  .word 0   


/* =====================================================================
 * ACTIVIDAD 9: Factorial de 8 bits
 * (Copia desde aquí hasta la siguiente actividad para simular)
 * ===================================================================== */
.text
.global _start

_start:
    mov r0, #5           @ n = 5 (Calcularemos 5! = 120)
    mov r1, r0           @ Acumulador
    mov r2, r0           @ Decrementador

    cmp r0, #1
    ble caso_base_fact

loop_factorial:
    sub r2, r2, #1       @ n = n - 1
    cmp r2, #1           
    beq fin_factorial    @ Si es 1, termina
    
    mul r3, r1, r2       @ Acumulador * (n-1)
    mov r1, r3           
    b loop_factorial     

caso_base_fact:
    mov r1, #1           

fin_factorial:
    mov r7, #1
    svc 0                @ Fin


/* =====================================================================
 * ACTIVIDAD 10: Ciclo For (j = 0; i <= 50; i++) { j = j + 2; }
 * (Copia desde aquí hasta el final del archivo para simular)
 * ===================================================================== */
.text
.global _start

_start:
    mov r1, #0           @ j = 0
    mov r0, #0           @ i = 0

loop_for:
    cmp r0, #50          @ i <= 50?
    bgt fin_for          @ Si i > 50, sale del ciclo
    
    add r1, r1, #2       @ j = j + 2
    add r0, r0, #1       @ i++
    b loop_for           

fin_for:
    mov r7, #1
    svc 0                @ Fin