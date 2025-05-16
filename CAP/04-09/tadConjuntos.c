/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 04/09/24
Data de modificação: 04/09/24
Objetivo: Implemente as operações de um Tipo Abstrato de Dados (TAD) Conjunto. O conjunto irá armazenar números reais (double).
*******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 1000

typedef struct {
    double elementos[MAX];
    int nElementos;
} tConjunto;

// Protótipos das funções
void iniciarConjunto(tConjunto *c);
void inserirElemento(tConjunto *c);
void inserirVariosElementos(tConjunto *c);
void mostrarElementosDesor(tConjunto c);
void ordenarConjunto(tConjunto *c);
void mostrarElementosOrd(tConjunto *c);
void removerElemento(tConjunto *c, double elemento);
void verificarVazio(tConjunto c);
int quantElementos(tConjunto c);
void valorArmazenado(tConjunto c, double elemento);
int elementoExiste(tConjunto c, double elemento);
tConjunto uniaoConjuntos(tConjunto c1, tConjunto c2);
tConjunto intersecConjuntos(tConjunto c1, tConjunto c2);
tConjunto difConjuntos(tConjunto c1, tConjunto c2);
int estaContido(tConjunto a, tConjunto b);
int estaContidoOuIgual(tConjunto a, tConjunto b);
int contemConjunto(tConjunto a, tConjunto b);
int contemOuIgual(tConjunto a, tConjunto b);
int saoIguais(tConjunto a, tConjunto b);

int main() {
    tConjunto c1, c2, c3, c4, c5;
    iniciarConjunto(&c1);
    inserirVariosElementos(&c1);

    verificarVazio(c1);
    printf("Elementos do primeiro conjunto (desordenados): ");
    mostrarElementosDesor(c1);
    ordenarConjunto(&c1);
    printf("Conjunto ordenado: ");
    mostrarElementosOrd(&c1);
    double elemento;
    printf("Digite o elemento que deseja verificar: ");
    scanf("%lf", &elemento);
    valorArmazenado(c1, elemento);
    
    printf("Digite o elemento que deseja remover: ");
    scanf("%lf", &elemento);
    removerElemento(&c1, elemento);
    printf("Elementos após remoção: ");
    mostrarElementosDesor(c1);
    
    // Operações com 2 conjuntos
    printf("\nDados do segundo conjunto:\n");
    iniciarConjunto(&c2);
    inserirVariosElementos(&c2);
    
    verificarVazio(c2);
    printf("Elementos do segundo conjunto (desordenados): ");
    mostrarElementosDesor(c2);
    ordenarConjunto(&c2);
    printf("Segundo conjunto ordenado: ");
    mostrarElementosOrd(&c2);
    
    // Realizar a união dos conjuntos
    c3 = uniaoConjuntos(c1, c2);
    printf("\nUnião dos conjuntos (desordenada): ");
    mostrarElementosDesor(c3);
    ordenarConjunto(&c3);
    printf("União dos conjuntos ordenada: ");
    mostrarElementosOrd(&c3);
    
    // Realizar a interseção dos conjuntos
    c4 = intersecConjuntos(c1, c2);
    printf("\nInterseção dos conjuntos: ");
    mostrarElementosDesor(c4);
    
    // Realizar a diferença entre os conjuntos
    c5 = difConjuntos(c1, c2);
    printf("\nDiferença dos conjuntos (c1 - c2): ");
    mostrarElementosDesor(c5);
    
    // Verificar relações entre os conjuntos
    if (estaContido(c1, c2)) {
        printf("Conjunto c1 está contido em c2.\n");
    }
    if (estaContidoOuIgual(c1, c2)) {
        printf("Conjunto c1 está contido ou é igual a c2.\n");
    }
    if (contemConjunto(c1, c2)) {
        printf("Conjunto c1 contém c2.\n");
    }
    if (contemOuIgual(c1, c2)) {
        printf("Conjunto c1 contém ou é igual a c2.\n");
    }
    if (saoIguais(c1, c2)) {
        printf("Conjuntos c1 e c2 são iguais.\n");
    }
    
    return 0;
}

// Funções de manipulação de conjunto e verificação de relações

void iniciarConjunto(tConjunto *c) {
    c->nElementos = 0;
}

void inserirElemento(tConjunto *c) {
    if (c->nElementos < MAX) {
        printf("Digite o elemento que deseja inserir: ");
        scanf("%lf", &c->elementos[c->nElementos]);
        c->nElementos++;
    } else {
        printf("Conjunto está cheio!\n");
    }
}

void inserirVariosElementos(tConjunto *c) {
    char continuar = 'S';
    while (continuar == 'S' && c->nElementos < MAX) {
        inserirElemento(c);
        printf("Deseja inserir outro elemento? [S/N]: ");
        scanf(" %c", &continuar);
        continuar = toupper(continuar);  // Converte para maiúscula 
    }
}

void mostrarElementosDesor(tConjunto c) {
    for (int i = 0; i < c.nElementos; i++) {
        printf("%.2lf ", c.elementos[i]);  
    }
    printf("\n");
}

void ordenarConjunto(tConjunto *c) {
    double temp;
    for (int i = 0; i < c->nElementos - 1; i++) {
        for (int j = i + 1; j < c->nElementos; j++) {
            if (c->elementos[i] > c->elementos[j]) {
                temp = c->elementos[i];
                c->elementos[i] = c->elementos[j];
                c->elementos[j] = temp;
            }
        }
    }
}

void mostrarElementosOrd(tConjunto *c) {
    ordenarConjunto(c);
    for (int i = 0; i < c->nElementos; i++) {
        printf("%.2lf ", c->elementos[i]);  
    }
    printf("\n");
}

void removerElemento(tConjunto *c, double elemento) {
    int posicao = -1;
    for (int i = 0; i < c->nElementos; i++) {
        if (c->elementos[i] == elemento) {
            posicao = i;
            break;
        }
    }

    if (posicao != -1) {  // Elemento encontrado
        for (int i = posicao; i < c->nElementos - 1; i++) {
            c->elementos[i] = c->elementos[i + 1];
        }
        c->nElementos--;
        printf("Elemento %.2lf removido com sucesso.\n", elemento);
    } else {
        printf("Elemento %.2lf não encontrado no conjunto.\n", elemento);
    }
}

void verificarVazio(tConjunto c) {
    if (c.nElementos == 0) {
        printf("Conjunto vazio\n");
    } else {
        printf("Conjunto não está vazio\n");  
    }
}

int quantElementos(tConjunto c) {
    return c.nElementos;
}

void valorArmazenado(tConjunto c, double elemento) {
    int encontrado = 0;
    for (int i = 0; i < c.nElementos; i++) {
        if (c.elementos[i] == elemento) {
            encontrado = 1;
            break;
        }      
    }
    if (encontrado) {
        printf("Elemento: %.2lf está no conjunto\n", elemento);
    } else {
        printf("Elemento: %.2lf não está no conjunto\n", elemento);
    }
}

int elementoExiste(tConjunto c, double elemento) {
    for (int i = 0; i < c.nElementos; i++) {
        if (c.elementos[i] == elemento) {
            return 1; // Encontrado
        }
    }
    return 0; // Não encontrado
}

tConjunto uniaoConjuntos(tConjunto c1, tConjunto c2) {
    tConjunto c3;
    iniciarConjunto(&c3);

    // Adicionar todos os elementos de c1 a c3
    for (int i = 0; i < c1.nElementos; i++) {
        c3.elementos[c3.nElementos++] = c1.elementos[i];
    }

    // Adicionar elementos de c2 que não estão em c3
    for (int i = 0; i < c2.nElementos; i++) {
        double elem = c2.elementos[i];
        if (!elementoExiste(c3, elem)) {
            if (c3.nElementos < MAX) {
                c3.elementos[c3.nElementos++] = elem;
            } else {
                printf("Conjunto união atingiu o tamanho máximo!\n");
                break;
            }
        }
    }
    return c3;
}

tConjunto intersecConjuntos(tConjunto c1, tConjunto c2) {
    tConjunto c3;
    iniciarConjunto(&c3);

    for (int i = 0; i < c1.nElementos; i++) {
        if (elementoExiste(c2, c1.elementos[i])) {
            if (c3.nElementos < MAX) {
                c3.elementos[c3.nElementos++] = c1.elementos[i];
            } else {
                printf("Conjunto interseção atingiu o tamanho máximo!\n");
                break;
            }
        }
    }
    return c3;
}

tConjunto difConjuntos(tConjunto c1, tConjunto c2) {
    tConjunto c3;
    iniciarConjunto(&c3);

    for (int i = 0; i < c1.nElementos; i++) {
        if (!elementoExiste(c2, c1.elementos[i])) {
            if (c3.nElementos < MAX) {
                c3.elementos[c3.nElementos++] = c1.elementos[i];
            } else {
                printf("Conjunto diferença atingiu o tamanho máximo!\n");
                break;
            }
        }
    }
    return c3;
}

int estaContido(tConjunto a, tConjunto b) {
    for (int i = 0; i < a.nElementos; i++) {
        if (!elementoExiste(b, a.elementos[i])) {
            return 0; // Se encontrar um elemento de A que não está em B, retorna falso
        }
    }
    return 1; // Se todos os elementos de A estão em B, retorna verdadeiro
}

int estaContidoOuIgual(tConjunto a, tConjunto b) {
    return estaContido(a, b);
}

int contemConjunto(tConjunto a, tConjunto b) {
    return estaContido(b, a);
}

int contemOuIgual(tConjunto a, tConjunto b) {
    return estaContidoOuIgual(b, a);
}

int saoIguais(tConjunto a, tConjunto b) {
    return estaContido(a, b) && estaContido(b, a);
}

