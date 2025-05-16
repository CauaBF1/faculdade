# Alocação Dinamica de memoria
Utiliza stdlib.h
malloc para alocar e free para liberar

### Codigo de swap de variaveis sem alocação dinamica

```c
// Bibliotecas de funções predefinidas

#include <stdio.h>
#include <stdlib.h>

// Função principal

int main(int argc, char *argv[])
{

  // Declaração de variáveis e constantes locais
  
  int a, b;   // variáveis para armazenar os 2 valores
  int troca;  // variável temporária para permitir a troca dos valores
  
  int *pa, *pb, *ptroca;  // ponteiros para as variáveis a, b e troca
  
  // Inicialização
  // Leitura de Dados

  printf("Digite o valor de a: ");
  fflush(stdin);
  scanf("%d", &a);
  
  printf("Digite o valor de b: ");
  fflush(stdin);
  scanf("%d", &b);

  // Escrita dos valores de a e b
  // Valores originais

  printf("\n");
  printf("Valores originais:\n");
  printf("O valor de a = %d\n", a);
  printf("O valor de b = %d\n\n", b);
    
  // Troca de valores (i.e. swap)
  // Sem usar ponteiros
  
  troca = a;
  a = b;
  b = troca;
  
  // Escrita dos valores de a e b
  // Valores trocados

  printf("Valores trocados:\n");
  printf("O valor de a = %d\n", a);
  printf("O valor de b = %d\n\n", b);
  
  // Troca de valores (i.e. swap)
  // Sem usar ponteiros
  // Retorno aos valores originais
  
  troca = a;
  a = b;
  b = troca;
  
  // Escrita dos valores de a e b
  // Valores originais
  
  printf("Valores originais:\n");
  printf("O valor de a = %d\n", a);
  printf("O valor de b = %d\n\n", b);  
  
  // Inicialização dos ponteiros
  
  pa = &a;
  pb = &b;
  ptroca = &troca;
  
  // Troca de valores (i.e. swap)
  // Usando ponteiros

  *ptroca = *pa;
  *pa = *pb;
  *pb = *ptroca;

  // Escrita dos valores de a e b
  // Valores trocados

  printf("Valores trocados:\n");
  printf("O valor de a = %d\n", a);
  printf("O valor de b = %d\n\n", b);

  // Finalização do programa
  
  system("PAUSE");	
  return 0;
}
```

### Com alocação dinamica

```c
// Bibliotecas de funções predefinidas

#include <stdio.h>
#include <stdlib.h>

// Função principal

int main(int argc, char *argv[])
{

  // Declaração de variáveis locais
  
  int *pa, *pb, *ptroca;  // ponteiros para as variáveis a, b e troca
  
  // Alocação dinâmica de memória
  
  pa = (int*) malloc(sizeof(int)); // Ao inves de colocar tamanho em bytes coloca tamanho de int ja definido pela linguagem
  pb = (int*) malloc(sizeof(int));
  ptroca = (int*) malloc(sizeof(int));
    
  // Verificar se a alocação de memória foi realizada corretamente
    
  if (pa == NULL) { // Caso a alocação nao ocorra, nao tenha memoria disponivel.
    printf("Alocacao de memoria para o ponteiro A falhou ...\n\n");
    exit (1);
  }
    
  if (pb == NULL) {
    printf("Alocacao de memoria para o ponteiro B falhou ...\n\n");
    exit (1);
  }
    
  if (ptroca == NULL) {
    printf("Alocacao de memoria para o ponteiro TROCA falhou ...\n\n");
    exit (1);
  }  
  
  // Inicialização
  // Leitura de Dados

  printf("Digite o valor de a: ");
  fflush(stdin); // Limpar o buffer
  scanf("%d", pa); // Nao precisa de & porque é um ponteiro.
  
  printf("Digite o valor de b: ");
  fflush(stdin);
  scanf("%d", pb);

  // Escrita dos valores de a e b
  // Valores originais

  printf("\n");
  printf("Valores originais:\n");
  printf("O valor de a = %d\n", *pa);	
  printf("O valor de b = %d\n\n", *pb);
  
  // Troca de valores (i.e. swap)
  // Usando ponteiros

  *ptroca = *pa;
  *pa = *pb;
  *pb = *ptroca;

  // Escrita dos valores de a e b
  // Valores trocados

  printf("Valores trocados:\n");
  printf("O valor de a = %d\n", *pa);
  printf("O valor de b = %d\n\n", *pb);

  // Liberação de memória
  
  free(pa); // Libera a memoria alocada.
  free(pb);
  free(ptroca);

  // Finalização do programa
  
  system("PAUSE"); // Da uma pausa esperando uma tecla para retomar o programa utilizado para execução em windows e nao fechar 	 a janela no exato momento
  return 0;
}
```

