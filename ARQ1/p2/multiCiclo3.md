# Exercicio 1

A) Alem de funcionar como LW ao final deve incrementar RS + 4, para isso adicionar
caminho de REGB e colocar um MUX entre o MUXSrcA se for 1 passa valor de REGB se for 0
passa valor de MUXSrcA (controle chama LWVECTOR), esse mux só vai ser alterador no 3
estado para nao atrapalhar nenhuma outra instrução ja que LW deixa de usar a ULA e nao
no estado 4 pois la ja esta utilizando escrita em regs
B)
Estado 0:
PCsrc = 00,
PC =1,
load = 0,
MemRead = 1,
RIWrite = 1,
SrcA = 0,
SrcB = 01,
ALUOp = 00,

Estado 1:
SrcA = 0,
SrcB = 11,
ALUOP = 00, # soma

Estado 2:
SrcA = 1,
SrcB = 10,
ALUOP = 00,

Estado 3:
load = 1,
MemRead = 1,
LWVECTOR = 1,
SrcA = 1, # rs + 4
SrcB = 01,
ALUOp = 00,
MemToReg = 0,
RegWrite =1,

Estado 4:
MemToReg = 1,
RegDst = 0,
RegWrite 1,

---

# Exercicio 2

A) Funciona da mesma forma que sw so que precisa adicionar 4 no rs, para isso adicionar
caminho de REGB e colocar um MUX entre o MUXSrcA se for 1 passa valor de REGB se for 0
passa valor de MUXSrcA (controle chama SWVECTOR), só vai ser executado no Estado 5
o qual nao depende mais da ULA

Estado 0:
PCsrc = 00,
PC =1,
load = 0,
MemRead = 1,
RIWrite = 1,
SrcA = 0,
SrcB = 01,
ALUOp = 00,

Estado 1:
SrcA = 0,
SrcB = 11,
ALUOP = 00, # soma

Estado 2:
SrcA = 1,
SrcB = 10,
ALUOP = 00,

Estado 5:
SWVECTOR: 1,
AluOp = 00,
srcB = 01,
srcA = 1
load: 1,
MemWrite 1,
regWrite = 1, # Escrever rs + 4 em rs
