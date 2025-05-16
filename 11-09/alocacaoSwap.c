// Bibliotecas de funções predefinidas

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>   // biblioteca de alocação dinâmica

// Função principal

int main(int argc, char *argv[])
{

  // Declaração de variáveis locais
  
  int *pa, *pb, *ptroca;  // ponteiros para as variáveis a, b e troca
  
  // Alocação dinâmica de memória
  
  pa = (int*) malloc(sizeof(int));
  pb = (int*) malloc(sizeof(int));
  ptroca = (int*) malloc(sizeof(int));
    
  // Verificar se a alocação de memória foi realizada corretamente
    
  if (pa == NULL) {
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
  fflush(stdin);
  scanf("%d", pa);
  
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
  
  free(pa);
  free(pb);
  free(ptroca);

  // Finalização do programa
  
  system("PAUSE");	
  return 0;
}
