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


