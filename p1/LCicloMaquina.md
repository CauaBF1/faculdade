# Lista de exercicio clico maquina

Considere que o ciclo de máquina consista do ciclo de busca ("fetch") e ciclo de execução.
Considere que a máquina esteja executando a fração de código correspondente à seção de memória que se inicia no
endereço 0x05001010 com fim em 0x0500102C.

ENDEREÇO 	RÓTULO 		ASSEMBLY 				COMENTÁRIO
0x0500100C 			sll $s0,$t1,2 				# $s0 = $t1 * 4
0x05001010 Loop: 		add $t1,$s3,$s3 			# $t1 = 2 * i
0x05001014 			add $t1,$t1,$t1 			# $t1 = 4 * i
0x05001018 			add $t1,$t1,$s6 			# $t1 = endereço de X
0x0500101C 			lw $t0,0($t1) 				# $t0 recebe save[i]
0x05001020 			bne $t0,$s5,Exit 			# vá para Exit se X != k
0x05001024 			add $s3,$s3,$s4 			# i = i + j
0x05001028 			j Loop 					# salte para Loop
0x0500102C Exit: 		srl $s0,$t1,2 				# $s0 = $t1 / 4
0x05001030 			add $t1,$s3,$s3 			# $t1 = 2 * i

(a) Se no início do ciclo de execução de um ciclo de máquina, o valor do IR é 0x09400404 então, ao final do ciclo de
execução correspondente, qual o valor do PC?
(b) Em algum ciclo de máquina o valor do PC no início do ciclo é menor do que ao final do mesmo ciclo. Neste caso
qual o valor do PC ao final do ciclo correspondente? E ao final do ciclo seguinte? (Neste caso qual o valor do IR ao
final do ciclo correspondente?
(c) Em algum ciclo de máquina o valor do PC é acrescentado de um valor maior do que aquele acrescentado no ciclo de
máquina anterior. Para esse ciclo de máquina qual o valor do IR e do PC ao seu final?

---
## Resposta:

a) 
IR = 0x09400404

0000 1001 0100 0000 0000 0100 0000 0100 
MIPS:

000010 01010 00000 00000 10000 000100
(op)   (rs)  (rd)  (rt)  (shamt) (funct)

op = 2, portanto instrução jump

address = 0101 0000 0000 0001 0000 0001 00

PC <- {(PC + 4) [31:28], address, 00}
PC = 0x05001028 + 4 = 0x0500102C[31:28] = 0000 // 4 primeiros bits

PC = 0000, address,00
PC = 0000 0101 0000 0000 0001 0000 0001 0000
PC = 0x05001010


b)
Sim, durante um ciclo de maquina o valor do PC no inicio é menor doque no final do mesmo ciclo. Exp: 
PC = 0x05001014, PC ao final do ciclo correspondente = 0x05001018, IR do PC correspondente:

op = 000000
rs = 01001
rt = 10110
rd = 01001
shamt = 00000
funct = 100000

0000 0001 0011 0110 0100 1000 0010 0000
IR = 0x01364820


c)
Sim no { bne$t0, $s5, Exit }
do PC = 0x05001020 para 0x0500102C, PC ao final desse cliclo = 0x05001030

IR = srl $s0, $t1, 2

op = 000000
rs = 00000
rt = 01001
rd = 10000
shamt = 00010
funct = 000010

0000 0000 0000 1001 1000 0000 1000 0010
IR = 0x00098082










