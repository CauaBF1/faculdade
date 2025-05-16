#include <iostream>
#include <string>
#include "inventario.h"

using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(){
	string aux = "Motocicleta";

	Inventario i1("Inventario 1", 4);
	i1.setProduto(0, "Bicicleta");
	i1.setProduto(1, "Motocicleta");
	cout << i1.getInventario() << endl;
	
	if(i1.removeProduto(1, aux)){
		cout << "Produto removido: " << aux << endl;
	}
	
	cout << i1.getInventario() << endl;
	
	cout <<"Numero de inventarios criados: " <<  Inventario::getNInventarios() << endl;

	Inventario i2("Inventario 2", 9);

	cout << "Numero de inventarios criados: "<< i1.getNInventarios() << endl;

	//cout << Inventario::getNInventarios();
	
	return 0;

}
