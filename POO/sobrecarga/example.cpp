#include <iostream>
#include <math.h>
#include "meuint.h"
using namespace std;
const Meuint operator+(int a, const Meuint& b){
    return Meuint(a + b.numero);
}

const Meuint operator-(int a, const Meuint& b){
    return Meuint(a - b.numero);
}

const Meuint operator*(int a, const Meuint& b){
    return Meuint(a * b.numero);
}

const Meuint operator/(int a, const Meuint& b){
    return Meuint(a / b.numero);
}

bool operator>(int a, const Meuint& b){
    return a > b.numero;
}

bool operator<(int a, const Meuint& b){
    return a < b.numero;
}

bool operator==(int a, const Meuint& b){
    return a == b.numero;
}

// operador de saida

ostream& operator<<(ostream& saida, const Meuint& num){
    saida << num.numero;
    return saida;
}

istream& operator>>(istream& entrada, Meuint& num){
    entrada >> num.numero;
    return entrada;
}

const void eq2g (const Meuint& a, const Meuint& b, const Meuint& c){
    Meuint x1, x2;
    double delt1, delt2;

    delt1 = b.numero*b.numero - 4*a.numero*c.numero;
    delt1 = sqrt(delt1);
    delt2 = b.numero*b.numero - 4*a.numero*c.numero;
    delt2 = sqrt(delt2);

    x1 = ((-b.numero + delt1) / 2*a.numero);
    x2 = ((-b.numero - delt2) / 2*a.numero);
    cout << "x1 = " << x1 << " x2 = " << x2;
}

int main(){
    Meuint A, B, C;
    cout << "Digite os valores de A, B e C";
    cin >> A >> B >> C;
    
    eq2g(A,B,C);
    
    return 0;
}