# Variavel Composta Heterogênea(registro, struct(C))
Pode ter diferentes tipos de dados

Principal intuito: Agrupar dados relacionados a uma mesma entidade do mundo real
```txt
Exp(i) Cadastro de alunos:

int RA;
char nome[tamanhoNome];
int IRA;
char sexo;
char endenreço [tamanhoEndereço];
int idade;
```

```C
typedef int tIdade;
// Coloca primeiro a tipagem (tIdade funciona como um int), caso queira mudar para double(char,float) simplismente muda o typdef
tIdade idade;

// Transformando codigo acima(RA...) em uma coisa só em C

// tipo antigo
typedef
   struct{
    int RA;
    char nome[tamanhoNome];
    int IRA;
    char sexo;
    char endenreço [tamanhoEndereço];
    int idade;
}tAluno;
// tAluno se torna o novo tipo;

tAluno aluno;

// Para usar
aluno.RA=12345;
scanf("%d", &aluno.RA);
aluno.IRA=20000;
scanf("%d", &aluno.IRA);
aluno.sexo='masculino';
scanf("%c", &aluno.sexo);
aluno.nome='Caua';
scanf("%s", &aluno.nome);// scanf("%s", &aluno.nome[0]); = 0 é abreviado

```
---

Criando como identificar endereço dentro do exemplo anterior:
(validar se endereço esta na cidade de São Carlos)

```C
#include <strcpy>
#define TAMANHO 30
typedef struct{
    
    char tipoLogradouro[TAMANHO];
    char logradouro[TAMANHO];
    int numero;
    char complemento[TAMANHO];
    char bairro[TAMANHO];
    char cidade[TAMANHO];
    char CEP[TAMANHO];

}tEndereço;

scanf("%s", &aluno.endereço.cidade);//nao pode
strcpy(aluno.endereço.cidade, "Ribeirao preto");
```

```c
// Declarando 36 alunos
tAluno aluno[36];

for(int i = 0; i < 36; i++){
    scanf("%d", &RA;
    scanf("%d", 
}
```



## Exercicio ler dados dos alunos:

```c
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
        printf("Endereço: %s %s, %d, %s, %s, %s, %s\n", aluno[i].endereco.tipoLogradouro, aluno[i].endereco.logradouro, aluno[i].endereco.numero, aluno[i].endereco.complemento, aluno[i].endereco.bairro, aluno[i].endereco.cidade, aluno[i].endereco.CEP);
    }
}
```
