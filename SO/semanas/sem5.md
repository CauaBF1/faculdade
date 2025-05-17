# Problemas de IPC
## Produtor/Consumidor
O problema produtor / consumidor representa um tipo de interação comum entre tarefas em muitas aplicações. 

De maneira geral, trata-se uma aplicação multitarefa em que uma tarefa produz algo e, ao invés de ela mesma processar os dados produzidos, eles são repassados para outra tarefa. A tarefa produtora volta então à produção de novos dados, enquanto a tarefa consumidora estará tratando dos dados produzidos anteriormente.  

A separação das funções simplifica a lógica do código. Além disso, pode haver várias tarefas produtoras e também várias consumidoras, em números determinados pela lógica da aplicação e em função das taxas de produção e de consumo, que podem ser diferentes.

Exemplos de implementação do tipo produtor / consumidor:

    servidor Web multitarefa: uma tarefa (produtora) fica dedicada à espera de pedidos de conexão TCP; quando uma conexão é estabelecida, o identificador do socket com a conexão é repassado para uma tarefa consumidora, que vai tratar as requisições recebidas e enviar as respostas apropriadas;
    editor de texto: uma tarefa fica lendo os dados que o usuário digita e, assim que uma linha é preenchida, ela é repassada a uma outra tarefa que vai cuidar da formatação para exibição na tela;

No caso mais simples, há apenas 1 produtor e 1 consumidor. O produtor está inicialmente ativo, produzindo ou aguardando a chegada do dado (ou evento) desejado. O consumidor está inicialmente bloqueado, à espera de dados produzidos. À medida que o produtor produz algo, alguma notificação é passada ao consumidor, que é acordado e passa ao processamento. O produtor agora esperaria a conclusão deste processamento para produzir novos dados e os repassar ao consumidor.

Para que seja possível acomodar a situação em que vários itens são produzidos antes que algum item anterior seja consumido, é comum que exista um buffer para comunicação entre o produtor e o consumidor. 

Um buffer é basicamente um espaço em memória, como um vetor de tamanho limitado, em cujas posições podem ser armazenados os dados produzidos. À medida em que vai "produzindo dados", o produtor os insere em um buffer compartilhado, ao invés de ter que aguardar para passar um dado de cada vez ao consumidor. Já o consumidor, por sua vez, ao invés de esperar o dado a consumir diretamente do produtor, pode pegá-los do buffer, se houver. Caso haja mais de um dado no buffer, o consumidor pode ir consumindo os dados já produzidos. Se não há dados no buffer, o consumidor comumente deve ser bloqueado.

Como o buffer compartilhado entre produtor e consumidor tem tamanho limitado, eventuais rajadas de produção podem encher o buffer. Neste caso, o produtor deve ser bloqueado até que exista espaço livre. Quando não há dado no buffer, o consumidor pode ser bloqueado.

Já dá para perceber que esse é um problema que envolve comunicação e sincronização!

Semáforos, mutexes e um buffer circular compartilhado são normalmente usados na solução para esse problema.

Considerando um buffer de tamanho N posições, é comum usar:

    1 semáforo para indicar o número de posições livres no buffer: inicializado com valor N
    1 semáforo para indicar a quantidade de itens produzidos e inseridos no buffer: inicializado com valor 0
    1 mutex para controlar o acesso ao índice de escrita no buffer: inicializado com 0 (livre)
    1 mutex para controlar o acesso ao índice de leitura do buffer: inicializado com 0 (livre)

Produtor:
```
do {
  produz_item();         // função associada à geração ou ao recebimento dos dados para processamento
  sem_wait (sema_espaços);
  mutex_lock(mutex_inserção);
  insere_item();
  mutex_unlock(mutex_inserção);
  sem_post (sema_items);
} while (!fim);
```

Consumidor:
```
do {
  sem_wait (sema_itens);
  mutex_lock(mutex_retirada
  retira_item();
  mutex_unlock(mutex_retirada);
  sem_post (sema_espaços);
  consome_item();           // função de processamento das requisições ou dados recebidos
} while (!fim);
```

Há vários aspectos a notar aqui. Veja, por exemplo, que os bloqueios e liberações dos semáforos são invertidos entre produtor e consumidor. 

Vale observar também que a ordem de bloqueio dos semáforos e mutexes deve ser a mesma: sem_wait (); mutex_lock(); 

Se houver uma inversão nessa ordem, há risco de deadlocks, ou seja, bloqueios fatais!

Considerando que o buffer é usado de forma circular, um detalhe a cuidar é fazer com que os índices voltem a 0 depois de chegar na posição final do buffer.

Assim, na inserção:

input = (input+1) % tam_buf;

Depois de retirar um item do buffer:

output = (output+1) % tam_buf;

## Leitores e escritores
Em aplicações em que múltiplas tarefas compartilham alguma estrutura de dados, é possível que apenas algumas delas alterem os valores da estrutura compartilhada, enquanto as demais realizam acessos somente para leitura dos valores.

É claro que é fundamental que os valores armazenados na estrutura compartilhada estejam sempre consistentes1. De maneira geral, isso significa que apenas uma operação de escrita pode ocorrer de cada vez e que nenhuma tarefa pode ler valores semi-preenchidos, durante uma atualização.

Porém, não há impedimento lógico para que mais de uma tarefas estejam lendo valores da estrutura compartilhada ao mesmo tempo.

Esse é o cenário caracterizado como problema dos leitores e escritores (reader-writer). 

Resumidamente, nesse cenário:

    apenas 1 escritor de cada vez pode estar em sua região crítica (associada a esse recurso); 
    múltiplos leitores podem estar em suas regiões críticas ao mesmo tempo, desde que nenhum escritor a tenha bloqueado.

Como consequência, um escritor em sua região crítica impede a entrada de outros escritores e de qualquer leitor. Já a existência de um leitor na região crítica não impede a entrada de outros leitores em suas respectivas regiões críticas.

Solução

Há APIs específicas para esse problema, como pthread_rwlock mas, em geral, esse problema é resolvido mantendo contadores para o número de leitores, acessíveis apenas com o controle de mutexes, e semáforos para controle de acesso. De todo modo, embora o uso de pthread_rwlock sirva para realizar os 2 tipos de bloqueio (leitura ou escrita), essa solução por si só não resolve o problema potencial de starvation. Ou seja, pode ser que escritores nunca consigam acesso ao recurso...

## Jantar dos Filósofos
jantar dos filósofos (the dining philosophers) trata de um problema de sincronização no uso de recursos compartilhados.

De maneira geral, este problema apresenta uma analogia para a situação em que um grupo de processos compartilha um conjunto de recursos. Cada recurso deve ser usado por apenas uma tarefa de cada vez. Como cada tarefa pode precisar de mais de um recursos ao mesmo tempo, há o risco de ocorrer deadlock, ou seja, um bloqueio infinito.


A situação

Cinco (ou mais) filósofos estão sentados a uma mesa redonda. Cada filósofo tem um prato de espaguete à sua frente e há um garfo posicionado na mesa entre cada prato (entre os filósofos).

Cada filósofo alterna seu tempo à mesa entre pensar e comer, indefinidamente!

Para comer, contudo, cada filósofo precisa dos 2 garfos em volta de seu prato, que devem ser pegos um de cada vez. Depois de comer um pouco, um filósofo deve (limpar e:) devolver cada garfo à mesa, passando a pensar por um tempo antes de tentar voltar a comer.

do {
  pensar por um tempo aleatório
  pegar um garfo (qual?)
  pegar o outro garfo
  comer por um tempo aleatório
  liberar um garfo (qual?)
  liberar o outro garfo
  [se for preciso, sai um pouquinho mas volta logo :-]
} while(1);

Solução

Para a solução deste problema é preciso considerar cada garfo como um recurso compartilhado, que precisa ser usado em regime de exclusão mútua. Assim, é preciso garantir que cada garfo está em uso por, no máximo, um filósofo de cada vez.

Algumas questões a considerar são:

    é possível pegar os 2 garfos de uma só vez?
    há uma ordem para cada filósofo pegar um garfo?
    há ordem entre os filósofos para pegar o(s) garfo(s)? 
    o que fazer se não for possível pegar os 2 garfos? 
    como garantir que não há bloqueios infinitos?
    como garantir que nenhum filósofo fique sem comer indefinidamente?
    há restrições sobre o número de filósofos para que a solução proposta funcione?

Possíveis soluções incluem o uso de semáforos, cuidando da ordem em que as operações sobre os semáforos são emitidas.

## Impasse: deadlocks
Além de sincronização e exclusão mútua, o cenário do problema do jantar dos filósofos, apresenta outras questões a considerar, que são possíveis quando mais de um recursos são necessários dentro de regiões críticas:

 - deadlocks: situação em que os recursos necessários estão bloqueados por tarefas distintas, que estão bloqueadas em espera por outro(s) recurso(s).
 - livelocks: condição em que as tarefas não estão bloqueadas, mas em que os recursos bloqueados impedem a realização das atividades previstas.
 - starvation: inanição, corresponde à situação em que tarefas nunca conseguem alocar os recursos que precisam, de forma que suas execuções são preteridas indefinidamente.

### Recursos

Como já discutido, um recurso usado por uma tarefa pode tratar-se de dispositivo, de estrutura de dados, de serviço, ou de qualquer estrutura física ou lógica de uso compartilhado. 

Recursos compartilhados comumente precisam ser usados com exclusão mútua, o que ocorre dentro de trechos de código denominados regiões críticas. O código de uma região crítica pode envolver a manipulação de um ou mais recursos compartilhados. Assim, para entrar numa região crítica, pode ser preciso conseguir bloquear o uso de mais de um recursos.

### Preempção

Considerando que uma tarefa está usando um recurso, uma preempção desse recurso ocorre se ele for retirado da tarefa, sem que isso gere problemas na lógica da aplicação ou no uso do recurso.

Um exemplo de preempção pode ser observado quando o processador que estava executando instruções de uma tarefa é direcionado para a execução de outra. É claro que, para isso, é preciso haver uma troca de contexto mas, do ponto de vista da tarefa que sofreu preempção, não houve prejuízo à lógica.

Já o acesso a um recurso como uma variável compartilhada, bloqueada por uma tarefa na entrada de sua região crítica, não pode sofrer preempção. Ou seja, não é possível tirar o direito de uso de uma tarefa e repassá-lo a outra pois, neste caso, a manipulação pela segunda tarefa pode tornar o conteúdo da variável inconsistente.

No uso de múltiplos recursos com exclusão mútua, se a preempção for permitida, pode-se liberar um recurso previamente alocado, se um segundo recurso necessário não estiver disponível. Ou, ainda, pode ser possível retirar de uma tarefa um  recurso passível de preempção porque ele agora é necessário por outra tarefa.

Recursos compartilhados, contudo, normalmente não são passíveis de preempção.

Solicitação para uso de recursos em exclusão mútua

Como vimos, há diferentes formas e primitivas para garantir o uso de um recurso com exclusão mútua. Na operação de semáforo, por exemplo, a tarefa solicitante emite uma chamada de bloqueio do semáforo (sem_wait, e.g.) e, se a operação de decremento do contador não for possível, a tarefa solicitante é automaticamente bloqueada na fila associada ao semáforo. 
Também existem primitivas em que a operação de bloqueio (de recurso) não é bloqueante (para a tarefa). A operação sem_trywait(), por exemplo, tenta decrementar o contador de um semáforo e retorna um valor que indica o sucesso da operação. Se a operação não foi bem-sucedida, retorna-se um valor de erro, e a tarefa sabe que precisa tentar novamente a operação antes de usar o recurso compartilhado.

Resumidamente, para usar um recurso compartilhado, uma tarefa precisa:

    Solicitar recurso (ou verificar se o contador de um semáforo indica que há recursos, ou que um evento ocorreu, ...)
    Usar recurso
    Liberar recurso (incrementando o contador do semáforo via operação sem_post, por exemplo)

E se vários recursos são necessários em exclusão mútua?

Uma estratégia é associar um semáforo a cada recurso. Assim, para um caso de 2 semáforos, a sequência de operações pode ser:

```
sem_wait (sem_1);
sem_wait (sem_2);
usa_ambos_os_recursos();
sem_post (sem_2);
sem_post (sem_1);
```

### Impasses (deadlocks)

Vejamos 2 exemplos de alocação de 2 recursos (a e b) com semáforos inicializados com valor 1 no contador:

```
(a)                                
   void tarefa_A() {         void tarefa_B() {
     sem_wait(s1);              sem_wait(s1);
     sem_wait(s2);              sem_wait(s2);
     usa_recursos();            usa_recursos();
     sem_post(s2);              sem_post(s2);
     sem_post(s1);              sem_post(s1);
  }                          }

```

Neste primeiro caso, não importa a ordem em que as tarefas são executadas. Qualquer uma delas que começar a executar, ou mesmo se as 2 estiverem sendo executadas simultaneamente em 2 cores, alguma delas vai conseguir executar a operação de decremento do semáforo s1 e a outra vai acabar bloqueada ao tentar fazer essa operação. A tarefa que foi bem-sucedida decrementa, então o semáforo 2 e entra em sua região crítica.

```
(b)
void tarefa_A() {            void tarefa_B() {
   sem_wait(s1);                sem_wait(s2);
   sem_wait(s2);                sem_wait(s1);
   usa_recursos();              usa_recursos();
   sem_post(s2);                sem_post(s1);
   sem_post(s1);                sem_post(s2);
}                            }
```

Neste caso, suponha que as 2 tarefas estão sendo executadas simultaneamente em 2 cores e as 2 realizam com sucesso a primeira operação sem_wait(). Cada uma terá então bloqueado um semáforo diferente. Assim que tentarem realizar o decremento do outro semáforo, ambas ficarão bloqueadas. 

A essa situação dá-se o nome de deadlock, pois ambas as tarefas estão bloqueadas, aguardando por um evento que só pode ser realizado por uma outra tarefa, que está também bloqueada.

Formalmente, diz-se que um conjunto de tarefas estará em deadlock (impasse) se cada tarefa no conjunto estiver esperando por um evento que apenas outra tarefa do conjunto pode gerar.

# Impasses: condições e tratamentos




