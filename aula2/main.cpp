#include <iostream>
#include "vetorD.h"
int main() {

    int tamanho;
    std::cout << "Digite tamanho do vetor impar: " << std::endl;
    std::cin >> tamanho;

    Vetor_Inteiro* vetorPtr;
    vetorPtr = new Vetor_Inteiro ;
    Vetor_Inteiro vetorImpar(tamanho);
    Vetor_Inteiro vetorPar;

    int i = 0;

    while (vetorPar.setValor(i, i*2)) {
        i++;
    }

    i=0;
    while (vetorImpar.setValor(i, i*2+1)) {
        i++;
    }

    std::cout << "vetor par" << std::endl;
    vetorPar.imprime();
    std::cout << "vetor impar" << std::endl;
    vetorImpar.imprime();

    delete vetorPtr;

    return 0;
}