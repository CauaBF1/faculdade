#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *pa, *pb, *pMult;

    pa = (int*) malloc(sizeof(int));
    pb = (int*) malloc(sizeof(int));
    pMult = (int*) malloc(sizeof(int));

    if(pa == NULL){
        printf("Alocação de pa falhou");
        return 0;
    }
    if(pb == NULL){
        printf("Alocação de pb falhou");
        return 0;
    }
    if(pMult == NULL){
        printf("Alocação de pMult falhou");
        return 0;
    }

    printf("Digite o valor de A: ");
    scanf("%d", pa);

    printf("Digite o valor de B: ");
    scanf("%d", pb);

    *pMult = *pa * *pb;

    printf("Multiplicação é: %d", *pMult);

    return 0;

}
