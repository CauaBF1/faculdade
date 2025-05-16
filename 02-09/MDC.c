/******************************************************************************

Autor: Cauã Borges Faria
Data de criação: 02/09/24
Data de modificação: 02/09/24
Objetivo: Calcular MDC.

*******************************************************************************/
#include <stdio.h>

// Usar função dentro da main
int calcularMDC(int, int);

// Função Principal
int main() {
    int num1, num2, mdc;

    // Solicita ao usuário que insira dois números inteiros separados por espaço
    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &num1, &num2);

    // Chama a função calcularMDC e armazena o resultado em mdc
    mdc = calcularMDC(num1, num2);

    // Exibe o resultado
    printf("O MDC de %d e %d é: %d\n", num1, num2, mdc);

    return 0;
}

/*
Sub-rotina: calcularMDC
Objetivo: calcular MDC pelo teorema de euclides
Parâmetros:
- Parâmetro1: inteiro A
- Parâmetro2: inteiro B
- Retorna = calculo MDC
*/
int calcularMDC(int a, int b) {
    // Enquanto b não for 0
    while (b != 0) {
        int resto = a % b; // Calcula o resto da divisão de a por b
        a = b;             // Atualiza a para b
        b = resto;         // Atualiza b para o resto
    }
    return a; // Retorna o valor de a, que é o MDC
}
