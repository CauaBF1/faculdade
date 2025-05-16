/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo:Maior valor da matriz.
******************************************************************************/

#include <stdio.h>
int main(){

	// Declaração de variaveis
	int nLinhas1, nColunas1;
	
	// Entrada do numero de linhas e de colunas da matriz
	printf("Digite o numero de linhas da matriz: ");
	scanf("%d", &nLinhas1);
	printf("Digite o numero de colunas da matriz: ");
	scanf("%d", &nColunas1);
	
    // Declaração da matriz
	double matriz1[nLinhas1][nColunas1];
    double vmaior;
    
    // Entrada de dados da matriz
	for(int i = 0; i<nLinhas1; i++){
		for(int j = 0; j<nColunas1;j++){
			printf("Digite o elemento [%d][%d] da matriz1: ", i, j);
			scanf("%lf", &matriz1[i][j]);
		}
	}

    // Calculo maior valor 
    vmaior = 0;
    for(int i = 0; i<nLinhas1; i++){
        for(int j = 0; j<nColunas1; j++){
            if (matriz1[i][j] > vmaior){
                vmaior = matriz1[i][j];
            }
        }
    }
    // Exibição da matriz e do maior valor
    printf("Matriz: \n");
    for(int i = 0; i < nLinhas1; i++){
        for(int j = 0; j < nColunas1; j++){
            printf("%.2lf ", matriz1[i][j]);
        }
    printf("\n");
    }
    printf("O maior valor é: %.2lf\n", vmaior);
}



