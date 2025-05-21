# ELF 
As informações de um processo em um arquivo ELF (Executable and Linkable Format) são organizadas em uma estrutura bem definida, composta principalmente pelos seguintes componentes:

 - ELF Header: É o primeiro bloco do arquivo, contendo informações essenciais como o tipo do arquivo (executável, objeto, biblioteca), arquitetura (32 ou 64 bits), ponto de entrada do programa, e os offsets para as tabelas de headers de programas e seções. Ele identifica o arquivo como ELF e orienta o carregador do sistema operacional sobre como interpretar o restante do arquivo.

 - Program Header Table: Contém descrições dos segmentos do programa, que são as partes que realmente serão carregadas na memória para execução. Cada entrada descreve um segmento, incluindo o tipo, permissões, endereço virtual e tamanho. Essa tabela é fundamental para o carregamento do executável pelo sistema operacional


 - Section Header Table: Lista todas as seções do arquivo, como .text (código), .data (dados inicializados), .bss (dados não inicializados), .rodata (dados somente leitura), .got (tabela global de offset), entre outras. Cada seção tem um propósito específico, como armazenar código, dados, símbolos, ou informações de depuração. 

 - Seções/Segmentos: As seções são áreas do arquivo reservadas para diferentes tipos de dados e instruções, cada uma com permissões próprias (leitura, escrita, execução). Os segmentos agrupam seções semelhantes para facilitar o carregamento em memória. Por exemplo, as seções .data e .bss podem estar no mesmo segmento de dados.

 - Outras informações: O ELF também armazena informações como símbolos, tabelas de relocação, e strings de nomes de seções, que são usadas pelo linker e pelo carregador do sistema operacional durante a ligação e execução do programa. 

Resumindo, o arquivo ELF organiza todas as informações necessárias para que o sistema operacional possa carregar, interpretar e executar um programa, separando código, dados, permissões e metadados em estruturas bem definidas e padronizadas.


# MMAP
A função mmap() serve para criar um mapeamento entre uma região de memória virtual do processo e um arquivo ou dispositivo, ou ainda para alocar memória anônima (sem associação a arquivo), diretamente no espaço de endereçamento do processo.
Isso permite que:

 - Um arquivo seja acessado como se fosse um array na memória, facilitando leitura e escrita sem a necessidade de chamadas explícitas de leitura e gravação.

 - Dois ou mais processos compartilhem uma mesma região de memória, usando o mesmo arquivo mapeado, o que é útil para comunicação entre processos (IPC).

 - Grandes blocos de memória sejam alocados de forma eficiente, especialmente quando não se deseja usar a heap padrão do processo. 

Além disso, mmap() é amplamente utilizada para carregar bibliotecas compartilhadas e para otimizar o desempenho de acesso a arquivos e dispositivos, já que o sistema operacional pode gerenciar o carregamento sob demanda das páginas de memória necessárias.
