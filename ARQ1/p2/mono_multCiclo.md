# Exercicio 1

TI: 1
Q: 5
N: 4
SOMAN: 0

    7 (la and lw)
    1 beq
    1 sw
    1 addiu

loop:
1 beq
1 lw
1 sw
2 add(i and u)
1 multu
1 mflo
1 jump

loop vai ser executado 4 vezes, portanto 8x4 = 32 ciclos em loop
10 instruções antes do loop portanto o total de ciclos é 42.

cada ciclo é de 200mhz portanto cada ciclo tem duração de
1 / 100x10⁶ = 5ns
tempo de execução = numero de ciclos x tempo de cada = 42 x 5ns = 210ns

# Exercicio 2

a) com esse erro no mux2 nao seria possil o uso do immd poranto qualquer instrução que precisasse dele nao iria funcionar,
como exemplo beq, addi, lw, sw ...
b)
com essa falha no mux1 qualquer instrução que fosse usar o regD nao conseguiria dessa forma as instruções add, sub, or, and
ou qualquer outra instrução que precise do regD

# Exercicio 3

Monociclo utiliza o tempo mais lento para todas as instruções como o mais lento é lw de 800ns basta multiplicar pela quantidade
de instruções que são:
Programa A: 1145 _ 800ns = 916000ns = 916 microsegundos
Programa B: 7256 _ 800ns = 5804800ns = 5,804800 milisegundos

No multiciclo cada ciclo demora 200ns dessa forma é preciso organizar quantos ciclos cada instrução vai usar e quantas instruções vao ser
PROGRAMA A:
lw = 5 _ 200 = 1000ns _ 200instruções = 200000
sw = 5 _ 200 = 1000ns _ 200instruções = 200000
add = 4 _200 = 800ns _ 550instruçoes = 440000
addi = 4 _200 = 800ns _ 50instruçoes = 040000
sub = 4*200 = 800ns * 30 = 024000
beq = 3*200 = 600ns * 65 = 039000
slt = 4*200 = 800ns * 30 = 024000
j = 3*200 = 600ns *20 = 012000

---

979,000

PROGRAMA B:
lw = 5 _ 200 = 1000ns _ 125instruções = 125000
sw = 5 _ 200 = 1000ns _ 70instruções = 070000
add = 4 *200 = 800ns *2048instruçoes =1638400
addi = 4 *200 = 800ns *4242instruçoes =3393600
sub = 4*200 = 800ns * 27 = 021600
beq = 3*200 = 600ns * 113 = 067800
slt = 4*200 = 800ns * 117 = 093600
j = 3*200 = 600ns *514 = 324000

---

5,733,000

# Exercicio 4:

Precisa de outro banco de registradores para ler conteudo de $rd e sair para MUX criado
Sinal de controle adicional: Adicionar um sinal de controle chamado CIFMOVE na unidade de controle para identificar a nova instrução.
Banco de registradores: Não é necessário um banco de registradores auxiliar. O banco de registradores existente já permite leitura e escrita em $rd, $rs e $rt.
MUX na entrada A da ULA: Adicionar um MUX antes da entrada A da ULA. Ele terá duas entradas:

    Entrada 0: valor de $rs (para operações normais).
    Entrada 1: valor de $rd (quando a instrução for CIFMOVE).
    O controle desse MUX será ativado pelo sinal CIFMOVE.

Comparador para verificar $rs > 0: Inserir um comparador que verifica se o valor de $rs é maior que zero ($rs > 0). A saída será binária:

    Saída = 1: indica que $rs > 0.
    Saída = 0: indica que $rs ≤ 0.

MUX antes do controle ALUOp: Adicionar um MUX antes do sinal ALUOp. Ele terá duas entradas:

    Entrada 0: ALUOp normal gerado pela unidade de controle (para outras instruções).
    Entrada 1: ALUOp configurado diretamente para soma (00) ou subtração (01), dependendo do resultado do comparador:
        Se comparador = 1: ALUOp = 00 (soma).
        Se comparador = 0: ALUOp = 01 (subtração).
    O controle desse MUX será ativado pelo sinal CIFMOVE.

Operação da ULA:

    Se $rs > 0, a ULA realiza soma ($rd + $rt) porque ALUOp será configurado como 00.
    Caso contrário, a ULA realiza subtração ($rd - $rt) porque ALUOp será configurado como 01.

Escrita no registrador destino ($rd): Reutilizar o caminho existente para escrever o resultado da operação no registrador destino ($rd).
