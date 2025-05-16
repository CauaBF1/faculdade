/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 26/08/24
Data de modificação: 26/08/24
Objetivo: Ler os dados de alunos e armazená-los em um vetorde estruturas, para em seguida imprimir as informações e o IRA médio.
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

// Declaração das funções para imprimir os dados de um aluno e o IRA medio
void printAluno(tAluno);
double iraMedio(tAluno alunos[], int nAlunos);

int main() {
    int nAlunos;

    // Receber o número de alunos a serem lidos
    printf("Quantos alunos quer ler: ");
    scanf("%d", &nAlunos);

    // Declaração do vetor de alunos
    tAluno alunos[nAlunos];

    // Leitura dos dados dos alunos
    for(int i = 0; i < nAlunos; i++) {
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
    for(int i = 0; i < nAlunos; i++) {
        // Usa função para mostrar os alunos    
        printAluno(alunos[i]);  
    }
    
    // Cálculo e exibição da média do IRA
    double media = iraMedio(alunos, nAlunos);
    printf("\nO IRA médio dos alunos é: %.2lf\n", media);

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
Nome: iraMedio
Objetivo: Calcular a média do IRA dos alunos
Parâmetros:
- Parâmetro1: alunos do tipo tAluno[]
- Parâmetro2: nAlunos do tipo int
Retorno: Média do IRA do tipo double
*/
double iraMedio(tAluno alunos[], int nAlunos) {
    double soma = 0.0;
    for(int i = 0; i < nAlunos; i++) {
        soma += alunos[i].IRA;
    }
    
    return soma / nAlunos;
}

