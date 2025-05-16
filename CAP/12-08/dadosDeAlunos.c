/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 12/08/2024
Data de modificação: 12/08/2024
Objetivo: Receber dados do aluno atraves do struct para o aluno e para o endereço.
*******************************************************************************/
#include <stdio.h>
#include <string.h>
#define tamanho 30
int main()
{
    typedef struct{
        char tipoLogradouro[tamanho];
        char logradouro[tamanho];
        int numero;
        char complemento[tamanho];
        char bairro[tamanho];
        char cidade[tamanho];
        char CEP[tamanho];
    }tEndereço;
    
    
    typedef struct{
        int RA;
        char nome[tamanho];
        int IRA;
        char sexo[tamanho];
        tEndereço endereco;
        int idade;
    }tAluno;
    
    
    tAluno aluno[36];
    
    for(int i =0; i<2; i++){
        printf("Digite RA: ");
        scanf("%d", &aluno[i].RA);
        getchar();
        
        printf("Digite nome: ");
        scanf("%[^\n]%*c", aluno[i].nome);
        
        printf("Digite IRA: ");
        scanf("%d", &aluno[i].IRA);
        
        printf("Digite sexo: ");
        scanf("%s", aluno[i].sexo);
        
        printf("Digite a idade: ");
        scanf("%d", &aluno[i].idade);
        
        printf("Digite tipo de logradouro: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.tipoLogradouro);
        
        printf("Digite logradouro: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.logradouro);
        
        printf("Digite número: ");
        scanf("%d", &aluno[i].endereco.numero);
        
        printf("Digite complemento: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.complemento);
        
        printf("Digite bairro: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.bairro);
        
        printf("Digite cidade: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.cidade);
        
        printf("Digite CEP: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.CEP);   
        
    }
    
    for(int i = 0; i < 2; i++){
        printf("\nDados do Aluno [%d]:\n", i+1);
        printf("RA: %d\n", aluno[i].RA);
        printf("Nome: %s\n", aluno[i].nome);
        printf("IRA: %d\n", aluno[i].IRA);
        printf("Sexo: %s\n", aluno[i].sexo);
        printf("Idade: %d\n", aluno[i].idade);
        printf("Endereço: %s %s, %d, %s, %s, %s, %s\n", aluno[i].endereco.tipoLogradouro, aluno[i].endereco.logradouro, aluno[i].endereco.numero, aluno[i].endereco.complemento, aluno[i].endereco.bairro, aluno[i].endereco.cidade, aluno[i].endereco.CEP);
        
    }
}
