/*
Cauã Borges Faria (834437)
Nicolas Magno Messias da Silva (834054)
Ryan Augusto Ribeiro (830913)
Murilo Oliva Mantovani (834730)
Lucas Rodrigues da Silva (834724)
*/

#ifndef LIVROS_H
#define LIVROS_H

#include <string>

using std::string;
using std::cout;
using std::cin;
using std::endl;

class Livros {
private:
    int id;
    string titulo;
    string autor;
    string editora;
    int ano;
    string genero;
public:
    void set_livro(int, string&, string&, string&, int, string&);
    void set_id(int);
    void set_titulo(string&);
    void set_autor(string&);
    void set_editora(string&);
    void set_ano(int);
    void set_genero(string&);
    int get_id() const;
    string get_titulo() const;
    string get_autor() const;
    string get_editora() const;
    int get_ano() const;
    string get_genero() const;
    void imprime() const;
};

inline void Livros::set_livro(int id, string& titulo, string& autor, string& editora, int ano, string& genero) {
    set_id(id);
    set_titulo(titulo);
    set_autor(autor);
    set_editora(editora);
    set_ano(ano);
    set_genero(genero);
}

inline void Livros::set_id(int id) {
    this->id = id;
}

inline void Livros::set_titulo(string& titulo) {
    this->titulo = titulo;
}

inline void Livros::set_autor(string& autor) {
    this->autor = autor;
}

inline void Livros::set_editora(string& editora) {
    this->editora = editora;
}

inline void Livros::set_ano(int ano) {
    this->ano = ano;
}

inline void Livros::set_genero(string& genero) {
    this->genero = genero;
}

inline int Livros::get_id() const {
    return id;
}

inline string Livros::get_titulo() const {
    return titulo;
}

inline string Livros::get_autor() const {
    return autor;
}

inline string Livros::get_editora() const {
    return editora;
}

inline int Livros::get_ano() const {
    return ano;
}

inline string Livros::get_genero() const {
    return genero;
}

inline void Livros::imprime() const {
    cout << "ID: " << id << endl << "Titulo: " << titulo << endl <<
        "Autor: " << autor << endl << "Editora: " << editora << endl <<
            "Ano: " << ano << endl << "Genero: " << genero << endl;
}

#endif