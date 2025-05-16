/*
Cauã Borges Faria (834437)
Nicolas Magno Messias da Silva (834054)
Ryan Augusto Ribeiro (830913)
Murilo Oliva Mantovani (834730)
Lucas Rodrigues da Silva (834724)
*/

#include <iostream>
#include "livros.h"

using std::cout;
using std::endl;
using std::cin;

int main() {
    Livros* livroPtr;
    livroPtr = new Livros;
    Livros livro;

    livro.set_id(1234);
    cout << livro.get_id() << endl;

    string titulo = "Cronicas do mitin";
    livro.set_titulo(titulo);
    cout << livro.get_titulo() << endl;

    string autor = "Caua";
    livro.set_autor(autor);
    cout << livro.get_autor() << endl;

    string editora = "Ufscar";
    livro.set_editora(editora);
    cout << livro.get_editora() << endl;

    livro.set_ano(1980);
    cout << livro.get_ano() << endl;

    string genero = "Aventura";
    livro.set_genero(genero);
    cout << livro.get_genero() << endl;

    int id2, ano2;

    string titulo2, autor2, editora2, genero2;
    cout << "Digite o id do livro: " << endl;
    cin >> id2;
    cout << "Digite o titulo do livro: " << endl;
    cin >> titulo2;
    cout << "Digite o autor do livro: " << endl;
    cin >> autor2;
    cout << "Digite a editora do livro: " << endl;
    cin >> editora2;
    cout << "Digite o ano do livro: " << endl;
    cin >> ano2;
    cout << "Digite o genero do livro: " << endl;
    cin >> genero2;


    livro.set_livro(id2, titulo2, autor2, editora2, ano2, genero2);
    livro.imprime();

    delete livroPtr;
    return 0;
}
