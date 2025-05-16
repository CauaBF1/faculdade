/*
Autor: Cauã Borges Faria
Data de criação: 28/08/2024
Data de modificação: 28/08/2024
objetivo: ler 2 circulos escrever eles e fazer operações de area, perimetro, distancia entre os centros, distancia
minima entre eles  e deslocamento do circulo
*/


// bibliotecas

#include <stdio.h>
#include <string.h>
#include <math.h>

// declarações globais

typedef struct {
  double x; // coordenada do eixo x
  double y; // coordenada do eixo y
} tPonto; // ponto no espaço Euclidiano bidimensional

typedef struct {
    tPonto centro;
    double raio;
} tCirculo;

// protótipos

void leiaCirculo(tCirculo *);
void escrevaCirculo(tCirculo);
double areaCirculo(tCirculo);
double perimetroCirculo(tCirculo);
double distanciaMinimaCirculos(tCirculo, tCirculo);
double distanciaCentros(tCirculo, tCirculo);
void deslocaCirculo(tCirculo *);

// função principal

int main()
{
  // declarações locais
  
  tCirculo circulo1;
  tCirculo circulo2;
  double area1, area2, perimetro1, perimetro2, distancia1, distancia2;
  char res[4];
  int nCirculo;
  // leitura de dados
  
  printf("Circulo 1\n");
  leiaCirculo(&circulo1);
  escrevaCirculo(circulo1);
  
  printf("Circulo 2\n");
  leiaCirculo(&circulo2);
  escrevaCirculo(circulo2);
  
//   operações com círculo
  
  area1 = areaCirculo(circulo1);
  printf("area do circulo 1 = %lf\n", area1);
  
  area2 = areaCirculo(circulo2);
  printf("area do circulo 2 = %lf\n", area2);
  
  perimetro1 = perimetroCirculo(circulo1);
  printf("perimetro do circulo 1 = %lf\n", perimetro1);

  perimetro2 = perimetroCirculo(circulo2);
  printf("perimetro do circulo 2 = %lf\n", perimetro2);

  distancia1 = distanciaCentros(circulo1, circulo2);
  printf("Distancia entre os centros do circulo 1 e circulo 2 = %lf\n", distancia1);
  
  distancia2 = distanciaMinimaCirculos(circulo1, circulo2);
  printf("Distancia mínima entre circulo1 e circulo2 = %lf\n", distancia2);  
  
  printf("Deseja deslocar o circulo ?[sim/nao]");
  scanf("%3s", res);
  
  if(strcmp(res, "sim") == 0){
        printf("Qual circulo voce deseja deslocar ? [1 ou 2]");
        scanf("%d", &nCirculo);
        if (nCirculo == 1) {
            deslocaCirculo(&circulo1);
            escrevaCirculo(circulo1);  // Mostra os dados do círculo 1 após o deslocamento
        } else {
            deslocaCirculo(&circulo2);
            escrevaCirculo(circulo2);  // Mostra os dados do círculo 2 após o deslocamento
        }       
  }
  
  
//   finalização do programa
  
  return 0;
}

/* 
  Nome: leiaCirculo
  Objetivo: ler os dados de um círculo, ou seja, ler as
            coordenadas de seu ponto central e o valor
            do seu raio.
  Parâmetro Formais
  - circulo: circulo que terá os seus dados lidos
             (parâmetro de saída de dados)
  Valor de retorno: nenhum.
 */

void leiaCirculo(tCirculo *circulo)
{
  printf("Digite as coordenadas do circulo:\n");
  printf("Digite o valor da coordenada x: ");
  // scanf("%lf", &(*circulo).centro.x);
  scanf("%lf", &circulo->centro.x);
  printf("Digite o valor da coordenada y: ");
  // scanf("%lf", &circulo->centro.y);
  scanf("%lf", &(*circulo).centro.y);
  printf("Digite o valor do raio do circulo: ");
  // scanf("%lf", &(*circulo).raio);
  scanf("%lf", &circulo->raio);

}

/* 
  Nome: escrevaCirculo
  Objetivo: escrever os dados de um círculo, ou seja, as
            coordenadas de seu ponto central e o valor
            do seu raio.
  Parâmetro Formais
  - c: circulo que terá os seus dados escritos
             (parâmetro de entrada de dados)
  Valor de retorno: nenhum.
 */
 
void escrevaCirculo(tCirculo c)
{
  printf("Dados do circulo:\n");
  printf("Coordenada x = %.2lf\n", c.centro.x);
  printf("Coordenada y = %.2lf\n", c.centro.y);
  printf("Raio = %.2lf\n", c.raio);
}


/* 
  Nome: areaCirculo
  Objetivo: calcular area do circulo
  Parâmetro Formais
  - c
  Valor de retorno: area.
 */

double areaCirculo(tCirculo c){
    double area, pi = 3.141592653589793;
    
    area = pi*(c.raio * c.raio);
    return area;
}

/* 
  Nome: perimetroCirculo
  Objetivo: calcular perimetro do circulo
  Parâmetro Formais
  - c
  Valor de retorno: area.
 */

double perimetroCirculo(tCirculo c){
    double perimetro, pi = 3.141592653589793;
    perimetro = 2 * pi * c.raio;
    return perimetro;
}

/* 
  Nome: distanciaMinimaCirculos
  Objetivo: calcular distancia minima entre circulos
  Parâmetro Formais
  - c1
  - c2
  Valor de retorno: area.
 */
double distanciaMinimaCirculos(tCirculo c1, tCirculo c2){
    double distanciaCentros, distanciaRaios;
    
    // Calcula a distância entre os centros dos círculos
    distanciaCentros = sqrt(pow(c2.centro.x - c1.centro.x, 2) + pow(c2.centro.y - c1.centro.y, 2));
    
    // Calcula a distância entre os raios (distância entre os centros menos a soma dos raios)
    distanciaRaios = distanciaCentros - (c1.raio + c2.raio);
    
    return distanciaRaios;
    
}


/* 
  Nome: distanciaCentros
  Objetivo: calcular distancia entre centro dos circulos
  Parâmetro Formais
  - c1
  - c2
  Valor de retorno: area.
 */

double distanciaCentros(tCirculo c1, tCirculo c2) {
    double distanciaCentros, distanciaMinima;
    // Calcula a distância entre os centros dos círculos
    distanciaCentros = sqrt(pow(c2.centro.x - c1.centro.x, 2) + pow(c2.centro.y - c1.centro.y, 2));
    return distanciaCentros;
}

/* 
  Nome: deslocaCirculo
  Objetivo: deslocar circulo
  Parâmetro Formais
  - c1
  Valor de retorno: area.
 */
void deslocaCirculo(tCirculo *circulo){
    printf("Digite as novas coordenadas do circulo:\n");
    printf("Digite o valor da coordenada x: ");
    // scanf("%lf", &(*circulo).centro.x);
    scanf("%lf", &circulo->centro.x);
    printf("Digite o valor da coordenada y: ");
    // scanf("%lf", &circulo->centro.y);
    scanf("%lf", &(*circulo).centro.y);
    //printf("Digite o valor do raio do circulo: ");
    // scanf("%lf", &(*circulo).raio);
    //scanf("%lf", &circulo->raio);
}


