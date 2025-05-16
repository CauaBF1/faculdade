# Lista de programação 2 avaliação 1
---

## Exercicico
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

Em seguida são apresentados alguns códigos que falham, quando executados, em alcançar o objetivo, a saber,
armazenar na região MEM1 os 3 Bytes de dados disponíveis nos bits menos significativos do registrador $t1, mantendo
a ordem como aparecem neste registrador $t1.

Para cada opção descrita em seguida:

(a) identificar quais linhas de código impedem que o objetivo definido seja alcançado; e

(b) apresentar a solução para o problema, ou seja, substituir cada uma das linhas de código identificadas no
item (a) por uma outra única linha, de forma que o código, ao final, alcance o objetivo proposto quando executado


OPÇÃO B:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 0x0F
- and $s3, $s2, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)

OPÇÃO C:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 0x0F
- and $s3, $s2, $s3
- and $s3, $s3, $t1
- sw $s3, 0($0)

OPÇÃO D:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 255
- and $t1, $t1, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)

OPÇÃO E:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 1023
- add $s3, $s2, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)



### Resposta:

OPÇÃO B:
- lw $s2, 0($s0)
- sll $t1, $t1, 8x
- adi $s3, $zero, 0x0F
- and $s3, $s2, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)

a) $st1 nao existe é $t1, adi nao é um minemonico deveria ser addi, e M[0] nao é um endereço valido.

b)
lw $s2, 0($s0)
sll $t1, $t1, 8
addi $s3, $zero, 0x0F
and $s3, $s2, $s3
add $s3, $s3, $t1
sw $s3, 0($s0)

---
OPÇÃO C:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 0x0F
- and $s3, $s2, $s3
- and $s3, $s3, $t1
- sw $s3, 0($0)

a) $st1 nao existe, adi nao é valido, $0 nao é um endenreço de memoria valido, and $s3 $s3 $t1 subscreve os valores de $s3

b)
lw $s2, 0($s0)
sll $t1, $t1, 8
addi $s3, $zero, 0x0F
and $s3, $s2, $s3
or $s3, $s3, $t1
sw $s3, 0($s0)

---

OPÇÃO D:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 255
- and $t1, $t1, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)

a) $st1 nao existe, adi nao é valido, $0 nao é um endereço de memoria valido, add nao faz a combinação de bits de forma apropriada, deveria ser or com $s2 ja que $s3 nao foi mascarado

b)
lw $s2, 0($s0)
sll $t1, $t1, 8
addi $s3, $zero, 255
and $t1, $t1, $s3
or $s3, $s2, $t1
sw $s3, 0($s0)

---

OPÇÃO E:
- lw $s2, 0($s0)
- sll $st1, $st1, 8
- adi $s3, $zero, 1023
- add $s3, $s2, $s3
- add $s3, $s3, $t1
- sw $s3, 0($0)


a) $st1 nao existe, adi nao é valido, $0 nao é um endereço de memoria valido, add nao faz a combinação de bits de forma apropriada, deveria ser and, 2 and deveria ser or para fazer combinação correta de bits

b)
lw $s2, 0($s0)
sll $t1, $t1, 8
addi $s3, $zero, 1023
and $s3, $s2, $s3
or $s3, $s3, $t1
sw $s3, 0($s0)
---


### Para pegar os 3 bits menos signficativos precisa desse codigo.
**Nao tenho ideia de como faz para arrumar os codigos das opções, consegui realizar em 6 linhas assim é possivel fazer o codigo sem adicionar nenhuma linha porem todos os codigos iam mudar completamente**

add $t2, $t1, $zero 
sb $t2, 0($s0) 
srl $t3, $t2, 8 
sb $t3, 1($s0) 
srl $t4, $t2, 16 
sb $t4, 0($s1) 

