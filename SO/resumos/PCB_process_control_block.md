# Process Control Block (PCB)

## O que é:

O Process Control Block (PCB) é uma estrutura de dados mantida pelo Sistema Operacional para armazenar todas as informações necessárias para controlar e monitorar um processo.

Toda vez que um processo é criado, o SO aloca um PCB para ele. Esse bloco fica armazenado em uma área de memória do núcleo (kernel) e não é acessível diretamente pelos processos de usuário.

Você pode pensar no PCB como a "ficha cadastral" de um processo.

## O que o PCB contém:

| **Campo**                                   | **Descrição**                                                                                                                 |
| :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------- |
| **Process ID (PID)**                        | Identificador único do processo.                                                                                              |
| **Estado do Processo**                      | Estado atual: _Running_, _Ready_, _Waiting_, _Terminated_, etc.                                                               |
| **Contador de Programa (PC)**               | Endereço da próxima instrução a ser executada pelo processo.                                                                  |
| **Contexto de CPU (Registradores)**         | Valores dos registradores gerais, do PC, do Stack Pointer e outros que precisam ser salvos/restaurados em trocas de contexto. |
| **Informações de gerenciamento de memória** | Posição da tabela de páginas, base e limite de segmentos, ou informações sobre área de memória alocada.                       |
| **Informações de escalonamento**            | Prioridade, tempo de CPU consumido, tempo de espera, ponteiro para filas de escalonamento.                                    |
| **Lista de arquivos abertos**               | Descritores de arquivos, sockets, pipes, etc., abertos pelo processo.                                                         |
| **Informações de comunicação (IPC)**        | Dados usados para comunicação com outros processos (se necessário).                                                           |
| **Informações de controle e contabilidade** | Dados como tempo total de CPU usado, ID do usuário proprietário do processo, permissões, etc.                                 |

## Para que o PCB serve ?

O PCB permite que o Sistema Operacional:

    Faça trocas de contexto de forma segura e eficiente, salvando o contexto atual de um processo no PCB e carregando o de outro.

    Acompanhe o estado de todos os processos ativos, suspensos ou finalizados.

    Controle os recursos alocados para cada processo (memória, arquivos abertos, dispositivos).

    Implemente mecanismos de escalonamento, decidindo qual processo executar a seguir.

    Permita comunicação entre processos, monitorando permissões, mensagens ou áreas de memória compartilhada.

## Exemplo:

Imagine que o Processo A está executando, e ocorre uma interrupção para trocar para o Processo B:

    O SO salva no PCB de A:

        Valor atual do contador de programa (PC)

        Registradores de CPU

        Estado: de Running para Ready

    Carrega no CPU as informações do PCB de B:

        Contador de programa de B

        Registradores de B

        Estado: de Ready para Running

    Execução de B continua de onde parou.
