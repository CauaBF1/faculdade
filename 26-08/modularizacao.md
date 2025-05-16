# Subrotinas
Tem dois tipos:
- Função(retorna um valor)
- procedimento(gera um novo comando)

## Função
```txt
                          parametros formais                        
                            |           |
                            \/         \/
function aumentoSalario(salario, percentualAumento) : real 

    novoSalario <- salario * (1 + percentualAumento)

    return novoSalario


end-function
```

Não recomendado
```c
#include <stdio.h>

double aumentoSalario(double salario, double percentual){
    
    double novoSalario;
    novoSalario = salario * (1 + percentual);
    return novoSalario;
}

int main() {
    double salarioFuncionario = 20000;
    double percentual = 0.2;
    
    salarioFuncionario = aumentoSalario(salarioFuncionario, percentual);
    printf("salario: %lf", salarioFuncionario);
    
    return 0;
}

```
Recomendado:
```c
#include <stdio.h>

double aumentoSalario(double, double);
int main() {
    double salarioFuncionario = 20000;
    double percentual = 0.2;
    
    salarioFuncionario = aumentoSalario(salarioFuncionario, percentual);
    printf("salario: %lf", salarioFuncionario);
    
    return 0;
}

double aumentoSalario(double salario, double percentual){
    
    double novoSalario;
    novoSalario = salario * (1 + percentual);
    return novoSalario;
}
```


## Procedimento

```c
// Para isso
    void printAluno(tAluno);

int main(){
    // criado um aluno com struct
    tAluno a1;
    
    // depois
    printAluno(a1);
}

void printAluno(tAluno aluno){
    printf("RA = %d", a1.RA);
}


```
