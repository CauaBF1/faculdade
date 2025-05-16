/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 26/08/24
Data de modificação: 26/08/24
Objetivo: Ler os dados de alunos e armazená-los em um vetorde estruturas, para em seguida imprimir as informações.
*******************************************************************************/

#include <stdio.h>
#include <string.h>

#define TAMANHO_MAX 30

// Definição da estrutura tAluno
typedef struct {
    char nome[TAMANHO_MAX];
    double IRA;
    int RA;
    char sexo;
} tAluno;

// Declaração da função para imprimir os dados de um aluno
void printAluno(tAluno aluno);

int main() {
    int nAlunos;

    // Receber o número de alunos a serem lidos
    printf("Quantos alunos quer ler: ");
    scanf("%d", &nAlunos);

    // Declaração do vetor de alunos
    tAluno alunos[nAlunos];

    // Leitura dos dados dos alunos
    for(int i = 0; i < nAlunos; i++){
        getchar();
	printf("Digite o nome do aluno: ");
        scanf("%[^\n]%*c", alunos[i].nome);

        printf("Digite o IRA do aluno: ");
        scanf("%lf", &alunos[i].IRA);

        printf("Digite o RA do aluno: ");
        scanf("%d", &alunos[i].RA);

        printf("Digite o sexo do aluno (M/F): ");
        scanf(" %c", &alunos[i].sexo);
    }

    // Impressão dos dados dos alunos
    for(int i = 0; i < nAlunos; i++){
	// Usa função para mostrar os alunos	
        printAluno(alunos[i]);  
    }

    return 0;
}

/*
Nome: printAluno
Objetivo: Mostrar os dados do aluno
Parâmetros:
- Parâmetro1: aluno do tipo tAluno
*/
void printAluno(tAluno aluno) {
    printf("\nDados do Aluno:\n");
    printf("Nome: %s\n", aluno.nome);
    printf("IRA: %.2lf\n", aluno.IRA);
    printf("RA: %d\n", aluno.RA);
    printf("Sexo: %c\n", aluno.sexo);
}



/*

#include <stdio.h>
#include <string.h>

#define TAMANHO_MAX 30

// Definição da estrutura tAluno
typedef struct {
    char nome[TAMANHO_MAX];
    double IRA;
    int RA;
    char sexo;
} tAluno;

// Declaração da função para imprimir os dados de um aluno
void printAluno(tAluno aluno, int index);

int main() {
    int nAlunos;

    // Receber o número de alunos a serem lidos
    printf("Quantos alunos quer ler: ");
    scanf("%d", &nAlunos);

    // Declaração do vetor de alunos
    tAluno alunos[nAlunos];

    // Leitura dos dados dos alunos
    for(int i = 0; i < nAlunos; i++){
        getchar();
	printf("Digite o nome do aluno: ");
        scanf("%[^\n]%*c", alunos[i].nome);

        printf("Digite o IRA do aluno: ");
        scanf("%lf", &alunos[i].IRA);

        printf("Digite o RA do aluno: ");
        scanf("%d", &alunos[i].RA);

        printf("Digite o sexo do aluno (M/F): ");
        scanf(" %c", &alunos[i].sexo);
    }

    // Impressão dos dados dos alunos
    for(int i = 0; i < nAlunos; i++){
	// Usa função para mostrar os alunos	
        printAluno(alunos[i], i+1);  
    }

    return 0;
}

void printAluno(tAluno aluno, int index) {
    printf("\nDados do Aluno %d:\n", index);
    printf("Nome: %s\n", aluno.nome);
    printf("IRA: %.2lf\n", aluno.IRA);
    printf("RA: %d\n", aluno.RA);
    printf("Sexo: %c\n", aluno.sexo);
}


*/
