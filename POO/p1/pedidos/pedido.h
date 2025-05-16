// numero sequencial unico e imutavel definido automaticamente no momento de criação do objeto
// nome da criança
// numero de itens e itens
 // informar numero que itens e nome
// vetor dinamico para armazenar esses itens
// metodo que retorno total de pedidos ativos no momentos (chamados a qualquer momento)
// total de itens solicitados em todos os pedidos ativos  (chamados a qualquer momento)
//
#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::cin;


class Pedido{
private:
	const int n;
	static int contN;
	string nome;
	int quantItem;
	string *ptrItem;
	static int atvM;
	static int tItems;
public:
	Pedido(string nome = "Anonimo", int quantItem = 0);
	~Pedido();
	string getNome() const;
	int getN() const;
	int getQuantItem() const;
	bool getItem(int pos, string& val) const;
	bool setItem(int pos, string val);
	void setNome(string nome);
	static int getPedidosAtv();
	static int getItemstotal();
};

int Pedido::atvM = 0;
int Pedido::tItems = 0;
int Pedido::contN = 0;

Pedido::Pedido(string nome, int quantItem):n(++contN){
	this->nome = nome;
	if(quantItem > 0){
		this->quantItem = quantItem;
		ptrItem = new string[quantItem]; 
	}else{
		this->quantItem = 0;
		ptrItem = NULL;
	}
	atvM++;
	tItems += quantItem;
}

Pedido::~Pedido(){
	atvM--;
	delete [] ptrItem;
}

string Pedido::getNome() const {
	 return nome;
}

int Pedido::getN() const {
	return n;
}

int Pedido::getQuantItem() const {
	return quantItem;
}

bool Pedido::getItem(int pos, string& val) const {
	if(pos >= 0 && pos < quantItem){
		val = ptrItem[pos];
		return true;
	}else{
		return false;
	}
}

bool Pedido::setItem(int pos, string val){
	if(pos >= 0 && pos < quantItem){
		ptrItem[pos] = val;
		return true;
	}else{
		return false;
	} 
}

void Pedido::setNome(string nome){
	this->nome = nome;
}


int Pedido::getPedidosAtv(){
	return atvM;
}
int Pedido::getItemstotal(){
	return tItems;
}





