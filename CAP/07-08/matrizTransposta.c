/******************************************************************************
Autor: Cauã Borges Faria (834437)
Data de Criação: 07/08/24
Data de Alteração: 07/08/24
Objetivo: Leia os elementos de uma matriz de números reais e depois mostre a matriz transposta.
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
    double elemento[nLinhas][nColunas];
    double transposta[nColunas][nLinhas];
    
    // Recebendo os elementos da matriz 
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("Digite o elemento da matriz [%d][%d]", i, j);
            scanf("%lf", &elemento[i][j]);
        }
    }
    
    //Transpondo a matriz
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            transposta[j][i] = elemento[i][j];
        }
    }
    
    //Mostrando matriz original
    printf("Matriz original:\n ");
    for(int i = 0; i < nLinhas; i++){
        for(int j = 0; j < nColunas; j++){
            printf("%7.2lf ", elemento[i][j]);
        }
        printf("\n");
    }
    
    // Mostrando matriz transposta
    printf("Matriz Transposta:\n");
    for(int i = 0; i < nColunas; i++){
        for(int j = 0; j < nLinhas; j++){
            printf("%7.2lf ", transposta[i][j]);
        }
        printf("\n");
    }
}