/******************************************************************************

Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Calcule e mostre os dados do vinho mais caro (nome, preço e tipo).

*******************************************************************************/
#include <stdio.h>
#include <string.h>

int main()
{
    // Declaração de variaveis
    char nome[50], tipo[50], nomeMaior[50], tipoMaior[50];
    double preco, precoMaior = 0;
    
    
    while(1){
        
        // Recebendo tipo do vinho
        printf("Digite o tipo do vinho (T = Tinto, B = Branco, R = Rosé ou FIM para parar): ");
        scanf("%s", tipo);
        
        // strcasecmp compara ignorando se esta em maiusculo ou minusculo
        if(strcasecmp(tipo, "FIM") == 0){
            break;
        }
        
        // Recebendo nome do vinho mesmo com espaços e limpando o prompt
        getchar();
        printf("Digite o nome do vinho: ");
        scanf("%[^\n]%*c", nome);
        
        // Recebendo preço do vinho
        printf("Digite o preço do vinho:: ");
        scanf("%lf", &preco);
        
        // Validando qual é o vinho mais caro
        if(preco > precoMaior){
            strcpy(nomeMaior, nome);
            strcpy(tipoMaior, tipo);
            precoMaior = preco;
        }
        
    }
    
    // Modificando variavel tipo para escrever tipo do vinho
    if(strcasecmp(tipoMaior, "T")){
        strcpy(tipoMaior, "Tinto");
    }
    if(strcasecmp(tipoMaior, "B")){
        strcpy(tipoMaior, "Branco");
    }
    if(strcasecmp(tipoMaior, "R")){
        strcpy(tipoMaior, "Rosé");
    }
    
    // Exibindo resultado    
    printf("Nome do vinho mais caro: %s\n", nomeMaior);
    printf("Tipo do vinho mais caro: %s\n", tipoMaior);
    printf("Preço do vinho mais caro: R$ %.2lf\n", precoMaior);
    
}
