# Lista de exercicios 3

## Questão 1

Considere que a arquitetura MIPS1 possui duas organizações, uma
Monociclo e outra utilizando a técnica de Pipelining. Na organização monociclo cada
instrução requer 160ɳs e na organização utilizando pipelining o clock possui período de 40
ɳs. Para fins deste exercício considere a tabela apresentada no exercício 3. Qual o tempo
necessário para executar um programa de 10², 10³, 10⁴, 10⁵, 10⁶, 10⁹ e 10¹² instruções em
ambas as organizações. Considere para o caso da organização com pipelining que todas as
instruções requerem exatamente 4 ciclos de clock.

---

### Resposta:

Como cada instrução requer 160ns para calcular o tempo necessario para um programa ser executado no monociclo basta:
160 _ 10²
160 _ 10³
agora para realizar o calculo com pipeline:
é necessario saber quantos ciclos de clock sao necessarios por instrução, supondo que são 4
dessa forma
tempo total = tempo da primeirao instrução + (n-1)*40 {40 = ciclo de clock}
tempo total = 160 + (10² - 1)*40 = 4.160 ns
etc...

## Questão 2

Considere os seguintes dados abaixo acerca do tempo de execução de
cada um dos subsistemas que compõem um processador monociclo que utiliza a técnica de
pipelining:
Passo Tempo
BI – Busca Instrução 200 ɳs
DI – Ler Regs /
Decod. Instrução 100 ɳs
EX – Executar Operação 200 ɳs
MEM - Acessar Memória 200 ɳs
ER – Escrita Registrador 100 ɳs

a)
Monte o gráfico de alocação de subsistemas para a parcela de programa dado abaixo:
lw $s1,0($s7)
add $s0,$s4,$s5
sub $s2,$s6,$s2
beq $s8,$s3, SALTO

---

### Resposta:

Não é necessário uso de stalls ja que nao ha conflito de execução nem de dados(registradores escrevendo e lendo)

## Exercicio 3

Um determinado processador digital de
propósito geral possui 6 estágios de processamento em cascata, ou 6 estágios de pipeline.
O primeiro estágio, o de busca de instrução, e o último estágio, o de armazenamento do
resultado, levam 2 ciclos de relógio cada para executar. Os demais estágios levam 1 ciclo.
O número máximo de instruções que esse processador consegue executar em 70 ciclos é:

---

### Resposta:

BI DI EX MEM ER XX  
 BI DI EX MEM ER XX
BI DI EX MEM ER XX
BI DI EX MEM ER XX
BI DI EX MEM ER XX
BI DI EX MEM ER XX
dessa forma a cada 2 ciclos uma nova instrução é executada portanto 70/2 = 35 instruções em 70 ciclos

## Exercicio 4

```c
float v1[] = {33.0, 71.2, 19.1, 2.0, 99.9, 44.1, 123.12, 77.12};
float v2[] = {66.3, 1.4, 22.7, 4.1, 1.0, 1.1, 5.7, 99.9};
float v3[8];
void vectoradd(float* a, float* b, float* c, int len){
    int i;
    for(i=0; i<len; i++){
        c[i] = a[i] + b[i];
    }
}
```

Suponha que o programa acima seja compilado para um processador MIPS de 32 bits que
tenha uma cache com capacidade de 4096 bytes e um tamanho de bloco de 16 bytes
mapeados de forma direta. Também suponha que a variável i, o parâmetro len e os
ponteiros a, b e c estejam todos localizados em registradores. Além disso, assumimos que a
cache está inicialmente vazia e que o código assembly primeiro carrega um elemento por
meio do ponteiro a, seguido por um carregamento por meio do ponteiro b, antes de
finalmente escrever os dados na memória usando o ponteiro c.

(a) Assumimos que v1 está localizado no endereço 0x10008000 e que a alocação de v2 e
v3 estão alocados consecutivamente depois na memória sem espaço vazio entre os vetores
declarados. Qual é então a taxa de acertos do cache de dados para executar o seguinte
chamada de função:

    vectoradd(v1,v2,v3,8);

Existe localidade temporal ou localidade espacial ou ambas?

(b)Se usarmos as mesmas suposições de (a), mas agora executarmos o seguinte código

    vectoradd(v1,v1,v3,8);

Qual é então a taxa de acertos do cache de dados? Existe localidade temporal ou
localidade espacial ou ambos

(c) Finalmente, se assumirmos agora que v1 está localizado no endereço 0x10008000, v2
está localizado no endereço 0x10009000 e v3 está localizado no endereço 0x1000a000, e
nós executamos

    vectoradd(v1,v2,v3,8);

Qual é então a taxa de acertos do cache de dados? Existe localidade temporal ou
localidade espacial ou ambos? Que outro problema é introduzido neste exemplo?

---

### Resposta:

a) Tamanho do bloco = 16bytes | cada float = 4bytes | vetor ocupa = 32 bytes
portanto cada vetor precisa de 2 blocos

ex em v1 bloco 1:{33,71.2,19.1,2.0} | | bloco 2:{99.9, 44.1, 123.12, 77.12}

Ao acessar a memoria cache para ler os vetores acontece um cache miss no primeiro elemento(33.0) dessa forma a unidade de gerenciamento de memoria load todo o bloco, dessa forma é lido os 3 proximos valores.(1 chache miss e 3 hits)
Ao chegar no 5 elemento ele pertence a um bloco diferente que ainda nao foi carregado dessa forma acontece um cache miss e é dado load no restante do bloco dessa forma (1 cache miss 3 hits)
No total do carregamento dos 2 blocos ococorreram 2 cache miss e 6 cache hits, gerando 75% de acerto

são 8 interações em 3 vetores = 24
são 6 acertos em 3 vetores = 18
18/24 = 75% total

Haverá a localidade espacial, elementos próximos do vetor são carregados conjuntamente
quando há um cache-miss.

Como isso se aplica ao vetor v3?

Na função vectoradd, v3 é usado apenas como destino das somas (c[i] = a[i] + b[i]). Isso significa que:

    Não há leituras de v3, apenas escritas.

    O comportamento do cache durante as escritas depende da política adotada:

        Se for write-through, cada escrita pode causar um cache miss inicialmente (se o bloco ainda não estiver carregado).

        Se for write-back, cada escrita inicial também causará um cache miss, pois o bloco precisa ser carregado no cache antes de ser modificado.

Portanto, mesmo que v3 seja apenas escrito, ele ainda pode causar cache misses quando os blocos correspondentes não estão no cache.

b)
continua 3 vetores 8 interações = 24
acertos = 6 + 8 + 6 = 20
20/24 = 83%

c)
vetores v1,v2,v3 (0x10008000 0x10009000 e 0x1000a000) todos terão o mesmo set na cache, dessa forma vai ser sobreescrito todo momento que um elemento do vetor foi lido dessa forma acontece um cacho miss de 100%

Todos os vetores (v1, v2, v3) têm o mesmo set index (set index = 0) devido à separação dos endereços por potências de dois (os endereços diferem apenas nos bits mais altos). Isso significa que todos os vetores competem pelo mesmo conjunto no cache, criando um problema de sobrescrições constantes (cache thrashing).

Para cada iteração da função:

    Um elemento de v1 é lido.

    Um elemento de v2 é lido.

    O resultado é escrito em v3.

    O cache é mapeado diretamente, então cada conjunto pode armazenar apenas um bloco por vez.

    Como todos os vetores (v1, v2, v3) têm o mesmo set index (set index = 0) mas diferentes tags, eles sobrescrevem uns aos outros no mesmo conjunto.

    Sempre que um vetor é acessado, ele sobrescreve o bloco anterior no conjunto correspondente.

    Isso significa que nenhum bloco permanece no cache entre as iterações.

## Exercicio 5

Considere um sistema hipotético contendo apenas cache L1 e memória principal. Suponha que o acesso ao cache L1 leve 1 ciclo de CPU, enquanto o acesso à memória leva 101 ciclos de CPU (incluindo o 1 ciclo inicial para verificar o cache).

(a) Você escreve um programa e o executa na máquina. Você observa através de testes
que o programa exibe uma taxa de acerto da cache de 97%. Calcule o número médio de
ciclos necessários para atender a cada acesso a dados.

(b) Mais tarde, você reestrutura os loops de seu programa para melhorar sua localidade e
descobre que a taxa de acerto da cache aumenta para 99%. Calcule o novo número médio
de ciclos necessários para atender a cada acesso a dados. Qual é o impacto deste aumento
de 2% na taxa de acerto?

---

### Resposta:

Media ponderada
0.97 _ 1 + 0.03 _ 101 / 0.97 + 0.03 = 0.97 + 3.03 = 4 ciclos 4

há duas possibilidades o dado ja esta na cache entt usa somente um ciclo ou o dado nao esta na cache e deve buscar ele na memoria usando 101 ciclos

Multiplicamos o acesso a cache pela taxa de acertos mostrando caso acerte esteja na cache quantos ciclos usam
Multiplicamos o acesso a memoria pela taxa de error mostrando caso erre o numero de ciclos necessarios para buscar na memoria principal, somando recebemos o numero de ciclos medio

(b)

0.99 _ 1 + 0.01 _ 101 = 0.99 + 1.01 = 2 ciclos essa taxa de acertos de 99% reduziu o numero de ciclos pela metade.

Isso representa uma melhoria significativa no desempenho, reduzindo pela metade o tempo médio necessário para cada acesso a dados devido ao aumento na localidade e na eficiência da cache.

## Exercicio 6

Um programa de benchmark é executado em um processador a 40 MHz.
O programa executado consiste em 100.000 execuções de instrução, com a seguinte
mistura de instruções e quantidade de ciclos de clock:

| Tipo de instrução         | Quantidade de instruções | Ciclos por Instrução |
| ------------------------- | ------------------------ | -------------------- |
| Aritmética de inteiros    | 45.000                   | 1                    |
| Transferência de dados    | 32.000                   | 2                    |
| Ponto flutuante           | 15.000                   | 2                    |
| Transferência de controle | 8.000                    | 3                    |

Determine o CPI e o tempo de execução para esse programa

### Resposta:

CPI = 45*1 + 32 * 2 + 15 * 2 + 8*3 / 110 = 1.63
tempo de execução = tempo de CPU = (ic _ CPI) / clockrate
100.000 _ 1.63 / 40\*10⁶ = 4.075 ms

## Exercicio 7

Usando a mesma tabela da questão acima, qual seria o speed up se houvesse uma
melhoria no número de ciclos por instrução da transferência de controle e este passasse a
ser 2? Comente sobre o resultado.

para calcular speedup usa lei de Amdhal
Speedup = 1/(1 - f + f/s)

f = tempo usado no fator de melhoria / tempo total

f = [IC * 0.08 * 3 * (periodo de clock)] / [IC * CPI (periodo de clock)]
IC = 100.000
clock = 40 \* 10⁶
CPI = 1.63

f = 0.15
speedup = 1 / (1-f+fs)
s = 3/2 (ciclo antigo/ ciclo novo) = 1.5
speedup = 1 / (1-0.15+ 0.15/1.5)
speedup = 1/0.95
speedup = 1.05

Essa melhoria ocorreu em uma parte do programa que não é frequentemente executada, por isso é esperado um speedup pequeno.
