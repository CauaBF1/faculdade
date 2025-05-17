# Mecanismos de IPC

Usando o modo de endereçamento protegido e o mecanismo de memória virtual do processador, o SO consegue prover a separação dos espaços de endereçamento dos processos que executam no mesmo sistema computacional. Isso é bom pois previne interferências entre processos.

Por outro lado, ao criar-se uma aplicação que divida suas atividades entre vários processos, pode ser desejável a comunicação entre eles. 

Para processos que estão em computadores (nós) separados, a comunicação via passagem de mensagens em rede é a saída. Por outro lado, para processos sob o comando do mesmo SO, no mesmo nó e, portanto, compartilhando a mesma memória física, é possível realizar a comunicação de maneira mais eficiente.

Uma solução é usar o sistema de arquivos, já que a visão da árvore de diretórios é normalmente a mesma para todos os processos no mesmo nó (exceto se forem usadas árvores de diretórios diferentes, definidas com a chamada chroot, ou namespaces distintos). Assim, para comunicarem-se, basta que os processos escolham um arquivo num diretório visível por todos para que um escreva e outro leia dados dali. 

A comunicação via arquivos pode não ser eficiente, contudo, uma vez que qualquer transferência entre os processos vai envolver uma série de etapas:

(escrita)

    cópia dos dados da área de memória do processo (user space) para um espaço na área de memória do SO (buffers do sistema de arquivos - kernel space);
    cópia dos dados da área de memória do SO para o sistema de arquivos, o que envolve o auxílio de um controlador de disco, e.g.

(leitura)

    [se dados não estiverem na memória] cópia dos dados do disco para buffers na área de memória do SO;
    cópia da área de memória do SO (kernel space) para o espaço de memória do processo (user space)

Além de arquivos, há serviços do SO que podem permitir a comunicação entre processos usando estruturas baseadas em memória apenas. Diversas estruturas podem ser usadas para isso: pipes e fifos, filas de mensagens, semáforos, sockets (unix domain) e arquivos mapeados em memória. Algumas dessas estruturas são consideradas mecanismos clássicos de IPC, como as filas de mensagem e os semáforos. 

Em todos esses casos, informações sendo enviadas entre processos envolvem ainda a cópia de dados do user space para kernel space, na escrita, e a cópia de dados do kernel space para o user space na leitura. 

Como melhoria extrema para a comunicação entre processos, o SO permite o compartilhamento explícito de áreas de dados entre eles. 

**Para tanto, há chamadas de sistema que tratam da alocação de áreas de memória compartilhadas. Um processo pode então pedir ao SO para associar uma variável (ponteiro) à área compartilhada criada. Esse ponteiro é ajustado para apontar para o início de uma página lógica não mapeada pela tabela de páginas. Após isso, o SO ajusta a tabela de páginas para que a página indicada pelo ponteiro aponte para a página física compartilhada. Pronto! Agora, esse endereço de memória apontado pelo ponteiro indicado serve para comunicação entre processos, sem sequer ser necessário fazer cópia de dados em memória. O que um processo escreve na área de memória compartilhada pode ser lido pelo outro, e vice-versa, sem intermédio do SO.**

Cabe à lógica da aplicação evitar conflitos de acesso, contudo, se for relevante.

Também pode ser relevante haver sincronizações entre processos ou threads. Vários mecanismos são disponíveis para isso:

    Arquivos de bloqueio
    Bloqueio de registros (record locking) 

    fcntl - manipulate file descriptor (F_SETLK, F_SETLKW, and F_GETLK are used to acquire, release, and test for the existence of record locks)
    int flock(int fd, int operation);

    System V semaphores
    Posix Semaphores
    Mutexes
    Condition variables
    Read-write locks
    Barriers
    Spins

Na sincronização, vale ficar atento para a questão de cópias de dados entre user space e kernel space também.

# Pipes e Fifos


Pipes e FIFOs (estes também chamados named pipes) são mecanismos para comunicação entre processos, criados sob demanda no espaço do kernel. Exceto pela forma de criação, pipes e fifos são equivalentes e correspondem a um buffer logicamente contíguo, com armazenamento sequencial de dados. Assim, pipes (e fifos) são usados tipicamente como um canal de dados unidirecional para comunicação entre processos.

A criação de um pipe é feita com as chamadas pipe(2) e pipe2(2), que têm como parâmetro um vetor de 2 posições inteiras:

int pipe (int pipefd[2]); 
int pipe2 (int pipefd[2], int flags);

 pipe2() é semelhante a pipe(), adicionando-se a possibilidade de indicar nos flags os parâmetros para não bloquear nas operações de leitura e escrita (O_NONBLOCK) e o fechamento automático do pipe quando a chamada exec() é realizada (O_CLOEXEC).

Na chamada de criação de um pipe, o SO aloca estruturas apropriadas em sua memória, incluindo espaço para o armazenamento de dados. Em sistemas Linux, esse espaço está limitado a até 64KB por pipe. 

int pfd[2];
int status = pipe(pfd);

Se a chamada de criação de um pipe for bem sucedida, são geradas 2 novas entradas no vetor de arquivos abertos do processo que fez a chamada. Essas entradas são indicadas pelos valores armazenados nas posições 0 e 1 do vetor de inteiros passado como parâmetro na chamada de criação.

No vetor de arquivos abertos do processo, a posição indicada por pfd[0] é aberta apenas para leitura (O_RDONLY) e a posição pfd[1] é aberta apenas para escrita (O_WRONLY). Assim, um pipe é usado tipicamente para que um processo escreva dados e outro os leia.

Dados escritos no pipe são bufferizados até a chamada de uma operação de leitura, que os consome. A leitura e a escrita num pipe são realizadas com as chamadas comuns de leitura e escrita de arquivo (read(2) e write(2)).

**A forma de criação de um pipe, instanciado na área de memória do SO e referenciado pelo vetor de arquivos abertos do processo, faz com que apenas processos com um ancestral comum possam comunicar-se via essa estrutura. Isso ocorre porque a única forma de mais de um processos obterem referência a um pipe é através da herança do vetor de arquivos abertos, realizada na chamada fork(2), com as referências já estabelecidas para o pipe.**

Para possibilitar que processos não relacionados usem o mecanismo de pipe para comunicação, deve criar-se um fifo, ou named pipe.

FIFO (First In First Out) é um pipe que tem um nome na árvore do sistema de arquivos. Essa entrada é criada com a chamada mkfifo(3) e é aberta (instanciada pelo SO) quando um processo realiza a chamada open(2) para abri-lo.

int mkfifo (const char *pathname, mode_t mode);

Na abertura de um FIFO, é comum que um processo a faça usando a flag O_RDONLY e outro O_WRONLY, para que um escreva e outro leia no pipe/fifo. Assim, quaisquer processos que tiverem permissão de acesso ao fifo no sistema de arquivos, e as devidas permissões (rw), podem abri-lo, fazendo com que o SO instancie um pipe/FIFO na memória.

os dados nele escritos não são armazenados no sistema de arquivos, mas são mantidos em memória, como ocorre com pipes.
é preciso que o shell crie o pipe primeiro, para passar sua referência por herança aos processos filhos. O shell cria um pipe, cria processos filhos 1 e 2, redireciona stdout do filho 1 para o pipe (pipefd[1]) e stdin do filho 2 para o pipe (pipefd[0]). A seguir, fecha as 2 entradas do pipe nos filhos 1 e 2 e chama exec p1 no filho 1 e exec p2 no filho 2.


# Memória compartilhada

A forma mais eficiente de comunicação entre processos em um mesmo sistema computacional é o compartilhamento de áreas de memória dentro do espaço de endereçamento desses processos. Com essa técnica, não é preciso haver cópias entre user e kernel space para um processo enviar dados ao outro. Havendo alguma área comum, basta que um escreva e o outro leia e vice-versa. É certo, porém, que qualquer sincronização ou controle de acesso à área compartilhada cabe aos próprios processos.

Considerando o endereçamento de memória protegido, com tradução usando tabelas de páginas, um compartilhamento é obtido fazendo com que páginas lógicas  desses processos apontem para a mesma página física (page frame) na memória. Para tanto, processos devem solicitar explicitamente ao SO que mapeie alguma parte de sua área de memória a um espaço compartilhado.

O compartilhamento de memória pode ser realizado com primitivas da API SystemV e usando a chamada de sistema mmap.

## System V shared memory
O compartilhamento de memória com primitivas de IPC System V requer inicialmente uma chamada ao SO para a alocação de um espaço. Isso é feito com a chamada shmget:

int shmget (key_t key, size_t size, int shmflg);

shmget cria um bloco de memória compartilhada, ou localiza um bloco alocado previamente e que contenha um valor de chave especificado, e retorna um identificador para operações sobre esse bloco. O tamanho da área desejada é especificado como parâmetro e é arredondado para um número inteiro de páginas de memória.

Para que esse bloco possa ser usado, contudo, um ponteiro dentro do espaço de endereçamento do processo deve ser associado ao bloco alocado, o que é feito com a chamada shmat:

void *shmat (int shmid, const void *shmaddr, int shmflg);

shmat associa (attaches) o bloco de memória identificado ao espaço de endereçamento to processo. Permissões padrão de leitura e escrita aplicam-se no mapeamento.

O endereço de associação é especificado como parâmetro e é tratado da seguinte forma:

    Se shmaddr é NULL, SO escolhe endereço disponível adequado para a associação;
    Se shmaddr é diferente de NULL e SHM_RND foi especificado em shmflg, associação ocorre no endereço identificado mais próximo correspondente ao múltiplo de SHMLBA;
    Caso contrário, shmaddr deve ser um endereço alinhado com o início de uma página,

**Na prática, a associação faz com que a variável ponteiro aponte para uma posição de memória que corresponde ao início de uma página lógica que ainda não foi mapeada na tabela de páginas. Assim, o SO tem a chance de fazer a entrada correspondente da tabela de páginas do processo apontar para a página física previamente reservada como memória compartilhada.**

A liberação de um bloco de memória compartilhado requer que todos os processos que a utilizam façam antes a desassociação (detachment) de seus ponteiros para a área, usando shmdt, e que seja feita uma chamada explícita de liberação usando o comando shmctl.

int shmdt (const void * shmaddr);

shmctl realiza operações de controle sobre a área alocada, como a sua liberação depois de todas as desassociações de ponteiros. Operações: IPC_STAT, IPC_SET, IPC_RMID, IPC_INFO, SHM_STAT, SHM_LOCK, SHM_UNLOCK.

int shmctl (int shmid, int cmd, struct shmid_ds *buf);

Considerando as chamadas da API System V, o compartilhamento de áreas de memória entre processos ocorre dos seguintes modos:

    processo aloca área de memória compartilhada e associa ponteiro a ela;
    processo cria filho com fork( ). Filho é cópia do pai e também terá ponteiro (entrada na tabela de páginas) apontando para a área compartilhada;
    uso do ponteiro em memória compartilhada é feito da maneira usual de ponteiros;
    após o uso, e antes de terminar os programas, ambos os processos devem desassociar seus ponteiros da SHM;
    algum dos processos (o pai, depois de esperar o filho terminar, por exemplo) realiza a chamada shmctl para liberação da SHM.
 ou


    ambos os processos fazem chamada a shmget, passando o mesmo valor no campo de chave e flags contendo a opção IPC_CREATE. Primeira chamada faz com que SO aloque a área. Segunda chamada já encontrará a área com chave especificada e apenas retorna o identificador apropriado;
    ambos os processos chamam shmat para associar algum ponteiro (qualquer) à área de memória compartilhada;
    após o uso e antes de terminar o programa, ambos os processos devem desassociar seus ponteiros à SHM;
    algum dos processos (desenvolvedor escolhe (?)) realiza a chamada shmctl para liberação da SHM.


O compartilhamento de memória também pode ocorrer como o mapeamento de arquivos em memória, usando arquivos ou mapeamentos anônimos. Isso é feito com a chamada de sistema mmap(2).

# MMAP
A chamada de sistema mmap permite a criação de mapeamentos de áreas de memória no espaço de endereçamento de um processo.

De maneira geral, mmap faz o mapeamento de arquivos ou dispositivos na memória. Como resultado, o conteúdo do arquivo mapeado pode ser manipulado facilmente na memória, cabendo ao SO fazer com que o conteúdo correspondente do sistema de arquivos seja trazido para a memória e acessível ao processo.

Por exemplo, suponha que uma aplicação de banco de dados permite a edição de tuplas (registros) de uma tabela armazenada num arquivo em disco:

    Para fazer essa edição, é preciso primeiro identificar qual registro se deseja manipular. Sabendo a posição do registro na tabela (3o, 21o, 100o, etc.), é preciso identificar seu endereço lógico dentro do arquivo em disco. Isso é feito multiplicando-se a posição lógica do registro na tabela pelo tamanho de cada registro. 
    Para acessar o registro efetivamente, é agora preciso lê-lo do arquivo que contém a tabela. 
    Para ler dados do arquivo, o programa deve abrir o arquivo e ajustar a sua posição corrente, ou seja o seu offset, usando a chamada lseek.
    O registro desejado pode então ser lido para a memória, pedindo ao SO que leia tamanho_do_registro bytes do arquivo para uma posição de memória indicada. Isso pode ser feito com a chamada read (fd, buf, count). (Isso também pode ser feito com pread(2), sem ajuste do offset).
    Depois de editado o registro na memória, um procedimento de gravação precisa ser realizado sobre o arquivo da tabela. 
    Novamente, calcula-se a posição lógica do registro dentro do arquivo e ajusta-se o offset corrente do arquivo com a chamada lseek. 
    Pede-se, então, ao SO para realizar uma operação de escrita no arquivo, em sua posição corrente (offset ajustado), passando-se como parâmetro o identificador do arquivo, o ponteiro para os dados na memória e o tamanho do registro. Isso também pode ser feito com pwrite(2), sem ajuste do offset. 

A chamada mmap permite que se especifique um endereço lógico, dentro do espaço de endereçamento do processo, que vai mapear o conteúdo de um arquivo em disco. O tamanho do mapeamento e a posição inicial da área do arquivo mapeada podem ser especificados como parâmetros. 

Como era de se esperar, o mapeamento de áreas de memória envolve o uso da tabela de paginação. Assim, o endereço especificado para o mapeamento deve estar relacionado com o início de uma nova página dentro do espaço de endereçamento do processo. É comum, contudo, usar-se o valor 0 para esse parâmetro, deixando a critério do SO escolher a posição lógica de memória à qual o arquivo será mapeado. O offset especificado como ponto inicial do mapeamento do arquivo também precisa ser um múltiplo do tamanho de uma página de memória.

Diferentes atributos de proteção podem ser ajustados ao espaço de memória mapeado, combinações (bitwise OR) de um ou mais desses valores: 

PROT_EXEC    Pages may be executed.

PROT_READ    Pages may be read.

PROT_WRITE  Pages may be written.

PROT_NONE    Pages may not be accessed.

O argumento flags permite ainda especificar diferentes tipos de mapeamento. O mapeamento padrão é MAP_FILE, e não precisa ser especificado. Também é possível especificar se o mapeamento vai ser privado (MAP_PRIVATE) ou compartilhado (MAP_SHARED) com outros processos que mapearem o mesmo arquivo. Também é possível fazer um mapeamento anônimo, sem arquivo associado (MAP_ANONYMOUS ou MAP_ANON).

Como resultado, mapeamentos criados com mmap também podem servir para compartilhamento de memória entre processos. 
Usando um arquivo como referência, por exemplo, dois ou mais processos podem mapear esse arquivo em suas áreas de memória de forma compartilhada, como ilustrado a seguir:

size_t length = 1024 * 1024; // exemplo de tamanho da área do arquivo mapeada

off_t offset = 0;                        // usado para fazer o mapeamento a partir do começo do arquivo

int fd;                                         // para conter o índice do arquivo no vetor de arquivos abertos

void *addr;                               // endereço de memória onde ocorrerá o mapeamento. NULL deixa a cargo do SO escolher a posição

// Abre o arquivo que será mapeado na memória

fd = open (nome_arquivo, O_RDWR, S_IRUSR| S_IWUSR );  // S_IRUSR | IWUSR  ou 0644

// void * mmap(void *addr, size_t len, int port, int flags, int fd, off_t offset);

addr = mmap (NULL, length, PROT_READ | PROT_WRITE, MAP_SHARED, fd, offset);

Também é possível compartilhar áreas de memória realizando um mapeamento anônimo, sem arquivo associado, como ilustrado a seguir:

addr = mmap (NULL, length, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_SHARED,0,0);

 

No mapeamento anônimo não há referência a um arquivo. Assim, os parâmetros fd e offset são ignorados pela implementação. 

Como não há arquivo ou outra referência à área de memória compartilhada, mapeamentos anônimos só servem para processos com parentesco, passando a referência ao mapeamento como herança.

Nesses dois exemplos, por tratarem-se de mapeamentos compartilhados (MAP_SHARED), com permissões de leitura e escrita, todos os processos que fizerem esses mapeamentos terão acesso a uma área de memória compartilhada.

### Uso de mmap pelo carregador de programas

mmap é uma chamada bastante poderosa, servindo até para mapear bibliotecas compartilhadas e áreas do programa em disco a espaços de memória do programa. Ao mapear regiões de um arquivo executável em regiões de memória do processo, isso permite que o SO não faça o carregamento completo do programa em sua iniciação, por exemplo, deixando que as páginas necessárias sejam trazidas para a memória por demanda, quando houver falta de páginas. É claro que esse mecanismo de mapeamento já contém indicações de onde obter os dados a partir do arquivo neste caso!


