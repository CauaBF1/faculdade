Gerenciamento de Arquivos e Operações de E/S em Sistemas Operacionais

Esta apostila foi elaborada com base nas informações fornecidas em diversas  fontes, cobrindo os fundamentos dos sistemas de arquivos, sua  implementação, operações de entrada e saída (E/S), e mecanismos de  segurança e gerenciamento de usuários, com foco especial nas  particularidades do Linux.

1. Conceitos Fundamentais de Sistemas de Arquivos

As aplicações de computador necessitam armazenar e recuperar informações [1]. Manter essas informações restritas ao espaço de endereçamento virtual de um processo apresenta problemas, como a perda de dados ao término do processo e a restrição do acesso a apenas aquele processo [1]. Por exemplo, um diretório telefônico  online armazenado no espaço de um processo seria acessível somente por  ele [2].

Para resolver esses desafios, os sistemas de arquivos surgem como uma solução para o armazenamento de informações por longo prazo, atendendo a três requisitos principais [2]:

1.

Deve ser possível armazenar uma quantidade muito grande de informações [2].

2.

As informações devem sobreviver ao término do processo que as está utilizando [2].

3.

Múltiplos processos devem ser capazes de acessá-las ao mesmo tempo [2].

Historicamente, discos magnéticos foram amplamente utilizados para esse armazenamento de longo prazo [3]. Mais recentemente, as unidades de estado sólido (SSDs) ganharam popularidade devido à ausência de partes móveis, o que as torna mais resistentes a falhas [3].

Podemos considerar um disco como uma sequência linear de blocos de tamanho fixo, que suporta duas operações básicas: "Leia o bloco k" e "Escreva no bloco k" [3]. Embora existam outras operações, essas duas são suficientes para o armazenamento de longo prazo [3]. No entanto, acessar informações  diretamente por blocos é muito inconveniente em sistemas grandes com muitos usuários e aplicações [4]. Questões complexas surgem rapidamente, como encontrar informações, impedir que um usuário leia dados de outro e saber quais blocos estão livres [4].

As abstrações de processos (e threads), espaços de endereçamento e arquivos são os conceitos mais importantes relacionados com os sistemas operacionais [4]. Os arquivos são unidades lógicas de informação criadas por processos [4]. Um disco normalmente contém milhares ou milhões de arquivos, cada  um independente dos outros [4]. As informações armazenadas em arquivos  devem ser persistentes, ou seja, não devem ser afetadas pela criação e término de um processo;  um arquivo só deve desaparecer quando seu proprietário o remove  explicitamente [5].

Os arquivos são gerenciados pelo sistema operacional, e a parte do SO que lida com eles é conhecida como Sistema de Arquivos (SA) [5, 6]. O sistema de arquivos oferece uma maneira de armazenar e recuperar informações de modo que isole o usuário dos detalhes de como e onde os dados estão armazenados [7-9]. Ele interage com os controladores de disco para converter  requisições de programas em solicitações de transferência de blocos,  abstraindo o tamanho do bloco para o programador [10-12].

2. Conceitos de Arquivos

2.1. Nomeação de Arquivos

Quando um processo cria um arquivo, ele lhe atribui um nome [7]. Mesmo após o término do processo, o arquivo continua a existir e  pode ser acessado por outros processos utilizando seu nome [7]. As  regras de nomeação variam entre sistemas, mas a maioria dos sistemas  operacionais atuais permite cadeias de uma a oito letras, dígitos e  caracteres especiais [7, 13].

Uma distinção importante é a sensibilidade a maiúsculas e minúsculas:

•

O UNIX (incluindo OS X) faz essa distinção (ex: maria, Maria, MARIA são três arquivos distintos) [13, 14].

•

O MS-DOS não faz essa distinção (ex: todos esses nomes se referem ao mesmo arquivo) [13, 14].

Muitos sistemas operacionais aceitam nomes de arquivos de duas partes separadas por um ponto (ex: prog.c), onde a parte após o ponto é chamada de extensão do arquivo [13-15]. As extensões frequentemente indicam o tipo ou propósito do arquivo [15].

2.2. Estrutura de Arquivos

Arquivos podem ser estruturados de diversas maneiras [15]:

•

Sequência desestruturada de bytes (a) [15]: O sistema operacional não se preocupa com o conteúdo do arquivo;  ele vê apenas bytes. Qualquer significado deve ser imposto por programas em nível de usuário. Essa abordagem oferece a máxima flexibilidade [15].

•

Sequência de registros de tamanho fixo (b) [16]: Cada registro possui alguma estrutura interna. A ideia  fundamental é que a operação de leitura retorna um registro e a operação de escrita sobrepõe ou anexa um registro [16].

•

Árvore de registros (c) [16]: O arquivo consiste em uma árvore de registros, não  necessariamente do mesmo tamanho, cada um contendo um campo chave em uma posição fixa. A árvore é ordenada pelo campo chave, permitindo uma busca rápida por uma chave específica [16].

2.3. Tipos de Arquivos

Muitos sistemas operacionais, como UNIX (incluindo OS X) e Windows, suportam vários tipos de arquivos [14, 17]:

•

Arquivos Regulares: Contêm informações do usuário [14, 17]. Podem ser:

◦

Arquivos ASCII: Consistem em linhas de texto. Em alguns sistemas, cada linha termina com um caractere de retorno de carro (carriage return); em outros, um caractere de próxima linha (line feed) [18].

◦

Arquivos Binários: Significa que não são arquivos ASCII [18]. Listá-los em uma impressora  resultaria em algo incompreensível, pois geralmente possuem uma  estrutura interna conhecida apenas pelos programas que os utilizam [19]. Um exemplo é um arquivo binário executável, que, embora seja uma  sequência de bytes, é executado pelo SO apenas se tiver o formato  apropriado, como as cinco seções de um executável UNIX: cabeçalho, texto, dados, bits de realocação e tabela de símbolos. O cabeçalho geralmente começa com um "número mágico" que o identifica como executável [19, 20].

•

Diretórios: São arquivos de sistema que mantêm a estrutura do sistema de arquivos [14, 17].

•

Arquivos Especiais de Caracteres: Relacionados com entrada/saída e usados para modelar dispositivos de  E/S seriais como terminais, impressoras e redes [14, 17, 18]. Em  sistemas Unix, a interação com controladores de dispositivos é feita  através desses arquivos especiais, criados no diretório /dev usando a chamada mknod [21]. O acesso a eles é sequencial, lendo ou escrevendo uma palavra de cada vez [22].

•

Arquivos Especiais de Blocos: Usados para modelar discos [14, 18]. Também criados no diretório /dev via mknod [21]. Nesses dispositivos, as transferências ocorrem em blocos, permitindo acesso aleatório [22].

Cada entrada no diretório /dev criada com mknod possui dois valores de controle associados: o major number, que indica o controlador de dispositivo (device driver) relacionado à entrada, e o minor number, que diferencia os dispositivos tratados por esse driver [21, 23].

2.4. Acesso aos Arquivos

Os primeiros sistemas operacionais ofereciam apenas um tipo de acesso aos arquivos: sequencial [20]. Nesses sistemas, um processo lia todos os bytes ou registros em  um arquivo em ordem, do início ao fim, sem poder pular ou lê-los fora de ordem [20]. Arquivos sequenciais podiam ser "trazidos de volta" para o  ponto de partida [20]. Esse tipo de acesso era conveniente quando o meio de armazenamento era uma fita magnética [24].

Com o advento dos discos, tornou-se possível ler bytes ou registros de um arquivo fora de ordem ou acessá-los pela chave [24]. Arquivos ou registros que podem ser lidos em qualquer ordem são chamados de arquivos de acesso aleatório [14, 24].

2.5. Atributos de Arquivos (Metadados)

Todo arquivo possui um nome e seus dados [24]. Além disso, os sistemas operacionais associam outras informações aos arquivos, como a data e hora da última modificação e o tamanho do arquivo [25]. Esses itens extras são conhecidos como atributos do arquivo ou metadados [25]. Outros atributos típicos incluem a identificação do usuário associado e listas de permissões que indicam quais usuários e grupos podem realizar quais tipos de acesso (leitura, escrita, ajuste de parâmetros, remoção) [8].

3. Gerenciamento de Diretórios

Para controlar e organizar os arquivos, os sistemas de arquivos utilizam diretórios, também conhecidos como pastas, que são, por si só, arquivos [8, 14, 25]. A forma mais simples de sistema de diretório é ter um diretório-raiz único que contém todos os arquivos [25]. Embora adequado para aplicações  dedicadas muito simples, um único diretório seria impossível para  usuários modernos com milhares de arquivos [26].

A necessidade de agrupar arquivos relacionados levou à adoção de uma estrutura hierárquica, onde os usuários podem ter tantos diretórios quantos forem necessários  [26]. Além disso, em ambientes multiusuário, cada usuário pode ter um  diretório-raiz privado para sua própria hierarquia [26, 27].

É conveniente que arquivos compartilhados apareçam simultaneamente em  diretórios diferentes, pertencentes a usuários distintos [28]. A conexão entre o diretório de um usuário e um arquivo compartilhado é chamada de ligação (link) [29]. Quando ligações são permitidas, o sistema de arquivos se torna um Gráfico Acíclico Orientado (Directed Acyclic Graph – DAG) [29].

3.1. Comandos Comuns de Gerenciamento de Diretórios

Os sistemas operacionais fornecem diversas funções e comandos para criar,  remover, listar, renomear e ajustar atributos de diretórios [30]. Alguns exemplos de comandos e chamadas de sistema incluem [31-34]:

•

mkdir(1), mkdir(2): Cria diretórios vazios [31].

•

rmdir(1), rmdir(2): Remove diretórios vazios [31].

•

cd, chdir(2): Muda o diretório corrente [31, 34].

•

pwd, getcwd(2): Informa o diretório corrente [31, 34].

•

cp: Copia arquivos e diretórios (usa -r para recursivo) [31].

•

mv: Move e/ou renomeia arquivos e diretórios [31].

•

rm: Remove arquivos e diretórios (usa -r para recursivo em diretórios) [31].

•

ln, link(2): Cria links (atalhos) para arquivos e diretórios [31].

•

ls, opendir(3), readdir(3), getdents(2): Lista o conteúdo de diretórios [31-33].

•

closedir(3), rewinddir(3), scandir(3), seekdir(3), telldir(3): Outras funções para manipulação de diretórios [32, 33].

•

chroot(2): Muda a raiz do sistema de arquivos para o processo [34].

3.2. Estrutura Hierárquica no Linux (FHS)

O sistema de arquivos em ambientes Unix é baseado em uma única estrutura hierárquica (árvore) de diretórios, começando pela raiz / [23, 35]. Não existem unidades lógicas como em sistemas Windows (C:,  D:) [35]. Durante o boot, o sistema de arquivos de uma partição é  montado na raiz /, tornando-se acessível [35]. Outros sistemas de arquivos em outras  partições (locais, remotas, fixas, removíveis) também precisam ser  montados em algum subdiretório da árvore [35]. Por exemplo, uma partição separada para áreas de trabalho de usuários pode ser montada em /home, e mídias removíveis são tipicamente montadas em /media/xxx [36].

Para uniformizar os sistemas Linux, existe uma hierarquia de diretórios definida a partir da raiz, conhecida como File System Hierarchy (FHS) [23, 37]. Alguns diretórios principais incluem [23, 37-39]:

•

/: Diretório raiz, concentra toda a estrutura [23, 37].

•

/etc: Arquivos de configuração [23, 37].

•

/bin: Utilitários de uso geral [23, 37].

•

/sbin: Utilitários de administração, alguns restritos ao usuário root [23, 37].

•

/dev: Arquivos especiais que representam dispositivos, criados com mknod [23, 37]. Contêm o major number (driver) e minor number (dispositivo específico) [23].

•

/usr: Hierarquia secundária (inclui /usr/lib para bibliotecas e /usr/include para arquivos de definição) [23, 38].

•

/lib: Bibliotecas compartilhadas essenciais [23, 38].

•

/home: Área de trabalho dos usuários [23, 38].

•

/var: Área para spool de impressão, e-mails e logs [23, 38].

•

/boot: Arquivos para inicialização do sistema [23, 38].

•

/mnt: Diretório para sistemas de arquivos temporários montados [23, 38].

•

/media: Ponto de montagem para mídias removíveis [39].

•

/tmp: Armazenamento temporário [39].

•

/proc: Sistema de arquivos em memória com informações sobre o sistema e seus processos (específico do Linux) [39].

•

/opt: Aplicativos não fornecidos com o sistema [39].

•

/srv: Dados de serviços providos por esse sistema [39].

4. Implementação do Sistema de Arquivos

Implementadores de sistemas de arquivos focam em como arquivos e diretórios são  armazenados, como o espaço em disco é gerenciado e como garantir  eficiência e confiabilidade [27].

Sistemas de arquivos são armazenados em discos [27, 40]. A maioria dos discos pode ser dividida em uma ou mais partições, cada uma contendo um sistema de arquivos independente [27, 40]. O Setor 0 do disco é chamado de MBR (Master Boot Record) e é usado para inicializar o computador [41, 42].

Criar um sistema de arquivos ou "formatar" uma partição significa identificar quantos blocos de armazenamento existem e criar estruturas que  identifiquem os blocos livres e alocados [43]. Blocos alocados são  aqueles que contêm dados de arquivos, portanto, um sistema de arquivos  precisa de uma estrutura de dados que represente arquivos e os blocos de disco que eles utilizam [43]. Dentro de um sistema de arquivos, há  blocos que contêm informações de controle e blocos que contêm dados de arquivos [44].

4.1. Estruturas Essenciais na Partição

Ao criar ou formatar uma partição, são estabelecidas estruturas importantes [42]:

•

Superbloco: Contém todos os parâmetros-chave a respeito do sistema de arquivos e é lido para a memória na  inicialização do computador ou no primeiro acesso ao sistema de arquivos [41, 42].

•

Informações sobre blocos disponíveis: Podem estar na forma de um mapa de bits ou de uma lista de ponteiros [41, 45]. Um disco com n blocos exige um mapa de bits com n bits [45, 46].

•

O restante do disco contém todos os outros diretórios e arquivos [41, 42].

•

Na formatação, pode-se agrupar setores contíguos do disco (ex: 512 bytes) para formar blocos lógicos maiores (ex: 4KB) [22, 44].

4.2. Métodos de Alocação de Blocos

Vários métodos são utilizados para controlar quais blocos de disco pertencem a quais arquivos [47, 48]:

•

Alocação Contígua: O esquema mais simples é armazenar cada arquivo como uma sequência contígua de blocos de disco [47, 48]. Para monitorar a localização dos blocos de um arquivo, basta lembrar de dois números: o endereço em disco do primeiro bloco e o número de blocos no arquivo [47]. O desempenho da leitura é excelente, pois o arquivo inteiro pode ser lido em uma única operação, sem buscas  ou atrasos rotacionais após a busca inicial [48, 49]. No entanto, sua  principal desvantagem é a fragmentação do disco ao longo do tempo [48, 49], onde lacunas de blocos livres aparecem  quando arquivos são removidos, e o disco não é compactado imediatamente  [50].

•

Alocação por Lista Encadeada: Cada arquivo é mantido como uma lista encadeada de blocos de disco [48, 50]. A primeira palavra de cada bloco é usada como um ponteiro para o próximo bloco, e o restante do bloco é reservado para dados [51]. A vantagem é que nenhum espaço é perdido para a fragmentação de disco [48, 51]. As desvantagens incluem o acesso aleatório extremamente lento (pois é preciso seguir a cadeia de ponteiros) e a perda de espaço para  os ponteiros, o que faz com que a quantidade de dados que um bloco pode  armazenar não seja uma potência de dois [48, 51].

•

Alocação por Lista Encadeada Usando uma Tabela na Memória (FAT): Para eliminar as desvantagens da lista encadeada pura, as palavras do ponteiro de cada bloco de disco são colocadas em uma tabela na memória [48, 51, 52]. Essa tabela, chamada FAT (File Allocation Table - Tabela de Alocação de Arquivos), permite seguir a cadeia de blocos de um arquivo rapidamente [53].  Embora melhore drasticamente o acesso aleatório, a principal desvantagem é que a tabela inteira precisa estar na memória o tempo todo para funcionar [48, 53].

•

I-nodes (Index-nodes): Este método associa cada arquivo a uma estrutura de dados chamada i-node, que lista os atributos e os endereços de disco dos blocos do arquivo [48, 53]. A grande vantagem é que o i-node precisa estar na memória apenas quando o arquivo correspondente estiver aberto [48, 54]. Um problema com i-nodes é que cada um tem espaço para um  número fixo de endereços de disco; quando um arquivo cresce além desse  limite, a solução é reservar o último endereço de disco não para um  bloco de dados, mas para o endereço de um bloco contendo mais endereços  de blocos de disco (indireção) [54, 55]. Sistemas do tipo Unix, por  exemplo, mantêm ponteiros diretos e indiretos para blocos de dados em uma estrutura i-node [56].

4.3. Implementação de Diretórios

Os sistemas de arquivos mantêm vários atributos para cada arquivo, que devem ser armazenados em algum lugar [55].

•

Uma possibilidade é armazenar os atributos diretamente na entrada do diretório [55]. Nesse design simples, um diretório consiste em uma lista de  entradas de tamanho fixo, uma por arquivo, contendo o nome do arquivo  (de tamanho fixo), uma estrutura dos atributos do arquivo e um ou mais  endereços de disco (até um máximo) indicando onde estão os blocos de  disco [28, 55].

•

Para sistemas que usam i-nodes, outra possibilidade é armazenar os atributos nos próprios i-nodes, em vez de nas entradas do diretório [28]. A entrada do diretório então  pode ser mais curta, contendo apenas o nome do arquivo e o número do  i-node [28].

4.4. Gerenciamento e Otimização de Sistemas de Arquivos

O gerenciamento de espaço em disco é uma preocupação importante [29]. Para armazenar um arquivo de n bytes, duas estratégias gerais são possíveis: alocar n bytes consecutivos (alocação contígua) ou dividir o arquivo em uma  série de blocos (não necessariamente contíguos) [57]. Essa escolha é  similar à segmentação pura versus paginação no gerenciamento de memória  [57].

Se a opção for por blocos de tamanho fixo, é preciso decidir qual será o tamanho do bloco [57]. Candidatos óbvios são o setor, a trilha e o cilindro do disco [57]. Em um sistema de paginação, o tamanho da página também é um argumento importante [46].

Uma vez escolhido o tamanho do bloco, a próxima questão é como monitorar os blocos livres [46]. Dois métodos são amplamente usados [45, 46]:

1.

Lista Encadeada de Blocos de Disco: Cada bloco contém tantos números de blocos livres de disco quantos couberem nele [45, 46].

2.

Mapa de Bits: Um bit para cada bloco do disco, indicando se está livre ou ocupado [45, 46]. Um disco com n blocos exige um mapa de bits com n bits [46].

5. Desempenho e Caching do Sistema de Arquivos

O acesso ao disco é muito mais lento do que o acesso à memória [58]. Se apenas uma única palavra for necessária, o acesso à memória  pode ser um milhão de vezes mais rápido que o acesso ao disco [58].  Devido a essa diferença, muitos sistemas de arquivos foram projetados  com otimizações para melhorar o desempenho [58].

5.1. Buffering e Caching no SO

O Sistema Operacional é responsável por interagir com os controladores de disco, convertendo as requisições de programas em solicitações para  transferências de blocos, o que faz parte da abstração de arquivos como  sequências de bytes [10-12]. O programador pode solicitar quantidades de bytes adequadas às suas aplicações, independentemente dos tamanhos dos  blocos nos discos [10].

•

Leitura: Se um programa solicita a leitura de apenas alguns bytes (menos que o tamanho de um bloco), o sistema de arquivos deve ler um bloco inteiro do disco e guardá-lo na memória, em uma área de buffer ou cache [12, 59]. Dali, os bytes solicitados são copiados para a área de  memória indicada pelo programa [59]. Numa próxima operação de leitura,  o(s) bloco(s) necessário(s) já pode(m) estar no cache, resultando em uma cópia mais rápida [12, 59, 60]. Requisições também podem envolver a  transferência de dados de vários blocos, que são trazidos para áreas de  memória do SO e copiados para o espaço de endereçamento da aplicação  [59].

•

Escrita: Se o programa solicita a gravação de poucos bytes, o sistema de  arquivos não pode gravá-los diretamente no disco [61]. É comum que se  espere até que um bloco completo seja preenchido ou até que o programa decida fechar o arquivo [61]. O SO pode gravar um bloco inteiro, indicando quanto dele está efetivamente em uso (isso é chamado de fragmentação no contexto da escrita em blocos incompletos) [61]. Na escrita sobre  arquivos existentes, o sistema de arquivos pode primeiro ler um bloco do disco, modificar os bytes solicitados e só então gravar o bloco de  volta [61].

A importância de um mecanismo de cache do sistema de arquivos, mantido pelo SO em memória, é clara [60]. O controle do cache é uma atividade complexa [60]. Se há  bastante memória RAM disponível, os sistemas de arquivos geralmente  utilizam um espaço considerável para o cache [60]. Técnicas comuns  incluem:

1.

Cache de blocos (ou cache de buffer): A técnica mais comum para reduzir acessos ao disco [58, 62].

2.

Leitura antecipada de blocos (pre-fetching): Tenta transferir blocos para o cache antes que sejam necessários, aumentando a taxa de acertos [60, 62].

3.

Redução do movimento do braço do disco: Coloca blocos que têm maior chance de serem acessados em sequência  próximos uns dos outros, preferencialmente no mesmo cilindro, para  diminuir o movimento do braço do disco (em HDDs) [12, 62, 63].

5.2. Escrita Adiada (Delayed Write) e Consistência

Para responder rapidamente às operações de gravação, o SO pode aceitar os pedidos mas retardar a gravação efetiva nos blocos do disco até um momento oportuno [12, 60, 64]. Essa estratégia é chamada de delayed write [60, 64]. Os dados solicitados são copiados para buffers internos no  espaço do kernel antes da gravação efetiva em disco, o que melhora o  tempo de resposta da aplicação [64]. O SO tipicamente realiza a gravação em disco em ocasiões específicas, como no fechamento de um arquivo, ou  quando há uma chamada explícita para isso, ou através de salvamentos  periódicos [65]. Em sistemas Linux, o parâmetro dirty_expire_centisecs em /proc/sys/vm/ controla o tempo (em centésimos de segundo) que blocos alterados permanecem na memória antes de serem salvos no disco [65, 66].

Uma consequência do adiamento das gravações é que, em caso de falta de energia, os dados no cache podem não ter sido gravados no disco, e os arquivos podem ficar inconsistentes [12, 63, 67]. Por isso, é preciso informar o SO antes de remover dispositivos de armazenamento USB, permitindo que o SO grave quaisquer dados pendentes [12, 63].

Para tornar os sistemas de arquivos menos suscetíveis a falhas, alguns sistemas operacionais usam mecanismos de controle de transações nas operações de escrita, comumente chamados de journaling [12, 68]. Esses mecanismos gravam informações sobre as operações  pendentes no disco, permitindo a recuperação do estado correto do  sistema em caso de falha [12, 68].

De todo modo, usando as chamadas sync(2) e fdatasync(2), o programa pode solicitar ao SO que salve em disco as informações de um arquivo (dados + metadados, ou só dados, respectivamente) que foram alteradas em memória [33, 68, 69].

Caso a aplicação deseje uma garantia de escrita imediata, é possível ajustar o modo de operação de arquivos individuais para escrita síncrona [66]. Com a flag O_SYNC na chamada open(2), qualquer write() nesse descritor de arquivo bloqueará o processo chamador até que os  dados tenham sido fisicamente gravados no hardware [12, 66, 70]. Para  arquivos já abertos, a chamada fcntl(2) com o parâmetro F_SETFL pode ajustar essa flag [70, 71].

6. Operações de Entrada/Saída (E/S)

A manipulação de arquivos em C pode ocorrer diretamente através das chamadas de sistema ou usando a estrutura FILE, provida pela biblioteca C [72]. Quem realmente faz a manipulação de arquivos é o sistema operacional, e a estrutura FILE é apenas uma interface para um arquivo do SO [72].

6.1. Comparativo open vs. fopen

| Característica     | open (Chamada de Sistema) [69, 73]                           | fopen (Função da Biblioteca C) [69, 73]                      |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Natureza           | Chamada de sistema [69, 73].                                 | Função da biblioteca C [69, 73].                             |
| Buffering          | Não provê buffering diretamente ao programa; o SO lida com isso [73]. | Provê E/S bufferizada na área de dados da memória do programa [69, 73, 74]. |
| Desempenho         | Otimizado pelo SO.                                           | Pode prover melhor desempenho em acessos sequenciais devido ao buffering transparente [69, 73]. |
| Portabilidade      | Dependente do SO [73].                                       | Chamada C padronizada, tornando o programa independente do SO [69, 73]. |
| Valor de Retorno   | Um número inteiro, que é o índice do arquivo no vetor de arquivos abertos do processo (descritor de arquivo) [69, 75]. | Um ponteiro para uma estrutura FILE (FILE *) [69, 75].       |
| Funções Associadas | read, write, lseek, close, unlink, fcntl, dup2, fsync, fdatasync, truncate, ftruncate, fstat, stat, lstat, umask [33]. | fread, fwrite, fseek, fsetpos, rewind, getpos, ftell, fclose, fscanf [33]. |
| Uso com formatado  | Geralmente requer parsing manual.                            | Pode ser acessada com funções como fscanf e outras que tratam o formato dos dados lidos [75]. |

A função fread() internamente utiliza os serviços da chamada de sistema read() [76]. Mesmo que o programa solicite um número pequeno de bytes, fread faz solicitações ao SO usando tamanhos de requisição múltiplos do tamanho dos blocos de disco usados no sistema de arquivos (ex: 4KB) [69, 76, 77].

6.2. Abertura de Arquivos

Antes de ser manipulável, um arquivo deve ser criado ou aberto [78]. A chamada creat(2) é usada para criar arquivos, enquanto open(2) pode ser usada tanto para abrir um arquivo existente quanto para criar um novo [33, 78].

A especificação do arquivo é feita a partir de seu nome, que pode ser um caminho completo a partir da raiz (/) ou um caminho relativo ao diretório corrente do processo [56, 79]. O diretório corrente pode ser consultado com getcwd() e ajustado com chdir() [34, 78].

Ao abrir um arquivo, o SO gera uma nova entrada no vetor de arquivos abertos do processo corrente (files_struct) [80-83]. Para cada arquivo aberto, o SO mantém informações como um i-node lógico (com informações obtidas do i-node efetivo em disco) [80-82]. Para  arquivos em diferentes formatos de sistema de arquivos, campos da  estrutura de controle do disco podem ser mapeados para os campos do  i-node lógico [80].

Em sistemas Linux, para possibilitar a manipulação de arquivos em diferentes sistemas de arquivos, usa-se uma abstração do sistema de arquivos chamada Virtual File System (VFS) [84-87]. Independentemente do tipo de sistema de arquivos, para cada  arquivo aberto, as informações no vetor de arquivos incluem um ponteiro para um vetor de funções de manipulação de arquivo (file_operations) [82, 84, 88]. Esse ponteiro é ajustado na abertura do arquivo,  apontando para o vetor de funções apropriado para o sistema de arquivos  (ex: ext4, nfs, ntfs) [82, 84]. Existem também funções para manter uma interface uniforme  para leitura de informações globais do sistema de arquivos em disco (super_block / super_operations) [84, 89].

Ao receber um pedido de abertura de arquivo, o SO usa o nome especificado  (path) para localizar as informações do arquivo no sistema de arquivos  [56]. Dados relevantes sobre o arquivo são carregados na memória  (incluindo informações sobre blocos de dados), mas os conteúdos desses  blocos só são carregados sob demanda [67].

A chamada openat(2) opera de forma similar a open(), mas utiliza o argumento dirfd em conjunto com pathname para interpretar caminhos relativos em relação a um descritor de  diretório específico, em vez do diretório de trabalho corrente [90, 91]. Isso permite que uma aplicação evite condições de corrida que poderiam ocorrer se um componente do caminho do diretório fosse alterado em paralelo com a chamada open() [69, 80].

6.3. Operações de Leitura e Escrita

•

read(2) e write(2): São as chamadas de sistema fundamentais para leitura e escrita de dados [33, 69].

•

lseek(2): Permite reposicionar o offset corrente dentro de um arquivo, ou seja, onde a próxima operação de leitura/escrita começará [33, 69].

•

close(2): Fecha um descritor de arquivo [33, 69].

•

unlink(2): Remove um arquivo [33, 69].

•

truncate(2) / ftruncate(2): Alteram o tamanho de um arquivo [33, 69]. Alterações no tamanho do  arquivo podem ser feitas na estrutura de controle na memória e  posteriormente gravadas no disco [67].

•

fcntl(2): Permite ajustar diferentes parâmetros sobre a operação de um arquivo após sua abertura, utilizando diversos  comandos (cmds) [33, 92]. Exemplos de flags que podem ser alteradas com F_SETFL incluem O_APPEND, O_ASYNC, O_DIRECT, O_NOATIME, O_NONBLOCK, e O_SYNC [70, 71, 93].

6.4. Operações de E/S Assíncronas (AIO)

A interface POSIX Asynchronous I/O (AIO) permite que aplicações iniciem uma ou mais operações de E/S que são executadas assincronamente (em segundo plano) [94]. A aplicação pode escolher ser notificada da conclusão da operação de E/S de diversas maneiras: por entrega de um sinal, por instanciação de uma thread, ou sem notificação alguma [94].

•

aio_read(): Esta função enfileira a requisição de E/S descrita pelo buffer apontado por aiocbp [94]. É a análoga assíncrona de read(2) [94]. Os argumentos de read(fd, buf, count) correspondem, em ordem, aos campos aio_fildes, aio_buf, e aio_nbytes da estrutura aiocbp [94].

•

No macOS, aio_read() lê aiocbp->aio_nbytes do descritor aiocbp->aio_fildes, começando no offset aiocbp->aio_offset, para o buffer aiocbp->aio_buf [95]. A chamada retorna imediatamente após a requisição ser enfileirada; a leitura pode ou não ter sido concluída quando a chamada retorna [95, 96]. O argumento aiocbp->aio_lio_opcode é ignorado por aio_read() [95]. Os dados são lidos a partir da posição absoluta aiocbp->aio_offset, independentemente do offset do arquivo [97]. Após a chamada, o valor do offset do arquivo é não especificado [97].

•

Estrutura aiocb: Contém campos como aio_fildes (descritor de arquivo), aio_offset (offset do arquivo), aio_buf (local do buffer), aio_nbytes (tamanho da transferência), aio_reqprio (prioridade da requisição), aio_sigevent (método de notificação/número e valor do sinal), e aio_lio_opcode (operação, usado apenas por lio_listio()) [97].

•

Verificação de Conclusão: A função aio_error(3) é usada para testar o status de erro de uma requisição AIO [96, 98].

◦

EINPROGRESS: Se a requisição ainda não foi concluída [99].

◦

ECANCELED: Se a requisição foi cancelada [99].

◦

0: Se a requisição foi concluída com sucesso [99].

◦

Um número de erro positivo: Se a operação AIO falhou (o mesmo valor que seria armazenado em errno para uma chamada síncrona) [99].

•

Obtenção do Status de Retorno: O status de retorno de uma operação de E/S concluída pode ser obtido por aio_return(3) [96, 98].

•

Notificação Assíncrona: Pode ser obtida configurando aiocbp->aio_sigevent adequadamente [96].

•

Outras funções AIO incluem aio_write, aio_cancel, aio_error, aio_return e aio_fsync [98, 99].

6.5. Leitura Não Bloqueante (O_NONBLOCK)

Por padrão, as operações de leitura em arquivos são bloqueantes [100]. Isso significa que a aplicação solicitante da operação ficará  bloqueada até que os dados estejam disponíveis, o fim do arquivo seja  atingido ou ocorra um erro [100].

Este modo de operação pode ser ajustado na abertura do arquivo ou enquanto ele permanece aberto [100].

•

Na abertura: Usando a flag O_NONBLOCK na chamada open(2) [92, 100]. Quando possível, o arquivo é aberto em modo não bloqueante, e nem open() nem operações subsequentes no descritor de arquivo causarão o processo a esperar [92].

•

Enquanto aberto: Usando a chamada fcntl(2) com o comando F_SETFL e o parâmetro O_NONBLOCK [92, 93]. Se nenhum dado estiver disponível para uma chamada read(), ou se uma operação write() bloquearia, a chamada retorna -1 e a variável errno é ajustada com o valor EAGAIN [93, 101].

•

A flag O_ASYNC em fcntl(2) habilita o sinal SIGIO para ser enviado ao grupo do processo quando a E/S for possível (ex: dados disponíveis para leitura) [101].

O fato de as operações de leitura não serem bloqueantes tem implicações  na lógica da aplicação, exigindo que o programa verifique o valor de  retorno e errno para lidar com a ausência de dados [101, 102].

6.6. Monitoramento de E/S (select)

Em vez de tentar realizar diretamente as operações de E/S, é possível consultar o estado dos descritores antes [103]. Isso pode ser feito com as chamadas select(2) e pselect(2) [103].

select() permite determinar grupos de descritores de arquivo (ou sockets) que se deseja monitorar à espera da disponibilidade para leitura, escrita ou de mudanças de estado [103-105]. Um valor de timeout pode ser passado como parâmetro, indicando o tempo máximo de espera [103].

select() monitora três conjuntos independentes de descritores de arquivo [105]:

•

readfds: Para ver se caracteres estão disponíveis para leitura (ou se read(2) não bloquearia, incluindo fim de arquivo) [105].

•

writefds: Para ver se há espaço disponível para escrita (embora uma grande escrita ainda possa bloquear) [105].

•

exceptfds: Para exceções [105].

Após o retorno da chamada, os conjuntos são modificados para indicar quais  descritores realmente mudaram de status [105]. Qualquer um dos três  conjuntos pode ser NULL se não houver descritores para monitorar para a classe de eventos correspondente [105].

6.7. E/S Vetorizada (readv, writev)

As chamadas de sistema readv() e writev() permitem leitura e escrita usando múltiplos buffers [104, 106]. Elas são conhecidas como operações de scatter/gather I/O [107].

•

readv(): Lê iovcnt buffers do arquivo associado ao descritor de arquivo fd para os buffers descritos por iov ("scatter input") [107]. Funciona como read(2), mas múltiplos buffers são preenchidos [107].

•

writev(): Escreve iovcnt buffers de dados descritos por iov para o arquivo associado ao descritor de arquivo fd ("gather output") [107]. Funciona como write(2), mas múltiplos buffers são escritos [107].

Ambas as funções utilizam uma array de estruturas iovec, onde cada struct iovec contém um ponteiro iov_base para o endereço inicial do buffer e iov_len para o tamanho da memória apontada por iov_base [107, 108]. Outras variações incluem preadv, pwritev, preadv2, pwritev2 que permitem especificar um offset e flags adicionais [106].

6.8. Mapeamento de Memória (mmap)

Outra forma de acessar arquivos é através de seus mapeamentos no espaço de memória virtual do processo [69, 109]. Um exemplo desse mapeamento é realizado pelo carregador do programa (loader / exec()), que associa as áreas do arquivo executável e das bibliotecas  compartilhadas necessárias a áreas de memória dentro do espaço de  endereçamento do processo [109].

A chamada mmap() permite fazer diferentes tipos de mapeamentos de arquivos em memória  [109]. Pode-se, por exemplo, abrir um arquivo e pedir ao SO para mapear  seus offsets para alguma área de memória [109]. A partir daí, o acesso aos dados dessa região mapeada do arquivo pode ser feito como se fosse  uma estrutura localizada por um ponteiro de memória [109].

Um ponteiro é associado à área mapeada, e o SO faz os ajustes para que a estratégia de paginação seja utilizada para a busca das partes do arquivo no disco que são necessárias na memória [110]. Para arquivos muito grandes, pode não ser possível alocar espaços na memória para seus mapeamentos  completos, cabendo à aplicação determinar os espaços a serem mapeados  conforme sua demanda [110].

As funções relacionadas são:

•

mmap(): Mapeia o arquivo na memória virtual [110].

•

munmap(): Desfaz o mapeamento da memória [110].

•

msync(): Sincroniza as alterações na memória mapeada de volta para o disco [111].

7. Segurança e Controle de Acesso

A segurança e o controle de acesso às informações do sistema de arquivos em sistemas Unix são baseados na atribuição de privilégios a um proprietário e um grupo associados a cada objeto armazenado [8, 112, 113].

7.1. Permissões Tradicionais (rwx)

O comando ls -l exibe informações sobre os direitos de acesso a arquivos e diretórios em 10 colunas [112, 113]:

•

A coluna mais à esquerda indica o tipo da entrada no sistema de arquivos: d (diretório), l (link), b (dispositivo de bloco), c (dispositivo de caractere), s (socket), p (pipe) [112, 114].

•

Seguem-se 9 colunas de permissões, divididas em 3 grupos de 3 permissões [112-114]:

◦

rwx______: Direitos do proprietário (owner) [114].

◦

____rwx___: Direitos do grupo [114].

◦

_______rwx: Direitos dos outros usuários (não proprietário ou grupo) [114].

Permissões de arquivos [112, 114]:

•

r (read): Leitura.

•

w (write): Escrita.

•

x (execute): Execução.

Permissões de diretórios [112, 114]:

•

r: Permite listar o conteúdo do diretório (ls).

•

w: Permite criação, remoção e renomeação de arquivos dentro do diretório.

•

x: Permite entrar no diretório (cd), tornando-o o diretório corrente.

7.2. Comandos de Gerenciamento de Permissões

•

chown: Altera o proprietário de arquivos e diretórios [112, 115]. Somente o superusuário (root) pode executá-lo [112, 115].

•

chgrp: Altera o grupo associado a arquivos e diretórios [112, 115]. Usuários podem alterar  apenas grupos de arquivos de sua propriedade, e apenas para grupos aos  quais pertencem [112, 115].

•

chmod: Ajusta os direitos de acesso [112, 115]. Apenas root e o proprietário do arquivo/diretório podem alterar suas permissões [112, 115]. Pode ser usado com notação simbólica (u+s, o-w) ou octal (ex: chmod 754 arq -> rwxr-xr--) [112, 116, 117]. Na notação octal, 3 dígitos são usados (proprietário,  grupo, outros), onde cada dígito (0-7) representa 3 bits (rwx) [116,  117].

7.3. Permissões Padrão e umask

Por padrão, um arquivo recém-criado recebe permissões 666 (leitura e escrita para todos), e um diretório 777 (total para todos) [117]. Contudo, isso é modificado por uma configuração chamada umask, que define quais privilégios serão removidos (suprimidos) dos novos arquivos e diretórios criados [112, 117, 118]. O valor octal de umask é complementar ao valor dos privilégios desejados [118]. Por exemplo, umask 022 remove a permissão de escrita para membros do grupo e para outros usuários, sendo essa uma máscara padrão comum [118]. Se umask for 027, membros do grupo não terão permissão de escrita, e os demais usuários não terão permissão alguma [119]. O comando umask é normalmente ajustado nos arquivos de configuração do shell [118].

7.4. Atributos Especiais (setuid, setgid, sticky bit)

Independentemente do proprietário de um arquivo executável, processos iniciados a partir  dele geralmente preservam a identidade do usuário que os inicia [119].  No entanto, é possível forçar a manutenção da identidade do usuário (setuid) ou grupo (setgid) do arquivo nos processos criados a partir dele, o que é útil para  programas que precisam de privilégios especiais (tipicamente root) [120, 121].

•

setuid (u+s ou 4xxx): Quando aplicado a um executável, o processo resultante herda o UID do proprietário do arquivo, não do usuário que o invocou [120, 122]. Por exemplo, o programa ping necessita de privilégio de root para criar um socket raw [122]. Programas setuid geralmente diminuem seus privilégios após a parte inicial da execução que exige privilégios [122].

•

setgid (g+s ou 2xxx):

◦

Em executáveis: O processo herda o GID do grupo do arquivo [120, 122].

◦

Em diretórios: Novos arquivos criados nesse diretório herdam o grupo associado ao diretório, em vez do grupo padrão do usuário que os cria [120, 123].

•

sticky bit (+t ou 1xxx): Atribuído a um diretório (ex: /tmp), permite que qualquer usuário crie arquivos, mas somente o proprietário do arquivo ou o root pode remover/renomear os arquivos dentro desse diretório [120, 123, 124]. Isso preserva os direitos de  acesso a arquivos em diretórios compartilhados, evitando exclusões  acidentais por outros usuários [120, 124].

Esses ajustes são feitos com chmod, utilizando bits de permissões especiais [121, 125].

7.5. POSIX ACLs (Access Control Lists)

POSIX ACLs são um mecanismo que permite definir permissões de acesso de forma mais refinada a arquivos e diretórios [126].

•

Um objeto pode ter uma Access ACL associada, que governa o acesso discricionário a ele [126].

•

Um diretório pode ter uma Default ACL, que governa a Access ACL inicial para objetos criados dentro dele [126, 127].

Uma ACL consiste em um conjunto de ACL entries [128]. Cada entrada especifica as permissões (leitura, escrita,  execução/busca) para um usuário individual ou grupo de usuários [128].  Uma entrada ACL contém um entry tag type, um optional entry tag qualifier, e um conjunto de permissões [128].

•

Comandos: As permissões são definidas com o utilitário setfacl e consultadas com getfacl [128-130].

•

Suporte no Sistema de Arquivos: É preciso verificar se o sistema de arquivos foi montado com suporte a ACL (usando tune2fs) [128, 131]. Caso contrário, pode ser remontado com a opção acl (ex: sudo mount -o remount -o acl /dev/sda1) e tornado persistente em /etc/fstab [131].

•

Máscara (mask): Uma máscara associada às permissões de um arquivo indica as permissões máximas que podem ser atribuídas a usuários nomeados, grupos nomeados e ao grupo proprietário sobre esse arquivo, mas não afeta as permissões do proprietário do arquivo e do grupo "outros" [127, 129].

•

Herança: ACLs permitem que um valor default de ACL seja atribuído para um diretório, de forma que essas permissões sejam válidas por padrão para todos os  arquivos e subdiretórios criados nesse diretório [127, 130].

8. Gerenciamento de Usuários e Grupos

Em sistemas Unix, as informações sobre usuários e grupos locais são mantidas em arquivos específicos no diretório /etc [132-134].

8.1. Arquivos de Configuração de Usuários e Grupos

•

/etc/passwd: Contém informações das contas de usuários locais [132-134]. Todos têm permissão de leitura a este arquivo [135].

◦

Cada linha (entrada de usuário) é organizada em colunas, separadas por : [136]: 1. Login: Nome de usuário para autenticação [136]. 2. Senha: Comumente contém x, indicando que a senha criptografada está em /etc/shadow [137]. 3. Identificador (UID): ID único do usuário, usado pelo SO para controlar acesso a recursos (arquivos, processos) [137, 138]. 4. Grupo (GID): ID do grupo base do usuário, que será associado por padrão a arquivos e processos gerados [137]. 5. Descrição: Informações sobre o usuário (nome completo, sala, telefone, etc.) [139]. 6. Área de trabalho (Home Directory): Diretório padrão de trabalho do usuário, geralmente com permissões de acesso exclusivas [139]. 7. Shell: Programa a ser executado após o login (comumente o shell padrão) [139]. Por segurança, algumas contas podem ter /sbin/nologin [139].

•

/etc/group: Contém informações sobre os grupos de usuários locais [132-134, 140].

◦

Cada linha (entrada de grupo) contém campos separados por : [140]: 1. Nome do grupo. 2. x (ou senha criptografada, obsoleta/não usada). 3. GID: Número identificador do grupo, usado em mecanismos de permissão [141]. 4. Lista de usuários, separados por vírgula, que pertencem a esse grupo [141].

•

/etc/shadow: Armazena os valores das senhas criptografadas com acesso restrito (permissões ----------) [132-135]. O proprietário (root) sempre pode acessá-lo [135].

◦

O objetivo é retirar as senhas de /etc/passwd para evitar exposição [134, 137].

◦

Comandos pwconv e pwunconv permitem separar ou mesclar informações entre passwd e shadow [134, 136].

◦

Contém informações adicionais de controle sobre expiração de senhas [134, 142]: * Login. * Senha criptografada: Valor que inclui o algoritmo de criptografia, um "sal" (valor aleatório) e o resultado da criptografia do sal com a senha [132, 142, 143]. O "sal" garante que senhas idênticas resultem em valores criptografados diferentes, impedindo ataques de dicionário e tabelas arco-íris [132, 143-146]. * Data da última alteração de senha. * Número de dias até que a senha POSSA ser alterada (min_days). * Número de dias até que a senha TENHA que ser alterada (max_days). * Número de dias de aviso antes da expiração. * Número de dias de validade da conta após a expiração da senha. * Data de expiração da conta. * Campo reservado [142, 147].

◦

A senha real não é salva [132, 144]. Na autenticação, o SO gera a criptografia da senha  fornecida com o "sal" armazenado e compara o resultado com o valor salvo [132, 144].

•

/etc/default/useradd: Contém informações padrão para a criação de contas de usuário com useradd [148, 149].

•

/etc/skel: Mantém arquivos de configuração que são copiados para a área de usuário na criação de sua conta [148].

•

/etc/login.defs: Armazena informações sobre restrições de logins e senhas (ex: PASS_MAX_DAYS, PASS_MIN_DAYS, PASS_WARN_AGE, PASS_MIN_LEN) [149-151].

8.2. Comandos de Gerenciamento de Usuários e Grupos

•

useradd: Cadastra um novo usuário [132, 148, 152].

•

userdel: Remove as informações de uma conta de usuário [132, 141, 152]. A opção -r remove também o diretório do usuário [141].

•

usermod: Altera atributos de conta [132, 152].

•

groupadd: Adiciona um grupo [132, 152].

•

groupdel: Remove um grupo [132, 152].

•

groupmod: Modifica informações de um grupo existente [132, 152].

•

passwd: Altera a senha de um usuário [132, 152].

•

gpasswd: Modifica senha, administrador e membros de grupos [140, 152].

•

chage: Modifica atributos associados à expiração da senha de um usuário [148, 151]. Permite consultar (-l) e ajustar configurações como data da última alteração, expiração, etc. [151, 153].

•

chfn: Altera informações sobre o nome do usuário (exibidas por finger) [148].

•

chsh: Altera o shell de login do usuário [148].

•

id: Apresenta informações sobre o UID, grupo base e todos os grupos a que um usuário pertence [154].

•

whoami / who am i: Mostra o login_name efetivo do usuário corrente [154].

•

groups: Informa os grupos a que pertence o usuário corrente [154].

•

who, w, users: Mostram quem está usando o sistema [154].

•

finger: Programa para pesquisa de informações sobre usuários [154].

Contas com UIDs inferiores a 1000 são usadas como contas "de serviço", para execução de programas servidores, o que melhora a segurança do sistema [155].

8.3. Comunicação entre Usuários

•

write: Escreve uma mensagem para outro usuário conectado ao sistema [156].

•

wall: Envia uma mensagem para o terminal de todos os usuários conectados [156].

•

mesg: Controla a escrita de mensagens no terminal (mesg y ou mesg n) [156].

•

talk: Programa para conversa interativa (chat) com outros usuários [156].

9. Gerenciamento de Privilégios e Autenticação

Em sistemas Unix, apenas o usuário root, com UID 0, possui privilégios totais e pode realizar certas operações no sistema  [157, 158]. Embora o Linux possua um mecanismo mais refinado de controle de privilégios chamado capabilities, ainda é comum que apenas root realize certas operações [157].

Administradores de sistema frequentemente precisam executar comandos específicos com privilégio de root [159]. Em vez de fazer login como root, existem comandos para mudar o privilégio da sessão de shell corrente ou obter privilégio apenas para executar o comando necessário [159].

9.1. Comando su (Switch User)

O comando su serve para mudar a identificação do usuário na sessão de shell corrente [157, 159]. Se nenhum usuário for especificado, assume-se a tentativa de acesso à conta de root [159]. Em ambos os casos, é preciso saber a senha do usuário especificado [159].

Ao ser executado, su solicita a senha do root (ou do usuário alvo) e, se fornecida corretamente, o usuário passa a  executar comandos como o usuário especificado [160]. O parâmetro - (menos) com su indica que ajustes de uma sessão de login completa serão feitos, executando as configurações em arquivos como .bash_login, .bash_profile, .profile do diretório home do usuário alvo [160].

Para limitar quais usuários podem executar su, pode-se configurar o arquivo /etc/pam.d/su para que apenas membros do grupo wheel possam usar o comando [161]. Autorizações concedidas ou negadas são registradas nos arquivos de log do sistema (/var/log/secure ou /var/log/auth.log) [161]. O prompt do shell muda (ex: # para root em vez de $) [162]. Para encerrar a sessão como outro usuário, usa-se exit [162].

9.2. Comando sudo (SuperUser DO)

Ao invés de transformar a sessão de shell corrente em uma sessão de root, o comando sudo permite a concessão de privilégio para a execução de comandos específicos, um comando de cada vez [157, 163]. Assim, usa-se sudo comando, e se autorizado, apenas o comando especificado é executado com  privilégios de superusuário, retomando-se o privilégio do usuário após a execução [163].

A configuração de quais usuários e membros de quais grupos podem executar quais comandos usando sudo é feita através do arquivo /etc/sudoers [157, 164]. Para validar a autorização, a senha do próprio usuário que está executando sudo (não a do root) deve ser informada [164].

Autorizações são registradas nos arquivos de log [165]. Por padrão, autorizações  bem-sucedidas permitem a execução de outros comandos autorizados com sudo por 5 minutos sem requerer nova senha [165]. Usuários cadastrados como "Administradores" geralmente fazem parte do grupo wheel, que é autorizado a usar sudo por padrão [165]. A edição do arquivo /etc/sudoers deve ser feita com visudo, que previne erros de edição simultânea e verifica a sintaxe [165]. A sintaxe do sudoers define qual usuário (ou membro de grupo) pode executar qual comando a partir de qual computador [166]. Ex: root ALL = (ALL) ALL ou %wheel ALL = (ALL) ALL permitem que root e membros de wheel executem qualquer comando de qualquer host [166].

9.3. Política de Senhas

A utilização de senhas apropriadas é fundamental para a segurança do  sistema [166]. Aspectos dos requisitos de senhas e autenticações são  configurados por arquivos como /etc/pam.d/common-password (para comprimento mínimo, ex: minlen=8) e /etc/login.defs (para tempo de expiração, mínimo/máximo de dias entre mudanças, aviso de expiração) [150, 151].

O comando chage pode ser usado pelo root para consultar e ajustar as configurações de expiração de senhas dos usuários [148, 151, 153].

9.4. Autenticação de Usuários a Partir de Servidores de Rede

Além de usuários configurados localmente, sistemas Unix permitem a autenticação de usuários a partir de servidores remotos utilizando protocolos e serviços como LDAP, NIS, Active Directory [153]. Geralmente, é necessário que os diretórios de trabalho desses usuários sejam montados localmente a partir de um servidor que os compartilha, tipicamente via protocolo NFS [167].