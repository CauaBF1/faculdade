# Processador Simplificado

- PC(armazena endereço da próxima instrução)
- Memoria de instruções(lidas as instruções recebidas do pc, opcode da instrução que estao armazanada nesse modulo)
- Nessa mem de instruções extrai opcode, os operandos(caso existam, sao endereços de um banco de registradores)
- Banco de registradores(recebe endereço do operando e extrai seu conteudo, ou coloca seu dado escrita do registrador destino)
- Ula recebe os dados do banco de registradores, calculando as operações entre dois operandos ou endereço em instruções branch etc
- ULA devolve para o banco de registradores resultado
- Memoria de dados recebe o endereço da ula e o dado do banco de registradores

Datapath é o conjunto banco de registradores ULA e memoria de dados
para tudo funcionar é necessario a unidade de controle para realizar tarefas diferentes, exp ULA recebe conteudo dos registradores ou offset(immed) para instruções branch

# Exercicios Datapah Monociclo

---

1. Dadas as seguintes instruções em bytes, informe quais são os seus sinais de controle
   a) 01111022
   c) 08000244
   d) 8D2A0250

---

Resposta:
a)
0000 0001 0001 0001 0001 0000 0010 0010
MIPS:
000000 01000 10001 00010 00000 100010 -> sub rs($8) rt($17) rd($2)
regDst = 1;
ALUsrc = 0;
memToreg 0;
regWrite = 1;
memRead = 0;
memWrite = 0;
Branch = 0;
aluOP = 10;
Jump = 0;

b)
0000 1000 0000 0000 0000 0010 0100 0100
MIPS:
000010 00000 00000 00000 01001 000100 -> jump

regDst = X;
ALUsrc = X;
memToreg 0;
regWrite = 0;
memRead = 0;
memWrite = 0;
Branch = 0;
aluOP = XX;
Jump = 1;

c)  
1000 1101 0010 1010 0000 0010 0101 0000
MIPS:
100011 01001 01010 00000 01001 010000 -> lw
regDst = 0;
ALUsrc = 1;
memToreg 1;
regWrite = 1;
memRead = 1;
memWrite = 0;
Branch = 0;
aluOP = 00;
Jump = 0;

---

2. Caso a questão 1a fosse executada com o sinal memWrite igual a 1, address = rs - rt
   0x1510 - 0xCA08 = 0x4b08, os 16bits da istrtrução são o immed 00010 00000 100010
   0001 0000 0010 0010 = 1022, o valor 0x4b08 é escrito no endereço 1022.

3. o registrador a ser alterado seria o $0, mas como não é possivel alteralo nao tem valor corretor para quesão

4. pode ser tanto juump quanto sw portanto não

5. se são executadas sequencialmente basta somar o tempo gasto para cada instrução,
   a instrução lw gasta:
   lw add sw
   5ns + 5ns 5ns+
   2ns + 2ns 2ns+
   3ns + 3ns 3ns+
   8ns + 0ns 8ns+
   2ns + 2ns 0ns+

---

20ns + 12ns + 18ns == 50ns

Resposta correta é 60, todas gastam o mesmo tempo em uma maquina monociclo.

6.  tempo de clock seria de 20ns que é o pior tempo possivel para cada instrução, em
    monociclo mesmo tendo instruções mais rapidas todas seguem o clock daa mais lenta

7.  como instruções do tipo R usam 12ns o tempo de ociosidade é de 8ns.

8.  ainda seria 20ns pois todas tempo o tempo de pior caso.
