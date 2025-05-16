#include <iostream>
#include "fracao.h"

using std::cout;
using std::cin;
using std::endl;
using namespace std;
Fracao multiplica(Fracao f1, Fracao f2){
	Fracao resultado;
	resultado.setNum(f1.getNum()*f1.getNum());
	resultado.setDen(f1.getDen()*f2.getDen());
	return resultado;
}
 
// definida de forma global para acessar f1.num precisa ser friend
Fracao operator *(Fracao f1, Fracao f2){
	Fracao resultado;
	resultado.setNum(f1.num*f2.getNum());
	resultado.setDen(f1.getDen()*f2.getDen());
	return resultado;
}

// definida de forma global precisa ser "friend" da classe
bool operator>(int n, Fracao f){	
	if ( n > (double)f.num/f.den)
		return true;
	return false;
}

Fracao operator++(Fracao f1){
  f1.num = f1.num + f1.den;
  return f1;
}

// Usando operator cout para imprimir funcao ao inves da funcao Imprimir() 
ostream& operator<<(ostream & saida, Fracao f){
  saida << f.num << "/" << f.den << endl;
  return saida;
}

istream& operator>>(istream &entrada, Fracao &f){
  int n;
  int d;
  entrada >> n;
  entrada.ignore();
  entrada >> d;
  f.setNum(n);
  f.setDen(d);
  return entrada;
}

int main(){
	Fracao f1(1,4), f2(1,2), f3, f4(7,2);
  cin >> f1;
  cout << "f1 = ";
	cout << f1;

	cout << "f2 = ";
	cout << f2;	
	
	cout << "f3 = ";
	f3 = f1.operator*(5);
	cout << f3;

	cout << "f4 = ";
	cout << f4;
// operator > frações
	if(f1 > f2) { 
		cout << "f1 maior que f2" << endl;
	}else{
		cout << "f1 menor que f2" << endl;
	}
// operator > fracao <-> int
	if(f4>1) { 
		cout << "f4 maior que 1" << endl;
	}else{
		cout << "f4 menor que 1" << endl;
	}
// operator > int <-> fracao
	if(1>f2) { 
		cout << "1 maior que f2" << endl;
	}else{
		cout << "1 menor que f2" << endl;
	}
// incremento fracao
	++f2;
	cout << "F2 = " << f2;
  
// incremento pos
  f3 = ++f1;
  cout << "F3 = "<< f3;

	return 0;
}
