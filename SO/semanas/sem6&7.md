# Gerenciamento de memória
Como já sabemos, um sistema operacional permite que vários programas estejam carregados na memória ao mesmo tempo, e divide os tempos de uso do(s) processador(es) para a execução das instruções desses programas. 

Há várias questões importantes a serem resolvidas para que esse modelo de coexistência na memória funcione, contudo.

    Sabendo que a memória de um sistema computacional é usada para armazenamento de suas instruções (código), seus dados e de sua área de pilha, como é possível manter vários programas ativos ao mesmo tempo, cada um com suas demandas para uso da memória?
    De que maneira são criados os programas para conseguir saber os endereços efetivos de suas instruções e dados na memória quando forem colocados em execução?
    Como fazer para ter mais de um programa carregados para execução ao mesmo tempo, sem que um interfira com as áreas de memória dos outros?

Ao longo da evolução dos sistemas computacionais e seus sistemas operacionais, o funcionamento dos mecanismos de endereçamento e as formas de uso da memória foram mudando para acomodar eficientemente vários programas.

De maneira resumida:

    Inicialmente, foi preciso tratar o posicionamento de um programa em locais de memória que poderiam variar a cada execução. Isso foi tratado com o uso de registradores de relocação, que continham um endereço base que era somado a cada endereço referenciado por um programa.
    Seguiu-se o desenvolvimento de técnicas que impunham verificações de limites de tamanhos das áreas para evitar interferências entre os programas.
    Outra evolução foi o uso de estratégias que permitiam que cada programa não precisasse mais ser alocado em um espaço grande suficiente para contê-lo de forma contígua na memória. Isso foi obtido com o uso de diferentes segmentos.
    Posteriormente, criou-se um mecanismo que segmentava os endereços e as áreas de memória em blocos de tamanho fixo. Esta técnica foi chamada de paginação.

Atualmente, basicamente, usa-se memória virtual com paginação.

## Memória virtual endereçamento lógico
Para que os processos sejam executados, é preciso que tanto seus códigos (suas sequências de instruções) quanto os dados que eles manipulam sejam carregados na memória principal.

Uma vez residentes na memória principal, programas podem fazer referências a endereços de trechos de código, como funções chamadas durante a execução, e também a variáveis, que correspondem a posições de memória nas áreas de dados.

**A memória é gerenciada por software, pelo Sistema Operacional, e manipulada por  elementos específicos do hardware.** Cabe ao SO decidir sobre a forma como a memória será ocupada pelos processos, sobre o local onde cada processo deve ser carregado, por quanto tempo um processo deve permanecer carregado na memória, etc. Outro aspecto fundamental para a presença de vários processos na memória é a existência de mecanismos para impedir a interferência, proposital ou involuntária, entre suas áreas.

**Memória virtual é o nome que se dá a uma abstração que faz com que as referências a posições de memória feitas pelos processos sejam relativas a um espaço lógico, e não diretamente à memória física. Um mecanismo de tradução dos endereços lógicos em endereços efetivos é realizado pelo hardware em tempo de execução.**

Uma das **vantagens** desta técnica é que os programas podem ser **posicionados em qualquer parte da memória**. Além disso, os **programas em execução e suas áreas de dados não precisam estar completamente na memória o tempo todo**, permitindo que a memória seja usada por mais programas do que caberia de uma vez.

### Segmentação e paginação

Um primeiro aspecto do endereçamento virtual é o uso de áreas em segmentos (regiões de memória) separados para códigos, dados e pilha. Esse modelo é comum em processadores 32 bits da linha x86, por exemplo.

Usando um registrador como base para o endereço de código, por exemplo, todas as referências de endereços das instruções passam a ser relativas, somadas ao endereço inicial do segmento de código.

A mesma lógica vale para os endereços de dados, em posições relativas ao início do segmento de dados, e para o endereço do topo da pilha, em relação ao endereço base do semento de pilha.

Em geral, contudo, mesmo esses endereços relativos formados da soma do endereço base do segmento com o endereço de código, dados ou pilha, ainda podem ser endereços virtuais, que precisam ser traduzidos para endereço físicos da memória. Essa tradução de endereços virtuais em endereços efetivos de memória é comumente feita com técnicas de paginação.

### Paginação
Quando a tradução dos endereços é feita usando blocos de tamanho fixo, tem-se a técnica denominada paginação. A paginação consiste em dividir o espaço de endereçamento de um processo em blocos de tamanho fixo, que são chamados de páginas. Dessa forma, todo endereço passa a ter 2 dimensões: uma indicação da página lógica, que deve ser mapeada para uma página física, e o deslocamento dentro dessa página.

Dado o número de bits de um endereço no processador alvo (32, por exemplo), considera-se que os N bits menos significativos desse endereço estão associados ao deslocamento dentro de uma página, e os restantes indicam a qual página o endereço se refere. Na arquitetura x86 (PCs) as páginas tipicamente têm tamanho de 4096 (4k) bytes. Assim, os 12 bits menos significativos indicam o deslocamento, ou a posição de um endereço na página física que contém a página lógica referenciada.

Mas de que maneira os endereços virtuais, decompostos em páginas lógicas e deslocamentos dentro dessas páginas, são traduzidos em endereços efetivos de memória?
### Tabela de páginas
Nos sistemas computacionais que têm suporte à paginação, a memória física é logicamente subdividida em quadros (frames) do mesmo tamanho que as páginas lógicas (e.g. 4K). 

As páginas do espaço de endereçamento virtual de um processo são então mapeadas em quadros (page frames) do espaço de memória física. Esse mapeamento normalmente é feito com o auxílio de uma tabela de páginas, que contém o endereço físico (número do frame) de cada página da memória de um processo. Por exemplo, um processo de 20 KB pode ter o seu espaço de endereçamento subdividido em 5 páginas de 4 KB cada. 

A tradução de um endereço lógico, referenciado por um processo, para o endereço físico correspondente ocorre com o auxílio de uma tabela de páginas. Para tanto, substitui-se os bits que correspondem ao número da página lógica pelo número do frame (página física) que a contém. É responsabilidade do SO criar e manter uma tabela de páginas para cada processo ativo. É o SO que aloca (escolhe entre as disponíveis) páginas físicas (frames) para conter as páginas lógicas dos processos. 

A tradução dos endereços, contudo, ocorre durante a execução das instruções, a cada referência de endereços, e é feita de maneira eficiente por um componente do processador, chamado de unidade de gerenciamento de memória (Memory Management Unit - MMU). 

Na figura acima vê-se um exemplo de tradução de endereço com segmentação paginada. Como se observa, o endereço virtual tem 3 componentes lógicos: o indicador do segmento, o indicador da páginas e o deslocamento dentro da página. Para que o processador possa fazer a tradução do endereço, SO deve manter 2 tabelas de tradução de endereços para cada processo. A tabela de segmentos contém informações para traduzir o segmento lógico num valor que indica qual tabela de páginas usar. Cada tabela de páginas contém informações sobre a tradução de valores de páginas lógicas em páginas físicas. A parte do endereço lógico correspondente ao deslocamento dentro da página é a mesma tanto para o endereço virtual quanto para o endereço real.

Outro aspecto relevante que se observa na figura acima é a presença de uma espécie de cache da tradução de endereços. Esse cache é mantido automaticamente pelo processador, sem interferência do SO. Na arquitetura do PC, esse cache é chamado de TLB (Translation Lookaside Buffer). Ali são mantidas informações de algumas das traduções de endereços mais recentes, acelerando suas traduções nas referências futuras à memória para o mesmo processo.

Esse cache é caracterizado como uma memória associativa pois sua tecnologia permite testar a presença de um dado em todas as posições ao mesmo tempo, sem ter que verificar se o conteúdo de memória buscado está em cada  uma das posições dessa memória. Quando o dado de tradução está em qualquer uma das posições deste cache, ele é obtido bem mais rapidamente do que quando é preciso fazer a tradução usando a tabela de segmento e a tabela de páginas.


### Segmentação com paginação

Divisão do espaço de endereçamento virtual

    O endereço virtual é dividido em três partes:

        Número do segmento: identifica qual segmento está sendo acessado (ex: código, pilha, heap, dados).

        Número da página dentro do segmento: identifica qual página daquele segmento está sendo acessada.

        Deslocamento: indica a posição exata dentro da página.

Tabelas usadas

    Tabela de segmentos: cada processo tem uma tabela de segmentos. Cada entrada aponta para uma tabela de páginas daquele segmento e informa o tamanho máximo do segmento.

    Tabelas de páginas: para cada segmento, existe uma tabela de páginas. Cada entrada dessa tabela indica em qual quadro de memória física está a página correspondente daquele segmento.

Tradução do endereço virtual para físico

    O número do segmento seleciona a entrada na tabela de segmentos.

    Essa entrada fornece o endereço base da tabela de páginas do segmento.

    O número da página dentro do segmento indexa a tabela de páginas, que aponta para o quadro físico.

    O deslocamento é somado ao início do quadro para formar o endereço físico final

## Tradução de endereços

Considerando um endereço de 32 bits e usando páginas de 4KB, os 12 bits menos significativos de cada endereço indicam o deslocamento dentro da página. 

 2^12 = 2^2 * 2^10 = 4 * 1K = 4 KB

 Os 20 bits mais significativos indicam a página. 2^20 = 2^10 * 2^10 = 1K * 1K = 1M páginas

 Ou seja, endereços de 32 bits permitem endereçar 4 GB posições de memória, 2^20 * 2^12 = 1 M * 4K = 4 GB

 Assim, num processador com suporte a memória virtual com paginação, a tradução de endereços é feita substituindo-se o endereço da página lógica (indicada pelos 20 bits mais significativos do endereço - p/32 bits) pelo endereço da página efetiva (page frame) na memória. Um page frame é uma posição normal na memória, começando num bloco de 4K. Trata-se apenas de uma forma de o SO organizar os espaços de memória disponíveis.

 Para ser eficiente, essa tradução tem que ser feita por circuito, pelo processador, por uma unidade interna de tradução de endereços chamada MMU. A tradução é feita na busca de instruções pelo processador, ou seja, a MMU vê o valor contido no registrador de instruções (PC - Program Counter, ou CS / EIP nos X86s (*)) e troca os seus 20 bits mais significativos antes de buscar a instrução na memória. Na prática, na arquitetura X86, tem-se um esquema se segmentação paginada. Isso significa que o valor no registrador de segmento indica um segmento lógico que é traduzido pela MMU para um endereço base. O deslocamento indicado pelo EIP é então somado ao endereço base do segmento, formando um endereço linear virtual. É esse endereço que vai ser traduzido com o esquema de paginação para chegar-se ao endereço efetivo que contém a instrução.

A instrução é trazida para um registrador interno da CPU chamado IR (instruction register) a partir de onde ela é decodificada e executada. Dependendo da instrução, há um novo acesso à memória para recuperar ou armazenar informações. Para acessar esse novo endereço também é necessária uma tradução, da mesma maneira (DS / offset). 

 Para fazer a tradução, a MMU usa a tabela de páginas do processo corrente. Na verdade, a CPU nem sabe qual é o processo corrente, ela só sabe onde deve buscar as informações para a tradução. Cabe ao SO criar e manter uma tabela de páginas para cada processo e ajustar o registrador no processador que indica onde está essa tabela de páginas. Isso é feito a cada troca de contexto. 

 Como a tabela de páginas é referenciada a cada instrução, ela certamente acaba sendo copiada para o cache do processador, numa área chamada Translation lookaside buffer (TLB), tornando a tradução de endereços mais eficiente.

 Quanto à localização das áreas do processo no disco, isso não é mantido na tabela de páginas. As informações típicas de uma entrada na tabela de páginas incluem:
```
_PAGE_PRESENT -> Page is resident in memory and not swapped out.

_PAGE_PROTNONE -> Page is resident, but not accessible.

_PAGE_RW -> Set if the page may be written to

_PAGE_USER -> Set if the page is accessible from userspace

_PAGE_DIRTY -> Set if the page is written to

_PAGE_ACCESSED -> Set if the page is accessed 
```
A partir do nome do arquivo executável que deu origem ao processo e das bibliotecas e outros arquivos mapeados no espaço de endereçamento do processo, o SO consegue buscar uma página em falta.

## Memória virtual na arquitetura x86

Na arquitetura x86, há algumas formas de endereçamento, tipicamente baseadas no uso de segmentos e deslocamentos dentro desses segmentos.

**Segmentos podem ser usados para: code, data, stack, extra**

Cada programa pode ter até 6 segmentos, identificados pelos registradores:

cs,ds,ss,es,fs,gs 

Referências a endereços no código podem incluir prefixo com indicação do segmento:

    mov eax, ds:0x80 (load offset 0x80 from data into eax)
    jmp cs:0xab8 (jump execution to code offset 0xab8)
    mov ss:0x40, ecx (move ecx to stack offset 0x40)

Segmento apropriado também pode ser inferido em função da instrução:

    Instruções relacionadas ao controle de fluxo (jump, call, ...) usam o segmento de código
    Instruções que manipulam o conteúdo da pilha (push/pop) usam a pilha :-)
    A maioria das instruções de armazenamento ou carregamento de dados (load, store,...) usa o segmento de dados
    Segmentos extra  (es, fs, gs) devem ser usados explicitamente


1. Paginação Simples

    Divisão do endereço virtual:

        Número da página (p): Bits usados para indexar a tabela de páginas.

        Deslocamento (d): Bits para localizar o byte dentro da página.

    Exemplo com páginas de 4 KB (2^12 bytes):

        Deslocamento: 12 bits (para endereçar 4.096 bytes por página).

        Número da página: 20 bits (32 bits totais – 12 bits de deslocamento).

        Tabela de páginas: 2^20 entradas (1.048.576 páginas virtuais).

Parte	Bits	Função
Número da página	20	Índice na tabela de páginas.
Deslocamento	12	Posição dentro da página (0 a 4095).

2. Segmentação com Paginação

    Divisão do endereço virtual:

        Número do segmento (s): Índice na tabela de segmentos.

        Número da página (p): Índice na tabela de páginas do segmento.

        Deslocamento (d): Posição dentro da página.

    Exemplo típico:

        Segmento: 8 bits (256 segmentos).

        Página: 12 bits (4.096 páginas por segmento).

        Deslocamento: 12 bits (páginas de 4 KB).

Parte	Bits	Função
Número do segmento	8	Índice na tabela de segmentos.
Número da página	12	Índice na tabela de páginas do segmento.
Deslocamento	12	Posição dentro da página.

