
# Cauã Borges Faria RA: 834437

## Respostas: Árvores B+, Árvores B+ de Prefixos Simples e Árvores B Virtuais

---

### 🌳 Árvore B+

**8. O que é uma Árvore B+? Quais as diferenças entre uma Árvore B+ e uma Árvore B?**  

Uma **Árvore B+** é uma estrutura de dados em árvore balanceada utilizada para armazenar grandes volumes de dados em sistemas de banco de dados e sistemas de arquivos. Diferente da Árvore B, na Árvore B+ todas as chaves e dados estão presentes apenas nas folhas, e os nós internos armazenam apenas chaves de busca.

**Diferenças:**  
- **Árvore B:** dados podem estar nos nós internos e folhas.  
- **Árvore B+:** dados **somente nas folhas**; nós internos possuem apenas chaves de direcionamento.  
- As folhas de uma Árvore B+ são **ligadas sequencialmente** (lista encadeada), facilitando buscas intervalares.

**Diagrama:**  

```
       [30|60]
       /   |   \
  [10|20] [40|50] [70|80|90]
```

- Nós internos: armazenam apenas chaves.  
- Nós folha: armazenam as chaves e os dados associados.

---

**9. Quais as vantagens e desvantagens de uma Árvore B+ em relação a uma Árvore B? Em que situações uma Árvore B+ pode ser mais interessante?**  

**Vantagens:**  
- Melhora o desempenho em buscas sequenciais e intervalares (folhas ligadas sequencialmente).  
- Estrutura mais eficiente para sistemas de arquivos e bancos de dados.  
- Facilita varreduras completas ordenadas.  

**Desvantagens:**  
- Ocupa mais espaço, pois mantém ponteiros de lista encadeada nas folhas.  
- Pode exigir mais escrita ao manter a ordem na lista encadeada de folhas.

**Situações vantajosas:**  
- Em **bancos de dados** onde buscas intervalares e ordenadas são frequentes.  
- Sistemas de arquivos e aplicações que precisam de acesso sequencial eficiente.

---

### 🌳 Árvore B+ de Prefixos Simples

**10. O que é uma Árvore B+ de Prefixos Simples?**  

É uma variação da Árvore B+ em que os nós internos armazenam **prefixos comuns** entre as chaves para economizar espaço. Os prefixos ajudam a identificar rapidamente as chaves sem armazená-las completamente nos nós internos.

**Diagrama:**

```
        [30|60]
        /   |   \
 [10|20] [40|50] [70|80|90]
```

- Mas os nós internos podem armazenar apenas os **prefixos** necessários para a busca.

**Funcionamento:**  
Reduz a quantidade de informações armazenadas nos nós internos usando prefixos comuns.

---

**11. Qual a aplicabilidade de uma Árvore B+ de Prefixos Simples?**  

**Aplicações:**  
- **Índices de banco de dados com chaves textuais ou de longa extensão**.  
- Situações onde os dados possuem **prefixos repetidos ou previsíveis**.  
- Ambientes onde é necessário **economizar espaço em disco** nos nós internos.

**Exemplo:**  
Em sistemas onde as chaves são números de CPF, prefixos podem reduzir redundância e otimizar armazenamento.

---

### 🌳 Árvore B Virtual

**12. O que é uma Árvore B Virtual?**  

É uma estrutura de árvore B onde as páginas (blocos de dados) são organizadas virtualmente na memória, sendo carregadas sob demanda em buffer ou memória cache.

**Diagrama:**

```
          Disco
         /  |  \
 Buffer [30|60] ...
        /  |   \
    [10|20] ...
```

**Funcionamento:**  
As páginas são carregadas dinamicamente para o buffer quando necessárias, otimizando acessos a disco e minimizando leituras.

---

**13. Em quais situações uma Árvore B Virtual pode ser útil? Qual a otimização que ela proporciona em termos de acessos a disco?**  

**Situações úteis:**  
- Sistemas de banco de dados com grande volume de dados armazenados em disco.  
- Ambientes onde a memória principal não suporta todas as páginas da árvore simultaneamente.

**Otimização:**  
- **Minimiza o número de acessos ao disco**, mantendo no buffer as páginas mais frequentemente acessadas.  
- Aproveita **localidade temporal** e **espacial**.

---

**14. Em uma Árvore B Virtual, quais páginas seria interessante manter no buffer? Quais as possíveis políticas de reposição?**  

**Páginas interessantes:**  
- **Raiz e níveis superiores da árvore** (pois são mais acessadas).  
- **Páginas recentemente acessadas**.

**Políticas de reposição:**  
- **LRU (Least Recently Used):** remove a página menos recentemente usada.  
- **MRU (Most Recently Used):** remove a mais recentemente usada.  
- **LFU (Least Frequently Used):** remove a página menos frequentemente acessada.  
- **FIFO (First In, First Out):** remove a primeira página que entrou no buffer.

---

*Documento produzido por Cauã Borges Faria, RA: 834437.*
