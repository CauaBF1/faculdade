/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 05/08/2024
Data de modificação: 05/08/2024
Objetivo: Receber preço e quantidade de DVDs, e retornar o valor total no estoque e o preço medio
*******************************************************************************/
#include <stdio.h>
#define MAX_DVD 100
int main()
{
    double price[MAX_DVD], valorTotal = 0, precoMedio;
    int quant[MAX_DVD], i = 0, j, totalDVD = 0;
    
    do{
        printf("Digite o preço do DVD:");
        scanf("%lf", &price[i]);
        printf("Digite a quantidade do DVD: ");
        scanf("%d", &quant[i]);
        
        if(price[i] != 0 || quant[i] != 0){
            i++;
        }else{
            break;
        }
    }while (i < MAX_DVD);
    
    for (j = 0; j <= i; j++){
        valorTotal += price[j] * quant[j];
        totalDVD += quant[j];
    }
    
    precoMedio = valorTotal / totalDVD;
    
    if(totalDVD != 0){
        printf("Valor em estoque: R$ %.2lf\n", valorTotal);
        printf("Preço medio: R$ %.2lf", precoMedio);
    }else{
        printf("Lista vazia");
    }
}
