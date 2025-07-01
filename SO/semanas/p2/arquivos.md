Estrutura de Arquivos
Arquivos podem ser estruturados de várias maneiras. As fontes descrevem três possibilidades comuns
:
•
(a) Sequência desestruturada de bytes: O sistema operacional não sabe ou não se importa com o conteúdo do arquivo; ele apenas vê bytes
. Qualquer significado deve ser imposto por programas em nível de usuário. Essa abordagem oferece a máxima flexibilidade
.
•
(b) Sequência de registros de tamanho fixo: Nesse modelo, um arquivo é uma sequência de registros de tamanho fixo, cada um com alguma estrutura interna
. A operação de leitura retorna um registro, e a operação de escrita sobrepõe ou anexa um registro
.
•
(c) Árvore de registros: Um arquivo consiste em uma árvore de registros, não necessariamente todos do mesmo tamanho, onde cada registro contém um campo chave em uma posição fixa
. A árvore é ordenada no campo chave para permitir uma busca rápida por uma chave específica.

3.2 Estrutura Hierárquica Unix (FHS)

O sistema de arquivos Unix é baseado em uma única estrutura hierárquica (árvore) de diretórios, começando pela raiz /.

    /: Diretório raiz.
    /etc: Arquivos de configuração.
    /bin: Utilitários de uso geral.
    /sbin: Utilitários de administração (alguns restritos ao root).
    /dev: Arquivos especiais que representam dispositivos, criados com mknod. Contêm major number (driver) e minor number (dispositivo específico).
    /usr: Hierarquia secundária (incluindo /usr/lib e /usr/include).
    /lib: Bibliotecas compartilhadas essenciais.
    /home: Área de trabalho dos usuários.
    /var: Área para spool de impressão, e-mails e logs.
    /boot: Arquivos para inicialização do sistema.
    /mnt: Diretório para sistemas de arquivos temporários montados.

4.1. Estruturas Essenciais na Partição
Ao criar ou formatar uma partição, são estabelecidas estruturas importantes
:
•
Superbloco: Contém todos os parâmetros-chave a respeito do sistema de arquivos e é lido para a memória na inicialização do computador ou no primeiro acesso ao sistema de arquivos
.
•
Informações sobre blocos disponíveis: Podem estar na forma de um mapa de bits ou de uma lista de ponteiros
. Um disco com n blocos exige um mapa de bits com n bits
.
•
O restante do disco contém todos os outros diretórios e arquivos
.
•
Na formatação, pode-se agrupar setores contíguos do disco (ex: 512 bytes) para formar blocos lógicos maiores (ex: 4KB)
.

Vários métodos são utilizados para controlar quais blocos de disco pertencem a quais arquivos
:
•
Alocação Contígua: O esquema mais simples é armazenar cada arquivo como uma sequência contígua de blocos de disco
. Para monitorar a localização dos blocos de um arquivo, basta lembrar de dois números: o endereço em disco do primeiro bloco e o número de blocos no arquivo. O desempenho da leitura é excelente, pois o arquivo inteiro pode ser lido em uma única operação, sem buscas ou atrasos rotacionais após a busca inicial. No entanto, sua principal desvantagem é a fragmentação do disco ao longo do tempo, onde lacunas de blocos livres aparecem quando arquivos são removidos, e o disco não é compactado imediatamente
.
•
Alocação por Lista Encadeada: Cada arquivo é mantido como uma lista encadeada de blocos de disco
. A primeira palavra de cada bloco é usada como um ponteiro para o próximo bloco, e o restante do bloco é reservado para dados. A vantagem é que nenhum espaço é perdido para a fragmentação de disco. As desvantagens incluem o acesso aleatório extremamente lento (pois é preciso seguir a cadeia de ponteiros) e a perda de espaço para os ponteiros, o que faz com que a quantidade de dados que um bloco pode armazenar não seja uma potência de dois
.
•
Alocação por Lista Encadeada Usando uma Tabela na Memória (FAT): Para eliminar as desvantagens da lista encadeada pura, as palavras do ponteiro de cada bloco de disco são colocadas em uma tabela na memória
. Essa tabela, chamada FAT (File Allocation Table - Tabela de Alocação de Arquivos), permite seguir a cadeia de blocos de um arquivo rapidamente. Embora melhore drasticamente o acesso aleatório, a principal desvantagem é que a tabela inteira precisa estar na memória o tempo todo para funcionar
.
•
I-nodes (Index-nodes): Este método associa cada arquivo a uma estrutura de dados chamada i-node, que lista os atributos e os endereços de disco dos blocos do arquivo
. A grande vantagem é que o i-node precisa estar na memória apenas quando o arquivo correspondente estiver aberto. Um problema com i-nodes é que cada um tem espaço para um número fixo de endereços de disco; quando um arquivo cresce além desse limite, a solução é reservar o último endereço de disco não para um bloco de dados, mas para o endereço de um bloco contendo mais endereços de blocos de disco (indireção). Sistemas do tipo Unix, por exemplo, mantêm ponteiros diretos e indiretos para blocos de dados em uma estrutura i-node.


