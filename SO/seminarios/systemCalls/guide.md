# Estrutura Interna syscalls
## entry_64.S
Quando um syscall é chamada pelo usuário é necessário que a CPU realize algumas funções, essas funções são descritas no entry.s, ou seja, ele é responsavel pelo oque o hardware deve fazer ao uma syscall ser feita.

Por que salvar essas informações?

Quando o processador executa a instrução syscall, ele troca do modo usuário para o modo kernel, mas não salva automaticamente todo o estado do usuário na pilha do kernel. Para que o kernel possa executar a syscall e depois retornar ao usuário corretamente, ele precisa salvar o contexto do usuário — isto é, os registradores importantes e informações de segmento — em uma estrutura chamada pt_regs.

```asm
SYM_CODE_START(entry_SYSCALL_64)
    #Fornece metadados para desenrolamento de pilha (stack unwinding) durante depuração 
	UNWIND_HINT_ENTRY 
    
    # Instrução de segurança para Control-Flow Enforcement Technology (CET), prevenindo ataques de desvio de fluxo de execução.
	ENDBR 

    #Troca o registro GS entre usuário e kernel, permitindo acesso a dados por-CPU do kernel.
    swapgs 
	
    /* tss.sp2 is scratch space. */
    #Salva o stack pointer (RSP) do usuário no campo sp2 da Task State Segment (TSS) para uso posterior.
    movq	%rsp, PER_CPU_VAR(cpu_tss_rw + TSS_sp2)
    #Alterna para o CR3 do kernel (page tables do kernel), mitigando vulnerabilidades como Meltdown. Usa %rsp como registro temporário.
    SWITCH_TO_KERNEL_CR3 scratch_reg=%rsp
    #Define %rsp para o topo da pilha do kernel alocado para a CPU atual.
	movq	PER_CPU_VAR(cpu_current_top_of_stack), %rsp


SYM_INNER_LABEL(entry_SYSCALL_64_safe_stack, SYM_L_GLOBAL)
	ANNOTATE_NOENDBR

	/* Construct struct pt_regs on stack */
	#Empurra o segmento de dados do usuário para a pilha, armazenando o campo ss da estrutura pt_regs.
	pushq	$__USER_DS				/* pt_regs->ss */
	#Recupera o RSP do usuário salvo anteriormente e empurra para a pilha (campo sp do pt_regs).
	pushq	PER_CPU_VAR(cpu_tss_rw + TSS_sp2)	/* pt_regs->sp */
	#Salva RFLAGS do usuário (armazenado em %r11 pela instrução syscall).
	pushq	%r11					/* pt_regs->flags */
	#Empurra o segmento de código do usuário (campo cs do pt_regs).
	pushq	$__USER_CS				/* pt_regs->cs */
	#Salva RIP do usuário (armazenado em %rcx pela instrução syscall). Corresponde ao campo ip do pt_regs.
	pushq	%rcx					/* pt_regs->ip */

#Rótulo para pós-configuração do hardware frame.
SYM_INNER_LABEL(entry_SYSCALL_64_after_hwframe, SYM_L_GLOBAL)
	#Armazena o número da syscall no campo orig_ax do pt_regs.
	pushq	%rax					/* pt_regs->orig_ax */
	/*
	 - Empurra todos os registros gerais (RAX, RBX, ..., R15) para a pilha

	 - Limpa os registros para evitar vazamento de dados

	 - Define RAX = -ENOSYS (valor padrão para syscalls inválidas)
	*/
	PUSH_AND_CLEAR_REGS rax=$-ENOSYS


	/* IRQs are off. */
	#Passa o endereço do struct pt_regs (via %rdi) como primeiro argumento para do_syscall_64.
	movq	%rsp, %rdi
	/* Sign extend the lower 32bit as syscall numbers are treated as int */
	#Estende o número da syscall (32 bits em %eax) para 64 bits (%rsi), segundo argumento para do_syscall_64.
	movslq	%eax, %rsi

	/* clobbers %rax, make sure it is after saving the syscall nr */
	#Ativa Indirect Branch Restricted Speculation, mitigação para Spectre v2.
	IBRS_ENTER
	#Mitigação para Branch History Injection (BHI).
	UNTRAIN_RET
	#Limpa o histórico de branches (proteção contra Spectre v2).
	CLEAR_BRANCH_HISTORY

	/*
	Chama a função C do_syscall_64, que:

     - Verifica o número da syscall

     - Executa a syscall correspondente

     - Armazena o resultado em pt_regs->ax

     - Desabilita interrupções durante a execução
	*/
	call	do_syscall_64		/* returns with IRQs disabled */

```
Fluxo pós-execução:

Após do_syscall_64, o controle retorna para:

    Restauração de registros

    Troca de contexto de volta para usuário

    Instrução sysret para retorno ao espaço do usuário.


### Details:

A instrução syscall no processador x86-64 tem um comportamento especial:

    Ela salva o endereço de retorno (RIP) do usuário em %rcx.

    Ela salva o valor dos flags (RFLAGS) do usuário em %r11.

Isso é uma convenção do hardware para permitir que o kernel recupere esses valores ao retornar para o usuário via sysret. Portanto, %r11 não é um registrador qualquer; ele é usado para armazenar temporariamente os flags do usuário durante a syscall



    O kernel constrói um struct pt_regs na pilha do kernel empurrando os valores dos segmentos, ponteiro de pilha, flags e endereço de instrução do usuário.

    %rcx e %r11 são usados pelo hardware para salvar RIP e RFLAGS do usuário durante a instrução syscall.

    Essa estrutura é essencial para que o kernel possa restaurar o contexto do usuário corretamente ao finalizar a syscall.

Esse mecanismo garante a integridade da troca de contexto entre usuário e kernel, permitindo que o kernel execute chamadas de sistema de forma segura e transparente para o programa usuário.

### UNWIND_HINT_ENTRY
Em cada chamada de função, o endereço de retorno e, às vezes, o valor do ponteiro de quadro (frame pointer) são empilhados. O stack unwinding consiste em percorrer esses dados para reconstruir a sequência de chamadas. No passado, o kernel e aplicações dependiam do registrador de frame pointer (RBP), mas hoje, para aumentar o desempenho e reduzir o uso de registradores, o kernel Linux utiliza formatos como o ORC (Omnidirectional Resource Counter), que armazena metadados sobre o layout da pilha em uma seção especial do executável, permitindo desenrolar a pilha sem depender do frame pointer


Aplicação no kernel:
O marcador UNWIND_HINT_ENTRY no seu exemplo serve para instruir o sistema de desenrolamento de pilha (stack unwinder) sobre o ponto de entrada da função, facilitando a análise em caso de falha ou depuração

### CET
CET é uma tecnologia de segurança implementada em hardware (principalmente em CPUs Intel) para prevenir ataques de desvio de fluxo de controle, como ROP (Return-Oriented Programming), JOP (Jump-Oriented Programming) e COP (Call-Oriented Programming)

Principais componentes:

	Shadow Stack:
	Uma pilha secundária, protegida e invisível para o programa, que armazena cópias dos endereços de retorno. Quando uma função retorna, o processador compara o endereço de retorno da pilha principal com o da shadow stack. Se forem diferentes, gera uma exceção, impedindo ataques que tentam manipular a pilha para redirecionar o fluxo de execução

	Indirect Branch Tracking (IBT):
	Usa instruções especiais (como ENDBR) para marcar destinos válidos de saltos indiretos. Antes de realizar um salto indireto, o processador verifica se o destino possui o marcador correto. Se não tiver, o salto é bloqueado, prevenindo ataques que tentam desviar o fluxo para código malicioso


Aplicação no kernel:
O uso de ENDBR no seu código é um exemplo de IBT, onde o kernel marca pontos de entrada válidos para saltos indiretos, aumentando a proteção contra exploração de vulnerabilidades

### swapgs
O que o SWAPGS faz?

    Troca do GS base:
    O SWAPGS troca o valor do registrador base do segmento GS (um valor “escondido” usado para calcular endereços quando se usa o prefixo gs:) com o valor armazenado no MSR chamado IA32_KERNEL_GS_BASE (endereço MSR C0000102h)


Objetivo:
Isso permite que o kernel, ao entrar via syscall, tenha acesso imediato a uma área de dados específica para a CPU atual, sem precisar salvar registradores ou acessar memória antes de configurar a pilha do kernel


Uso típico:
O kernel usa o prefixo gs: para acessar variáveis per-CPU, como o ponteiro da pilha do kernel, identificador da tarefa atual, etc. Isso é feito logo após a entrada no kernel, antes de configurar a pilha do kernel


Por que é necessário?

    syscall não configura a pilha do kernel:
    Ao contrário de interrupções, a instrução syscall não configura automaticamente a pilha do kernel. O kernel precisa de um meio rápido para acessar dados locais da CPU para saber qual pilha usar.

    Sem registro livre:
    No momento da entrada no kernel, todos os registradores estão ocupados com valores do espaço do usuário. O SWAPGS permite acessar dados per-CPU sem destruir nenhum registrador

### TSS
O Task State Segment (TSS) é uma estrutura de dados específica da arquitetura x86 e x86-64, utilizada pelo sistema operacional para armazenar informações essenciais sobre uma tarefa (task) e facilitar a troca de contexto, principalmente durante interrupções, exceções e mudanças de nível de privilégio

### Troca de CR3
O que é o CR3?

    O CR3 é um registrador especial usado pela CPU para apontar para a Page Global Directory (PGD), que é a raiz das tabelas de páginas que traduzem endereços virtuais em físicos.

    Cada processo (ou contexto) tem sua própria tabela de páginas, que define o mapeamento da memória virtual para física.

    Em sistemas modernos, o kernel Linux implementa Page Table Isolation (PTI) para mitigar vulnerabilidades como Meltdown, mantendo duas tabelas de páginas separadas: uma para o espaço do usuário e outra para o espaço do kernel.

Por que trocar o CR3?

    Quando ocorre uma transição do espaço usuário para o kernel (por exemplo, numa syscall), o kernel precisa usar sua própria tabela de páginas para garantir que o acesso à memória seja seguro e que áreas do kernel não fiquem expostas ao usuário.

    Para isso, o kernel troca o valor do CR3 para apontar para sua tabela de páginas.

    Ao retornar para o usuário, o CR3 é trocado novamente para a tabela de páginas do processo usuário.


### IBRS, UNTRAIN_RET, CLEAR_BRANCH_HISTORY
IBRS significa Indirect Branch Restricted Speculation.
É uma mitigação de hardware para a Spectre v2, vulnerabilidade que permite a um atacante explorar a execução especulativa para vazar dados entre processos ou entre usuário e kernel.

Como funciona:

    Ativa restrições na execução especulativa:
    Quando ativado, o IBRS impede que a CPU siga ramificações indiretas (indirect branches) de forma especulativa após uma troca de contexto, evitando que um ataque explore o histórico de branches de outro processo ou modo de privilégio.

    Implementação:
    No código, IBRS_ENTER é uma macro que executa as instruções necessárias para ativar o IBRS no processador (por exemplo, usando a instrução wrmsr para escrever em um MSR específico).


UNTRAIN_RET é uma mitigação para ataques de Branch History Injection (BHI).

Como funciona:

    BHI:
    É uma variante de Spectre v2 que explora o histórico de branches (branch history) para influenciar a execução especulativa.

    UNTRAIN_RET:
    A macro executa uma sequência de instruções que "limpa" o histórico de branches do preditor de saltos da CPU, tornando mais difícil para um atacante influenciar a execução especulativa.

    Detalhe técnico:
    Normalmente envolve a execução de uma sequência de retornos (ret) controlados para “confundir” o preditor de saltos.


CLEAR_BRANCH_HISTORY é outra mitigação para ataques de especulação, especialmente Spectre v2 e variantes.

Como funciona:

    Limpa o histórico de branches:
    Essa macro executa instruções que forçam a CPU a limpar o histórico de branches do preditor de saltos (Branch Prediction Buffer).

    Objetivo:
    Impedir que um ataque explore informações residuais no preditor de saltos para vazar dados entre contextos de execução.

    Detalhe técnico:
    Pode envolver a execução de uma sequência de saltos controlados ou o uso de instruções específicas do processador para limpar o buffer de predição.
