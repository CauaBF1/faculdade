# Atividade Avaliativa 1
### Exercicio 1



### Exercicio 2
https://onlinegdb.com/_x_qBiJuV
```cpp
#include <iostream>
#define MAX_SIZE 10000

int size_str(const char* str) {
    if (*str == '\0') {
        return 0;
    }
    return 1 + size_str(str + 1);
}

int main() {
    // Cria ponteiro com tamamho maximo
    char* str = new char[MAX_SIZE];

    std::cout << "Digite a string: ";
    std::cin.getline(str, MAX_SIZE);

    std::cout << "Número de caracteres: " << size_str(str) << std::endl;

    // Retira uso de memoria do ponteiro
    delete[] str;
    return 0;
}

```

### Exercicio 3
https://onlinegdb.com/XGVlbOntJ
```cpp
#include <iostream>
using namespace std;

double maiorElemento(double* v, int size, double maior) {
    if(size == 0) {
        return maior;
    }
    if(*v > maior) {
        maior = *v;
    }
    return maiorElemento(v+1, size - 1, maior);
}


int main() {
    int size;
    cout << "Digite o numero de elementos do array:" << endl;
    cin >> size;

    double* array = new double[size];

    cout << "Digite os elementos do array:" << endl;
    for(int i = 0; i < size; i++) {
        cin >> array[i];
    }

    if(size == 0) {
        cout << "Array vazio" << endl;
    }else {
        cout << "Maior elemento: " << maiorElemento(array, size, array[0]) << endl;
    }

    delete [] array;
    return 0;
}
```

### Exercicio 4
https://onlinegdb.com/zZM9zCG5UQ
```cpp
#include <iostream>
#include <cmath>

bool isPrime(int n, int i) {
    if(n < 2) return false;
    if(i == 1) return true;// divisivel somente por 1 e por ele mesmo
    if(n % i == 0) return false; // divisivel por outro numero
    return isPrime(n, i - 1); // chama recursão com i - 1
}
// A função divide o numero por todos seus antecessores até chegar em 1,
// se o numero for divisivel por algum numero diferente de 1 e ele mesmo, ele não é primo

int main() {
    int numero;
    std::cout << "Digite um número: ";
    std::cin >> numero;

    int limite = std::sqrt(numero);

    if(isPrime(numero,limite)) {
        std::cout << "É primo" << std::endl;
    }else {
        std::cout << "Não é primo" << std::endl;
    }
}
```

### Exercicio 5
https://onlinegdb.com/jieTWQ6xP
```cpp
#include <iostream>

int josephus(int n, int k) {
    // se houver apenas uma pessoa, ela é o sobrevivente
    if (n == 1)
        return 0; // posição 0 do array
    else
        // caso de n-1 pessoas e ajusta a posição com (J(n-1, k) + k) % n
            return (josephus(n - 1, k) + k) % n;
}

int main() {
    int n, k;
    std::cout << "Digite o número de soldados (n): ";
    std::cin >> n;
    std::cout << "Digite o número de pulos (k): ";
    std::cin >> k;

    // A função retorna a posição com base em índice 0, então somamos 1 para ficar mais legivel.
    int sobrevivente = josephus(n, k) + 1;
    std::cout << "O sobrevivente está na posição: " << sobrevivente << std::endl;

    return 0;
}
```
O problema de josephus se trata de retornar a posição do soldado sobrevivente que vão se matando de k em k para isso o caso base é quando a somente um soldado que retorna 0(posição no array) o caso recursivo é chamando o algoritmo de josephus com (n-1, k) + k para ajeitar a posição no array depois da eliminação de um soldado e por final % n para que as posições sejam mantidas dentro do limite.  
Complexidade O(n).



