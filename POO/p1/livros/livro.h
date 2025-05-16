#include <iostream>
#include <string>

using std::cout;
using std::string;
using std::endl;


class Livro{
private: 
	const int id;
	static int totalLivros;
	static int contID;
	string titulo;
	string autor;
	string estado;
public:
	Livro(string titulo = "Livro", string autor = "Anonimo");
	void getDetalhes() const;
	void emprestarLivro();
	void devolverLivro();
	static int getTotalLivros();
};

int Livro::contID = 0;
int Livro::totalLivros = 0;

Livro::Livro(string titulo, string autor):id(++contID){
	this->titulo = titulo;
	this->autor = autor;
	this->estado = "disponível";
	totalLivros++;
}

void Livro::getDetalhes() const {
	cout<< "ID: " << id << endl <<
		"Titulo: " << titulo << endl << 
		"Autor: " << autor << endl << 
		"Estado: " << estado << endl;
}

void Livro::emprestarLivro(){
	if(estado != "emprestado"){
		estado = "emprestado";
		cout << "Livro emprestado com sucesso" << endl;
	}else{
		cout << "Livro ja emprestado" << endl;
	}
}

void Livro::devolverLivro(){
	if(estado != "disponível"){
		estado = "disponível";
		cout << "Livro devolvido com sucesso" << endl;
	}else{
		cout << "Livro ja foi devolvido" << endl;
	}
}

int Livro::getTotalLivros() {
	return totalLivros;
}
