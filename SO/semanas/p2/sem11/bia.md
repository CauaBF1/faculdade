1) Discorra sobre sistema de arquivos:

Sistema de arquivos é a forma de gerenciar toda a questão de armazenanmento de dados de forma não volatil e de grande quantidade. O sistema de arquivos gerencia a interação do com o disco rigido. De forma breve um arquivo são conjuntos de dados gerados por processos que devem ser armazenados no disco, a organização do disco é feita dividindo o mesmo em blocos de tamanho único dessa forma fica melhor a questão da transferencia de dados, nos sistemas POSIX os arquivos possuem i-nodes, que são estruturas de dados referentes ao arquivo, nessa estrutura estão presentes os metadados dos arquivos, como suas permissões, tamanho, dono, local do endereço no disco,..., as permissões serevem para organizar a hierarquia dos arquivos de forma que caso processo queira ler um arquivo só será possível caso tenha permissão para isso. Para operações com arquivos são usados os controladores de dispositivos que são configurados pelo device drivers(camada de software que direciona as instruçõe genéricas do SO para instruções de hardware especificos), para as operações como leitura e escrita serem utilizadas o arquivo deve ser aberto, para isso existem duas opções para uso da CPU, o busy-wainting em que nas operações a CPU fica esperando a transferencia de dados terminar e desperdiça ciclos de processamento e o orientado a interrupções em que CPU é direcionado a outra tarefa enquanto controlador de disco não gera uma interrupção dizendo que trasnferencia foi finaliza ou outra informação. Em ambas é possível usar comunicação via barramento ou via memmory mapped I/O, a primeira faz com que controlador de dispositivo coloque os dados em um buffer que será ligado via barramento a memória principal, através de isntruções como IN/Out, dessa forma a CPU precisa realizar essa trasnferencia, agora na memória mapeada o controlador de disco tem seu buffer e registradores mapeados em áreas sepadaras da memória principal, através ou de instruções IN/OUT ou DMA, em DMA transferencia não precisa da atenção da CPU. A abertura/operações em arquivos requerem um passo a passo(de forma breve) salvar contexto, mudar para kernel mode, varrer tabela de arquivos com fd, verificar permissões e validações, executar tratamento de interrupção, restauração de contexto(IRET), além disso está presente um buffer/cache no disco já que as informações são operadas em blocos de forma que é lido um bloco do disco colocado na cache e a próxima leitura estar no mesmo bloco(ja presente na cache).
*obs: diretórios também são arquivos, so que eles armazenam i-nodes dos arquivos presentes nele dessa forma a organização e hierarquia fica melhor presente.

___

Um sistema de arquivos é a estrutura e conjunto de regras que um sistema operacional utiliza para nomear, organizar, armazenar, recuperar e gerenciar arquivos e diretórios em dispositivos de armazenamento não volátil, como discos rígidos, SSDs e pendrives.

Ele define como os dados são agrupados em arquivos, como estes arquivos são organizados em diretórios (pastas) e como as informações de controle (metadados) são mantidas.

Nos sistemas baseados em POSIX, cada arquivo é representado por um i-node (index node), uma estrutura que armazena metadados como: permissões, tamanho, tipo, dono, timestamps e endereços dos blocos de dados no disco. Os arquivos são compostos por blocos de tamanho fixo, o que facilita a alocação, a leitura e a escrita no disco.

Diretórios são arquivos especiais que armazenam associações entre nomes de arquivos e seus respectivos i-nodes.

Para controlar o acesso, sistemas de arquivos implementam permissões que determinam quem pode ler, gravar ou executar arquivos e diretórios.

As operações de leitura e escrita são intermediadas pelo sistema operacional através de chamadas de sistema (syscalls) como open(), read(), write() e close(). Ao abrir um arquivo, o SO associa um file descriptor (fd) a ele, uma referência utilizada pelo processo.

Os dados são transferidos entre disco e memória principal usando controladores de dispositivos configurados por device drivers, podendo utilizar técnicas como Memory Mapped I/O ou DMA (Direct Memory Access) para otimizar a transferência.

No Memory Mapped I/O, registradores e buffers dos dispositivos são mapeados em endereços de memória. Já no DMA, o controlador de dispositivo movimenta dados diretamente para a memória sem intervenção contínua da CPU, liberando-a para outras tarefas.

As transferências podem ser feitas por busy-waiting, onde a CPU aguarda ativamente, ou por interrupções, onde o controlador notifica o término da operação, e a CPU retoma o controle.

Além disso, o sistema de arquivos utiliza buffers e caches para otimizar a performance, armazenando blocos recentemente acessados na memória, reduzindo acessos físicos ao disco, e aproveitando o princípio da localidade.

Exemplos de sistemas de arquivos incluem ext4, NTFS, FAT32 e XFS, cada qual com suas características e mecanismos internos.

___


