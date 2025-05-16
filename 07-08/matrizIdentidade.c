/******************************************************************************
Autor: Cauã Borges Faria (834437)
Data de Criação: 07/08/24
Data de Alteração: 07/08/24
Objetivo: Leia os elementos de uma matriz de números reais e depois verifique se a matriz é uma matriz identidade.
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
    
    
    // Validando se matriz é quadrada
    if(nLinhas != nColunas){
        printf("Não é uma matriz identidade");
    }else{
    
        // Declarando matriz
        int elemento[nLinhas][nColunas];
    
        // Recebendo cada elemento da matriz
        for(int i = 0; i < nLinhas; i++){
            for(int j =0; j < nColunas; j++){
                printf("Digite os numeros da matriz[%d][%d]: ", i, j);
                scanf("%d", &elemento[i][j]);
            }
        }
    
        // Validando se é uma matriz identidade
        for(int i = 0; i < nLinhas; i++){
            for(int j = 0; j < nColunas; j++){
                if(i == j && elemento[i][j] != 1){
                    identidade = 0;
                    break;
                }else if(i != j && elemento[i][j] != 0){
                    identidade = 0;
                    break;
                }else{
                    identidade = 1;
                }
            }

	     if (!identidade){
                break;
            }
        }
    
        // Mostrando resultado
        if(identidade == 1){
            printf("È uma matriz identidade");
        }else{
            printf("Não é uma matriz identidade");
        }
    }
}
