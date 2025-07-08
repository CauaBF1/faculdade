# Documentação do `truefield.py`

## Visão Geral
O `truefield.py` é um simulador de futebol desenvolvido em Python usando a biblioteca Pygame. O programa implementa uma simulação de futebol com recursos avançados como detecção de posse de bola usando estruturas de dados Quadtree, geração de heatmaps de movimentação dos jogadores e visualização em tempo real.

## Principais Classes e Componentes

### 1. **Classe Quadtree**
- **Propósito**: Estrutura de dados espacial para otimizar consultas de proximidade
- **Funcionalidades**:
  - `subdivide()`: Divide recursivamente o espaço em 4 quadrantes
  - `insert()`: Insere pontos (jogadores) na estrutura
  - `query()`: Busca eficiente por jogadores em uma área específica
  - `clear()`: Limpa a estrutura
  - `draw_debug()`: Visualiza a estrutura da quadtree

### 2. **Classe Campo**
- **Propósito**: Representa o campo de futebol e gerencia a lógica do jogo
- **Funcionalidades**:
  - Gerencia a quadtree dos jogadores
  - Detecta posse de bola baseada em proximidade
  - Desenha o campo com marcações oficiais
  - Verifica condições de gol

### 3. **Classe Bola**
- **Propósito**: Representa a bola do jogo
- **Funcionalidades**:
  - Movimentação com controles WASD
  - Renderização visual

### 4. **Classe Jogador**
- **Propósito**: Representa cada jogador no campo
- **Funcionalidades**:
  - Movimentação com restrições de campo
  - Visualização diferenciada quando tem posse da bola
  - Identificação numérica

## Recursos Principais

### **Sistema de Posse de Bola**
- Utiliza Quadtree para detecção eficiente de proximidade
- Distância configurável para posse (30px por padrão)
- Visualização em tempo real do jogador com posse
- Linha conectando bola ao jogador com posse

### **Heatmap de Movimentação**
- Coleta posições dos jogadores em intervalos regulares
- Gera mapa de calor das áreas mais utilizadas
- Suporte a heatmap individual por jogador
- Salva automaticamente ao sair do programa

### **Formação Tática**
- Times configurados em formação 4-3-3
- Time amarelo (esquerda) vs time azul (direita)
- 11 jogadores por time com posicionamento realista

## Controles

- **WASD**: Movimentar a bola
- **Setas**: Movimentar jogador selecionado
- **Click**: Selecionar jogador
- **Q**: Toggle debug da quadtree
- **H**: Toggle heatmap geral
- **N**: Alternar heatmap individual dos jogadores

## Constantes Configuráveis

```python
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FIELD_WIDTH, FIELD_HEIGHT = 1000, 600
BALL_RADIUS, PLAYER_RADIUS = 10, 15
BALL_SPEED, PLAYER_SPEED = 4, 4
POSSE_DISTANCE = 30  # Distância para posse de bola
SLICE_TIME = 100     # Intervalo de coleta do heatmap
```

## Funcionalidades Técnicas

### **Otimização de Performance**
- Quadtree para consultas espaciais O(log n)
- Renderização otimizada com Pygame
- Atualização eficiente de estado

### **Análise de Dados**
- Histórico de posições dos jogadores
- Geração de heatmaps por célula
- Exportação automática de dados

### **Interface Visual**
- Campo com marcações oficiais
- Placar em tempo real
- Instruções na tela
- Debug visual da quadtree

## Uso

Para executar o programa:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 truefield.py
```

O programa é ideal para análise de movimentação em jogos de futebol, estudos de estruturas de dados espaciais e desenvolvimento de jogos 2D com Pygame.
