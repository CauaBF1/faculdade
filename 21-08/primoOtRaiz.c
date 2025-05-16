/******************************************************************************

Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Mostre se numero é primo otimizado raiz de n

*******************************************************************************/
#include <stdio.h>
#include <math.h>
#include <stdbool.h>


int main()
{
    // Declaração de variaveis
    int num, temp;
    bool primo = true;
    // Entrada do numero
    printf("Digite o numero: ");
    scanf("%d", &num);
    
    // Verificando se numero é primo
    if(num < 2){
        primo = false;
    }else{
        for(int i =2; i <= sqrt(num); i++){
            if(num % i == 0){
                primo = false;
                break;
            }
        }
    }
    
    // Exibindo resultado
    if(!primo){
        printf("Não primo");
    }else{
        printf("primo");
    }
}
