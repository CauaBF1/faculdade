//
// Created by borgescaua on 11/22/24.
//

#ifndef VETORD_H
#define VETORD_H

#endif //VETORD_H

#include <iostream>

class Vetor_Inteiro {
private:
    int tamanho;
    int* ptrvalores;

public:
    Vetor_Inteiro(int tamanho);
    ~Vetor_Inteiro();
    int getTam() const;
    bool setValor(int pos, int valor);
    bool getValor(int pos, int& val) const;
    void imprime() const;
};

// Constructor
Vetor_Inteiro::Vetor_Inteiro(int tamanho = 10) {
    if(tamanho > 0) {
        this->tamanho = tamanho;
    }else {
        this->tamanho = 10;
    }
    ptrvalores = new int[tamanho];
}

Vetor_Inteiro::~Vetor_Inteiro() {
    delete[] ptrvalores;
}
// Get the size of the vector
int Vetor_Inteiro::getTam() const {
    return tamanho;
}

// Set value at a specific position
bool Vetor_Inteiro::setValor(int pos, int valor) {
    if (pos >= 0 && pos < tamanho) {
        ptrvalores[pos] = valor;
        return true;
    }
    return false;
}

// Get value from a specific position
bool Vetor_Inteiro::getValor(int pos, int& val) const {
    if (pos >= 0 && pos < tamanho) {
        val = ptrvalores[pos];
        return true;
    }
    return false;
}

// Print the vector
void Vetor_Inteiro::imprime() const {
    int valor;
    for (int i = 0; i < tamanho; i++) {
        getValor(i, valor);
        std::cout << valor << " ";
    }
    std::cout << std::endl;
}