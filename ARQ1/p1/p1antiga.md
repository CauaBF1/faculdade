# P1 2 semestre 2023
---

## Exercicio 1
Programa MIPS assembly para verificar se no codigo binario do numero X, a dois digitos Xî e Xî+1 iguais a 1, informar o menor indicice que ocorre essa repetição, X esta no registrador $8, e o indice I deve ser colocado no registrador $9. caso tal repetição nao exista registrador $9 deve receber 0xFFFFFFFF.

### Resposta:

```asm

addi $t1, $zero, 0xFF // mascara sobre os dois ultimos bits
addi $t3, $zero, 0 // gera contador na posição 0
addi $9, $zero, -1 // 0xFFFFFFF

(loop)
	and $t2, $8, $t1 // caso dois ultimos bits do $8 sejam 1
	beq $t2, $t1, achou
	srl $8, $8, 1 // desloco um bit do numero X	
	addi $t3, $t3, 1 // proximo indice
	bne $8, $zero, loop
	j fim 

(achou)
	addi $t3, $zero, 1 // soma 1 caso achou mostrando proximo indice
	add $9, $zero, $t3 // passa indice para registrador 9

(fim)
	end


# Nao precisa desse errou se colocar $9 como -1 padrao
#(errou)
#	bne $8, $zero, loop
#	addi $9, $zero, 0xFF_FF_FF_FF
```

**Funcionando MARS**

```asm
.data

.text

.macro end
	li $v0, 10
	syscall
.end_macro

.globl main

main:
	li $t8, 0x01200160 # 0000_0001_0010_0000_0000_0001_0110_0000 deve retornar posição 6
	li $t0, -1 # valor padrao dentro do $9
	addi $t1, $zero, 3 # valor 011 para mascara
	addi $t2, $zero, 0 #contador de indice

loop:
	and $t3, $t1, $t8 # verifico os dois bits do meu numero X(t8)
	beq $t3, $t1, achou # se meu $t3 voltar 11 é pq achou
	addi $t2, $t2, 1 #aumento meu contador 
	srl $t8, $t8, 1 # desloco um bit p direita
	bne $t8, $zero, loop # se $8 virou zero é pq ja deslocou tudo
	j fim
	
achou:
	addi $t2, $t2, 1
	add $t0, $zero,$t2 #coloca contador no $9($t0)

fim:
	end 
```

## Exercicio 2
---
Considere um computador MC. Sua arquitetura é do tipo registrador-registrador. No ciclo de busca somente uma leitura é executada. A memória é endereçada byte-a-byte e alinhada. Alguns outros parametros de seu projetor são:
 - NR: numero de registradores acessador pelo programador
 - NRI: numero de bits do registrador de instrução
 - NINST: numero de instruções distintas

Considere que a arquitetura adota a estratégia de endereçamento por deslocamento. Neste caso, apresente uma expressão para variavel X, em termos dos parametros acima (NR, NRI e NINST), que represente o maior deslocamento possivel, ou seja, qual a máxima distância possível que pode ser atingida em termos de endereço, a partir do registrador base. Aprensete uma expressão para Y, em termos dos parâmetros acima (NR, NRI e NINST), que represente o numero de palavras podem ser lidas, tomando-se endenreços positivos a partir do mesmo conteúdo do registrador base e variando-se o deslocamento(valor imediato).

obs: considere NR e NINST sejam potências de 2 (para efeitors de facilitar a representação das relações solicitadas).
obs: Considere que cada palavra corresponda a Z Bytes

### Resposta:
X = maxima distancia que pode ser atingida em termos de endereço a partir do registrador base
Y = numero de palavras podem ser lidas tomando-se endenreços positivos a partir do mesmo conteúdo do registrador base e variando-se o deslocamento(valor imediato).

Para calcular o maior deslocamento é necessario ver que 
NRI = log²(NINST) + 3*log²(NR) + bits deslocamento 
em que log²(NINST) é o opcode  e 3*(log²(NR)) é numero de bits de tres registradores(rs, rt, rd), sobrando assim o numero de bits que simboliza o deslocamento, portanto

bits deslocamento = NRI - log²(NISNT) - 3*log²(NR) -1 
X = 2^bits deslocamento - 1 
2 para ser complemento de 2 e -1 porque primeiro bit é usado para simbolizar o sinal

subtraímos 1 novamente para alinhar com índices ou endereços baseados em deslocamento. Isso geralmente acontece quando trabalhamos com endereços baseados em índices de array ou deslocamentos relativos.

_________________________________________________________________________________________________________

cada palavra ocupa Z bytes, maximo de palavras é o numero maximo de deslocamento + 1 / z
Y = 2^(NRI - log²(NISNT) - 3*log²(NR)-1  -1) + 1 / z


Exemplo:

NRI = 32 bits
NINST = 64
NR = 16
Z = 4 bytes

X = 2^[32 - log²(64) - 3*log²(NR) - 1] - 1
X = 2^[32 - 6 - 3*(4) - 1] -1
X = 2¹⁶ -1
X = 65535 bytes é o deslocamento maximo(distancia maxima)

Y = (65535 + 1) /4
Y =  16384 palavras



