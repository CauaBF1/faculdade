/******************************************************************************

Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Mostre se numero é primo força bruta

*******************************************************************************/
#include <stdio.h>

#include <stdbool.h>


int main()
{
    // Declaração de variaveis
    int num, temp;
    bool primo = true;
    
    printf("Digite o numero: ");
    scanf("%d", &num);
    // Verificando se é primo
    if(primo < 2){
        primo = false;
    }
    for(int i =2; i < num; i++){
        temp = num % i;
        
        if(temp == 0){
            primo = false;
            break;
        }
    }
    // Exibindo resultado
    if(!primo){
        printf("Não primo");
    }else{
        printf("primo");
    }
}
