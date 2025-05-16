/*
Autor: Cauã Borges Faria(834437)
Data de criação: 16/09/24
Data de modificação: 16/09/24
Objetivo: Com sub-rotinas verificar se é palavrinha ou palavrão
*/

#include <stdio.h>

// Declaração do protótipo da função
void palavras(char palavra[20]);  

int main() {
    // Declaração da palavra
    char palavra[20];
    
    // Lê a palavra de entrada
    scanf("%s", palavra);
    
    // Chama a função para verificar se é "palavrinha" ou "palavrão"
    palavras(palavra);
    
    return 0;
}

// Função para verificar o tamanho da palavra
void palavras(char palavra[20]) {
    int sizePalavra = 0;
    
    // Conta o número de caracteres até o '\0'
    for (int i = 0; i < 20; i++) {
        if (palavra[i] == '\0') {
            break;
        }
        sizePalavra++;
    }

    // Verifica se o tamanho da palavra é maior ou igual a 10
    if (sizePalavra >= 10) {
        printf("palavrao\n");
    } else {
        printf("palavrinha\n");
    }
}

