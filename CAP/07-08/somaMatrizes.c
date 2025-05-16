/******************************************************************************
Autor: Cauã Borges Faria (834437)
Data de Criação: 07/08/24
Data de Alteração: 07/08/24
Objetivo: Leia os elementos de duas matrizes de números reais e depois mostre a soma delas.
*******************************************************************************/
#include <stdio.h>

int main()
{
    // Declarando variaveis e recebendo numero de linhas e de colunas
    int nLinhas, nColunas, quantElementos, identidade = 1;
    printf("Digite o numero de linhas: ");
    scanf("%d", &nLinhas);
    printf("Digite o numero de colunas: ");
    scanf("%d", &nColunas);
    
    // Declarando as matrizes
    double matriz1[nLinhas][nColunas];
    double matriz2[nLinhas][nColunas];
    double matriz3[nLinhas][nColunas];
    
    // Recebendo os elementos da matriz 
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("Digite o elemento da primeira matriz: [%d][%d]", i, j);
            scanf("%lf", &matriz1[i][j]);
        }
    }
    // Recebendo os elementos da 2 matriz 
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("Digite o elemento da segunda matriz: [%d][%d]", i, j);
            scanf("%lf", &matriz2[i][j]);
        }
    }
    
    //Somando as matrizes
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }
    
    //Mostrando primeira matriz 
    printf("Primeira matriz :\n ");
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("%7.2lf ", matriz1[i][j]);
        }
        printf("\n");
    }
    
    //Mostrando segunda matriz 
    printf("Segunda matriz:\n ");
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("%7.2lf ", matriz2[i][j]);
        }
        printf("\n");
    }
    
    // Mostrando soma das matrizes
    printf("Soma das matrizes:\n ");
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("%7.2lf ", matriz3[i][j]);
        }
        printf("\n");
    }

}
