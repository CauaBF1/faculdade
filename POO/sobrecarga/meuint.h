#include <iostream>
#include <ostream>
#include <istream>
using namespace std;
class Meuint{
private:
    int numero;
public:
    Meuint(int numero = 0);
    void setNumero(int numero);
    int getNumero() const;
//?                                          Operators overloading

    // Unarios
    Meuint& operator++();
    const Meuint operator++(int);
    Meuint& operator--();
    const Meuint operator--(int);

    // Meuint com Meuint
    const Meuint operator+(const Meuint& a) const;
    const Meuint operator-(const Meuint& a) const;
    const Meuint operator*(const Meuint& a) const;
    const Meuint operator/(const Meuint& a) const;
    bool operator>(const Meuint& a) const;
    bool operator<(const Meuint& a) const;
    bool operator==(const Meuint& a) const;

    // Meuint com int
    const Meuint operator+(int a) const;
    const Meuint operator-(int a) const;
    const Meuint operator*(int a) const;
    const Meuint operator/(int a) const;
    bool operator>(int a) const;
    bool operator<(int a) const;
    bool operator==(int a) const;

    //================================Operadores NAO membros da classe
		// Int com MeuInt
    friend const Meuint operator+(int o1, const Meuint& o2);
    friend const Meuint operator-(int o1, const Meuint& o2);      
    friend const Meuint operator*(int o1, const Meuint& o2);  
    friend const Meuint operator/(int o1, const Meuint& o2); 
    friend bool operator>(int o1, const Meuint& o2);
    friend bool operator<(int o1, const Meuint& o2);
    friend bool operator==(int o1, const Meuint& o2);

    // Exercicio
    friend const void eq2g (const Meuint& a, const Meuint& b, const Meuint& c);
    

    
    // Fluxo de entrada e sa?da
    friend ostream &operator<<(ostream &saida, const Meuint &num);
    friend istream &operator>>(istream &entrada, Meuint &num);   
};



Meuint::Meuint(int numero){
    setNumero(numero);
}

void Meuint::setNumero(int numero){
    this->numero = numero;
}

int Meuint::getNumero() const{
    return this->numero;
}

Meuint& Meuint::operator++(){
    ++numero;
    return (*this);
}

const Meuint Meuint::operator++(int){
    Meuint copia (*this);
    ++numero;
    return copia;
}

Meuint& Meuint::operator--(){
    --numero;
    return (*this);
}

const Meuint Meuint::operator--(int){
    Meuint copia(*this);
    --numero;
    return copia;
}

// Meuint com Meuint
const Meuint Meuint::operator+(const Meuint& a) const{
    return Meuint(numero + a.numero);
}

const Meuint Meuint::operator-(const Meuint& a) const{
    return Meuint(numero - a.numero);
}

const Meuint Meuint::operator*(const Meuint& a) const{
    return Meuint(numero * a.numero);
}

const Meuint Meuint::operator/(const Meuint& a) const{
    return Meuint(numero / a.numero);
}

bool Meuint::operator>(const Meuint& a) const{
    return numero > a.numero;
}

bool Meuint::operator<(const Meuint& a) const{
    return numero < a.numero;
}

bool Meuint::operator==(const Meuint& a) const{
    return numero == a.numero;
}

// Meuint com int
const Meuint Meuint::operator+(int a) const{
    return Meuint(this->numero + a);
}

const Meuint Meuint::operator-(int a) const{
    return Meuint(this->numero - a);
}

const Meuint Meuint::operator*(int a) const{
    return Meuint(this->numero * a);
}

const Meuint Meuint::operator/(int a) const{
    return Meuint(this->numero / a);
}

bool Meuint::operator>(int a) const{
    return this->numero > a;
}

bool Meuint::operator<(int a) const{
    return this->numero < a;
}

bool Meuint::operator==(int a) const{
    return this->numero == a;
}


