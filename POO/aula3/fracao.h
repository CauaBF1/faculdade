#include <iostream>
using namespace std;

class Fracao{
friend Fracao operator *(Fracao f1, Fracao f2); // fracao que pode acessar as coisas privadas da classe tambem
friend bool operator>(int n, Fracao f);
friend Fracao operator++(Fracao f1); 
friend ostream& operator<<(ostream &saida, Fracao f);
friend istream& operator>>(istream &entrada, Fracao &f);
private:
	int num;
	int den;
public:
	Fracao(int num, int den);
	Fracao();
	int getNum() const;
	int getDen() const;
	void setNum(int num);
	void setDen(int den);
	void imprime();
	//Fracao operator*(Fracao f) const;
	Fracao operator*(int n) const;
	bool operator>(Fracao f2) const;
	bool operator>(int n) const;
	//Fracao& operator++();//pre
  //Fracao operator++(int);//pos
};

Fracao::Fracao (int num, int den){
	if(den != 0){
		this->num = num;
		this->den = den;
	}else{
		this->num = num;
		this->den = 1;
	}
}
	
Fracao::Fracao(){
	num = 0;
	den = 1;	
}

int Fracao::getNum() const{
	return num;
}

int Fracao::getDen() const{
	return den;
}

void Fracao::setNum(int num){
	this->num = num;
}

void Fracao::setDen(int den){
	if(den != 0){
		this->den = den;
	}
}

void Fracao::imprime(){
	std::cout << num << "/" << den << std::endl;
}

/* Deve ser const para nao modificar o objeto que esta chamando o metodo
Fracao Fracao::operator*(Fracao f) const{
	Fracao resultado;
	resultado.setNum(this->getNum() * f.getNum());
	resultado.setDen(this->getDen() * f.getDen());
	return resultado;
}
*/
Fracao Fracao::operator*(int n) const{
	Fracao resultado;
	resultado.setNum(this->getNum() * n);
	resultado.setDen(this->getDen());
	return resultado;
}

bool Fracao::operator>(Fracao f2) const {
    int left = this->num * f2.getDen();
    int right = this->den * f2.getNum();
    return left > right;
}

bool Fracao::operator>(int n) const{
	if ((double)num/den > n)
		return true;
	return false;
}

// preciso fazer retorno por referencia, para que ++f1 = f3 funcione(exp se f1 = vetor)
// Fracao& Fracao::operator++(){//pre 
// 	num = num + den;
// 	return *this;
// }

// Fracao Fracao::operator++(int){//pos
//   Fracao copia(*this);
//   num = num + den;
//   return copia;
// }
//





