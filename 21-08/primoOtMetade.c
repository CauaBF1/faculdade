/******************************************************************************

Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Mostre se numero é primo otimizado n/2

*******************************************************************************/
#include <stdio.h>

#include <stdbool.h>


int main()
{
    // Declarando variaveis
    int num, temp;
    bool primo = true;
    
    // Recebendo entrada
    printf("Digite o numero: ");
    scanf("%d", &num);
    
    // Verificando se numero é primo
    if(num < 2){
        primo = false;
    }else{
        for(int i =2; i <= num/2; i++){
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
