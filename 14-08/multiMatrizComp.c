/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo: Multiplicação de matrizes
*****************************************************************************/

#include <stdio.h>

int main(){

	// Declaração de variaveis
	int nLinhas1, nColunas1, nColunas2, linhaMult, colunaMult;
	
	// Entrada do numero de linhas e de colunas das matrizes
	printf("Digite o numero de linhas da matriz1: ");
	scanf("%d", &nLinhas1);
	printf("Digite o numero de colunas da matriz1(mesmo numero de linhas da matriz2): ");
	scanf("%d", &nColunas1);
	printf("Digite o numero de colunas da matriz2: ");
	scanf("%d", &nColunas2);
	
    // Declaração das matrizes
	double matriz1[nLinhas1][nColunas1];
	double matriz2[nColunas1][nColunas2];
	double resultado[nLinhas1][nColunas2];

    // Entrada de dados das matrizes
   
	 for (int i = 0; i < nLinhas1; i++) {
     	   for (int j = 0; j < nColunas2; j++) {
            resultado[i][j] = 0;
        }
    }

	for(int i = 0; i<nLinhas1; i++){
		for(int j = 0; j<nColunas1;j++){
			printf("Digite o elemento [%d][%d] da matriz1: ", i, j);
			scanf("%lf", &matriz1[i][j]);
		}
	}

	for(int i = 0; i<nColunas1; i++){
		for(int j = 0; j<nColunas2;j++){
			printf("Digite o elemento [%d][%d] da matriz2: ", i, j);
			scanf("%lf", &matriz2[i][j]);
		}
	}


    // Calculo da multiplicação das matrizes
   	for(int i = 0; i<nLinhas1;i++){
		for(int j = 0; j < nColunas2; j++){
			for(int k = 0; k < nColunas1; k++){
				resultado[i][j] += matriz1[i][k] * matriz2[k][j]; 
			}
		}
	}	
    // Exibição do resultado
	printf("Resultado da multiplicação das matrizes:\n");
    for (int i = 0; i < nLinhas1; i++) {
        for (int j = 0; j < nColunas2; j++) {
            printf("%.2lf ", resultado[i][j]);
        }
        printf("\n");
    }

}


