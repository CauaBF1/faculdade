
/******************************************************************************
Autor: Cauã Borges Faria
Data de criação: 26/08/24
Data de modificação: 26/08/24
Objetivo: Ler alunos e armazenar em um vetor de alunos
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

// Declaração das procedimentos para serem usados na main
void readAluno(tAluno *aluno);
void printAluno(tAluno aluno);

int main() {
    // Declaração variavel local
    int nAlunos;

    // Receber numero de alunos
    printf("Quantos alunos quer ler: ");
    scanf("%d", &nAlunos);

    // Declarar vetor com tamanho numero de alunos
    tAluno aluno[nAlunos];

    // Ler os dados de todos os alunos
    for(int i = 0; i < nAlunos; i++){
        readAluno(&aluno[i]);
    }

    // Mostrar os dados de todos os alunos
    for(int i = 0; i < nAlunos; i++){
        printAluno(aluno[i]);
    }


}

// Função para ler os dados de um aluno
void readAluno(tAluno *aluno) {
    getchar();
    printf("Digite o nome do aluno: ");
    scanf("%[^\n]%*c", aluno->nome);  // le a string e armazena no campo 'nome' do struct

    printf("Digite o IRA do aluno: ");
    scanf("%lf", &aluno->IRA);  // le IRA

    printf("Digite o RA do aluno: ");
    scanf("%d", &aluno->RA);  // le RA

    printf("Digite o sexo do aluno (M/F): ");
    scanf(" %c", &aluno->sexo);  // le sexo do alunos
}

// Função para escrever os dados de um aluno
void printAluno(tAluno aluno){
    printf("\nDados do Aluno:\n");
    printf("Nome: %s\n", aluno.nome);
    printf("IRA: %.2lf\n", aluno.IRA);
    printf("RA: %d\n", aluno.RA);
    printf("Sexo: %c\n", aluno.sexo);

}
