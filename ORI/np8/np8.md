# Cauã Borges Faria (834437)
## Questão 1

A técnica de hash para acesso a informações em arquivos consiste em aplicar uma função matemática, chamada função de hash, sobre a chave de um registro para determinar a posição onde ele será armazenado ou onde deverá ser buscado no arquivo. Essa função transforma a chave em um endereço dentro de um intervalo fixo de posições possíveis. O objetivo é possibilitar o acesso direto ao registro, sem necessidade de percorrer sequências ordenadas ou desordenadas de dados. As principais características desse método incluem a rapidez no acesso, a simplicidade na busca e a dependência de uma função de hash bem construída, que distribua os registros de forma uniforme. Um desafio desse sistema é lidar com as colisões, que ocorrem quando duas chaves diferentes geram o mesmo endereço.

### Diagrama de funcionamento

```
Chave -> Função Hash -> Endereço no Arquivo
Ex: 1754 -> h(1754) = 4 -> posição 4 no arquivo
```

Suponha que se deseja armazenar as chaves 1754, 4891 e 3072 usando a função h(chave) = chave mod 10:

* h(1754) = 1754 mod 10 = 4
* h(4891) = 4891 mod 10 = 1
* h(3072) = 3072 mod 10 = 2

Assim, cada registro seria armazenado diretamente em sua posição resultante no arquivo.

## Questão 2

Uma colisão em um sistema de arquivos com acesso hash ocorre quando duas ou mais chaves diferentes, ao serem processadas pela função de hash, resultam no mesmo endereço de armazenamento no arquivo. Como cada posição só pode guardar um registro, é necessário adotar estratégias para resolver essas colisões. Elas são inevitáveis, especialmente quando o número de registros começa a se aproximar da quantidade de posições disponíveis ou quando a função de hash não distribui as chaves de forma uniforme.

## Questão 3

A técnica de tratamento de colisões chamada "progressive overflow", ou "endereçamento aberto", funciona tentando encontrar outra posição disponível no próprio arquivo quando ocorre uma colisão. Ao invés de utilizar estruturas auxiliares ou listas externas, o próprio arquivo é percorrido sequencialmente, a partir da posição calculada, até encontrar uma posição livre para inserir o novo registro. Esse processo de busca continua de maneira circular até que uma posição vaga seja localizada. É importante que exista espaço livre suficiente no arquivo para que o método funcione adequadamente, caso contrário a inserção falhará.

## Questão 4

A operação de busca ou consulta, em um sistema de arquivos utilizando hash com progressive overflow, começa aplicando a função de hash sobre a chave desejada para calcular seu endereço inicial. Em seguida, verifica-se o conteúdo dessa posição no arquivo. Se o registro encontrado corresponde à chave buscada, a pesquisa é concluída. Caso contrário, o sistema avança para a posição seguinte, de forma sequencial, respeitando o encadeamento circular do arquivo, até localizar a chave ou identificar que a posição inicial foi alcançada novamente sem sucesso, o que indica que o registro não está presente no arquivo.

## Questão 5

A operação de inserção de uma chave em um sistema de arquivos com hash usando progressive overflow também começa aplicando a função de hash sobre a chave para determinar seu endereço inicial. Se essa posição estiver livre, o registro é inserido ali. Caso contrário, ocorre uma colisão, e o sistema passa a procurar sequencialmente pela próxima posição disponível no arquivo. Esse processo de busca continua de forma circular até encontrar uma posição livre para a nova chave. Uma vez localizada, o registro é armazenado e a operação termina.

## Questão 6

A operação de remoção de uma chave, nesse contexto, inicia-se aplicando a função de hash para localizar a posição inicial onde a chave deveria estar. Se a chave estiver nessa posição, o registro é removido, e a posição pode ser marcada como "vaga especial" ou com um marcador indicando exclusão, para preservar o funcionamento do progressive overflow em buscas futuras. Caso a chave não esteja na posição prevista, o sistema avança sequencialmente, seguindo o encadeamento circular, até encontrá-la ou identificar que não está presente. Se encontrada, a chave é removida e a posição marcada de forma apropriada para manutenção da integridade da estrutura.

## Questão 7

A operação de alteração de uma chave em um sistema de arquivos com hash e progressive overflow pode ocorrer de duas formas, dependendo se apenas o valor associado ao registro será alterado ou se a própria chave sofrerá modificação. No primeiro caso, aplica-se a função de hash para localizar a posição do registro, seguindo o mesmo processo sequencial caso necessário. Ao encontrá-lo, o valor é atualizado diretamente. Se a alteração envolver a chave, o registro precisará ser removido da posição atual e reinserido, aplicando a função de hash à nova chave e tratando possíveis colisões com progressive overflow, garantindo que a estrutura continue funcional e as regras de endereçamento sejam mantidas.

