## 1- Mini Campo de Futebol com Mapeamento de Jogadores (TrueField)

## 2- Equipe:

- Cauã Borges Faria(834437)
- Vitor Rodruigues da Mata (831591)
- Yuri Arita de Carvalho (832916)

## 3- Definição da aplicação ou tema de estudo

A aplicação consiste em um mini campo de futebol virtual que será exibido durante transmissões esportivas, mostrando em tempo real a posição dos jogadores em campo. Este sistema utiliza tecnologia de rastreamento por sensores embutidos nos uniformes dos jogadores ou visão computacional para capturar suas posições, e as representa graficamente em um mapa bidimensional do campo, exibido no canto inferior da tela.

O mini campo funcionará como uma ferramenta complementar à transmissão principal, permitindo que os telespectadores visualizem a distribuição tática e o posicionamento de todos os jogadores simultaneamente, mesmo quando a câmera principal está focada em apenas uma parte do campo. Cada jogador será representado por um marcador distinto, identificado por número e/ou cor da equipe, e o sistema atualizará suas posições em tempo real conforme os movimentos em campo.

Além da visualização básica, o sistema **poderá** incluir funcionalidades adicionais como:

- Visualização de formações táticas
- Medição de distâncias entre jogadores
- Análise de cobertura espacial das equipes

Esta aplicação resolve um problema comum nas transmissões esportivas: a limitação da visão parcial do campo proporcionada pelas câmeras tradicionais, que frequentemente não permite ao espectador compreender completamente o contexto tático e posicional do jogo.

## 4- Estruturas estudadas na disciplina que serão utilizadas/estudadas/ilustradas

A principal estrutura de dados a ser utilizada neste projeto é a QUADtree (Quadtree), que é especialmente adequada para aplicações que lidam com dados espaciais bidimensionais. A QUADtree é uma estrutura de árvore em que cada nó interno possui exatamente quatro filhos, e é utilizada para particionar recursivamente um espaço bidimensional em quatro quadrantes.

No contexto do mini campo de futebol, a QUADtree será implementada para:

1. **Representação espacial eficiente**: O campo de futebol será representado como um espaço bidimensional que pode ser recursivamente subdividido em quadrantes, permitindo localizar rapidamente jogadores em regiões específicas.

2. **Consultas espaciais otimizadas**: A estrutura permitirá consultas rápidas como "quais jogadores estão nesta região do campo?" ou "qual é o jogador mais próximo desta posição?", essenciais para análises táticas em tempo real.

3. **Detecção de colisão/proximidade**: Facilitará a identificação de jogadores próximos uns aos outros ou de determinadas áreas do campo, útil para análises de marcação e cobertura.

4. **Atualização dinâmica eficiente**: Como as posições dos jogadores mudam constantemente, a QUADtree permite atualizações rápidas sem necessidade de reconstruir toda a estrutura.

5. **Otimização de renderização**: Permite renderizar apenas os elementos visíveis ou relevantes para a visualização atual, melhorando o desempenho.

Além da QUADtree, o projeto também poderá utilizar estruturas auxiliares como:
- Tabelas hash para associar identificadores de jogadores a suas informações
- Listas encadeadas para armazenar históricos de posicionamento
- Filas de prioridade para processamento de eventos de atualização

## 5- Principais unidades de software (caso pertinente) ou Referências iniciais de estudo

O sistema será composto pelas seguintes unidades de software principais:

1. **Módulo de Estrutura Espacial (QUADtree)**: Núcleo do sistema que implementa a estrutura de dados QUADtree para organizar e consultar eficientemente os dados espaciais:
   - Construção e manutenção da QUADtree
   - Algoritmos de inserção, remoção e busca espacial
   - Otimização para atualizações em tempo real
2. **Módulo de Renderização Gráfica**: Responsável pela representação visual do mini campo e dos jogadores:
   - Renderização do campo de futebol em 2D
   - Visualização dos marcadores dos jogadores
   - Elementos gráficos adicionais (zonas de calor, vetores de movimento, etc.)
   - Adaptação para diferentes resoluções e formatos de tela

## 6- Organização / divisão do trabalho

A organização do trabalho será estruturada em etapas funcionais, cada uma responsável por componentes específicos do sistema:

1. **Etapa de Estruturas de Dados e Algoritmos**:
   - Implementação da estrutura QUADtree
   - Desenvolvimento de algoritmos de consulta espacial
   - Otimização de desempenho para processamento em tempo real
   - Testes de eficiência e escalabilidade
3. **Etapa da Interface Gráfica**:
   - Design do mini campo e elementos visuais
   - Implementação do módulo de renderização
   - Otimização para diferentes resoluções e dispositivos
   - Testes de usabilidade e experiência do usuário

## 7- Plano de implantação (etapas / cronograma) – ideia geral

O plano de implantação será dividido em fases incrementais, permitindo validações parciais e ajustes ao longo do desenvolvimento:

**Fase 1: Concepção e Prototipagem**

- Definição detalhada dos requisitos e especificações
- Estudo aprofundado da estrutura QUADtree e suas aplicações espaciais
- Desenvolvimento de protótipos conceituais
- Validação da viabilidade técnica
- Definição da arquitetura do sistema

**Fase 2: Desenvolvimento do Núcleo**

- Implementação da estrutura QUADtree básica
- Desenvolvimento do módulo de aquisição de dados com dados simulados
- Criação da primeira versão do módulo de renderização
- Testes unitários dos componentes principais
- Integração inicial entre os módulos básicos

**Fase 3: Refinamento**

- Refinamento da interface gráfica
- Validação da estrutura QUADtree

**Marcos principais:**
- Final da Fase 1: Protótipo conceitual aprovado
- Final da Fase 2: Sistema básico funcional com dados simulados
- Final da Fase 3: Sistema completo otimizado em ambiente controlado
