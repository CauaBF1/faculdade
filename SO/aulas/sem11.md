# Entrada e Saída
Como se trata de um barramento, todos os controladores conectados têm acesso às informações ali transmitidas. É preciso, então, usar um mecanismo de endereçamento para selecionar o controlador com o qual se deseja comunicar. Chamados de portas de E/S (IO ports) esses endereços são pré-definidos pela indústria em faixas para cada tipo de dispositivo. Dentro dessas faixas há alguma liberdade de configuração para cada controlador de dispositivo. Para os controladores de dispositivos conectados ao barramento PCI, por exemplo, há até um protocolo para negociação dos endereços que serão usados pelos controladores.

Controladores de discos ligados via barramento e se comunicam com restante do SO por esse barramento, SO estabelece comandos para o processador executar. Dessa forma, SO consegue enviar comandos, receber assim conversando com esses controladores.

32 bits de faixas de endereçamento para os controladores portanto mapeando para os 4gb da memoria, existe mmu para controladores que permite acessar maiores faixar de endereçamento.

Controladores dedicados que conseguem se comunicar com CPU e SO, através de barramentos.
controlador USB conectado a barramento USB, junto com processador e dispositivo USB. Usando comandos especificos.

Portas de E/S
in/out : le e escreve barramento (palavra a palavra)
E/S: mapeadas em memoria

device drivers = parte do SO que sabe interagir com controlador especificico, é necessário um divice driver para cada dispositivo, o driver depende ou do SO ou do fabricante

Software de entrada usa canal de /dev, para usar funções descritas que interagem com controladores.

no boot cabe so detectar quais dispositivos estão conectados, carregar device drivers apropriados -> existem comandos para interagir com controlador da bios e ver quais dispositivo ja foram dectados.

out: address data
in: address 
```
------- data 
------- add 
------- controle
é colocado operação de leitura 60H por exemplo, le ve que endereço é associado e caso necessário escreva uma resposta em data 
```
Device Driver, oque tem que fazer ?
 - definir como se comunicar com SO, entrada e saida ou memory ?
 Entrada e Saida:
 -  sudo cat /proc/ioports mostra as portas para cada controlador, resgistrar ao SO para as portas de endereço tal
 - ao se escrever no barramento todos controladores tem acesso, controlador deve ver se esta na faixa de enderenço que ele está associado se sim ele pega

Memory Mapped IO:
 - Falar para SO reservar faixa de endereço e processador deve criar faixa de exclusão para o controlador

No Memory Mapped I/O, os dispositivos de entrada e saída (I/O) compartilham o mesmo espaço de endereçamento da memória RAM. Ou seja, algumas faixas de endereços que normalmente seriam usadas para memória são reservadas para conversar com dispositivos de hardware, como teclados, displays, placas de rede etc.

Por exemplo:

    Endereços de 0x00000000 a 0x0000FFFF → Memória RAM

    Endereços de 0xFFFF0000 a 0xFFFFFFFF → Registradores de dispositivos de I/O

Quando a CPU acessa um endereço dentro dessa faixa especial, ela não acessa a RAM — ela acessa um dispositivo.
A faixa de exclusão se refere justamente a essa região de endereços que não está disponível para a memória RAM porque foi reservada para os dispositivos de I/O no mapeamento de memória.

Em termos práticos:

    Você exclui certas faixas de endereços da RAM porque elas serão usadas pelos dispositivos.

    Essas faixas são exclusivas para I/O — qualquer acesso ali é tratado pelo barramento como leitura/escrita para um periférico, não para a memória.


DMA (Acesso Direto à Memória) é um mecanismo onde um dispositivo de hardware (como um disco, placa de som, rede, ou outro periférico) pode ler ou escrever dados diretamente na memória RAM sem passar pela CPU a cada operação de leitura ou escrita.

Sem DMA:
Se a CPU precisasse transferir dados de um dispositivo para a memória (ou vice-versa), ela teria que:

    Ler um dado do dispositivo.

    Armazenar temporariamente em um registrador.

    Escrever esse dado na memória.

    Repetir isso para todos os dados.

Isso prende a CPU em uma tarefa repetitiva, que não exige processamento lógico, só movimentação de dados.

Com DMA:
Você configura o DMA dizendo:

    De onde os dados vão sair (endereço de origem).

    Para onde vão (endereço de destino).

    Quantos dados mover.

E o DMA faz a transferência sozinho.
A CPU é liberada para fazer outras coisas enquanto isso.

## Como funciona DMA

A CPU configura o controlador DMA:

    Endereço de origem

    Endereço de destino

    Tamanho da transferência

    Tipo de operação (leitura ou escrita)

O DMA inicia a transferência.

Durante a transferência:

    O DMA acessa diretamente o barramento de memória e/ou periféricos.

    A CPU continua executando outras instruções.

Quando termina, o DMA pode:

    Disparar uma interrupção para avisar a CPU.

    Ou continuar com outra tarefa programada.

Burst Mode: Transfere vários dados de uma vez antes de liberar o barramento.

Cycle Stealing: DMA "rouba" ciclos da CPU para mover um dado por vez.

Transparent Mode: DMA só opera quando a CPU não está usando o barramento.


