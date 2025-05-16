/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo: Encontrar elemento na matriz
*****************************************************************************/

#include <stdio.h>

int main(){
    // Declaração de variaveis
	int elemento, nLinhas, nColunas, encontrado;
    
    // Receber numero de linhas e colunas da matriz
	printf("Digite o numero de linhas da matriz: ");
	scanf("%d", &nLinhas);

	printf("Digite o numero de colunas da matriz: ");
	scanf("%d", &nColunas);
    
    // Declarar a matriz
	int matriz[nLinhas][nColunas];
    
    // Entrada de dados da matriz
	for(int i = 0; i < nLinhas; i++){
		for(int j = 0; j < nColunas; j++){
			printf("Digite o elemento [%d] [%d] da matriz: ", i, j);
			scanf("%d", &matriz[i][j]); 
		}
	}
    
    // Elemento que deve ser procurado
	printf("Digite o elemento que deve ser procurado: ");
	scanf("%d", &elemento);
	
	// Ver se elemento esta presente na matriz
	for(int i = 0; i < nLinhas; i++){
		for(int j = 0; j < nColunas; j++){
			if(elemento == matriz[i][j]){
				printf("Elemento está presente na matriz, linha %d coluna %d\n", i+1, j+1);
			    encontrado = 1;
			}
			
		}
	}
    // Caso elemento não esteja na matriz
    if(!encontrado){
        printf("Elemento não está presente na matriz");
    }
	return 0;
}

