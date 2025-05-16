# Lista de exercicios Miscelanea

## Exercicio 3
---
Uma palavra em um computador little endian tem
o valor em hexadecimal de 0003. Se ela for transmitida para um
computador big endian byte por byte e ali armazenada com o byte 0 no
byte 0, e assim por diante, qual é o seu valor numérico na máquina big
endian?

### Resposta:
little endian = 0003
big endian = 3000

## Exercicio 4
---
Uma certa máquina tem instruções de 16 bits e
endereços de 6 bits. Algumas instruções têm um endereço e outras têm
dois. Se houver n instruções de dois endereços, qual é o número máximo
de instruções de um endereço?

### Resposta:
endereços de 6 bits geral 2⁶ endereços possiveis, portanto 64 endereços distintos, sendo N o numero de instruções de 2 endereços, o numero de instruções de 1 endereço é 64-N.


## Exercicio 5
---
Escrever a instrução, ou menor conjunto de instruções em Assembly do 
MIPS, que realiza a operação em código C, seguintes:

a) a = a – 1
b) a = 0
c) v[10] = 0
d) a = v[10]
e) if (a < b) goto L1;
f) if (a > 0) goto L1;


### Resposta:
a) addi $t1, $t1, -1
b) add $t1, $zero, $zero
c) sw $zero, 40($t0) // 40 pois cada elemento do vetor ocupa 4 bytes(int = 4bytes em MIPS)
d) lw $s0, 40($t0)
e) slt $t2, $t0, $t1 // a < b ,  t0 < t1
   bne $t2, $zero, L1
f) bgtz $t0, L1  


## Exercicio 6
---
Transcreva o código C abaixo para assembly MIPS. Assuma que as
variáveis f, g foram designadas para os registradores $s0 e $s1,
respectivamente. Assuma, também , que o endereço base dos vetores A e
B estão nos registradores $s6 e $s7, respectivamente.
f = g - A[B[4]];

### Resposta:
// $s0 = f
// $s1 = g
// $s6 = A
// $s7 = B

```asm
lw $t0, 16($s7) // carrega valor de B[4] para t0
// Endereço do elemento= Endereço base do vetor+(Indice do elemento × Tamanho do tipo de dado)
// Endereço de B[4] = Endereço base de B + (4×4) = Endereço base de B+16
// para isso multiplicar x 4 o indice de B[4~]
sll $t0, $t0, 2 // *4
add $t0, $t0, $s6 // add endereço base de A calculando A[B[4]]
lw $t1, 0($t0) // coloca valor de A[B[4]]

sub $s0, $s1, $t1 // f = g - A[B[4]]
```


## Exercicio 7
---
Dado o código em assembly MIPS abaixo, escreva o seu correspondente em C.
Utilize “f” como nome da variável e “A” como o nome do vetor.

lw $s0, 4($s6)

```c
f = A[1]
```

