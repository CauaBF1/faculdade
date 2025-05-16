### Cauã Borges Faria (834437)

#### Link

https://onlinegdb.com/fUdJb_0us

#### Código

```cpp
#include <iostream>
#include <fstream>

using namespace std;

struct registro
{
    int id;
    char name[20];
    int age;
};

typedef struct registro Registro;

Registro r;
int n; // número de registros
int i; // contador

void escrever()
{
    cout << "Digite o número de registros que deseja inserir: ";
    cin >> n;
    ofstream arq("dados.dat", ios::binary);
    if (!arq)
    {
        cout << "Erro ao abrir o arquivo!" << endl;
        return;
    }

    for (i = 0; i < n; i++)
    {
        cout << "Digite o ID: ";
        cin >> r.id;
        cout << "Digite o nome: ";
        cin >> r.name;
        cout << "Digite a idade: ";
        cin >> r.age;

        arq.write((char *)&r, sizeof(r));
        cout << "dados lidos e gravados: " << r.id << " " << r.name << " " << r.age << endl;
    }
    arq.close();
}

void ler()
{
    ifstream arq("dados.dat", ios::binary);
    if (!arq)
    {
        cout << "Erro ao abrir o arquivo!" << endl;
        return;
    }

    while (arq.read((char *)&r, sizeof(r)))
    {
        cout << "ID: " << r.id << ", Nome: " << r.name << ", Idade: " << r.age << endl;
    }
    arq.close();
}

void lerRegistroEspecifico()
{
    ifstream arq("dados.dat", ios::binary);
    if (!arq)
    {
        cout << "Erro ao abrir o arquivo!" << endl;
        return;
    }

    int indice;
    cout << "Digite o índice do registro que deseja ler (0 a " << n - 1 << "): ";
    cin >> indice;

    if (indice < 0 || indice >= n)
    {
        cout << "Índice inválido!" << endl;
        arq.close();
        return;
    }

    // Calcula a posição do registro no arquivo
    arq.seekg(indice * sizeof(r), ios::beg); // ios::beg para começar do início do arquivo

    // Lê o registro específico
    if (arq.read((char *)&r, sizeof(r)))
    {
        cout << "Registro encontrado:" << endl;
        cout << "ID: " << r.id << ", Nome: " << r.name << ", Idade: " << r.age << endl;
    }
    else
    {
        cout << "Erro ao ler o registro!" << endl;
    }

    arq.close();
}

int main()
{
    int opcao;

    do
    {
        cout << "Menu:" << endl;
        cout << "1. Escrever registros" << endl;
        cout << "2. Ler registros sequencialmente" << endl;
        cout << "3. Ler registro específico" << endl;
        cout << "0. Sair" << endl;
        cout << "Escolha uma opção: ";
        cin >> opcao;

        switch (opcao)
        {
        case 1:
            escrever();
            break;
        case 2:
            ler();
            break;
        case 3:
            lerRegistroEspecifico();
            break;
        case 0:
            cout << "Saindo..." << endl;
            break;
        default:
            cout << "Opção inválida!" << endl;
        }
    } while (opcao != 0);

    return 0;
}

```
