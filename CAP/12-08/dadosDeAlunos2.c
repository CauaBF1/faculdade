/******************************************************************************
Autor: Cauã Borges Faria(834437)
Data de criação: 12/08/2024
Data de modificação: 12/08/2024
Objetivo: Receber dados do aluno atraves do struct para o aluno e para o endereço, alem de mostrar numero de alunos do sexo masculino e feminino, mostrar numero de alunos com nota maior que a media,numero de alunos que moram em Araraquara, terminar loop com letra F
*******************************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define tamanho 50
int main()
{
	// Declaração e iniciação das veriaveis
    double somaMedias=0, mediaTurma=0;
    int masculino=0, feminino=0, araraquara=0, maiorQueMedia=0, i=0;
    char tempRA[tamanho];
    	// Criação do struct para endereço
    typedef struct{
        char tipoLogradouro[tamanho];
        char logradouro[tamanho];
        int numero;
        char complemento[tamanho];
        char bairro[tamanho];
        char cidade[tamanho];
        char CEP[tamanho];
    }tEndereço;
    
    	// criação do struct para aluno
    typedef struct{
        int RA;
        char nome[tamanho];
        int IRA;
        char sexo[tamanho];
        tEndereço endereco;
        int idade;
        int notaMedia;
    }tAluno;
    
    // Inciação do numero maximo de alunos
    tAluno aluno[tamanho];
    
    // Receber dados dos alunos ate ser digitado F, ou atingit tamanho maximo da sala
    while(1){
        printf("Digite RA(ou F para finalizar): ");
        scanf("%s", tempRA);

        if (strcmp(tempRA, "F") == 0) {
            break;
        }
        
        if (i >= tamanho) {
            printf("Limite de alunos atingido.\n");
            break;
        }


        aluno[i].RA = atoi(tempRA);
    
        getchar();
        
        printf("Digite nome: ");
        scanf("%[^\n]%*c", aluno[i].nome);
        
        printf("Digite IRA: ");
        scanf("%d", &aluno[i].IRA);
        
        printf("Digite sexo(masc ou fem): ");
        scanf("%s", aluno[i].sexo);
	// Calcular numero de alunos do sexo masculino e feminino
        if(strcmp(aluno[i].sexo, "masc") == 0 || strcmp(aluno[i].sexo, "MASC") == 0){
            masculino++;
        }else if(strcmp(aluno[i].sexo, "fem") == 0 || strcmp(aluno[i].sexo, "FEM") == 0){
            feminino++;
        }
        printf("Digite a idade: ");
        scanf("%d", &aluno[i].idade);
        
        printf("Digite a nota media: ");
        scanf("%d", &aluno[i].notaMedia);
        
        somaMedias = somaMedias + aluno[i].notaMedia;
        
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
        // Calcular numero de alunos que moram em araraquara
        printf("Digite cidade: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.cidade);
        if(strcmp(aluno[i].endereco.cidade, "Araraquara") == 0 || strcmp(aluno[i].endereco.cidade, "araraquara") == 0 || strcmp(aluno[i].endereco.cidade, "ARARAQUARA") == 0){
            araraquara++;
        }
        printf("Digite CEP: ");
        scanf(" %[^\n]%*c", aluno[i].endereco.CEP);   
        i++;
    }
    // Calcular media da turma
    if (i > 0){
        mediaTurma = somaMedias / i;
    }
    // Calcular numero de alunos com nota maior que a media da turma
    for(int j = 0; j < i; j++){
        if(aluno[j].notaMedia > mediaTurma){
            maiorQueMedia++;
        }
    }
    // Apresentar os dados dos alunos
    for(int j = 0; j < i; j++){
        printf("\nDados do Aluno [%d]:\n", j+1);
        printf("RA: %d\n", aluno[j].RA);
        printf("Nome: %s\n", aluno[j].nome);
        printf("IRA: %d\n", aluno[j].IRA);
        printf("Sexo: %s\n", aluno[j].sexo);
        printf("Idade: %d\n", aluno[j].idade);
        printf("Endereço: %s %s, %d, %s, %s, %s, %s\n", aluno[j].endereco.tipoLogradouro, aluno[j].endereco.logradouro, aluno[j].endereco.numero, aluno[j].endereco.complemento, aluno[j].endereco.bairro, aluno[j].endereco.cidade, aluno[j].endereco.CEP);
    }
    // Apresentar os dados da turma
        printf("\nNumero de alunos do sexo feminino: %d\n", feminino);
        printf("Numero de alunos do sexo masculino: %d\n", masculino);
        printf("Numero de alunos com notas maiores que a media: %d\n", maiorQueMedia);
        printf("Numero de alunos que moram em Araraquara: %d\n", araraquara);
}
