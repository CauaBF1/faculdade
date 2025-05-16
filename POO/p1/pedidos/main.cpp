#include <iostream>
#include <string>
#include "pedido.h"

using std::cout;
using std::cin;
using std::string;
using std::endl;

int main(){
	Pedido p1("Cauã", 1);
	p1.setItem(0, "Bicicleta");
	//p1.setNome("Fernando");
	cout << "Id: " << p1.getN() << endl;
	cout << "Quantidade de items de " + p1.getNome() << " "<< p1.getQuantItem() << endl;
	string aux;
	p1.getItem(0, aux);
	cout << "Item: "<< aux << endl;
	cout <<"Numero de pedidos ativos: " << p1.getPedidosAtv() << endl;
	cout << "Numero total de items: " << p1.getItemstotal() << endl;


	
	Pedido p2("Pablo", 3);
	p2.setItem(0, "Moto");
	p2.setItem(1, "carro");
	p2.setItem(2, "puta");
	//p1.setNome("Fernando");
	cout << "Id: " << p2.getN() << endl;
	cout << "Quantidade de items de " + p2.getNome() << " "<< p2.getQuantItem() << endl;
	string aux1, aux2, aux3;
	p2.getItem(0, aux1);
	cout << "Item: "<< aux1 << endl;
	p2.getItem(1, aux2);
	cout << "Item: "<< aux2 << endl;
	p2.getItem(2, aux3);
	cout << "Item: "<< aux3 << endl;
	
	cout <<"Numero de pedidos ativos: " << p1.getPedidosAtv() << endl;
	cout << "Numero total de items: " << p1.getItemstotal() << endl;




	return 0;

}
