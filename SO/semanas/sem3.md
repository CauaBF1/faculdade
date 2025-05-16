# Threads

A paralelização é tipicamente feita na forma de uma decomposição das atividades a serem executadas na aplicação, usando estratégias

duas estratégias de decomposição são usadas: decomposição funcional e decomposição de dados. Na decomposição funcional, deve-se identificar os trechos de código do programa que podem ser executados de maneira independente / simultânea. Já na decomposição de dados, examina-se a(s) maior(es) estrutura(s) de dados manipuladas no programa e decide-se uma estratégia para sua manipulação em paralelo.

Threads correspondem a linhas (fluxos) de execução associada(o)s a um processo. Todo processo tem ao menos uma thread, associada à função main (para programas em C), e pode criar mais. A criação e a destruição de threads podem ocorrer de forma dinâmica ao longo do ciclo de vida de um processo.

Threads de um processo compartilham a maior parte de seus recursos. As áreas de memória do processo, apontadas por suas tabelas de páginas e por outras estruturas de controle mantidas pelo SO, são usadas por todas as suas threads. Assim, referências a uma mesma posição lógica de memória feitas por qualquer uma das threads de um processo são mapeadas para a mesma página física na memória. É claro que esse compartilhamento não vale entre threads de processos diferentes, já que há um isolamento entre processos.

Como a memória é compartilhada entre as threads de um processo, elas podem comunicar-se usando estruturas de dados (variáveis) globais deste processo. A sincronização desses acessos, se for relevante, não é feita pelo SO mas cabe à lógica da aplicação.

Outras estruturas de controle mantidas pelo SO para um processo também são compartilhadas entre suas threads. O **vetor de arquivos abertos**, por exemplo, é compartilhado. Assim, arquivos, pipes, named pipes, unix e inet domain sockets (e outros sockets) abertos são representados numa estrutura do processo que qualquer uma de suas threads pode usar. Por consequência, as entradas e saídas de dados do terminal feitas por qualquer thread do processo vão estar associadas ao mesmo terminal de controle, indicado pelas posições iniciais do vetor de arquivos abertos deste processo.

O tratamento de sinais também tem caráter global ao processo e é compartilhado por suas threads, embora cada uma possa ter uma máscara para o bloqueio de seus recebimentos. Informações de identificação de usuário, de grupo, valor da prioridade estática (nice), que têm sentido para um processo como um todo, também são compartilhadas.

Compartilhamento significa economia de recursos e de tempo que seria gasto com replicação. Assim, o código de uma thread é tipicamente associado a alguma função dentro do código do processo.

Para ser usada por mais de uma thread ao mesmo tempo, contudo, uma função precisa ser reentrante. Isso significa que essas funções devem apresentar comportamento correto mesmo quando executadas simultaneamente por diversas threads do mesmo processo. O uso de parâmetros nas funções, ao invés de variáveis globais, favorece a reentrância de código. Funções reentrantes não são necessariamente thread safe, o que implicaria poderem ser executadas simultaneamente por mais de uma threads do mesmo processo.

thread-safe when it can be invoked or accessed concurrently by multiple threads without causing unexpected behavior, race conditions(is the condition of an electronics, software, or other system where the system's substantive behavior is dependent on the sequence or timing of other uncontrollable events), or data corruption

Thread safety comumente pode ser obtida encapsulando (wrapping) a função original em uma nova, que utiliza um mecanismo de controle de acesso (mutex) antes e depois de acessar um recurso compartilhado. De maneira geral, as funções comuns da biblioteca C e as chamadas de sistema são non-thread-safe, a menos que indicado o contrário.

Em um programa multi-threaded, diversas funções podem ser selecionadas para execução simultânea. Para tanto, alguns recursos de controle devem ser replicados para cada thread. Por exemplo, cada thread deve ter alguma área para salvamento de sua cópia dos valores dos registradores, que constituem o contexto de hardware para suas execuções. Ao manter cópias dos valores dos registradores para cada thread, o SO permite que elas sejam executadas simultaneamente nos cores disponíveis e também possam ser suspensas, com seus contextos salvos para posterior continuação.

Assim, threads compartilham a mesma memória global (dados e heap) do processo, mas **cada uma possui sua própria pilha (stack).** Indicada pelo registrador ESP, a pilha é comumente usada para a passagem de parâmetros em chamadas de função e alocação de variáveis automáticas (automatic variables) declaradas no escopo das funções associadas às threads ou chamadas por elas. Além disso, a(s) pilha(s) têm papel fundamental no tratamento de interrupções, servindo para o salvamento do valor dos Flags, CS e EIP (PC), antes que o processador sobreponha os valores desses registradores com o endereço da rotina de tratamento apropriada.

+-----------------------------------------------------------------------+ 
| Process                                                               | 
|   +-------+     +-------------+  +-------------+  +-------------+     | 
|   | Files |     | Thread      |  | Thread      |  | Thread      |     | 
|   +-------+     |+-----------+|  |+-----------+|  |+-----------+|     | 
|                 || Registers ||  || Registers ||  || Registers ||     | 
|                 |+-----------+|  |+-----------+|  |+-----------+|     | 
| ....................................................................  | 
| . Memory        |             |  |             |  |             |  .  | 
| .               | +---------+ |  | +---------+ |  | +---------+ |  .  | 
| . +--------+    | |  Stack  | |  | |  Stack  | |  | |  Stack  | |  .  | 
| . |  Heap  |    | |         | |  | |         | |  | |         | |  .  | 
| . +--------+    | |         | |  | |         | |  | |         | |  .  | 
| .               | |         | |  | |         | |  | |         | |  .  | 
| . +--------+    | |         | |  | |         | |  | |         | |  .  | 
| . | Static |    | |         | |  | |         | |  | |         | |  .  | 
| . +--------+    | |         | |  | |         | |  | |         | |  .  | 
| .               | |         | |  | |         | |  | |         | |  .  | 
| . +--------+    | |         | |  | |         | |  | |         | |  .  | 
| . |  Code  |    | +---------+ |  | +---------+ |  | +---------+ |  .  | 
| . +--------+    +-------------+  +-------------+  +-------------+  .  | 
| ....................................................................  | 
+-----------------------------------------------------------------------+

A possibilidade de sobreposição de operações de entrada e saída, seja de arquivos, do terminal ou da rede, com a execução de outros trechos do código de um programa é um benefício da programação com threads.

Sempre que há eventos assíncronos no programa também pode ser vantajoso usar threads separadas para seus atendimentos, ao invés de bloquear o processo todo. Servidores WWW, por exemplo, costumam usar threads distintas para ficar à espera de pedidos de conexão TCP, e uma nova thread é criada para tratar cada conexão estabelecida. Isso melhora o tempo de resposta aos clientes remotos.

Da mesma maneira, uma aplicação de edição de texto pode usar threads para sobrepor a leitura dos dados digitados com atividades de correção automática e outros processamentos. Jogos que envolvem a comunicação em rede e a manipulação de múltiplos objetos distintos animados na tela também se favorecem com o uso de threads independentes.

a programação com múltiplas threads no mesmo processo tem **vantagens**. Isso inclui a maior rapidez na criação de threads, a eficiência da comunicação com memória compartilhada e a economia de recursos. 

É importante observar que, num sistema multithreaded, ou seja, quando o SO dá suporte para que cada processo tenha múltiplas threads, cada thread tem seu estado de execução, podendo ser bloqueada ou estar pronta para execução.

## Modelos de programação com threads


 - Mestre / escravo (master / slave): nesse modelo, a função main é comumente usada para criar e para esperar pela conclusão de outras threads do processo. Várias rodadas de criação e de sintonização podem ocorrer, mas a thread master é sempre responsável pela sincronização, sem efetivamente tomar parte na execução do código paralelo.
 - Pipeline: atividades a executar são quebradas em suboperações, executadas em série, mas de maneira concorrente, por threads diferentes. Os dados manipulados por uma thread são tipicamente encaminhados para a próxima depois de serem processados. A manutenção da estrutura de dados manipulada pelas threads numa área de memória global facilita as comunicações entre elas.
 - Peer: semelhante ao modelo mestre / escravo mas, depois de criar os escravos, thread principal participa na execução do trabalho.

A criação de programas portáveis que utilizam threads é normalmente feita usando a API pthreads (POSIX Threads).

## Threads no espaço do usuário
#### Antes do SO incorporara suporte para Threads 
as primeiras implementações de threads foram realizadas na forma de bibliotecas no espaço de usuário.
Ou seja, criou-se uma biblioteca que tinha funções para criar threads para executar o código de alguma função dentro do programa. Cabia a essa biblioteca manter uma tabela de threads lógicas criadas pela aplicação, com as devidas informações de controle sobre cada uma delas. Contextos e áreas de pilha tinham que ser salvos para cada thread dessa tabela.

A maior dificuldade era a alternância entre as "pseudo" tarefas. Uma função específica chamada thread_yield foi inventada para que uma thread voluntariamente liberasse o processador para outra. No fundo, essa função gerava uma chamada ao pseudo-escalonador das threads. Nem sempre era possível usar essa chamada de forma eficiente nos códigos das threads.

Além disso, como fazer para que o processo todo não ficasse bloqueado numa chamada feita dentro de uma thread, mas que o processador fosse direcionado para execução do código de outra tarefa?

Outro aspecto era como salvar o "contexto" dessas threads lógicas ao alternar-se o uso do processador entre elas, permitindo retomá-las posteriormente onde haviam parado.

Para evitar o bloqueio do processo como um todo e possibilitar redirecionar o processador uma estratégia era substituir as chamadas de sistema bloqueantes para leitura e escrita por operações não bloqueantes.

Abordagens para evitar o bloqueio do processo para chamadas de sistemas bloqueantes:

 - Por exemplo, antes de fazer uma operação de leitura com read(), era feita uma chamada de sistema do tipo select(), que permite verificar, entre outros aspectos, a disponibilidade de dados para leitura num arquivo. Se houver dados, a chamada read() é feita. Caso contrário, é feita uma troca de contexto entre as threads lógicas desse processo. Quando essa thread voltar a executar, o procedimento de teste é feito novamente, antes de liberar o acesso à operação read().

 - Outra abordagem consistia em ajustar o modo de operação do arquivo, tornando-o não-bloqueante. Isso pode ser feito com a chamada fcntl e o parâmetro F_SETFL e o atributo O_NONBLOCK. Quaisquer chamadas de sistema para leitura nesse arquivo agora retornam imediatamente, com sucesso e os dados requisitados, ou com erro, indicando que não havia dados prontos. Neste caso, a biblioteca de threads aproveitava e transferia o processador para executar código de outra thread! Posteriormente, quando essa thread voltasse a ocupar a CPU, a operação era tentada novamente.

usar um mecanismo de temporização provido pelo SO, associado ao tratamento de sinais. Resumidamente, instalava-se uma rotina de tratamento de sinal para o timer (SIGALRM) e instaurava-se um temporizador periódico com setitimer().  

Pronto! Periodicamente, um sinal do TIMER era gerado para o processo que, em sua rotina de tratamento do sinal, salvava o contexto da thread corrente, selecionava outra thread pronta, restaurava seu pseudo-contexto e direcionava o processador para executar seu código. Isso pode ser feito com a chamada de sistema setjmp(). 

Puxa, que trabalho! Tudo para não bloquear o processo e ficar alternando entre suas threads. Se houvesse mais de um processadores, contudo, apenas 1 poderia ser usado, já que o SO enxergava apenas 1 processo!

## Threads no espaço do kernel

No sistema Linux, por exemplo, há uma syscall específica para a criação de threads, chamada clone(). Na verdade, essa chamada tornou-se tão flexível e poderosa que ela permite tanto criar um novo processo quanto criar uma nova thread, ou ainda algo misto entre uma coisa e outra!

```
int clone(int (*fn)(void *), void *stack, int flags, void *arg, ...
           /* pid_t *parent_tid, void *tls, pid_t *child_tid */ );

```
Isso é possível porque a chamada leva como parâmetro um conjunto de flags que determina quais informações de controle da entidade chamadora desta função serão compartilhadas com a nova entidade criada.

Entre as estruturas de controle que podem ser compartilhadas, podem ser destacadas:
```
- CLONE_CLEAR_SIGHAND : signal dispositions in the child thread are the same as in the parent.
- CLONE_FILES : the calling process and the child process share the same file descriptor table. If CLONE_FILES is not set, the child process inherits a copy of all file descriptors opened in the calling process at the time of the clone call.
- CLONE_FS : indicates if the caller and the child process share the same filesystem information (the root of the filesystem, the current working directory, and the umask).
- CLONE_IO : if set, then the new process shares an I/O context with the calling process.
- ...
- CLONE_PARENT : if set, then the parent of the new child (as returned by getppid(2)) will be the same as that of the calling process.
- CLONE_PID : if set, the child process is created with the same process ID as the calling process.
- CLONE_SIGHAND : if set, the calling process and the child process share the same table of signal handlers.
- CLONE_THREAD : if set, the child is placed in the same thread group as the calling process.
- CLONE_VFORK : if set, the execution of the calling process is suspended until the child releases its virtual memory resources via a call to execve(2) or _exit(2) (as with vfork(2)).
- CLONE_VM : if set, the calling process and the child process run in the same memory space. If CLONE_VM is not set, the child process runs in a separate copy of the memory space of the calling process at the time of the clone call.
```

#### Exemplo chamando funções

```
$ strace -f -e trace=process thread_program
execve("./t", ["t"], [/* 45 vars */])   = 0
arch_prctl(ARCH_SET_FS, 0x7f33569b3700) = 0
clone(child_stack=0x7f33561f2ff0, flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, parent_
tidptr=0x7f33561f39d0, tls=0x7f33561f3700, child_tidptr=0x7f33561f39d0) = 9480
exit_group(0)                           = ?
+++ exited with 0 +++

(2)
$ strace -f -e trace=process fork_program
execve("./p", ["p"], [/* 45 vars */])   = 0
arch_prctl(ARCH_SET_FS, 0x7f14ba10f700) = 0
clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f14ba10f9d0) = 9484
exit_group(0)                           = ?
+++ exited with 0 +++

(3)
$ strace -e trace=process vfork_program
execve("./vf", ["vf"], 0x7ffdc27d0b20 /* 24 vars */) = 0
arch_prctl(ARCH_SET_FS, 0x7f16bdcf4740) = 0
vfork()                                 = 21844
--- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=21844, si_uid=1000, si_status=0, si_utime=0, si_stime=0} ---
exit_group(0)                           = ?
+++ exited with 0 +++
```

No caso (1), em que o programa usa a rotina pthread_create(), essa chamada foi mapeada pela biblioteca glibc numa chamada à syscall clone do Linux. Ali, vê-se que o parâmetro flag foi usado para indicar quais estruturas deveriam ser compartilhadas com a nova thread criada: 

```
flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID
```
Como threads de um processo devem compartilhar seu espaço de endereçamento, o tratamento de sinais, o vetor de arquivos abertos, a visão do sistema de arquivos, e mais alguma particularidade dependente de sistema, esses parâmetros são indicados nos flags!

No caso (2), em que o programa cria um novo processo fazendo chamada à função fork(), vê-se que a glibc gerou código fazendo uma chamada à syscall clone também. Nesse caso, contudo os flags indicavam apenas parâmetros específicos da chamada, sem compartilhar o espaço de endereçamento ou estruturas de controle. Assim, é de se esperar que o SO faça uma cópia de tudo do processo pai para o novo processo filho criado.

No caso (3), a chamada da função vfork() no programa foi mapeada para a syscall vfork().

## Processos, threads e tarefas no sistema Linux

Analisando as chamadas de criação de processos e threads no sistema Linux, que são mapeadas para a syscall clone(), é possível observar que, num sistema Linux, as entidades escalonáveis são representadas praticamente da mesma forma. Internamente, tudo é tratado com uma tarefa, representada por uma task_struct. 

Por fim, o que vai diferenciar uma tarefa da outra criada a partir dela são os recursos que serão compartihados ou copiados! Se a nova entidade sendo criada é um novo processo, copiam-se as estruturas de controle. Se o objetivo é criar uma nova thread do processo corrente, compartilham-se as áreas de memória, o vetor de arquivos, abertos, o tratamento de sinais, o PID e outras estruturas de controle.

Do ponto de vista da implementação interna, parece bem sensato e prático, não acham?

Ah, o que muda na seleção de tarefas para execução? Nada! Ao escalonador, basta selecionar a próxima tarefa, independentemente de logicamente ela ser um processo ou uma thread.

Considerando que, logicamente, todo processo tem ao menos uma thread, associada à função main(), são as threads é que entram nas filas de execução. Num sistema Linux, tudo é tarefa (task) e pronto!

## POSIX threads: pthreads
Para apoiar a criação de programas portáveis com threads, que podem ser recompilados em diferentes plataformas computacionais, há um padrão POSIX que define funções para isso. Ele é chamado de Posix Threads ou, simplesmente, pthreads.

```
$man pthreads
  
 POSIX.1 specifies a set of interfaces (functions, header files) for
 threaded programming commonly known as POSIX threads, or Pthreads.  A
 single process can contain multiple threads, all of which are
 executing the same program.  These threads share the same global
 memory (data and heap segments), but each thread has its own stack
 (automatic variables).

 POSIX.1 also requires that threads share a range of other attributes
 (i.e., these attributes are process-wide rather than per-thread):

 - process ID
 - parent process ID
 - process group ID and session ID
 - controlling terminal
 - user and group IDs
 - open file descriptors
 - record locks (see fcntl(2))
 - signal dispositions
 - file mode creation mask (umask(2))
 - current directory (chdir(2)) and root directory (chroot(2))
 - interval timers (setitimer(2)) and POSIX timers (timer_create(2))
 - nice value (setpriority(2))
 - resource limits (setrlimit(2))
 - measurements of the consumption of CPU time (times(2)) and resources (getrusage(2))

 As well as the stack, POSIX.1 specifies that various other attributes are distinct for each thread, including:

 - thread ID (the pthread_t data type)
 - signal mask (pthread_sigmask(3))
 - the errno variable
 - alternate signal stack (sigaltstack(2))
 - real-time scheduling policy and priority (sched(7))

 The following Linux-specific features are also per-thread:

 - capabilities (see capabilities(7))
 - CPU affinity (sched_setaffinity(2))
```




