#include <iostream>
#include <string>
#include "livro.h"
using std::cout;
using std::cin;
using std::endl;
using std::string;

int main(){
	Livro l1 ("Livro 1", "Cauã");
	l1.getDetalhes();
	l1.emprestarLivro();
	l1.getDetalhes();
	l1.emprestarLivro();
	l1.devolverLivro();
	cout << "Numero de livros criados: " << Livro::getTotalLivros();
}
