#include <iostream>
#include <string>

using std::cout;
using std::string;
using std::endl;

class Inventario{
private:
	const int id;
	static int contID;
	string name;
	int quantProd;
	string *ptrProd; // aponta para começo vetor
	static int totalInventarios;
public:
	Inventario(string name, int quantProd);
	~Inventario();
	bool setProduto(int pos, string val);
	bool removeProduto(int pos, string& val);
	string getInventario() const;
	static int getNInventarios();
};

int Inventario::contID = 0;
int Inventario::totalInventarios = 0;
Inventario::Inventario(string name, int quantProd):id(++contID){
	if(quantProd > 0){
		this->quantProd = quantProd;
		this->name = name;
		ptrProd = new string [quantProd];
		totalInventarios++;
	}else{
		this->quantProd = 0;
		ptrProd = nullptr;
	}
}


Inventario::~Inventario(){
	delete [] ptrProd;
	totalInventarios--;
}		
	
bool Inventario::setProduto(int pos, string val){
	if(ptrProd != nullptr && pos >=0 && pos < quantProd){
		ptrProd[pos] = val;
		return true;
	}else{
		cout << "Erro" << endl;
		return false;
	}
}

bool Inventario::removeProduto(int pos, string& val){
	if(ptrProd != nullptr && pos >= 0 && pos < quantProd){
		if(!ptrProd[pos].empty()){
			val = ptrProd[pos];
			ptrProd[pos] = "";
			return true;
		}else{
			cout << "slot ja vazio" << endl;
			return false;
		}
	}else{
		cout << "posição invalida" << endl;
		return false;	
	}	
}

string Inventario::getInventario() const {
	if (ptrProd == nullptr){
		return "Inventario vazio";
	}
	string detalhes =  "ID: " + std::to_string(id) +" \n" +
		"Nome: " + name + "\n" + 
		"Quantidade maxima de produtos: " + std::to_string(quantProd) + "\n";
	for (int i = 0; i < quantProd; ++i) {											   detalhes += "Produto[" + std::to_string(i) + "]: " + (ptrProd[i].empty() ? "Vazio" : ptrProd[i]) + "\n";
    	}
	return detalhes;
}

int Inventario::getNInventarios(){
	return totalInventarios;
}


