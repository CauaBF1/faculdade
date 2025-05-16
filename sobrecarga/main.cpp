/*
Cauã Borges Faria 834437
Lucas Rodrigues da Silva 834724
Murilo Oliva Mantovani 834730
Nicolas Magno Messias da Silva 834054
Ryan Augusto Ribeiro 830913
*/

#include <iostream>
using namespace std;

class Complex{
    private:
        double real;
        double imag;
    public:

        Complex(double real = 0, double imag = 0){
            this->real = real;
            this->imag = imag;
        }

    // Complex + Complex || Complex + double
        const Complex operator+(const Complex& a) const{
            return Complex(real + a.real, imag + a.imag);
        }

        const Complex operator+(double a) const{
            return Complex(real + a, imag);
        }

        const Complex operator-(const Complex& a) const{
            return Complex(real - a.real, imag - a.imag);
        }

        const Complex operator-(double a) const{
            return Complex(real - a, imag);
        }

        const Complex operator*(const Complex& a) const{
            return Complex(real*a.real - imag*a.imag, real*a.imag + imag*a.real);
        }

        const Complex operator*(double a) const{
            return Complex(real*a, imag*a);
        }
    
    // Unarios
        // pre
        const Complex operator++(){
            return Complex(real + 1, imag);
        }
        // pos
        const Complex operator++(int){
            return Complex(real++, imag);
        }

        const Complex operator--(){
            real -= 1;
            return *this;
        }

        const Complex operator--(int){
            return Complex(real--, imag);
        }

        // Double + Complex || Saida e Entrada
        friend const Complex operator+(double a, const Complex& b);
        friend const Complex operator-(double a, const Complex& b);
        friend const Complex operator*(double a, const Complex& b);
        friend istream& operator>>(istream& entrada, Complex& num);
        friend ostream& operator<<(ostream& saida, const Complex& num);
};

const Complex operator+(double a, const Complex& b){
    return Complex(a + b.real, b.imag);
}

const Complex operator-(double a, const Complex& b){
    return Complex(a - b.real, -b.imag);
}

const Complex operator*(double a, const Complex& b){
    return Complex(a*b.real, a*b.imag);
}

istream& operator>>(istream& entrada, Complex& num){
    entrada >> num.real >> num.imag;
    return entrada;
}

ostream& operator<<(ostream& saida, const Complex& num){
    saida << num.real << " + " << num.imag << "i";
    return saida;
}


int main(){
    // Construtor
    Complex A, B;
    cout << "Digite o valor de A: " << endl;// operador de saida
    cin >> A; // operador de entrada
    cout << "Digite o valor de B: " << endl; // operador de saida
    cin >> B; // operador de entrada

    cout << "A + B = " << A + B << endl; // operador de soma
    cout << "A - B = " << A - B << endl; // operador de subtração
    cout << "A * B = " << A * B << endl; // operador de multiplicação
    cout << "A + 2 = " << A + 2 << endl; // operador de soma
    cout << "A - 2 = " << A - 2 << endl; // operador de subtração
    cout << "A * 2 = " << A * 2 << endl; // operador de multiplicação
    cout << "2 + A = " << 2 + A << endl; // operador de soma(double + complex)
    cout << "2 - A = " << 2 - A << endl; // operador de subtração(double - complex)
    cout << "2 * A = " << 2 * A << endl; // operador de multiplicação(double * complex)

    cout << "Valor inicial de A: " << A << endl;
    cout << "A++ retorna: " << A++ << endl; // operador de incremento pós fixado
    cout << "Valor de A após A++: " << A << endl;

    cout << "Valor inicial de A: " << A << endl;
    cout << "A-- retorna: " << A-- << endl; // operador de decremento pós fixado
    cout << "Valor de A após A--: " << A << endl;

    cout << "++A = " << ++A << endl; // operador de incremento pré fixado
    cout << "--A = " << --A << endl; // operador de decremento pré fixado
    return 0;
}

