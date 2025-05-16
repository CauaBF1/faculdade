# Lista de exercicios programação assembly

## Exercicio 1
---
Elaborar um programa em linguagem Assembly MIPS para determinar o valor da soma de n parcelas de
uma PA (Progressão Aritmética). Considere que o primeiro termo, a razão e o número de parcelas da PA estejam
presentes em registradores (de escolha do programador). O resultado deve ser armazenado em registrador. Indique uma
legenda para identificar o conteúdo dos registradores com dados do enunciado e o resultado determinado. 

Obs.: Não use instrução de multiplicação.
Posso usar loop
### Resposta:
 - Calcular o An = a1 + (n-1).r
 - Calcular a soma de n parcelas: Sn = ((a1+an).n) / 2

primeiro termo  = $s1
razão em  = $s2
numero de parcelas  = $s3
resposta  = $s5
```asm
// Cálculo de a_n = a_1 + (n - 1) * r
addi $t1, $s3, -1        // $t1 = n - 1 (calcular quantas vezes somar r)
addi $t2, $zero, 0       // $t2 = 0 (acumulador para (n - 1) * r)
addi $t3, $s1, 0         // $t3 = a_1 (copia a1 para t3)

Loop1: 
    add $t2, $t2, $s2     // Soma r ao acumulador: $t2 = $t2 + r
    addi $t1, $t1, -1      // Decrementa n - 1
    bne $t1, $zero, Loop1  // Continua o loop enquanto t1 != 0

add $t4, $t3, $t2        // $t4 = a_1 + (n - 1) * r -> a_n

// Cálculo de S_n = ((a_1 + a_n) * n) / 2
addi $t5, $s3, 0         // $t5 = n (contador para somar n vezes)
addi $t6, $zero, 0       // $t6 = 0 (acumulador para a soma de a_1 + a_n)
add $t6, $t6, $s1        // Soma a_1 a $t6: $t6 = a_1

Loop2:
    add $t6, $t6, $t4     // Soma a_n a $t6: $t6 = $t6 + a_n
    addi $t5, $t5, -1     // Decrementa contador n
    bne $t5, $zero, Loop2 // Continua o loop enquanto t5 != 0

sra $s5, $t6, 1           // $s5 = S_n = (a_1 + a_n) * n / 2 (divide por 2 usando shift à direita)
			  // Usa sra pq pode ser negativo 

```

## Exercicio 2
---
Elaborar um programa em linguagem Assembly MIPS para determinar o resultado de uma multiplicação
de dois números positivos de 16 bits. Considere que os argumentos da operação estejam presentes em registradores (de
escolha do programador). O resultado deve ser armazenado em registrador. Indique uma legenda para identificar o
conteúdo dos registradores com dados do enunciado e o resultado determinado

### Resposta
$s1 = Primeiro numero
$s2 = Segundo numero
$s3 = resultado

```asm
mult $s1, $s2
mflo $s3 // 16 bits menos significativos da mult
mfhi $s4 // 16 bits mais significativos da mult

sll $s4, $s4, 16 // desloca 16 bits para serem os mais sig de $s4
or $s3, $s3, $s4 // combinação de ambos os numeros LO(s3) e HI(s4) gerando numero de 32 bits.
```


## Exercicio 3
---
Encontre uma forma indireta, dentre as instruções básicas MIPS (arquivo fonte 2 no ambiente da disciplina
no AVA), para mover o conteúdo de um registrador para outro diferente.

### Resposta

```asm
add $t1, $t2, zero // se isso for considerado direto
//---------------//
// forma indereta usando memoria ao inves de registradores
sw $t2, 0($s0)
lw $t1, 0($s0) 
```


## Exercicio 4
---
Encontre uma forma para que cada um dos bits de um registrador seja negado (seja argumento de um
operador de negação lógica).

### Resposta:
função nor $rd, $rs, $rt
exp:
nor $s0, $s0, $s0

## Exercicio 5
---
Quais são as possíveis consequências se as seguintes instruções são aplicadas em sequência:
- sll $1, $1, #0x01
- srl $1, $1, #0x01
e no caso da sequência seguinte:
- sll $1, $1, #0x01
- sra $1, $1, #0x01

### Resposta:
- sll $1, $1, #0x01
- srl $1, $1, #0x01

como srl é para numeros sem sinal, o numero vai ser restaurado sendo positivo e vai mudar caso negativo

- sll $1, $1, #0x01
- sra $1, $1, #0x01
como sra é para numeros com sinal, o numero vai ser restaurado sendo positivo ou negativo

## Exercicio 6
---
Elabore um programa em linguagem Assembly MIPS para determinar o valor lógico do n-th bit de uma
palavra. Elabore alternativas ao programa proposto.

### Resposta:
palavra = 0x12345678
```asm
// carragar a palavra
lui $t0, 0x1234
ori $t0, $t0, 0x5678

// carregar a posição do bit
ori $t1, $t1, 0x5 // exp posição 5

// colocar mascara numero 1 na posição desejada
lui $t2, 0x1
sll $t2, $t2, $t1 // desloca $t2 para posição 5

// pegar n-th bit
and $t3, $t0, $t2
 
bne $t3, $zero, Ligado
lui $v0, 0x0

Ligado:
  lui $v0, 0x1
```
