/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 02/09/24
Data de modificação: 02/09/24
Objetivo: Manipulação de números racionais.
*******************************************************************************/

#include <stdio.h>

// Definição do tipo de dado para um número racional
typedef struct {
    int n; // numerador
    int d; // denominador
} tRacional;

// Protótipos das funções
void lerRacional(tRacional *r);
void escreverRacional(tRacional r);
void simplificarRacional(tRacional *r);
tRacional somarRacionais(tRacional r1, tRacional r2);
tRacional subtrairRacionais(tRacional r1, tRacional r2);
tRacional multiplicarRacionais(tRacional r1, tRacional r2);
tRacional dividirRacionais(tRacional r1, tRacional r2);
int calcularMDC(int a, int b);

/******************************************************************************
Função Principal
Objetivo: Realizar operações com números racionais.
*******************************************************************************/
int main() {
    tRacional r1, r2, resultado;

    // Leitura do primeiro número racional
    printf("Leitura do primeiro numero racional:\n");
    lerRacional(&r1);

    // Leitura do segundo número racional
    printf("Leitura do segundo numero racional:\n");
    lerRacional(&r2);

    // Exibir números racionais lidos
    printf("Primeiro numero racional: ");
    escreverRacional(r1);

    printf("Segundo numero racional: ");
    escreverRacional(r2);

    // Soma
    resultado = somarRacionais(r1, r2);
    printf("Soma: ");
    escreverRacional(resultado);

    // Subtração
    resultado = subtrairRacionais(r1, r2);
    printf("Subtracao: ");
    escreverRacional(resultado);

    // Multiplicação
    resultado = multiplicarRacionais(r1, r2);
    printf("Multiplicacao: ");
    escreverRacional(resultado);

    // Divisão
    resultado = dividirRacionais(r1, r2);
    printf("Divisao: ");
    escreverRacional(resultado);

    return 0;
}

/******************************************************************************
Sub-rotina: calcularMDC
Objetivo: Calcular o MDC pelo teorema de Euclides.
Parâmetros:
- Parâmetro1: inteiro A
- Parâmetro2: inteiro B
Retorno: Valor do MDC.
*******************************************************************************/
int calcularMDC(int a, int b) {
    while (b != 0) {
        int resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

/******************************************************************************
Sub-rotina: lerRacional
Objetivo: Ler um número racional e simplificá-lo.
Parâmetros:
- Parâmetro1: ponteiro para tRacional r (número racional a ser lido)
Retorno: nenhum (modifica o número racional via ponteiro).
*******************************************************************************/
void lerRacional(tRacional *r) {
    printf("Digite o numerador: ");
    scanf("%d", &r->n);
    do {
        printf("Digite o denominador (diferente de zero): ");
        scanf("%d", &r->d);
    } while (r->d == 0);

    simplificarRacional(r);

    if (r->d < 0) {
        r->n = -r->n;
        r->d = -r->d;
    }
}

/******************************************************************************
Sub-rotina: escreverRacional
Objetivo: Exibir um número racional na forma "numerador/denominador".
Parâmetros:
- Parâmetro1: tRacional r (número racional a ser exibido)
Retorno: nenhum (apenas exibe o número).
*******************************************************************************/
void escreverRacional(tRacional r) {
    printf("%d/%d\n", r.n, r.d);
}

/******************************************************************************
Sub-rotina: simplificarRacional
Objetivo: Simplificar um número racional para sua forma mais básica.
Parâmetros:
- Parâmetro1: ponteiro para tRacional r (número racional a ser simplificado)
Retorno: nenhum (modifica o número racional via ponteiro).
*******************************************************************************/
void simplificarRacional(tRacional *r) {
    int mdc = calcularMDC(r->n, r->d);
    r->n /= mdc;
    r->d /= mdc;

    if (r->d < 0) {
        r->n = -r->n;
        r->d = -r->d;
    }
}

/******************************************************************************
Sub-rotina: somarRacionais
Objetivo: Somar dois números racionais e simplificar o resultado.
Parâmetros:
- Parâmetro1: tRacional r1 (primeiro número racional)
- Parâmetro2: tRacional r2 (segundo número racional)
Retorno: tRacional (resultado da soma).
*******************************************************************************/
tRacional somarRacionais(tRacional r1, tRacional r2) {
    tRacional resultado;
    resultado.n = r1.n * r2.d + r2.n * r1.d;
    resultado.d = r1.d * r2.d;
    simplificarRacional(&resultado);
    return resultado;
}

/******************************************************************************
Sub-rotina: subtrairRacionais
Objetivo: Subtrair dois números racionais e simplificar o resultado.
Parâmetros:
- Parâmetro1: tRacional r1 (primeiro número racional)
- Parâmetro2: tRacional r2 (segundo número racional)
Retorno: tRacional (resultado da subtração).
*******************************************************************************/
tRacional subtrairRacionais(tRacional r1, tRacional r2) {
    tRacional resultado;
    resultado.n = r1.n * r2.d - r2.n * r1.d;
    resultado.d = r1.d * r2.d;
    simplificarRacional(&resultado);
    return resultado;
}

/******************************************************************************
Sub-rotina: multiplicarRacionais
Objetivo: Multiplicar dois números racionais e simplificar o resultado.
Parâmetros:
- Parâmetro1: tRacional r1 (primeiro número racional)
- Parâmetro2: tRacional r2 (segundo número racional)
Retorno: tRacional (resultado da multiplicação).
*******************************************************************************/
tRacional multiplicarRacionais(tRacional r1, tRacional r2) {
    tRacional resultado;
    resultado.n = r1.n * r2.n;
    resultado.d = r1.d * r2.d;
    simplificarRacional(&resultado);
    return resultado;
}

/******************************************************************************
Sub-rotina: dividirRacionais
Objetivo: Dividir dois números racionais e simplificar o resultado.
Parâmetros:
- Parâmetro1: tRacional r1 (primeiro número racional)
- Parâmetro2: tRacional r2 (segundo número racional)
Retorno: tRacional (resultado da divisão).
*******************************************************************************/
tRacional dividirRacionais(tRacional r1, tRacional r2) {
    tRacional resultado;
    resultado.n = r1.n * r2.d;
    resultado.d = r1.d * r2.n;

    if (resultado.d == 0) {
        printf("Erro: divisao por zero.\n");
        resultado.n = 0;
        resultado.d = 1;
    } else {
        simplificarRacional(&resultado);
    }

    return resultado;
}

