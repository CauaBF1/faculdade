# Gerenciamento de memória


 - No funcionamento de computadores segundo a arquitetura de Von Neumann, a memória é usada para armazenar instruções e dados.
 - Além de seus próprios códigos e de bibliotecas estáticas ligadas ao programa na compilação e geração de código, é comum que códigos de bibliotecas compartilhadas necessárias sejam mapeadas no espaço de endereçamento dos programas em seus carregamentos.
 - Independentemente de qual programa está sendo executado, é claro que o código do SO relacionado às chamadas de sistema (syscalls) e ao tratamento das interrupções deve estar mapeado na área de memória acessível por cada programa.
 - Outro aspecto a considerar é que nem o programador, ou o compilador, ou o gerador de código sabem exatamente onde um programa será posicionado na memória quando for carregado para execução.
 - Comumente, há vários programas a executar ao mesmo tempo e um programa não pode interferir nas áreas de memória dos demais.
 - Áreas de memória de um programa são mapeadas sobre um espaço de endereçamento virtual.
 - Programas são carregados na memória para execução e as áreas que ocuparam são liberadas quando os programas terminam. 
 - Demanda por áreas de memória pode variar ao longo da execução de um programa. Programas podem solicitar aumento em suas áreas de dados e também podem solicitar o mapeamento de áreas de memória.
 - SO precisa gerenciar os espaços livres e alocados na memória.
 - Ao carregar um programa é preciso alocar espaço para contê-lo.
 - A demanda de memória de um programa, ou a soma das demandas de memória de todos os programas em execução, pode ser maior do que a memória física disponível.
 - Ao longo da evolução das técnicas de gerenciamento de memória pelo SO e dos processadores, foram criados mecanismos de relocação e técnicas de swap (troca, apoiada pelo armazenamento em disco). Evolução levou à criação dos mecanismos de memória virtual.

## Áreas de memória de um processo

No modelo de computadores que seguem a arquitetura de Von Neumann, a memória serve para armazenamento de instruções e dados. Assim, em tempo de execução, a memória de um computador de uso geral é ocupada por códigos e dados do sistema operacional e códigos e dados dos processos associados às aplicações em execução.

O gerenciamento das áreas de memória de um processo começa na fase de compilação. Cabe ao compilador organizar os vários trechos de código, identificar as variáveis e seus tipos, as constantes e as eventuais atribuições de valores iniciais a variáveis. 

Tratando do código, o compilador determina um posicionamento sequencial de todas as funções num bloco de código e traduz as referências aos nomes de cada uma delas por desvios aos endereços onde cada um desses códigos foi posicionado. No caso de funções situadas em bibliotecas de link dinâmico, contudo, as referências aos seus endereços só serão resolvidas no momento em que o programa estiver sendo carregado para execução.

Do ponto de vista das variáveis globais e estáticas, cabe ao compilador determinar quanto espaço de memória será necessário para contê-las, posicionar cada variável logicamente nesse espaço, e resolver as referências aos nomes das variáveis no código por seus endereços relativos na área de dados.

O espaço reservado para as variáveis é tratado de maneira diferente para variáveis inicializadas e não inicializadas. Para tratar as variáveis globais e estáticas (static) não inicializadas, o gerador de código apenas precisa indicar no cabeçalho do arquivo do programa o espaço total de memória que deverá ser reservado na criação do processo. Já as variávies inicializadas precisam ser salvas num espaço reservado no arquivo do programa executável, para que sejam copiadas para uma área de memória de dados do processo em tempo de carregamento / execução. 

Espaços para variáveis declaradas localmente, dentro dos códigos das funções, serão reservados na pilha antes de cada chamada, em tempo de execução, de acordo com as convenções de chamadas de função estabelecidas. 

Também os espaços para onde apontarão as variáveis do tipo ponteiro, alocadas dinamicamente, serão determinados em tempo de execução, numa área de memória chamada heap. Essa área é reservada na criação do processo e pode ser ajustada sob demanda. Quando um programa faz uma chamada do tipo malloc, essa função verifica se há espaço disponível no heap, reserva esse espaço e retorna um ponteiro ao programa. Se não houver espaço, a própria função malloc pede ao SO para aumentar o tamanho atual do heap e reserva o espaço dentro dessa nova área.

```
#include <stdlib.h>

char *palavra = "constante";      // variável global inicializada com valor constante
int global_nao_inic;              // variável global não inicializada
int global_inic = 1;              // variável global inicializada

int 
main()
{
   int local;                   // variável local
   static int local_estatica;   // variável local estática (preserva valor)
   int *pont;                   // variável tipo ponteiro; inicialmente, aponta para NULL

   pont = (int*)malloc(sizeof(int));  // faz ponteiro apontar para área no heap

   return 0;
}
```

```
$ gccc progc.c -o prog

$ nm prog
  ...
  0000000000201048 D global_inic
  0000000000201060 B global_nao_inic
  ...
  000000000020105c b local_estatica.3311
  ...
  0000000000201050 D palavra
  ...
  
  
$ man nm
   ...
   "B"
   "b" The symbol is in the BSS data section.  This section typically contains zero-
       initialized or uninitialized data, although the exact behavior is system
       dependent.
   ...
   "D"
   "d" The symbol is in the initialized data section.
   ...
   "U" The symbol is undefined.
```
Como se vê, a variável global_inic é definida dentro da área de dados do programa. Já as variáveis global_nao_inic e local_estática são definidas dentro da área do BSS, cujo espaço só será alocado no carregamento do programa.

## Criação de um processo

Um novo processo é criado pela chamada fork, que duplica o processo que emite a chamada. Teoricamente, o SO deve copiar as áreas de memória do processo pai para o processo filho. Há, contudo, uma série de otimizações que são comumente feitas neste caso. 

Por exemplo, o SO pode optar por compartilhar as áreas de código do processo pai com o processo filho, já que os conteúdos desta área não são alterados em tempo de execução. 

Outra estratégia que o SO pode adotar na chamada fork() é compartilhar inicialmente as áreas de dados, usando uma estratégia chamada copy-on-write, já que as áreas de dados podem não ser alteradas imediatamente. Caso algum dos processos, pai ou filho, tente alterar esta área, inicia-se uma cópia para o processo filho.

É na fase de carregamento de um programa, ou seja, quando é realizada a chamada de sistema execve(2), que as áreas de memória de um processo são ajustadas, substituindo as áreas de memória do processo que fez essa chamada.

De maneira geral, o carregamento de um programa (program loading) trata do mapeamento de segmentos de arquivos em sementos de memória virtual, além de outros ajustes necessários em função da ABI utilzada

Informações contidas em cabeçalhos de controle do arquivo executável (ELF, em sistemas Linux), permitem ao carregador do SO (loader) identificar características de algumas das áreas de memória do processo sendo criado. 

Para programas no formato ELF, a seção .interp comumente contém uma indicação do carregador que deve ser usado.

**As áreas de memória de um processo são tipicamente organizadas em seções, ou segmentos: segmento de código (code segment), segmento de dados (data segment) inicializados e não inicializados (block started by symbols - bss) e segmento de pilha (stack).**

O segmento de código de um processo contém suas instruções, que são mapeadas do arquivo executável (.text) para a área de memória do processo. Essa área é ajustada com permissões de leitura e execução, sem possibilidade de serem alteradas pelo processo. Deste modo, é comum que áreas de código possam ser compartilhadas entre processos, como ocorre no caso de blibliotecas compartilhadas (shared libraries).

Tratando-se de um arquivo executável que usa bibliotecas de link dinâmico, os cabeçalhos de seu arquivo ELF deverão conter referências às bibliotecas dinâmicas compartilhadas necessárias. No carregamento do arquivo executável, os códigos e eventuais áreas de dados dessas bibliotecas também são mapeados na área de memória do processo, ficando associados a seções dos arquivos correspondentes. Usando uma tabela de símbolos presente no arquivo da biblioteca compartilhada, o loader também consegue realizar ajustes aos endereços nas chamadas das funções utilizadas. 

As áreas de código do SO, relacionadas às chamadas de sistema e tratamentos de interrupção, por exemplo, também têm que ser mapeadas, de forma compartilhada, no espaço de endereçamento de todos os processos. Áreas de código não são alteráveis em tempo de execução na memória, de forma que os códigos de serviço do SO podem ser compartilhados e não replicados para todos os processos!

Havendo valores constantes no programa, esses terão sido salvos na seção de dados de leitura apenas (.rodata) do arquivo executável. Essa área do arquivo também é mapeada para uma área de dados do processo na memória, com permissão de leitura apenas.

Variáveis (globais e estáticas) pré inicializadas no código vão estar salvas numa sessão separada do arquivo executável. Essa área do arquivo é mapeada na área de memória de dados do processo com permissões de leitura e escrita. 

Como seria esperado, os espaços associados às variáveis globais e estáticas não inicializadas definidas no programa não ficam salvos no arquivo executável. Sabendo qual é a quantidade total de espaço necessário para essas variáveis, o compilador / linker apenas inclui no cabeçalho do arquivo executável informações sobre qual deve ser o tamanho da área de memória reservada para essas variáveis no carregamento do programa. Essas **informações são salvas na seção .bss** do cabeçalho do arquivo executável. No carregamento do processo, é criada uma área do tamanho necessário, com permissão de leitura e escrita. Todos os bytes dessa área são comumente inicializados com o valor 0 antes do uso.

Outra área de dados associada a um processo é a área reservada para alocação dinâmica, chamada de **heap**. Não há referência a essa área no arquivo executável. Cabe à função de inicialização da biblioteca de gerenciamento de alocação dinâmica (malloc e afins, quando usadas pelo programa) fazer a reserva de uma área de heap para o processo, posicionando-a tipicamente logo após o .bss configurado para as variáveis globais. Em tempo de execução, o  heap é comumente gerenciado pelas funções de alocação dinâmica (malloc, calloc, realloc e free), que se encarregam inclusive de solicitar ao SO que aumente seu tamanho através das  chamadas de sistema brk() e sbrk(). Também é possível que novos espaços de memória para o heap sejam alocados sob demanda para um processo pelas funções da biblioteca do malloc, usando a chamada mmap().


### Pilha(stack)
Uma área de pilha (stack) também é alocada ao processo sendo criado, em tamanho escolhido pelo SO. Cada processo tem permissões de leitura e escrita nessa área. Também é comum que essa área seja expandida automaticamente em tempo de execução, até um tamanho máximo definido na configuração do SO. No Linux, esse tamanho é tipicamente limitado a 8MB. No shell, esse limite pode ser visto com o comando ulimit ($ ulimit -s). 

Em tempo de execução, a pilha é manipulada por instruções de carregamento e descarregamento de valores, sendo que o ponteiro da posição atual decresce à medida que dados são inseridos na pilha.

De acordo com a API Linux SUS, a configuração inicial da pilha de um novo processo deve conter valores específicos, assim como devem ser ajustados os valores de alguns registradores

### mmap
O mapeamento de outros arquivos em áreas de memória dentro do espaço de endereçamento do processo pode ser realizado com a chamada mmap(2).

No sistema Linux, áreas de memória de um processo são identificadas pela estrutura mm dentro de sua task_struct. Cada página física da memória, por sua vez, é mapeada por uma estrutura page.

Examinando um arquivo executável

Os utilitários objdump , readelf e nm permitem observar aspectos das seções definidas em arquivos executáveis, objetos ou bibliotecas.

## Espaço de endereçamento de um processo

Em ambientes compartilhados, multitarefas, cada processo tem seu próprio espaço lógico de endereçamento (virtual). Esse espaço corresponde a toda área de endereçamento que é possível referenciar nas instruções do computador. Numa arquitetura 32 bits, por exemplo, é possível referenciar diretamente 4GB, independentemente da quantidade de memória RAM existente no computador. 

No carregamento de um processo, cada uma das suas áreas de memória, como código, dados e pilha, vai estar associada a alguma posição lógica dentro desse espaço de endereçamento. Por razões de segurança, a posição lógica de cada área mapeada, contudo, varia de maneira aleatória pelo SO para cada processo carregado. 

Usando o modo de 32 bits dos processadores x86, registradores de segmento (CS, DS, ES, FS, GS, SS) podem ser usados para identificar as diferentes áreas lógicas de um processo, a partir de onde está sendo buscada a instrução a executar (CS), ou onde está sendo lido ou escrito um dado na memória (DS), ou onde será salvo o dado da pilha (SS).

Em tempo de execução, os valores contidos nesses registradores de segmento são convertidos dinamicamente pela MMU do processador em endereços base, aos quais são somados os deslocamentos de endereço (EIP), de dado e de pilha (ESP), por exemplo. O endereço linear virtual obtido é então convertido a endereços físicos através do mecanismo de paginação, em que a MMU novamente realiza uma tradução usando tabelas de páginas mantidas pelo SO para cada processo.

No funcionamento desse mecanismo de endereçamento indireto, cabe ao SO ajustar os endereços das estruturas de tradução de endereço em registradores apropriados do hardware, cada vez que restaura o contexto de execução de um novo processo (ou thread).

## ELF
Quando um programa está sendo carregado para execução, cabe ao loader do SO interpretar as informações de controle contidas nos cabeçalhos deste programa para fazer o ajuste apropriado das áreas de memória desse processo.

In Unix, the loader is the handler for the system call execve(). The Unix loader's tasks include:

 - validation (permissions, memory requirements etc.);
 - copying the program image from the disk into main memory;
 - copying the command-line arguments;
 - initializing registers (e.g., the stack pointer);
 - jumping to the program entry point (_start).

ELF (ELF 101 define um padrão unificado para a interface binária das aplicações ( ABI) em sistemas Unix. Esse formato é utilizado como padrão para arquivos executáveis, código objeto, bibliotecas compartilhadas e arquivos com despejos de memória (core dumps).

An ELF object file consists of the following parts:

        
 - File header, which must appear at the beginning of the file.
 - Section table, required for relocatable files, and optional for loadable files.
 - Program header table, required for loadable files, and optional for relocatable files. 
 - This table describes the loadable segments and other data structures required for loading a program or dynamically-linked library in preparation for execution.
 - Contents of the sections or segments, including loadable data, relocations, and string and symbol tables.


Em slstemas Linux, o utilitário readelf pode ser usado para prover detalhes de um programa ELF:
$ readelf -S -W hello

Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings)
  I (info), L (link order), G (group), x (unknown)
  O (extra OS processing required) o (OS specific), p (processor specific)


