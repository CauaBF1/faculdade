#include <iostream>
using std::ostream;
using std::istream;

class Array {

private:
  int size;
  int *ptr;
public:
  Array (int = 10);// construtor
  Array (const Array &);// copia
  ~Array();
  int getSize() const;
  
  const Array &operator=(const Array&); // atribuição
  bool operator==(const Array&) const; // igualdade
  bool operator!=(const Array &right) const{
    return ! (*this == right); //usando Array::operator==
  }
  // alocação dinamica
  int &operator[](int);

  const int operator[] (int) const;
};

Array::Array(int size){
  if(size > 0){
    this->size = size;
  }else{
    this->size = 10;
  }
    ptr = new int [size];

  for (int i = 0; i < size; i++){
    ptr[i] = 0;
  }
}


Array::Array(const Array &arr):size(arr.size){
  ptr = new int [size];
  for (int i = 0; i < size; i++) {
    ptr [i] = arr.ptr[i];
  }
}

Array::~Array(){
  delete [] ptr;
}

int Array::getSize()const{
  return size;
}

const Array &Array::operator==(const Array &right){
  if(&right != this){
    if(size != right.size){
      delete [] ptr;
      size = right.size;
      ptr = new int [size];
    }
    for(int i = 0; i < size; i++){
      ptr[i] = right.ptr[i];
    }
  }
  return *this;
}

bool Array::operator==(const Array &right) const {
  if(size != right.size){
    return false;
  }

  for(int i = 0; i < size; i++){
    if(ptr[i] != right.ptr[i]){
      return false;
    }
  }
  return true;
}

// sobrecarregando subscrito, inteiro1[5] vai chamar inteiro1.operator[] (5)
int &Array::operator[](int subscript){
  if(subscript < 0 || subscript >= size){
    cout << "\nErro: indice" << subscript << "fora do range" << endl;
    exit(1);
  }
  return ptr[subscript];
}




