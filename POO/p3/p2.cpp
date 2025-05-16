#include <iostream>
using namespace std;

template <class T>
class Fila {
private:
  int size;
  int top;
  T * filaptr;

public:
  Fila(int s = 10) {
    size = s;
    top = -1;
    filaptr = new T[size];
  }

  ~Fila() {
    delete [] filaptr;
  }

  void push(T data) {
    if (isFull()) {
      cout << "Fila cheia" << endl;
      return;
    }
    filaptr[++top] = data;
  }

  T pop() {
    if (isEmpty()) {
      cout << "Fila vazia" << endl;
      return T(); // Retorna valor padrão de T
    }
    T data = filaptr[0];
    for (int i = 0; i < top; i++) {
      filaptr[i] = filaptr[i + 1];
    }
    top--;
    return data;
  }

  bool isEmpty() {
    return top == -1;
  }

  bool isFull() {
    return top == size - 1;
  }

  T front() {
    if (isEmpty()) {
      cout << "Fila vazia" << endl;
      return T(); // Retorna valor padrão de T
    }
    return filaptr[0];
  }

  T back() {
    if (isEmpty()) {
      cout << "Fila vazia" << endl;
      return T(); // Retorna valor padrão de T
    }
    return filaptr[top];
  }
};


int main(){
  Fila <int>a;
  Fila <string>b;
  a.push(1);
  b.push("teste");
  cout << a.pop() << endl;
  cout << b.pop() << endl;
}


/*
Questão 2
int main(){
    Instrumento * ptr = new Sax;
    ptr->Nome();
    delete ptr;
    return 0;
}

output: "Instrumento" como o metodo Nome() não é virtual e o ponteiro é do tipo Instrumento ele chama o metodo da classe base

Questão 3
int main(){
    Instrumento * ptr = new Sax;
    ptr->Tocar();
    delete ptr;
    return 0;
}

não compila, pois Sax herda de Sopro e Sopro não implementou o metodo  virtual puro Tocar()

Questão 4
int main(){
    Instrumento * ptr = new Sax;
    ptr->Afinar();
    delete ptr;
    return 0;
}

output: "Sax afinado" pois o metodo Afinar() é virtual e foi implementado na classe Sax

Questão 5
int main(){
    Sopro obj1;
    obj1.Nome();
    return 0;
}

não compila, pois Sopro é uma classe abstrata(ainda tem um metodo virtual puro) e não pode ser instanciada. Não é possível instanciar objetos de uma classe abstrata.

Questão 6
int main(){
    Trombone obj2;
    obj2.Nome();
    return 0;
}

class Trombone : public Sopro{
    public:
        void Nome() const{
            Sopro::Nome();
            cout << " - Trombone";
        }
        
        virtual void Afinar() const{
            cout << "Trombone afinado";
        }

        virtual void Tocar() const{
            cout << "Trombone tocando";
        }
}

output: "Instrumento - Sopro - Trombone" pois o metodo Nome() da classe Sopro foi chamado e depois foi impresso " - Trombone"

foi necessário implementar os metodos Afinar() e Tocar() pois eles são virtuais puros na classe Sopro e Instrumento respectivamente
*/