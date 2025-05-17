# Threads

 Em suma, um processo é um programa em execução, mas já sabemos mais do que isso: 

 - para criar um processo num sistema  baseado em Unix, é preciso usar uma chamada de sistema fork();
 - esta chamada gera uma cópia do processo atual, sendo que os dois processos, o criador (processo pai) e a criatura (processo filho) vão continuar suas execuções na instrução seguinte à chamada fork();
 - o valor de retorno da chamada fork(), se ela foi bem sucedida, permite identificar, dentro do código, em tempo de execução, qual é o processo pai e qual é o filho;
 - comumente, espera-se que o processo filho execute um código diferente; para isso ele executa a chamada de sistema execve();
 - execve() faz com que a imagem do processo atual seja sobreposta com as configurações contidas num arquivo executável especificado;
 - caso esses processos, pai e filho, precisem se comunicar para trocar informações ou sincronizar suas atividades, é possível usar chamadas a serviços do SO ou pedir ao SO para criar uma área de memória compartilhada entre eles.

threads, que são linhas de execução criadas a partir de um programa. 

Elas são criadas a partir de códigos de funções no código e são reconhecidas pelo SO como entidades escalonáveis, ou seja, dá para ter várias threads do programa em execução ao mesmo tempo, ao invés de ficar alternando o tempo de uso do processador deste processo entre suas atividades.

Além disso, as threads de um processo compartilham as áreas de memória deste processo. Assim, a comunicação entre elas é mais simples: basta declarar as variáveis compartilhadas na memória global!

O resultado? Quando se deseja criar uma aplicação com atividades que podem (ou precisam) ser executadas em paralelo, o mais comum é criar múltiplas threads.

# POSIX threads

threads devem **compartilhar** os seguintes atributos:


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
 - interval timers (setitimer(2)) and POSIX timers (timer_create())
 - nice value (setpriority(2))
 - resource limits (setrlimit(2))
 - measurements of the consumption of CPU time (times(2)) and resources (getrusage(2))

Por outro lado, além da pilha (stack), POSIX.1 determina que os seguintes atributos devem ser **distintos** para cada thread:

 - thread ID (the pthread_t data type)
 - signal mask (pthread_sigmask())
 - the errno variable
 - alternate signal stack (sigaltstack(2))
 - real-time scheduling policy and priority (sched_setscheduler(2) and sched_setparam(2))

Em sistemas Linux, os seguintes atributos também são mantidos para cada thread:

 - capabilities (capabilities(7))
 - CPU affinity (sched_setaffinity(2))

 As funções da API POSIX threads podem ser agrupadas em 2 grupos principais: 

 - serviços para gerenciar threads, que definem atributos e criam threads, e 
 - serviços para sincronização da execução das threads e bloqueio do acesso a recursos.

## Criação de uma nova thread

A função ptrhead_create ( ) cria uma nova thread, especificando a função que deve ser executada:

int pthread_create (pthread_t * thread, const pthread_attr_t * attr, void * (*start_routine)(void *), void *arg);

Ex: result = pthread_create (&th, NULL, função, NULL);

    Quando um programa é iniciado com exec, uma única thread é criada (initial thread ou main thread).
    Threads adicionais do processo podem ser criadas com pthread_create
    O efeito da criação de uma thread é semelhante à combinação de fork + exec, com espaço de endereçamento compartilhado. Não há hierarquia entre as threads de um processo, contudo.
    Retorna um thread id em thread
    Se attr é NULL, usa parâmetros default

Diferentes atributos podem ser associados a uma thread em sua criação e alguns podem ser ajustados em tempo de execução.

Para criar uma thread já com atributos específicos é preciso criar uma estrutura de atributos, chamar funções que ajustam parâmetros deste atributo e a passar uma referência do endereço desta estrutura na criação da  thread.

Entre os atributos que podem ser ajustados na criação de uma thread estão o tamanho (stacksize) e o endereço (stackaddr) da pilha, a política de escalonamento (schedpolicy: other, rr ou fifo), a indicação se outras threads podem esperar pela conclusão da thread (detachstate) ou se seus recursos serão imediatamente liberados na conclusão, e o valor da prioridade de tempo real (schedparam) para as políticas rr e fifo.

## Termino de uma thread
Threads encerram suas execuções ao retornar da função associada. Essa conclusão também pode ocorrer de maneira explícita, através da função pthread_exit:

void pthread_exit(void *value_ptr);

Ao chamar essa função, uma thread é encerrada e, se a thread for do tipo joynable (padrão), o valor de retorno é disponibilizado para qualquer outra thread do processo que fizer a chamada à função pthread_join.

O retorno da função main, contudo, gera uma chamada implícita à função exit(), que termina a execução do processo (e todas as suas  threads). Assim, caso a função (thread) main não participe das atividades do processo junto com as outras threads, é preciso encerrá-la também com a chamada pthread_exit. Ou, então, também é possível esperar pela conclusão das demais threads, usando a função pthread_join, antes de terminar.

int pthread_join(pthread_t thread, void **value_ptr);

**Pthread_join suspende a execução da thread corrente até que a thread especificada termine, ou retorna imediatamente se essa thread já terminou. Um valor de retorno pode ser fornecido pela thread em sua chamada a pthread_exit, e este é colocado no endereço especificado por value_ptr, caso esse seja não nulo**

# Identificadores
pthread_self ( )
retorna um identificador da thread

pthread_equal (thread1, thread2)
Compara 2 identificadores de thread. 
Retorno 0 indica que threads são diferentes
Operador C “= =” não deve ser usado para comparação, já que thread IDs são objetos.

pthread_once (once_control, init_routine)
Executa a função init_routine uma única vez em um processo
Primeira chamada faz com que a função seja executada, sendo que chamadas subsequentes não têm efeito.
init_routine é tipicamente uma função de inicialização

Parâmetro once_control requer inicialização:
pthread_once_t once_control = PTHREAD_ONCE_INIT;

# Sinais
Threads compartilham o tratamento de sinais do processo ao qual estão associadas. Contudo, cada thread pode ter sua própria máscara para bloqueio do recebimento de sinais pendentes.

Tipos de sinais:

    Asynchronous: entregue para alguma thread que não o está bloqueando
    Synchronous: entregue para a thread que o causou. Ex. SIGFPE, SIGBUS, SIGSEGV, SIGILL
    Directed: entregue para uma thread específica (pthread_kill( ))


int pthread_kill (pthread_t thread, int sig);

Realiza o envio de um sinal para uma thread específica do processo corrente, que está executando a chamada.

Considerando os sinais enviados para o processo com o comando kill( ), estes afetam todas as threads (o processo como um todo). 
Qualquer thread que não tenha bloqueado o sinal, através de sua máscara, pode tratá-lo.

int pthread_sigmask(int how, const sigset_t  *newmask,  sigset_t  *oldmask);

pthread_sigmask( ) é semelhante a sigprocmask( )

Tratadores de sinal (gerenciados com sigaction ou signal) estão associados ao processo (e suas threads). Máscaras de sinais são individualizadas para cada thread.

Também é possível a qualquer thread de um processo bloquear-se à espera de um sinal. Isso é feito com a chamada sigwait().

// select any of pending signals from SET or wait for any to arrive:

int sigwait(const sigset_t *set, int *sig);

Em um processo com múltiplas threads, é possível considerar diferentes estratégias para o tratamento de sinais:

    Definição de uma rotina de tratamento para sinal.
    Seleção de threads dedicadas ao tratamento de sinais específicos, controlando suas máscaras individuais.







