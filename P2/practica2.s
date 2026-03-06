@ actividad 1

.data
i: .skip 64          @ 16 enteros de 32 bits (16*4 = 64 bytes)

.text
.global main

main:
    LDR R1, =i       @ R1 = dirección base del arreglo
    MOV R2, #0       @ R2 = contador

loop:
    CMP R2, #16
    BEQ fin

    STR R2, [R1, R2, LSL #2]   @ i[R2] = R2

    ADD R2, R2, #1
    B loop

fin:
    B fin

@ actividad 2

.data
i: .skip 64

.text
.global main

main:
    LDR R1, =i
    MOV R2, #0
    MOV R3, #16

loop:
    CMP R2, R3
    BEQ fin

    STR R2, [R1], #4   @ Guarda y luego incrementa R1 en 4
    ADD R2, R2, #1
    B loop

fin:
    B fin

@ actividad 3
.data
A: .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
B: .skip 64

.text
.global main

main:
    LDR R0, =A
    LDR R1, =B

    MOV R2, #15       @ índice final
    MOV R3, #0

loop:
    CMP R3, #16
    BEQ fin

    LDR R4, [R0, R2, LSL #2]
    STR R4, [R1, R3, LSL #2]

    SUB R2, R2, #1
    ADD R3, R3, #1
    B loop

fin:
    B fin

@ actividad 4

.data
A: .skip 80
SUMA: .word 0

.text
.global main

main:
    LDR R0, =A
    MOV R1, #3      @ i inicial
    MOV R2, #0
    MOV R4, #0      @ suma

loop:
    CMP R2, #20
    BEQ guardar

    STR R1, [R0, R2, LSL #2]
    ADD R4, R4, R1

    MOV R1, R1, LSL #1   @ multiplica por 2
    ADD R2, R2, #1
    B loop

guardar:
    LDR R3, =SUMA
    STR R4, [R3]

fin:
    B fin

@ actividad 5

.data
A: .byte 1,2,3,4
B: .byte 5,6,7,8
C: .skip 4

.text
.global main

main:
    LDR R0, =A
    LDR R1, =B
    LDR R2, =C

    LDRB R3, [R0]        @ A
    LDRB R4, [R0, #1]    @ B
    LDRB R5, [R0, #2]    @ C
    LDRB R6, [R0, #3]    @ D

    LDRB R7, [R1]        @ E
    LDRB R8, [R1, #1]    @ F
    LDRB R9, [R1, #2]    @ G
    LDRB R10,[R1, #3]    @ H

    MUL R11, R3, R7
    MLA R11, R4, R9, R11
    STRB R11, [R2]

    MUL R11, R3, R8
    MLA R11, R4, R10, R11
    STRB R11, [R2,#1]

    MUL R11, R5, R7
    MLA R11, R6, R9, R11
    STRB R11, [R2,#2]

    MUL R11, R5, R8
    MLA R11, R6, R10, R11
    STRB R11, [R2,#3]

fin:
    B fin

@ actividad 6

.data
A: .word 4,7,1,9,3,15,2,8,6,11,5,10,14,13,12,16,18,17,19,20
MAYOR: .word 0
DIR: .word 0

.text
.global main

main:
    LDR R0, =A
    LDR R1, [R0]      @ mayor inicial
    MOV R2, #0
    MOV R3, #20

loop:
    CMP R2, R3
    BEQ guardar

    LDR R4, [R0, R2, LSL #2]
    CMP R4, R1
    BLE siguiente

    MOV R1, R4
    ADD R5, R0, R2, LSL #2

siguiente:
    ADD R2, R2, #1
    B loop

guardar:
    LDR R6, =MAYOR
    STR R1, [R6]

    LDR R6, =DIR
    STR R5, [R6]

fin:
    B fin

@ actividad 7
.data
A: .word 9,3,5,1,8,7,2,6,4,10,11,15,14,13,12,16,20,18,19,17,21,22,25,24,23,26,27,28,29,30,32,31
B: .skip 128

.text
.global main

main:
    LDR R0, =A
    LDR R1, =B
    MOV R2, #0

copy:
    CMP R2, #32
    BEQ sort

    LDR R3, [R0, R2, LSL #2]
    STR R3, [R1, R2, LSL #2]
    ADD R2, R2, #1
    B copy

sort:
    MOV R4, #0

outer:
    CMP R4, #31
    BEQ fin

    MOV R5, #0

inner:
    CMP R5, #31
    BEQ next

    LDR R6, [R1, R5, LSL #2]
    ADD R7, R5, #1
    LDR R8, [R1, R7, LSL #2]

    CMP R6, R8
    BLE no_swap

    STR R8, [R1, R5, LSL #2]
    STR R6, [R1, R7, LSL #2]

no_swap:
    ADD R5, R5, #1
    B inner

next:
    ADD R4, R4, #1
    B outer

fin:
    B fin
