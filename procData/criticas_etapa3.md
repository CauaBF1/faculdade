# Grupo 1 — Climatologia e Sensoriamento Remoto

A relação com o GP3 está no contraste entre modelos mais sofisticados e abordagens mais simples/distribuídas. O grupo 1 comparou bem scale-up em GPU contra scale-out em Spark, parecido com o GP3 ao discutir GAT/deep learning versus classificadores tabulares em Spark. Porém, a comparação deles parece menos direta, porque os modelos usam horizontes, entradas e resoluções diferentes; o GP3 deixou mais claro o cuidado metodológico ao adaptar os métodos para o mesmo domínio/dataset.

# Grupo 2 — Risco de Crédito/Inadimplência

Esse tema se aproxima bastante do GP3, porque ambos trabalham com previsão de risco a partir de comportamento histórico: inadimplência no grupo 2 e churn/não recompra no GP3. O ponto forte deles foi comparar desempenho, custo computacional e explicabilidade. A crítica é que poderiam discutir mais se o ganho do CIF justifica a complexidade em produção, assim como o GP3 discutiu que nem sempre vale usar GAT se o grafo for artificial ou pouco defensável.

# Grupo 4 — Redes Sociais e Plataformas Digitais

A relação com o GP3 está no problema de escala: ambos discutem como adaptar métodos para caber em infraestrutura real. O grupo 4 foi forte na parte de arquitetura, Docker, Spark e GPUs, enquanto o GP3 conectou melhor a saída dos modelos com uma decisão prática de negócio. A crítica é que o grupo 4 poderia deixar mais claro como as características extraídas dos memes viram uma métrica final ou decisão, enquanto o GP3 transformou os resultados em ações de marketing, como retenção e priorização de clientes.

# Grupo 5 — Saúde e Tecnologia

O grupo 5 se relaciona com o GP3 pelo desafio de comparar uma solução mais simples com uma abordagem mais sofisticada: Spark + CNN centralizada versus aprendizado federado com EfficientNet, enquanto o GP3 comparou RFM/regressão/classificadores Spark com churn baseado em deep learning/grafos. A crítica é que a comparação mistura dois níveis diferentes: processamento distribuído de dados e treinamento distribuído federado. O GP3 foi mais cuidadoso ao explicar que técnicas diferentes resolvem partes diferentes do problema, em vez de tratá-las como concorrentes diretas.


