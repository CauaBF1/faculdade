#include <stdio.h>
#include <stdlib.h>


int main(){

	int *pa, *pb, *ptroca;

	pa = (int*) malloc(sizeof(int));
	pb = (int*) malloc(sizeof(int));
	ptroca = (int*) malloc(sizeof(int));


	if (pa == NULL){
		printf("Alocação de pa não pode ser realizada");
		return 0;
	}
	if (pb == NULL){
		printf("Alocação de pb não pode ser realizada");
		return 0;
	}
	if (ptroca == NULL){
		printf("Alocação de ptroca não pode ser realizada");
		return 0;
	}

	printf("Digite o valor de a:");
	scanf("%d", pa);

	printf("Digite o valor de b:");
	scanf("%d", pb);

	printf("Valores originais: \n");
	printf("A: %d\n", *pa);
	printf("B: %d\n", *pb);


	*ptroca = *pa;
	*pa = *pb;
	*pb = *ptroca;

	printf("Valores trocados: \n");
	printf("A: %d\n", *pa);
	printf("B: %d\n", *pb);

	free(pa);
	free(pb);
	free(ptroca);

	return 0;

}
