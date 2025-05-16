### Cauã Borges Faria (834437)

#### Questão 3

Sim, um registro com número fixo de campos geralmente terá tamanho fixo desde que todos os campos sejam de tipos de tamanho fixo, como int, float. Nesse caso, o compilador aloca uma quantidade fixa de memória para cada campo, porém se o registro tiver campos com tamanho variavel como ponteiros para listas, o tamanho dos dados pode variar.

#### Questão 4

Em arquivos com registros de tamanho variável, isso não é possível diretamente, pois os registros ocupam espaços diferentes e não há uma fórmula simples para calcular a posição de um registro. Nesse caso, é necessário manter uma estrutura auxiliar, como um índice, que armazene os offsets de cada registro para permitir acesso direto.

#### Questão 9

Para armazenar informações sobre preços de produtos em um e-commerce, a melhor escolha seria usar registros de tamanho fixo com campos bem definidos, como ID do produto, nome e preço. Isso permite acesso direto e eficiente aos dados, facilitando consultas frequentes e rápidas.

#### Questão 10

Armazenar os dados com tamanho variado organizados por tags, onde cada cenário é representado por uma tag que agrupa suas imagens, sons e demais atributos.

#### Questão 11

- Processamento sequencial: Percorre todos os registros do arquivo um a um, na ordem em que foram armazenados
- Acesso direto (RRN / Byte Offset): Permite localizar rapidamente um registro específico usando seu número relativo (RRN) ou o deslocamento em bytes.(Precisa ter tamanho fixo ou índice)
- Busca por chave primária: Localiza um registro específico com base em um identificador único, como um código ou ID.
- Busca por valor de campo: Retorna um ou mais registros que possuam um determinado valor em um campo(ex: retorna todos os cadernos).

#### Questão 12

A operação de acesso sequencial funciona lendo ou processando os registros de um arquivo na ordem em que eles foram armazenados, exemplo: emissão de boletos bancários no final do mês. O sistema percorre, um por um, todos os registros de clientes cadastrados no arquivo e gera o boleto correspondente para cada um, seguindo a ordem de armazenamento.

#### Questão 13

Operação de acesso direto via RRN é um método utilizado para acessar diretamente registros em um arquivo de dados baseado em números de registros, ele facilita o acesso direto a um registro específico, sem a necessidade de percorrer todos os registros anteriores. Exemplo: um arquivo de dados de 840 produtos é preciso consultar o estoque do produto 720, dessa forma é somente utilizar o RRN associado ao produto 720.
