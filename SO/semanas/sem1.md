# Threads

Há muitas situações em que programas ficam bloqueados à espera de dados ou de alguma condição que precisa ser satisfeita. Nesses casos, se houver algo mais, outra parte do código do programa, que possa ser executada, poderia ser interessante não bloquear o processo como um todo, mas apenas desviar o processador para execução de outro trecho de código deste programa.
De maneira geral, duas estratégias de decomposição são usadas: decomposição funcional e decomposição de dados. Na decomposição funcional, deve-se identificar os trechos de código do programa que podem ser executados de maneira independente / simultânea. Já na decomposição de dados, examina-se a(s) maior(es) estrutura(s) de dados manipuladas no programa e decide-se uma estratégia para sua manipulação em paralelo.

Percebe-se assim que seria interessante ter várias partes de um programa sendo executadas em paralelo, compartilhando a mesma área de código, seja para a execução de funções diferentes ou para a execução simultânea de múltiplas instâncias de uma mesma função, cada uma manipulando partes distintas dos dados.

Pois é nesse contexto que surgem as threads. Threads correspondem a linhas (fluxos) de execução associada(o)s a um processo. Todo processo tem ao menos uma thread, associada à função main (para programas em C), e pode criar mais. A criação e a destruição de threads podem ocorrer de forma dinâmica ao longo do ciclo de vida de um processo.

Threads de um processo compartilham a maior parte de seus recursos. As áreas de memória do processo, apontadas por suas tabelas de páginas e por outras estruturas de controle mantidas pelo SO, são usadas por todas as suas threads. Assim, referências a uma mesma posição lógica de memória feitas por qualquer uma das threads de um processo são mapeadas para a mesma página física na memória. É claro que esse compartilhamento não vale entre threads de processos diferentes, já que há um isolamento entre processos.

Como a memória é compartilhada entre as threads de um processo, elas podem comunicar-se usando estruturas de dados (variáveis) globais deste processo. A sincronização desses acessos, se for relevante, não é feita pelo SO mas cabe à lógica da aplicação.

Outras estruturas de controle mantidas pelo SO para um processo também são compartilhadas entre suas threads. O vetor de arquivos abertos, por exemplo, é compartilhado. Assim, arquivos, pipes, named pipes, unix e inet domain sockets (e outros sockets) abertos são representados numa estrutura do processo que qualquer uma de suas threads pode usar. Por consequência, as entradas e saídas de dados do terminal feitas por qualquer thread do processo vão estar associadas ao mesmo terminal de controle, indicado pelas posições iniciais do vetor de arquivos abertos deste processo.

Compartilhamento significa economia de recursos e de tempo que seria gasto com replicação. Assim, o código de uma thread é tipicamente associado a alguma função dentro do código do processo.

Para ser usada por mais de uma thread ao mesmo tempo, contudo, uma função precisa ser reentrante. Isso significa que essas funções devem apresentar comportamento correto mesmo quando executadas simultaneamente por diversas threads do mesmo processo. O uso de parâmetros nas funções, ao invés de variáveis globais, favorece a reentrância de código. Funções reentrantes não são necessariamente thread safe, o que implicaria poderem ser executadas simultaneamente por mais de uma threads do mesmo processo.

Thread safety comumente pode ser obtida encapsulando (wrapping) a função original em uma nova, que utiliza um mecanismo de controle de acesso (mutex) antes e depois de acessar um recurso compartilhado. De maneira geral, as funções comuns da biblioteca C e as chamadas de sistema são non-thread-safe, a menos que indicado o contrário.

Em um programa multi-threaded, diversas funções podem ser selecionadas para execução simultânea. Para tanto, alguns recursos de controle devem ser replicados para cada thread. Por exemplo, cada thread deve ter alguma área para salvamento de sua cópia dos valores dos registradores, que constituem o contexto de hardware para suas execuções. Ao manter cópias dos valores dos registradores para cada thread, o SO permite que elas sejam executadas simultaneamente nos cores disponíveis e também possam ser suspensas, com seus contextos salvos para posterior continuação.

Assim, threads compartilham a mesma memória global (dados e heap) do processo, mas cada uma possui sua própria pilha (stack). Indicada pelo registrador ESP, a pilha é comumente usada para a passagem de parâmetros em chamadas de função e alocação de variáveis automáticas (automatic variables) declaradas no escopo das funções associadas às threads ou chamadas por elas. Além disso, a(s) pilha(s) têm papel fundamental no tratamento de interrupções, servindo para o salvamento do valor dos Flags, CS e EIP (PC), antes que o processador sobreponha os valores desses registradores com o endereço da rotina de tratamento apropriada.

**A possibilidade de sobreposição de operações de entrada e saída, seja de arquivos, do terminal ou da rede, com a execução de outros trechos do código de um programa é um benefício da programação com threads.**

Sempre que há eventos assíncronos no programa também pode ser vantajoso usar threads separadas para seus atendimentos, ao invés de bloquear o processo todo. Servidores WWW, por exemplo, costumam usar threads distintas para ficar à espera de pedidos de conexão TCP, e uma nova thread é criada para tratar cada conexão estabelecida. Isso melhora o tempo de resposta aos clientes remotos.

Da mesma maneira, uma aplicação de edição de texto pode usar threads para sobrepor a leitura dos dados digitados com atividades de correção automática e outros processamentos. Jogos que envolvem a comunicação em rede e a manipulação de múltiplos objetos distintos animados na tela também se favorecem com o uso de threads independentes.

Comparada com a programação de várias atividades em paralelo usando processos, a programação com múltiplas threads no mesmo processo tem vantagens. Isso inclui a maior rapidez na criação de threads, a eficiência da comunicação com memória compartilhada e a economia de recursos.

Do ponto de vista da seleção de atividades para execução, talvez já seja possível perceber que são as threads de um processo é que são colocadas em execução. Ou seja, um processo tem ao menos uma thread e pode ter mais. **As threads são as entidades escalonáveis em um SO!**

É importante observar que, num sistema multithreaded, ou seja, quando o SO dá suporte para que cada processo tenha múltiplas threads, cada thread tem seu estado de execução, podendo ser bloqueada ou estar pronta para execução

#### Modelos de programação com threads

- Mestre / escravo (master / slave): nesse modelo, a função main é comumente usada para criar e para esperar pela conclusão de outras threads do processo. Várias rodadas de criação e de sintonização podem ocorrer, mas a thread master é sempre responsável pela sincronização, sem efetivamente tomar parte na execução do código paralelo.
- Pipeline: atividades a executar são quebradas em suboperações, executadas em série, mas de maneira concorrente, por threads diferentes. Os dados manipulados por uma thread são tipicamente encaminhados para a próxima depois de serem processados. A manutenção da estrutura de dados manipulada pelas threads numa área de memória global facilita as comunicações entre elas.
- Peer: semelhante ao modelo mestre / escravo mas, depois de criar os escravos, thread principal participa na execução do trabalho.
