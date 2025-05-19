# Criação de Processos
É o SO quem faz essa criação. Para solicitar esse serviço existe uma chamada de sistema: fork(2) ($ man 2 fork :-)

Ao executar a chamada fork o SO faz uma cópia do processo atual. Para tanto, é preciso inicialmente alocar um novo descritor de processos que, no Linux, chama-se task-struct.

Caberá ao SO determinar um identificador único para esse novo processo, chamado PID. Além do pid, o SO mantém vários identificadores associados a um processo, como ppid (Parent PID), pgid, uid e gid, que indicam o processo pai, o grupo de processo (process group), o usuário e o grupo base associados ao processo. Enquanto o grupo de processos é usado para o envio de sinais no terminal, as identificações de usuário e grupo servem para o controle das permissões associadas ao processo. As permissões são herdadas do usuário ao qual o processo está associado, a menos que o arquivo executável tenha o atributo setuid ou setgid, que o fazem herdar os privilégios associados ao dono ou ao grupo do arquivo.

Prioridades, identificadores da política de escalonamento, contadores de uso de recursos, referências a threads associadas ao processo, e outras tantas informações, são mantidas pelo SO Linux na task_struct de um processo. Outras informações importantes incluem o vetor de arquivos abertos e uma estrutura para tratamento de sinais.

Como num ambiente multitarefa há um isolamento entre as áreas de memória dos processos, usando memória virtual, é preciso alocar áreas de memória para o processo filho sendo criado. Como veremos ao estudar gerenciamento de memória virtual, o SO cria uma nova page table para o processo. Essa tabela será mantida pelo SO com informações sobre a presença e localização das páginas de memória de código e dados deste processo, e será usada pela MMU do processador para traduzir endereços lógicos em endereços físicos.

Para que as traduções de endereço ocorram automaticamente na unidade de gerenciamento de memória do processador, o SO deve ajustar o endereço da tabela de páginas em registrador específico do processador ao restaurar o contexto de execução de um processo. Para acelerar as traduções de endereço, é comum que as informações da page table acabem sendo armazenadas numa memória cache do processador chamada TLB (translation lookaside buffer). 

Se o processo filho é uma cópia do pai, o SO deve copiar informações do descritor do processo pai para o descritor do processo filho. Também é preciso copiar áreas de memória de código e dados (segmento de dados, variáveis estáticas, heap e pilha, e outros mapeamentos). Para melhorar o tempo de criação de processos, contudo, Linux usa uma estratégia chamada copy-on-write. Neste caso, o SO apenas copia a tabela de páginas do processo pai para o filho, apontando para as mesmas páginas de memória do processo pai. Deste modo, se o processo filho terminar em seguida ou se fizer uma chamada para sobrepor sua área de código com a função exec, não houve gasto desnecessário com duplicações de memória. Por outro lado, se o processo filho ou o pai tentarem modificar qualquer página, é preciso gerar uma cópia desta página para o filho antes. Daí o termo cópia na escrita!

# Fork

De maneira resumida, a chamada de sistema fork cria uma cópia do processo atual. Após a criação, os 2 processos vão para a fila de processos prontos e, quando selecionados pelo escalonador, voltam à execução na instrução seguinte à chamada fork.

Uma questão importante na execução desses 2 processos (pai e filho) é como diferenciar o código do processo pai do processo filho após a execução da chamada fork(). Isso é feito analisando-se o valor de retorno da chamada fork. Para o processo pai, fork() retorna o PID do processo filho criado. Para o filho, o valor de retorno é 0 (zero), que indica sucesso na operação.

Sabendo no código qual processo é o pai e qual é o processo filho, é possível executar atividades diferentes em cada uma dessas cópias. Há situações em que pai e filho vão executar as mesmas operações e há situações em que uma chamada de função distinta é feita para cada um deles. Também há casos em que o processo filho é criado para executar um código completamente novo. Isso é o que comumente é feito pelo shell, ao tratar a linha de comandos digitada pelo usuário.

Vejamos um exemplo de código:

```
pid_t ret = fork();

if (ret==-1)  { 
  printf("Erro na execucao do fork, processo filho nao foi criado.\n"); 
  exit(0); 
} 

// se código chegou aqui é porque o fork funcionou. Há 2 processos executando a partir daqui.

if (ret==0) {  
   printf("Processo filho: %d\n",(int)getpid()); 

} else { // esse é o processo pai. Valor de retorno do fork é o pid do filho criado
   printf("Processo %d, pai de %d\n", (int)getpid(), (int)ret); 
}

// Os 2 processos prosseguem e vão executar a linha seguinte!
printf("%d terminando...\n");
```

Neste caso, o processo que estava executando chama fork para criar outro processo (uma cópia de si). Depois do fork, como os processos pai e filho estão executando o mesmo código, é preciso diferenciá-los. Isso é feito analisando o valor de retorno da chamada fork. 

 O processo filho será aquele para o qual o fork retornou 0. Para o processo pai, o valor de retorno da chamada fork é o pid do filho recém criado. Vejam que os 2 processos estão executando o mesmo código, salvo por diferenciações feitas como no comando if usado. Ambos executam o resto do código. No exemplo, ambos vão imprimir seus pids e o texto " terminando...".

# vfork

