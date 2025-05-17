# IPC Interprocess Communication

## Definição:
Seja para aproveitar a possibilidade de sobreposição de operações de E/S com processamento, para usar mais processadores ao mesmo tempo, ou apenas como estratégia de implementação, aplicações podem ser escritas de forma a usar vários processos (ou threads). 

Comumente, essas tarefas (processos ou threads) precisam se comunicar, para enviar dados umas para as outras, para sincronizar suas ações, ou ainda para controlar o acesso exclusivo a recursos compartilhados. As comunicações entre processos para essas finalidades são chamadas de IPC: Interprocess Communication.

Há diferentes estratégias e mecanismos de apoio para IPC, que levam em consideração aspectos relacionados ao isolamento das áreas de memória de processos e ao compartilhamento de áreas de memória entre threads de um mesmo processo.

A passagem de informações entre tarefas pode ser resolvida de diferentes formas, como veremos. Existem também vários mecanismos que permitem sincronizar e controlar o andamento relativo de tarefas. Muitos desses mecanismos e estratégias envolvem o acesso comum a recursos compartilhados, normalmente mantidos em áreas de memória do sistema operacional ou em áreas de memória comuns entre as tarefas.

## Programação Paralela 

Na computação paralela, ou computação de alto desempenho (HPC - High Performance Computing), o foco é direcionado à utilização de múltiplos processadores ao mesmo tempo para a execução simultânea de diferentes partes de um programa, ou de múltiplas instâncias de suas partes.

Em geral, o uso de vários processadores ocorre para procurar reduzir o tempo para conclusão das atividades, mas também pode ser aplicado para possibilitar o tratamento de conjuntos de dados maiores em tempos razoáveis.

Desafios para a programação paralela incluem o particionamento do código e/ou dos dados para que várias atividades sejam processadas ao mesmo tempo. Também é preciso minimizar dependências e comunicações entre as tarefas, já que isso pode ter impacto na possibilidade de sobreposição das atividades e nos tempos de espera. Além disso, é preciso tratar dos problemas da computação concorrente quando as tarefas competem pelo uso de recursos.

## Programação Concorrente
Já a programação concorrente, que também envolve o uso de múltiplas tarefas, tem como foco principal o gerenciamento de tarefas para o compartilhamento eficiente de recursos, sejam eles processadores, dispositivos físicos, ou estruturas lógicas em memória.

Em geral, busca-se garantir que a execução do programa usando múltiplas tarefas, que podem ser alternadas no uso do(s) processador(es), apresente resultados corretos independentemente da ordem em que as tarefas forem executadas.

Ou seja, é preciso garantir que a execução concorrente das tarefas não interfira no resultado lógico do programa.
Por exemplo, considere um vetor de valores inteiros mantido numa área de memória compartilhada entre várias tarefas. Algumas tarefas desejam escrever valores em alguma posição desocupada do vetor, enquanto outras querem consumir de forma exclusiva os valores ali indicados, tirando esses valores do vetor após a leitura. Um índice de entrada e outro índice de saída são usados para indicar, respectivamente, a posição de escrita do próximo novo valor no vetor e a posição onde se encontra o próximo elemento a ser consumido.

Nesse cenário, parece claro que apenas uma tarefa de cada vez pode ter acesso à posição corrente de escrita, e uma tarefa de cada vez pode manipular a posição de leitura. Caso mais de uma tarefas venham a escrever ou ler simultaneamente na mesma posição do vetor, haverá um comprometimento do funcionamento do sistema.

Como se pode imaginar, inúmeros outros problemas deste tipo podem ocorrer na programação com múltiplas tarefas, também chamada de programação concorrente. A esses problemas de sincronização dá-se o nome de **condição de corrida** (race condition). 

Parece viável supor que uma forma de solução para esse tipo de problema é garantir que apenas uma tarefa acesse o recurso compartilhado de cada vez. Essa estratégia é chamada de exclusão mútua (mutual exclusion), já que o fato de haver uma tarefa acessando o recurso exclui das demais a possibilidade de acesso durante aquele período.

Também é possível perceber que a exclusão mútua entre tarefas só deve ocorrer nos trechos de código em que elas tentam manipular o recurso compartilhado.

Ao trecho de código de uma tarefa que manipula o recurso compartilhado, e que deve portanto ser executado com exclusão mútua, é dado o nome de região crítica, ou seção crítica (critical session or critical region).

 - regiões críticas são definidas em relação a cada recurso (ou conjunto de recursos) compartilhado(s);
 - apenas uma tarefa (por recurso compartilhado) pode estar em sua região crítica de uma vez;
uma tarefa executando fora de sua região crítica não pode gerar a exclusão de outra tarefa que compartilha o(s) mesmo(s) recurso(s);
 - nenhuma tarefa pode ser preterida indefinidamente de entrar em sua região crítica.

Em suma, IPC é necessária, mas pode estar sujeita a problemas inerentes que devem ser considerados na lógica das tarefas:

 - Problema: Race conditions – condições de corrida / disputa, no acesso a recursos compartilhados.
 - Solução: Mutual exclusion – exclusão mútua, que garante acesso exclusivo ao recurso.
 - Mecanismo: Critical sections – regiões críticas, que definem o trecho de código para exclusão mútua.


## Estratégias para exclusão mútua

           Tempo --->
Processo A ----------|======================|----------------------
                     .                      .
                     . A: na região crítica .
                     .                      .
Processo B -----------------|...............|==============|-------
                     .      .               .              .
                     .      . B: bloqueado  .              .
                     .      .               . B: na região . 
                     .      .               .    crítica   .
                    (1) A entra na RC       .              .
                            .               .              .
                           (2) B tenta entrar na RC e é bloqueado
                                            .              .
                                           (3) A libera a RC; B é desbloqueado e entra na RC
                                                           .
                                                          (4) B sai da RC, deixando o recurso livre

Inicialmente, os processos A e B estavam em execução, ou ao menos prontos para execução. O recurso compartilhado associado à região crítica está livre. No instante (1), o processo A verifica que o recurso está livre e entra em sua região crítica. A execução de B prossegue normalmente, até que, no instante (2), ele tente executar sua região crítica, relacionada ao mesmo recurso manipulado por A. Como A já está em sua região crítica, B é bloqueado ao tentar entrar. 

No instante (3), A conclui o trecho de código de sua região crítica; B, que estava bloqueado, é colocado de volta à condição de pronto para execução e entra em sua região crítica. No instante (4), B sai de sua região crítica e o recurso compartilhado volta a estar livre para o próximo processo que o queira usar.

### Desabilitando interrupções

Supondo que um processo consiga entrar em sua região crítica, uma proposta para que outro concorrente não entre também em sua região crítica é evitar a troca de contexto. Como as trocas de contexto são, em geral, decorrentes de eventos associados a interrupções, pode-se supor que desabilitar a ocorrência de interrupções poderia ser uma solução para garantir exclusão mútua.

Vários problemas impedem essa estratégia, contudo:

 - processos executando em espaço de usuário e em anel de execução de menor privilégio (3 em x86-64), não podem executar a instrução que desabilita interrupções;
 - desabilitar INTs pode não ser desejável, pois a notificação de alguns eventos no sistema poderia ser prejudicada;
 - se há mais de um processador, desabilitar INTs em um deles não impactaria os demais.

### Variável global de bloqueio (lock)

Uma outra abordagem consiste em usar uma variável global, compartilhada entre os processos, para indicar se há algum processo executando código de sua região crítica (RC).

Antes de entrar na RC, um processo deve consultar o valor da variável de controle. Se o valor é 0, indica que nenhum processo está na RC. Este processo que deseja entrar, então, altera o valor da variável de controle, escrevendo nela o valor 1.

Outro processo que quiser entrar em sua região crítica vai, agora, identificar que a variável de controle tem valor 1, indicando que outro processo está em sua RC e, portanto, este não pode entrar.

Suponhamos agora que um processo deseja entrar em sua RC e consulta a variável de controle, que está zerada. Contudo, antes de alterar seu valor, ocorre uma interrupção que gera uma troca de contexto, colocando esse processo na fila de prontos.

Por coincidência, o próximo processo colocado em execução também deseja entrar em sua região crítica e testa a variável de bloqueio. Como ela está zerada, indicando que não há processo em região crítica associada a essa variável, este processo altera o valor da variável de bloqueio para 1 e entra em sua RC.

Após algum tempo, enquanto esse processo ainda executava código de sua região crítica, ocorre outra interrupção indicando fim da fatia de tempo. Esse processo vai então para a fila de prontos.

O processo anterior, que já consultara o valor da variável de bloqueio, volta à execução e executa a próxima instrução, que escreve o valor 1 na variável de bloqueio. Ele entra então em sua região crítica, quebrando a restrição de exclusão mútua.

Observa-se que esse problema só ocorreu porque é possível que as operações de consulta e alteração da variável de controle ocorram de maneira divisível (não contínua).

### Instrução TSL 

Uma proposta para resolver o problema é elaborar um mecanismo, uma instrução, para garantir que a consulta e a alteração de um valor numa posição de memória ocorra de maneira "atômica". 

Obs: o termo atômico em vários contextos de computação significa indivisível, como já se acreditou que o átomo era :-) Deixando de lado a física e as partículas sub-atômicas, fiquemos apenas com o conceito de que "operações atômicas" em computação são operações que não estão sujeitas a execuções parciais. Ou todas as operações de um bloco ocorrem, ou nenhuma delas.

Alguns processadores têm uma instrução que oferece o comportamento de consulta e alteração num único ciclo de instrução. Essa instrução é chamada logicamente de TSL (Test and Set Lock).

Na arquitetura x86-64, por exemplo, há uma instrução equivalente, chamada XCHG, que faz a troca do valor entre uma posição de memória e o conteúdo de um registrador (ou vice-versa), ou entre os conteúdos de 2 registradores.

Resumidamente, se é possível consultar e alterar o valor da variável de bloqueio, bloqueando-a numa única operação, o mecanismo de variável de bloqueio funciona!

Mas, o que fazer com o código do processo que encontra a variável de bloqueio fechada?

### Espera ocupada (busy wait)

Vejamos um exemplo de código em que dois processos (A e B) competem para execução de suas regiões críticas. Embora as regiões críticas tenham códigos diferentes (uma_região_crítica() e outra_região_crítica()), ambos os códigos manipulam o mesmo recurso compartilhado e, portanto, usam a mesma variável de bloqueio para controle de aceso (lock).

A variável lock deve ser uma variável global compartilhada entre os processos. Uma forma apropriada para fazer esse tipo de declaração será tratada em unidade posterior.

O código mais à direita apenas ilustra o uso da instrução XCHG, que pode fazer a consulta e alteração numa única operação.

```
  /* Processo A */             /* Processo B */                 
 1.   ...                          ...
 2.   extern int lock=0;           extern int lock=0;
 3.   ...                          ...                              
 4.   while (cond) {               while (outra_cond) {          // ex uso de instrução xchg
 5.     ...                           ...                        label: mv reg, 1
 6.     while (lock != 0);            while (lock != 0);                xchg reg, lock
 7.     lock = 1;                     lock = 1;                         cmp reg, 0
 8.     uma_região_crítica();         outra_região_crítica();           jnz label
 9.     lock = 0;                     lock = 0;                         ...
10.    ...                            ...
11.   }                           }

```

No exemplo de código acima, qual é o efeito do código na linha 6 dos processos A e B?  Trata-se de um loop que vai fazer com que o processo fique executando esse trecho de código até que a condição (lock == 0) seja satisfeita. 

Esse tipo de código, em que a tarefa fica num laço de verificação de uma condição, sem executar outras operações que lhe seriam úteis, é chamado de busy wait (espera ocupada). 

Embora seja mais fácil e direto escrever o código desta forma, é fácil observar que há um desperdício de uso do processador nesse trecho. Supondo que há apenas um processador, ele vai ficar executando instruções desse loop até que termine a fatia de tempo deste processo. Ou então, até que algum outro evento de interrupção desvie o processador para executar código do SO e este acabe fazendo uma troca de contexto.

### Sleep e Wakeup 
Para evitar a espera ocupada (busy wait) algumas primitivas lógicas foram definidas para o bloqueio de processos à espera de condições específicas: 

    sleep() : coloca o processo que emite a chamada num estado de bloqueio.   
                 // não confundir com a função sleep(), que coloca o processo para dormir pelo número de segundos
                 // especificado, e depois é acordado automaticamente.
    wakeup ( ref processo ) : acorda o processo especificado na chamada.

```
  /* Processo A */             /* Processo B */                 
 1.   ...                          ...
 2.   extern int lock=0;           extern int lock=0;
 3.   ...                          ...                             
 4.   while (cond) {               while (outra_cond) { 
 5.     ...                           ...               
 6.     if (lock == 0)                if (lock == 0)
 7.       lock = 1;                     lock = 1;
 8.     else                          else
 9.       sleep();                      sleep();         
10.     uma_região_crítica();         outra_região_crítica();
11.     if (sleeping(B))              if (sleeping(A))
12.       wakeup(B);                    wakeup(A);
13.     else                          else
14.        lock = 0;                    lock = 0; 
15.    ...                            ...
16.   }
```

No exemplo de código acima, observa-se o uso das primitivas sleep e wakeup.

Aqui também há o problema da consulta e atualização não ocorrerem de forma atômica (linhas 6 e 7).

Além disso, a lógica apresentada é sujeita a falhas de sincronização e algumas redundâncias. Por exemplo, na linha 11, há uma verificação se o outro processo estava dormindo. Se ele estiver sendo colocado para dormir, mas ainda não estiver, a condição falha. A variável de bloqueio pode ser liberada erroneamente.

## Semáforos
Semáforos são um mecanismo de sincronização oferecido pelos sistemas operacionais, para uso em diferentes tipos de aplicação que precisam coordenar suas ações ou para controlar o acesso a recursos compartilhados.

Associado a um semáforo, há um contador e uma fila. Tendo valor positivo, o contador indica que uma condição esperada está satisfeita e pode indicar também o número de recursos disponíveis.

Já a fila do semáforo é usada para o posicionamento de descritores de tarefas que não podem prosseguir suas execuções porque a condição esperada não está satisfeita.

As aplicações não têm acesso direto às estruturas internas do semáforo, contudo. Essas só podem ser manipuladas através de duas operações básicas:

    lock()   (ou sem_wait(), ou down() ou p() - nome originalmente proposto para esta operação)
    unlock()  (ou sem_post(), ou up() ou v() - nome originalmente proposto para esta operação)

Uma vez atribuído um valor inicial para o contador do semáforo em sua criação, o valor do contador só pode ser ajustado em função das operações lock e unlock.

A operação lock deve ser chamada por uma tarefa que quer certificar-se que um recurso está disponível. Sua operação pode ser resumida como segue:
```
// lock()
se (semáforo.contador > 0)
  semáforo.contador --
senão {
  salva estado da tarefa chamadora
  insere descritor desta tarefa na fila do semáforo (é um auto-bloqueio!)
  ativa escalonador (para selecionar outra tarefa e colocá-la em execução)
}
```

Como se pode perceber, uma tarefa que fizer a verificação do semáforo antes de usar um recurso compartilhado será automaticamente bloqueada caso a condição não seja satisfeita. Ela só poderá voltar a executar quando outra tarefa executar a operação de liberação deste semáforo. Vale observar também que o descritor da tarefa sai da fila de execução e passa à fila associada ao semáforo.

Já a operação unlock serve para incrementar o contador do semáforo, ou para acordar uma tarefa bloqueada em sua fila de espera:

```
// unlock()
se (semáforo.fila != NULL)     // há tarefa bloqueada na fila
   acorda tarefa da fila       // recoloca tarefa anteriormente bloqueada na fila de prontos
   chama escalonador           // é preciso decidir qual tarefa será colocada em execução
senão                          // não há tarefa(s) na fila
   semáforo.contador ++        // apenas indica que recurso agora está livre
```

O código efetivo da implementação das operações dos semáforos pode variar de acordo com o SO. Além disso, é de se esperar que as operações de consulta e ajuste do contador ocorram de maneira atômica.

Vale observar, contudo, que o uso das primitivas de semáforo fica a cargo das aplicações, ou seja, cabe a cada aplicação que usa recursos compartilhados inserir as chamadas apropriadas para acesso ao semáforo antes de usar o recurso cujo acesso se deseja controlar.

Com relação ao contador associado a um semáforo, há 2 tipos de semáforos: os binários e os de contagem. Nos semáforos binários, o valor do contador associado pode variar entre 0 e 1 apenas. Já nos de contagem, o valor vai de 0, quando não há recursos disponíveis, até um valor positivo qualquer, que indica o número de recursos disponíveis.

Por exemplo, pode-se usar um semáforo de contagem para indicar o número de posições num buffer, que inicialmente seria igual ao tamanho do buffer.

## Mutex
Assim como os semáforos, mutexes são estruturas para sincronização de tarefas. Suas operações também são comumente oferecidas pelo sistema operacional, ou por alguma biblioteca em espaço de usuário, mas que usa recursos do SO para bloqueios, quando necessários. 

Como o próprio nome indica, mutexes são comumente usados para controlar o acesso mutuamente exclusivo a uma região crítica, ou seja, para garantir que apenas uma tarefa de cada vez esteja executando sua seção crítica, provavelmente manipulando algum recurso compartilhado.

Mutexes também têm um contador e uma fila. Nesse caso, contudo, o contador só pode assumir os valores 0 ou 1, que indicam que a área de exclusão mútua está bloqueada ou liberada, respectivamente. Na iniciação do mutex, é comum que seu contador receba valor 1, indicando que a área de exclusão mútua está inicialmente liberada.

Assim como semáforos, mutexes também só podem ser manipulados através de operações específicas:

    mutex_lock
    mutex_unlock

```
mutex_lock:
    if (mutex.contador == 1)        // operações devem ocorrer
       mutex.contador = 0           // de maneira atômica
   else {
       salva contexto da tarefa atual
       bloqueia esta tarefa na fila do mutex
       chama escalonador
   }

mutex_unlock:
   if (há tarefa na fila do mutex) {
      acorda tarefa
      chama escalonador
   } else
       mutex.contador=1 
```

Novamente, vale ressaltar que cabe às aplicações usarem as chamadas do mutex antes e após usar recursos que devem ser manipulados em exclusão mútua.

Como é possível observar nos algoritmos das operações, é preciso garantir que a consulta e o ajuste do contador ocorram de maneira atômica. Além disso, é preciso garantir que apenas a tarefa que realizou o bloqueio seja capaz de liberá-lo, o que não é requerido com semáforos. Ou seja, apenas a tarefa que realizou com sucesso a operação mutex_lock pode, eventualmente, executar a chamada mutex_unlock para esse mutex.

## Monitores

Usuário não precisa lidar com bloqueiro e exclusão mutua, monitores criam funções primitivas de segurança 

Monitor é um mecanismo presente em algumas linguagens de programação, usado para oferecer uma interface de acesso controlado a "recursos" usados pelos programas. 

De maneira resumida, um programador define um monitor como um bloco de código fechado, em que apenas as interfaces de algumas funções são disponíveis para outros programadores que querem usar os recursos gerenciados por esse monitor.

Por exemplo, considere o uso de um buffer compartilhado entre várias threads de uma aplicação. 

Num código fonte, o programador do monitor poderia declarar o buffer e os índices de inserção e retirada no buffer. Nesse mesmo programa, estariam os códigos para inserir e retirar dados no buffer.

Na interface externa desse programa, por exemplo no arquivo .h, estariam apenas as interfaces das funções de retirada e inserção, de forma que o usuário desse código não tem acesso direto ao buffer e nem sabe as localizações ou os nomes das variáveis de inserção e retirada.

Se esse usuário do monitor quiser usar o buffer, apenas faz chamadas às funções de inserção e retirada, sem saber como elas funcionam.

Já o programador do monitor, que vai criar as funções de manipulação desse recurso, aproveita e insere nos códigos dessas funções, chamadas a primitivas de semáforo e de mutex antes de manipular os índices. Assim, ele força o uso das primitivas de segurança que garantem exclusão mútua e bloqueio enquanto condições não estão satisfeitas, sem que o usuário desse monitor tenha que preocupar-se com isso, e sem que seja possível a esse  usuário usar o recurso sem passar pelos mecanismos de exclusão mútua!

### produtor consumidor
```
Monitor monitor_do_buffer 
{
  public {
    void insere(int item);
    void retira(int *item);
  }

  private {

    #define TAM 128

    int buffer[TAM];
    int in, out;

    sem_t s_espaço, s_item; 
    pthread_mutex_t mutex;

    _init()
    { 
      in = out = 0;
      pthread_mutex_init(&mutex, NULL);
      sem_init(&s_espaço, TAM, 0);
      sem_init(&s_item, 0,0);
      ...
    } 

    void insere(int item) 
    { 
       sem_wait(&sem_espaço);
       pthread_mutex_lock(&_mutex);
     
       buffer[in] = item;
       in = (in+1) % TAM;

       pthread_mutex_unlock(&_mutex);
       sem_post(&sem_item);
     }

     void retira(int *item)
     {
       ...
     } 
}
```

Como se vê nesse caso, o monitor oferece uma interface de manipulação do "objeto" buffer, através das funções de inserção e retirada de itens. A garantia da exclusão mútua e dos bloqueios, contudo, já fica embutida nessas funções, e não há como uma aplicação subverter isso.

## Passagem de mensagem
A comunicação entre tarefas também pode ocorrer via passagem de mensagens, tipicamente usando primitivas específicas para o envio e o recebimento.

Parâmetros típicos dessas primitivas incluem uma identificação do destino ou da origem e um ponteiro para mensagem em si.

    send (destino, &msg);
    receive (origem, &msg);

Embora aparentemente simples, há muitos detalhes para a viabilização dessas primitivas. 

Por exemplo, a identificação dos processos origem e destino pode variar ao tratarem-se de processos locais e de qual mecanismo de identificação é utilizado (como PIDs). Para comunicação remota, como ocorre entre nós de rede na Internet, baseada na pilha de protocolos TCP/IP, é comum a identificação de um ponto de comunicação, representado por um número de porta do protocolo de transporte (TCP ou UDP). 

Em alguns casos, códigos específicos podem ser usados para permitir o recebimento de mensagens de origens variadas, ou até a comunicação em grupos. 

Já a mensagem pode ter tamanho fixo ou variável, mas limitado. O formato do conteúdo da mensagem também pode ser definido ou não, cabendo à lógica dos processos extrair os conteúdos de interesse. Caso tratem-se de processos em computadores distintos, também pode ser relevante especificar formas de empacotamento dos dados para transmissão, cuidando-se para a preservação dos conteúdos caso existam representações internas diferentes entre os processos.

Também é possível que as primitivas envolvam sincronização entre emissor e receptor, ou utilizem buffers tanto no lado do transmssor quanto do receptor.

## Barreiras
Uma outra estrutura para sincronização de tarefas é a barreira, usada para garantir que todas as tarefas de um programa atinjam um ponto específico do código antes de prosseguirem suas execuções. 

Assim como com semáforos e mutexes, barreiras não envolvem transmissões de dados entre as tarefas, mas apenas sincronizações de suas atividades.

Logicamente, uma barreira tem um contador e uma fila de tarefas. Quando uma estrutura de barreira é iniciada, é especificado o valor para o contador, que indica quantas tarefas vão participar da sincronização. Já a fila de tarefas é inicializada vazia.

    barrier_wait ( barreira )

Na evocação da primitiva típica, mostrada acima, o contador da barreira é decrementado. Caso o valor resultante seja maior que zero, o descritor desta tarefa é bloqueado na fila associada à barreira e o escalonador é ativado para selecionar uma nova tarefa para execução. 

Caso o valor do contador torne-se 0, todas as demais tarefas que emitiram a chamada e ficaram bloqueadas na fila da barreira são acordadas e recolocadas na fila de prontas, em condição de execução. Esta tarefa, que foi a última a chegar na barreira, também prossegue sua execução.

