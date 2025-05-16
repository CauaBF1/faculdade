/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 12/08/2024
Data de modificação: 12/08/2024
Objetivo:multiplicação da linha i da matriz A com a coluna j da matriz B, ambas de ordem n x n (quadrática). Deve-se ler a ordem das matrizes, os elementos de cada matriz, realizar a multiplicação e por fim apresentar o resultado da multiplicação.
******************************************************************************/

#include <stdio.h>

int main(){

	// Declaração de variaveis
	int nLinhas, nColunas, linhaMult, colunaMult;
	
	// Entrada do numero de linhas e de colunas das matrizes
	printf("Digite o numero de linhas das matrizes: ");
	scanf("%d", &nLinhas);
	printf("Digite o numero de colunas das matrizes: ");
	scanf("%d", &nColunas);
	
    // Declaração das matrizes
	double matriz1[nLinhas][nColunas];
	double matriz2[nLinhas][nColunas];
	double res = 0;

    // Entrada de dados das matrizes
	for(int i = 0; i<nLinhas; i++){
		for(int j = 0; j<nColunas;j++){
			printf("Digite o elemento [%d][%d] da matriz1: ", i, j);
			scanf("%lf", &matriz1[i][j]);
		}
	}

	for(int i = 0; i<nLinhas; i++){
		for(int j = 0; j<nColunas;j++){
			printf("Digite o elemento [%d][%d] da matriz2: ", i, j);
			scanf("%lf", &matriz2[i][j]);
		}
	}

    // Escolha de qual linha e qual coluna devem ser multiplicadas
	printf("Escolha uma das linhas da primeira matriz: ");
	scanf("%d", &linhaMult);

	printf("Escolha uma das colunas da segunda matriz: ");
	scanf("%d", &colunaMult);

    // Calculo da multiplicação dos elementos da linha da matriz A com uma coluna da Matriz B
	for(int i = 0; i < nLinhas; i++){
		res = res + matriz1[linhaMult-1][i] * matriz2[i][colunaMult-1]; 
	}
    
    // Exibição do resultado
	printf("O resultado é: %.2lf", res);

}

