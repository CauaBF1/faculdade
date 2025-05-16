# Lista Exercicios Memoria avaliação 1
---

A figura ao lado representa uma seção de memória
instalada em uma determinada máquina.

Considere que o valor lido da memória a partir da
execução de uma instrução de leitura seja Y =
0x78563412.

Obs.: O símbolo XX na figura ao lado representa um valor
desconhecido, podendo assumir valores diferentes ao
longo dos endereços.

ENDEREÇO 		CONTEÚDO
0x1C 0F 00 XX		      12
0x1C 0F 00 XX		      34
0x1C 0F 00 XX		      56
0x1C 0F 00 XX 		      78
0x1C 0F 00 XX 		      33
..............         .........


A)
Considere que a arquitetura é tal que:
- o acesso à memória se faz de forma alinhada;
- o endereçamento é byte a byte; e
- a ordenação é do tipo "bigendian".
Sendo assim, refaça a figura, definindo valores de XX em
cada um dos endereços.

**Resposta:**

ENDEREÇO 		CONTEÚDO
0x1C 0F 00 04		      12
0x1C 0F 00 03		      34
0x1C 0F 00 02		      56
0x1C 0F 00 01 		      78
0x1C 0F 00 05 		      33
..............         .........

B)
Considere que a arquitetura é tal que:
- o acesso à memória se faz de forma alinhada;
- o endereçamento é byte a byte; e
- a ordenação é do tipo "littlendian".
Sendo assim, refaça a figura, definindo valores de XX em
cada um dos endereços.

**Resposta:**

ENDEREÇO 		CONTEÚDO
0x1C 0F 00 01		      12
0x1C 0F 00 02		      34
0x1C 0F 00 03		      56
0x1C 0F 00 04 		      78
0x1C 0F 00 05 		      33
..............         .........

C)
Caso haja outros números distintos de 32 bits que
possam ser lidos da memória segundo outra distribuição de
XX, apresente as possibilidades e justifique.

**Resposta:**

Sim é possivel ter outros numeros distintos de 32 bits que podem ser lidos da memoria desde que seja multiplos de 8 ja que é byte a byte, alem da distribuição de XX a fim de melhorar o desempenho e custo é melhor ser alinhado porem tambem pode ser de valores arbitrarios porem vai exigir mais acessos.


