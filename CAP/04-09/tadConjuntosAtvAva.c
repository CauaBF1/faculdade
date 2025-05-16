/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 04/09/24
Data de modificação: 04/09/24
Objetivo: inserir elemento no Conjunto e inserir vários elementos no Conjunto
*******************************************************************************/
#include <stdio.h>
#include <string.h>
#define MAX 1000


typedef struct {
    double elementos[MAX];
    int nElementos;
} tConjunto;

// Protótipos das funções
void iniciarConjunto(tConjunto *c);
void inserirElemento(tConjunto *c);
void inserirVariosElementos(tConjunto *c);
void mostrarElementosDesor(tConjunto c1);

// Função principal
int main() {
    // Cria o primeiro conjunto
    tConjunto c1;
    // Incia o conjunto como um conjunto vazio
    iniciarConjunto(&c1);
    // Inserir elementos no conjunto
    inserirVariosElementos(&c1);
    // Mostrar elementos de forma desordenada
    mostrarElementosDesor(c1);

    return 0;
}


/*
Sub-rotina: iniciarConjunto
Objetivo: Inicializa o conjunto, definindo o número de elementos como zero.
Parâmetros:
- c: Ponteiro para um objeto do tipo tConjunto (entrada/saída de dados)
Valor de Retorno:
- Nenhum
*/
void iniciarConjunto(tConjunto *c) {
    c->nElementos = 0;
}

/*
Sub-rotina: inserirElemento
Objetivo: Insere um elemento no conjunto, desde que não esteja cheio.
Parâmetros:
- c: Ponteiro para um objeto do tipo tConjunto (entrada/saída de dados)
Valor de Retorno:
- Nenhum
*/
void inserirElemento(tConjunto *c) {
    if (c->nElementos < MAX) {
        printf("Digite o elemento que deseja inserir: ");
        scanf("%lf", &c->elementos[c->nElementos]);
        c->nElementos++;
    } else {
        printf("Conjunto está cheio!\n");
    }
}

/*
Sub-rotina: inserirVariosElementos
Objetivo: Permite ao usuário inserir múltiplos elementos no conjunto até que o usuário escolha parar ou o conjunto esteja cheio.
Parâmetros:
- c: Ponteiro para um objeto do tipo tConjunto (entrada/saída de dados)
Valor de Retorno:
- Nenhum
*/
void inserirVariosElementos(tConjunto *c) {
    char continuar[10] = "S";
    while ((strcasecmp(continuar, "S") == 0) && c->nElementos < MAX) {
        inserirElemento(c);
        printf("Deseja inserir outro elemento? [S/N]: ");
        scanf("%s", continuar);
    }
}

/*
Sub-rotina: mostrarElementosDesor
Objetivo: Exibe os elementos do conjunto de forma desordenada.
Parâmetros:
- c1: Objeto do tipo tConjunto (entrada de dados)
Valor de Retorno:
- Nenhum
*/
void mostrarElementosDesor(tConjunto c) {
    for (int i = 0; i < c.nElementos; i++) {
        printf("%.2lf ", c.elementos[i]);  
    }
    printf("\n");
}

