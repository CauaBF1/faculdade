# Exercicio 1

regDst =
Jump =
MemRead =
ALUOp =
MemtoReg =
Desvio =
MemWrite =
ALUSrc =
RegWrite =

### A (intrução JR)

JR = PC <- Rs
adicionar mux entre muxJump com o mesmo ligado em 0 e a saida REG1 ligada em 1, criando um novo sinal de controle chamado
JR caso esteja ligado PC <- REG1(RS), caso desligado PC <- muxJump

JR = 1
regDst = X
Jump = X
MemRead = 0
ALUOp = XX
MemtoReg = X
Desvio = 0
MemWrite = 0
ALUSrc = X
RegWrite = 0

### B (instrução JALR)

JALR
{
tmp ← R[$rs]
R[$rd] ← PC + 8
PC ← tmp
}
Sinal de controle chamado JALR
Adicionar somador de 4 + (resultado PC+4) ao lado de MUXmemtoreg
MUX pos muxmemtoreg com entras sendo (muxmemtoreg e resultado novoSomador), caso JALR = 0 passa muxmemtoreg caso 1 passa somador
adicionar mux entre muxJump com o mesmo ligado em 0 e a saida REG1 ligada em 1, criando um novo sinal de controle chamado
JR caso esteja ligado PC <- REG1(RS), caso desligado PC <- muxJump

JALR = 1
JR = 1
regDst = 1
Jump = X
MemRead = 0
ALUOp = XX
MemtoReg = X
Desvio = 0
MemWrite = 0
ALUSrc = X
RegWrite = 1

### C (instrução JAL)

Todos os mux usam sinal de controle JAL
Usar instrução jump da mesma forma de colocar mux entre entrada ESCRITA com IR[31] e saida muxRegDst, dessa forma acontecera escrita em R[31]
Somador que pega valor do somador de PC+4 com +4
Adicionar mux antes de DADO escrita, com saida do somador(1) e com muxmemtoreg(0)
Dessa forma o Jump acontece e a escrita de PC+8 em R[31] tbm

regDst = X
Jump = 1
MemRead = 0
ALUOp = XX
MemtoReg = 0
Desvio = 0
MemWrite = 0
ALUSrc = X
RegWrite = 1
JAL = 1

### D (instrução LUI)

Bloco com shiffter de 16 dessa forma transformando os [15,0] do immediate + 0x16 com um somador bloco pega antes da extensao.
colocar mux com sinal LUI antes de dado de escrita caso 0 passe memtoregMUX e caso 1 passa o resultado do bloco, dessa forma é escrito o imm+0 dentro de rt

LUI = 1
regDst = 0
Jump = 0
MemRead = XX
ALUOp = XX
MemtoReg = X
Desvio = 0
MemWrite = X
ALUSrc = X
RegWrite = 1
