# Processos

Como já mencionado, as técnicas de multiprogramação (sobreposição de E/S e processamento) e de compartilhamento de tempo (time-sharing) são usadas pelo SO para alternar o uso do(s) processador(es).
manter vários programas em execução, alternando o uso do(s) processador(es) entre eles, alguns requisitos são:

    identificar logicamente cada processo;
    manter informações de controle para cada processo (quais?);
    criar um mecanismo para direcionar um processador para executar código de um processo específico;
    limitar as áreas de memória que um processo acessa;
    criar mecanismos para retomar o controle do processador após tê-lo atribuído à execução de um processo;
    salvar o estado do hardware no momento em a execução de um processo for interrompida, para poder retomá-la posteriormente;
    criar mecanismos para oferecer serviços aos processos
    contabilizar o uso de recursos pelos processos
    manter informações sobre arquivos abertos e outros recursos em uso por um processo;

# Criação de precessos

Resumidamente, um arquivo de programa executável contém códigos, dados constantes e informações de controle que vão permitir ao SO criar um processo a partir de seu conteúdo.

Retomando o boot do sistema computacional, vemos que inicialmente o programa da BIOS é executado com o processador em modo real e endereçamento direto da memória. À medida que o SO é carregado, faz as inicializações e cria as estruturas de controle necessárias, ele pode passar o processador ao modo de operação protegido, que inclui suporte para a execução de múltiplas tarefas. A partir daí, o SO pode criar seus próprios processos, associados a atividades que estão fora do núcleo, implementadas como processos, ou tarefas, de maneira geral.

Nas configurações do SO existem listas de programas servidores que devem ser carregados na inicialização do sistema, dando origem a vários processos. Software instalado pelo usuário também pode gerar a ativação de programas automaticamente na fase inicial do sistema.

Após inicializado, o SO pode disponibilizar alguma interface de identificação e login do usuário. Alguns programas vão estar configurados para carregamento automático no início da sessão do usuário, que pode então iniciar programas via interface gráfica.

É comum que SOs tenham mecanismos para programar a execução de processos em instantes específicos (at), e mesmo que programas sejam executados periodicamente, a cada hora, dia, semana ou mês (cron).

a criação de processo sempre vai estar associada a uma solicitação explícita ao SO para que ele faça isso. A forma de criação dos processos, os parâmetros e outras informações de controle podem variar entre os SOs.

UNIX:
a criação de um novo processo é feita com a chamada de sistema fork(). Para tratar esta chamada, que não tem parâmetros, o SO cria um novo processo fazendo uma cópia do processo atual. Esse novo processo, considerado um processo filho daquele que o criou, passa a ser executado na instrução seguinte à chamada fork. Como os processos pai e filho executam o mesmo código, é comum que o programador insira um comando de decisão logo após a chamada fork, para que cada um dos processos (pai e filho) faça ações diferentes.

_Em geral, o processo filho criado faz uma outra chamada de sistema logo a seguir: execve(). Essa chamada pede ao SO para sobrepor o código corrente (e toda a configuração do processo) pelo código e pelas configurações definidas em um arquivo executável especificado como parâmetro da chamada._

Neste ponto, já dá para começar a intuir como um programa shell funciona: lê o comando digitado pelo usuário, faz uma chamada de sistema fork e, no processo filho, faz uma chamada de sistema execve para sobrepor sua imagem de processo a partir do arquivo executável indicado pelo usuário!

Em sistemas Windows, a chamada de sistema para criação de um novo processo é CreateProcess(). Como se vê na documentação, a abordagem é diferente, uma vez que o nome do programa (arquivo executável) é fornecido como parâmetro. Ou seja, faz-se uma chamada ao SO já indicando o programa que deve ser usado para a criação do processo, ao invés de duplicar o processo corrente e fazer a substituição posterior.

Em todos os casos, cada novo processo terá recursos específicos alocados pelo SO, incluindo um novo descritor de processo, áreas de memória para código e dados, informações de arquivos abertos, informações sobre o contexto de execução, etc. Alguns desses recursos, como algumas áreas de memória, podem eventualmente ser compartilhados pelo SO entre processos relacionados.

# Termino processo

Usando a linguagem C, é comum terminar um programa retornando um valor inteiro ao final da execução da função main(). De acordo com as especificações padrão da linguagem, o retorno desta função é equivalente à chamada da função exit(). Na prática, a biblioteca C padrão utiliza uma função inicial que ajusta parâmetros e invoca a função main. Assim, o valor de retorno da função main é passado à função exit().

O valor de retorno previsto é EXIT_SUCESS, para os casos em que o programa termina normalmente, e EXIT_FAILURE, para terminação mal-sucedida. O retorno de outros valores não é padronizado e, caso ocorram, seus significados e usos são dependentes da implementação. Ainda segundo o padrão, a função main deve ter um retorno explícito, para evitar comportamentos não definidos.

Em sistemas Unix, a função exit() comumente realiza operações de controle, que podem ser programadas pelo usuário usando a função atexit(), e faz uma chamada de sistema à syscall \_exit().

supõe-se que o processo concluiu sua execução e está fazendo uma chamada explícita ao SO para ser terminado.

Também é possível que a execução de um processo termine devido a uma situação de erro fatal.
Uma outra condição que pode levar ao término do processo é o recebimento de uma notificação gerada por outro processo. Em sistemas Unix é possível enviar sinais entre processos, através da chamada de sistema kill(). De maneira geral, essa chamada de sistema permite que um processo (do mesmo usuário ou do super-usuário) envie um sinal para outro processo. Diferentes sinais existem, com diferentes efeitos. Alguns deles, como os sinais SIGINT, SIGTERM e SIGKILL, comumente fazem com que a execução do processo que os receber seja terminada.

# Estados de processos

SPOOL:
sobrepor o uso do processador para execução de um programa com a fase de carregamento de outro programa; dados de outro programa, já terminado, poderiam estar ao mesmo tempo sendo gravados da memória para uma fita de saída, aproveitando a lentidão das operações de entrada e saida, como trasnferencia envolvendo disco, para direcionar o uso do processador do processo que solicitou a operação de E/S para outro que esta em condisão de ser executado

TIME-SHARING:
SO fica periodicamente alternando o uso do processador para a execução de vários processos aptos a executar.
um processo pode estar em diferentes estados:

    Em execução: quando um processador está executando suas instruções;
    Pronto: em condição de ser executado, mas o processador está sendo usado para executar outro processo;
    Bloqueado: não está em condição de execução pois aguarda algum evento ou ação que o desbloqueie.

Processos compostos basicamente por instruções do processador comumente ficam alternando entre os estados de pronto e em execução, e vice-versa. Isso ocorre cada vez que o mecanismo de compartilhamento de tempo é usado para alternar o uso do processador.

Já processos que precisam de dados de E/S podem acabar saindo de execução e sendo temporariamente bloqueados.
Exp:
suponha que um processo precisa que o usuário forneça um valor e, para tanto, emite uma chamada de sistema pedindo ao SO que leia dados do terminal. Até que o usuário digite os dados e o SO possa repassá-los ao processo, a execução deste processo não pode prosseguir.

Neste caso, o estado do processo é mudado para bloqueado. Além disso, a estrutura de dados usada pelo SO para representar esse processo é removida da fila dos processos prontos. É claro que, por razões de otimização de código, essa "remoção" da fila não implica mover dados de uma região de memória para outra. O SO apenas ajusta ponteiros de ligação de filas, encadeando os campos de ligação do descritor desse processo para a ligação em outra fila.

Quase sempre que um processo precisa aguardar pela leitura ou escrita de dados, como essas operações podem ser demoradas, o SO ativa os controladores de dispositivos apropriados para fazerem a transferência necessária e bloqueia o processo solicitante até que a operação seja concluída.

Desbloqueio:
Dispositivos de E/S comumente usam interrupções ao processador para indicar que concluíram uma operação solicitada. Quando a interrupção ocorre, o processador (salva o PC e) desvia o fluxo de execução para a rotina de tratamento desta interrupção (cujo endereço foi obtido do vetor de interrupções). Como essa rotina é código do SO, o que ocorre é que o SO assume o controle da CPU; agora o processador estará executando a rotina do SO para tratamento da interrupção.

Sabendo que essa interrupção indica que os dados solicitados pelo processo agora estão disponíveis, o SO copia os dados do local onde o controlador os colocou e os replica na área de memória indicada pelo processo na syscall de leitura. Esse processo agora está apto a voltar à execução, de forma que o SO muda seu estado para pronto e reinsere o descritor desse processo na fila de [processos] prontos.

PRONTO -> EXECUÇÃO
mecanismo de time-sharing, sabemos que o SO usa um gerador de interrupções periódicas para retornar o controle do processador e redirecioná-lo à execução de outro processo. A escolha de qual dos processos prontos deve ser o próximo a ser executado é chamada de escalonamento

# Representação de Processos

processos são programas em execução, sendo que cada programa é composto de sequências de instruções, escritas como se fossem ser executadas com o uso exclusivo do processador. Cabe ao SO implementar mecanismos para criar processos a partir dos códigos dos programas e compartilhar o uso do(s) processador(es) de maneira eficiente para a execução desses processos.
o processador é alternado para a execução de instruções de todos os processos prontos e, para isso, o SO precisa manter informações de controle de cada um dos processos, incluindo seus estados e o estado dos registradores do processador no instante em que cada processo deixa de ser executado.
A estrutura de controle de cada processo é comumente chamada de Bloco de Controle de Processo (BCP - ou Process Control Block) e é basicamente uma estrutura de dados, entre tantas outras, na área de memória do SO. Cada SO, contudo, define sua própria estrutura para a representação de processos.

No sistema Linux, usa-se uma estrutura para representação de tarefas, chamada de task_struct.

De maneira geral, além de particularidades de cada SO, uma estrutura de controle de processo inclui:

    Identificador do processo
    identificador do processo pai deste processo e possíveis outros relacionamentos hierárquicos com outros processos
    Identificador do usuário e de possível grupo associado à execução do processo
    Estado do processo
    Estado dos registradores do hardware
    Valor do contador de programa
    Estruturas para tratamento dos sinais
    Informações de contabilização do uso de recursos
    Alarmes e temporizadores do processo
    ...
    Diretório raiz e diretório corrente
    Vetor de informações dos arquivos abertos
    ...
    Ponteiro para a área de memória com o código
    Ponteiro para áreas de memória com dados
    Endereço da base e do topo da pilha na memória
    Informações sobre outras áreas de memória

## Contexto

Cada vez que um processo vai parar de ser executado, o SO precisa realizar um procedimento chamado de troca de contexto. Contexto, neste caso, refere-se basicamente ao estado dos registradores do hardware no momento em que um processo vai sair de execução; ou seja, quando o processador, que executava instruções deste processo, vai ser direcionado à execução de instruções de outro processo.

Assim, na troca do processo em execução, é feito o salvamento do contexto do processo que sai. Um novo processo é selecionado pelo escalonador do SO e o contexto de execução deste processo é restaurado no hardware.

A troca de contexto não é uma atividade simples e requer ações do processador e do SO.
Supondo que o processador está executando instruções de um dado processo. Isso significa que o registrador PC (contador de programa) do processador aponta para a área de memória onde estão as instruções deste processo. O registrador ponteiro de pilha (ESP) aponta para a área de memória reservada para a pilha deste processo, e os demais registradores de uso geral do processador contêm valores definidos ao longo da execução deste processo.

Como então o SO entra em ação e promove uma troca de contexto?
possibilidades para que o processador seja desviado para executar código do SO.

    Pode ocorrer uma interrupção externa, que é um evento completamente independente. Ao aceitar a interrupção, o processador irá salvar o valor do PC (comumente na pilha) e usar o número da interrupção (informado pelo controlador de interrupção) como um índice para consultar o vetor de interrupções. Na posição correspondente ao número da interrupção no vetor de interrupções estará o novo valor que deve ser atribuído ao PC. O SO pôs ali o endereço de sua rotina para tratamento desta interrupção e, assim, o processador passa a executar código do SO.

    O dispositivo de timer foi anteriormente programado pelo SO para gerar interrupções periódicas. Decorrido o intervalo programado, este dispositivo gera uma interrupção e, da maneira como descrita no item 1, o processador é desviado para executar uma rotina do SO.

    O processo em execução precisa de um serviço do SO e emite uma chamada de sistema.
    Se, para isso, for usada a instrução de interrupção, o procedimento é semelhante aos casos 1 e 2.
    Se a chamada for feita via instrução do processador específica para syscall, o processador salva o valor do PC (neste caso, em espaço reservado para isso) e atribui um novo valor ao PC, obtido de um registrador específico. Bem, o SO deve ter colocado ali o endereço de entrada de suas rotinas de tratamento de syscall, de forma que o processador é desviado para executar código do SO.

    Ocorre um erro ou uma falta na tentativa de execução da instrução corrente. Neste caso, o procedimento é semelhante aos casos 1 e 2.

Como se pode observar, o processador salvou automaticamente o valor do PC (contador de programa ou ponteiro de instruções), antes de substituir seu valor por algum endereço de rotina do SO. Alguma rotina do SO agora está em execução. Vale lembrar que junto com a mudança do PC, neste caso, ocorre também uma mudança para o anel de privilégio 0.

Antes de poder usar os registradores, a rotina do SO que entra em execução comumente salva seus valores na pilha do anel de privilégio corrente (0). Outras informações de controle sobre o processo que estava em execução são salvas no Bloco de Controle desse processo e, assim, fez-se o salvamento de seu contexto de execução!

O SO, agora em execução, pode então prestar os serviços solicitados e assim que acabar vai selecionar um processo para execução. Afinal, SO é um prestador de serviço eficiente e, tendo cumprido seu papel, vai direcionar o processador para a execução de código de algum processo o mais rapidamente possível.

o escalonador seleciona um processo pronto para execução. Pode ser o mesmo, se a interrupção foi rápida, ou algum outro processo. É preciso agora restaurar seu contexto de execução, para que tudo continue como se nenhuma parada tivesse ocorrido.

## restauração de contexto

A restauração de um contexto envolve ajuste de ponteiros de memória (como estudaremos posteriormente), configurações de informações de controle no processador, restauração dos valores dos registradores de uso geral, salvos anteriormente, e direcionamento do processador para executar esse processo. Junto com esse desvio do PC, ocorre uma nova mudança no anel de privilégio, que é recolocado em 3 (na arquitetura x86 e afins).

# Syscalls

Chamadas de sistema, system calls ou syscalls, são os nomes dados às solicitações dos serviços oferecidos por um sistema operacional aos programas. Serviços típicos de um SO incluem aqueles que oferecem acesso a dispositivos, como as operações de entrada e saída (I/O) e de acesso ao sistema de arquivos, e mecanismos para criação, gerenciamento e comunicação entre processos.

As chamadas de sistema normalmente não são invocadas diretamente, mas através de funções definidas numa interface em C, em sistemas que usam padrões Unix. Isso favorece a portabilidade dos programas. Cabe a essas funções em alto nível (wrapper functions) fazer ajustes necessários e realizar o acesso ao kernel de forma adequada à plataforma de hardware disponível. Normalmente, a implementação da função intermediária apenas faz uma cópia dos parâmetros para registradores e invoca a chamada de sistema via uma instrução de interrupção ou via instruções específicas desenvolvidas pelos processadores para chamada explícita ao kernel. Essas instruções, denominadas sysenter e syscall, estão presentes em processadores Intel e AMD, por exemplo. Pode caber à função de alto nível (wrapper) decidir qual mecanismo de chamada será utilizado para desviar o processador para a execução da rotina apropriada do código do SO.

É claro que a área do código do SO onde estão as rotinas das chamadas de sistema devem estar mapeadas no espaço de endereçamento de todas as tarefas.
Outro aspecto relevante da chamada de sistema é o ajuste do nível de execução para o o anel 0 (mais privilegiado). Isso ocorre ao desviar-se o processador da execução da aplicação para a execução do código do SO. Bits nos descritores de segmento do endereço desse código indicam o anel 0 de privilégio. Também o ponteiro da pilha é redirecionado para uma área específica para esse nível de execução (o SO precisa reservar uma área de pilha para cada anel de privilégio para cada tarefa).

o valor de retorno das chamadas de sistema em C que forem bem sucedidas varia, mas, em geral, é 0 (zero). Quando não são bem sucedidas, a maior parte das chamadas de sistema retorna um valor de erro negativo. Neste caso, a função equivalente em C da chamada de sistema copia o valor absoluto do código de erro na variável errno(3) e retorna o valor -1 para o programa que executou a chamada.

Funções da biblioteca C, como perror(3) e strerror(3), podem ser usadas nos programas para a tradução de um código de erro numa mensagem apropriada.

A biblioteca glibc ainda permite o acesso direto às chamadas de sistema, sem fazer a intermediação típica das chamadas (wrapping). Para tanto, é implementada uma função chamada syscall, que permite especificar o número da chamada de sistema e os parâmetros relevantes. A função syscall é útil principalmente quando se deseja usar uma chamada de sistema ainda não implementada pela versão da glibc disponível na distribuição Linux em uso.

realizar a chamada gettimeofday, por exemplo, de forma rápida, consiste em fazer o kernel manter as informações sobre o horário atual em uma localização fixa da memória, que é mapeada no espaço de endereçamento de todos os processos. Desta forma, a interface em alto nível da chamada de sistema pode apenas ler o valor e retorná-lo ao processo, sem gerar uma mudança do processador para modo kernel.

De maneira resumida, quando um processo (ou uma de suas threads) faz uma chamada de sistema, o SO entra em ação através de um desvio do ponteiro de instruções do processador. Do mesmo modo que no tratamento de interrupções, a instrução int vai gerar o salvamento do valor atual do ponteiro de instruções (registradores CS e EIP) antes de alterar seu valor. Isso é feito pelo próprio processador, tipicamente copiando seus valores na pilha da tarefa atual.

Usando agora o número da interrupção (informado pelo controlador de interrupção - IO APIC), da exceção, ou da instrução int, o processador (SO não entrou em ação ainda) consulta o vetor de interrupções (IDT - Interrupt Description Table) para obter um novo valor para os FLAGS e valores para os registradores CS e EIP. Pronto, o processador volta ao ciclo de busca e execução de instruções, agora desviado para a rotina de tratamento.

Do modo equivalente, na chamada de sistema via instruções syscall / sysenter, a execução dessas instruções pelo processador faz com que o o valor do registrador RIP (PC, na arquitetura 64 bits) seja salvo e seja substituído pelo endereço da rotina de entrada do SO. O endereço a ser atribuído ao RIP, contudo, agora é obtido a partir de registradores internos da CPU, cujos valores foram preenchidos pelo SO.

Normalmente, na fase inicial (boot), o SO carrega sua rotina de tratamento das chamadas de sistema para a memória e ajusta seu endereço no vetor de interrupções na memória e nos registradores de endereço específicos. Assim, sempre que uma chamada de sistema é feita, seja através da instrução de interrupção ou das instruções syscall / sysenter, o SO entra em ação porque o valor dos registradores [FLAGS,] CS e EIP (ou RIP) são salvos e alterados para o endereço do SO

$ man syscalls
...
System calls are generally not invoked directly, but rather via wrapper functions in glibc (or per-
haps some other library)... Often, but not always, the name of the wrapper function is the same as
the name of the system call that it invokes. For example, glibc contains a function truncate() which
invokes the underlying "truncate" system call.

Often the glibc wrapper function is quite thin, doing little work other than copying arguments to
the right registers before invoking the system call, and then setting errno appropriately after the
system call has returned. (These are the same steps that are performed by syscall(2), which can be
used to invoke system calls for which no wrapper function is provided.) Note: system calls indicate
a failure by returning a negative error number to the caller; when this happens, the wrapper func-
tion negates the returned error number (to make it positive), copies it to errno, and returns -1 to
the caller of the wrapper.

Sometimes, however, the wrapper function does some extra work before invoking the system call. For
example, nowadays there are (for reasons described below) two related system calls, truncate(2) and
truncate64(2), and the glibc truncate() wrapper function checks which of those system calls are pro-
vided by the kernel and determines which should be employed.

Examinando a documentação do código de entrada das chamadas de sistema usando a instrução SYSCALL no sistema Linux, vê-se que:

; _ 64-bit SYSCALL saves rip to rcx, clears rflags.RF, then saves rflags to r11,
; _ then loads new ss, cs, and rip from previously programmed MSRs.
; _ rflags gets masked by a value from another MSR (so CLD and CLAC
; _ are not needed). SYSCALL does not save anything on the stack
; _ and does not change rsp.
; _
; _ Registers on entry:
; _ rax system call number
; _ rcx return address
; _ r11 saved rflags (note: r11 is callee-clobbered register in C ABI)
; _ rdi arg0
; _ rsi arg1
; _ rdx arg2
; _ r10 arg3 (needs to be moved to rcx to conform to C ABI)
; _ r8 arg4
; _ r9 arg5

Agora sabendo que o valor no registrador rax é o número da chamada de sistema, podemos examinar no código do kernel do sistema Linux qual é a chamada cujo valor foi copiado para o registrador eax antes da chamada:

Pois é, todas as chamadas de sistema são feitas da mesma maneira, passando valores pelos registradores. Dentro da chamada, o valor que estiver no registrador eax vai indicar qual é a syscall solicitada.
