# Question 2

a) The following program is running on a 5-stage (F, D, E, M, W) pipelined MIPS processor:

add $s0, $0, $0 # i = 0
add $s1, $0, $0 # sum = 0
addi $t0, $0, 10 # $t0 = 10
loop:
slt $t1, $s0, $t0 # if (i < 10), $t1 = 1, else $t1 = 0
beq $t1, $0, done # if $t1 == 0 (i > = 10), branch to done
add $s1, $s1, $s0 # sum = sum + i
addi $s0, $s0, 1 # increment i
j loop
done:

i. Calculate the CPI of this code segment on a single-cycle and multi-cycles MIPS processor.
ii. Calculate the CPI of this code segment on a pipelined MIPS processor without a hazard
unit. Assume nop instructions are inserted to resolve RAW hazards.
iii. Calculate the CPI of this code segment on a pipelined MIPS processor having a full (data
and control) hazard unit with forwarding and stalling mechanisms. Show timing of one
loop cycle as follows:

---

## Resposta:

i. Na arquitetura monociclo o CPI é sempre 1, no multiciclo cada instrução tipo R precisa de 4 estados portanto 3 instruções 4 estados = 12 ciclos de clock de instruções fora do laço

o laço é executado 10 vezes
slt = 4 estados
beq = 3 estados
add = 4 estados
addi = 4 estados
j = 3 estados

dessa forma ((1*4 + 1 * 3 + 1 _ 4 + 1 _ 4 + 1 _ 3) _ 10 )+ 12 = 180 ciclos em 50 instruções

depois de 10 interações ainda precisa realizar slt e beq novamente = 7 ciclos 2 instruções

CPI = 12 + 180 + 7 / 3 + 50 + 2 = 199/55

ii.
