# Lista de exercicios programação avaliação 1

## Exercicio 
---
Considere que a arquitetura MIPS é BI-ENDIAN, no sentido de que a máquina pode ser ajustada em
qualquer um dos modos de operação. Considere uma região de memória livre ("vazia"), denominada MEM1, que se
inicia no endereço 0x00FF158C e se finaliza em 0x00FF158E, incluindo os endereços de início e fim apresentados.
Considere que a palavra 0x4E55F200 esteja armazenada na memória tal como apresentado na tabela em seguida.
Considere ainda que os endereços 0x00FF158C e 0x00FF158E estejam disponíveis em $s0 e $s1, respectivamente.

Nestas condições, desenvolva uma sequência de código em Assembly MIPS de forma que na sua execução armazene na
região MEM1 os 3 Bytes de dados disponíveis nos bits menos significativos do registrador $t1, mantendo a ordem
como aparecem neste registrador $t1.

ENDEREÇO MEMÓRIA 	 CONTEÚDO
0x00FF1610 		       4E
0x00FF1511 		       55
0x00FF1512 		       F2
0x00FF1513 		       00


### Resposta:

Armazenar dentro de MEM1 os 3 LSB no registrador $t1 mantendo a ordem
MEM1 = 0x00FF158C 0x00FF158D 0x00FF158E
	($s0)			($s1)

 -  Pega o byte menos significativo, fazendo and desse numero com 0000 0000 ... 1111 1111, dessa forma and com 0 é 0 e and de com 1 é X portanto fica em $t2 somente o byte(8b) menos significativo

 - Desloca para direita 8 bits (1 byte) para poder pegar 2 LSB byte

 - Pega LSB (coloco dentro dele mesmo o and com 0xFF, nao fiz isso com $t2 para nao modificar o $t1)

 - Desloco agora 16 bits(2bytes) para pegar 3 byte LSB

 - Pego LSB

 - Coloca dentro de $s0 o valor que estava em $t4
 - Coloca dentro de $s0+1 o valor que estava em $t3
 - Coloca dentro de $s1 o valor que estava em $t2


```asm
andi $t2 $t1 0xFF // 00
srl $t3 $t1 8 
andi $t3 $t3 0xFF // F2
srl $t4 $t1 16
andi $t4 $t4 0xFF // 55

sb $t4, 0($s0) // 0x00FF158C
sb $t3, 1($s0) // 0x00FF158D
sb $t2, 0($s1) // 0x00FF158E
```

```asm
sll $t1, $t1, 8
lw $t2, 0($so)
andi $t2, $t2, 0xFF
or $t1, $t1, $t2
sw $t1, 0($so)
```

#### Codigo Kevin:

```asm
ori $s2, $zero, 0x00FF
and $s0, $s0, $s2
sll $t1, $t1, 8
or $s0, $t1, $s0
```
