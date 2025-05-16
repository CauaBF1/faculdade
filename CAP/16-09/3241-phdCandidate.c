// Receber ou P=NP para retornar skipped ou uma expressão a+b(necessario sscanf para quebrar expressao e colocar em variaveis inteiras para realizar a soma

/*
Autor: Cauã Borges Faria(834437)
Data de criação: 16/09/24
Data de modificação: 16/09/24
Objetivo: Com sub-rotinas, resolva soma ou "skip" caso receba "P=NP"
*/

#include <stdio.h>
#include <string.h>

// Prototipo das funções
int verificaPNP(char []);
int soma(int, int);

int main() {
    // Varivel com numeros de testes
    int testcases;

    // Lê o número de casos de teste
    scanf("%d", &testcases);
    getchar();  // Remove o '\n' residual

    // Loop para cada caso de teste
    for (int i = 0; i < testcases; i++) {
        char input[20];
        // Lê a linha de entrada (ou "P=NP" ou uma soma "a+b")
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';  // Remove o '\n' da string

        // Usa a função verificaPNP para verificar se é "P=NP"
        if (verificaPNP(input)) {
            printf("skipped\n");
        } else {
            int a, b;
            // Faz a leitura dos dois números da expressão "a+b"
            sscanf(input, "%d+%d", &a, &b);
            // Chama a função de soma e imprime o resultado
            printf("%d\n", soma(a, b));
        }
    }

    return 0;
}


// Função para somar dois números
int soma(int a, int b) {
    return a + b;
}

// Função para verificar se a string é "P=NP"
int verificaPNP(char input[]) {
    // Retorna 1 se a string for "P=NP", 0 caso contrário
    if (strcmp(input, "P=NP") == 0) {
        return 1;
    }
    return 0;
}
