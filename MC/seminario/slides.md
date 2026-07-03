## Etapas do método

As etapas do Planejamento e Execução de Experimentos, também conhecido como DoE, organizam a pesquisa experimental para que ela não seja apenas uma sequência de testes aleatórios. A ideia central é transformar uma dúvida de pesquisa em um experimento controlado, capaz de gerar dados confiáveis e conclusões justificáveis.

A primeira etapa é a **definição do problema**. Nela, o pesquisador precisa deixar claro o que deseja investigar. Em computação, por exemplo, isso pode aparecer como a pergunta: “um novo algoritmo de ordenação é mais eficiente que o algoritmo tradicional?” ou “uma técnica de aprendizado de máquina melhora a precisão de classificação em determinado conjunto de dados?”. Essa etapa é importante porque um experimento mal definido tende a gerar resultados confusos, mesmo que a execução técnica seja correta.

Depois vem a **formulação da hipótese**. A hipótese é uma afirmação que será testada pelo experimento. Por exemplo: “se o algoritmo A usa uma estratégia de paralelização, então ele terá menor tempo de execução que o algoritmo B em grandes volumes de dados”. A hipótese precisa ser verificável, ou seja, deve ser possível coletar dados que indiquem se ela foi confirmada ou rejeitada.

A terceira etapa é a **identificação das variáveis do experimento**. No DoE, é comum separar as variáveis em fatores, níveis e variáveis de resposta. Os **fatores** são os elementos que o pesquisador manipula ou controla, como tipo de algoritmo, tamanho da entrada, compilador utilizado, número de threads ou configuração de hardware. Os **níveis** são os valores possíveis desses fatores. Por exemplo, o fator “número de threads” pode ter os níveis 1, 2, 4 e 8. Já a **variável de resposta** é aquilo que será medido, como tempo de execução, consumo de memória, taxa de acerto, latência, throughput ou consumo de energia.

Em seguida ocorre o **planejamento experimental** propriamente dito. Nessa fase, decide-se como o experimento será executado. É aqui que entram decisões como quantas repetições serão feitas, quais combinações de fatores serão testadas, como os testes serão distribuídos e como evitar interferências externas. Essa etapa é essencial porque permite reduzir vieses e aumentar a confiabilidade dos resultados. Por exemplo, se um algoritmo for testado sempre primeiro e outro sempre depois, pode haver interferência de cache, aquecimento da máquina ou uso variável de recursos do sistema. Por isso, técnicas como randomização, replicação e blocagem são usadas para melhorar a qualidade do experimento.

A **execução do experimento** é a etapa em que os testes planejados são realizados e os dados são coletados. Essa fase deve seguir rigorosamente o planejamento anterior. Em computação, isso significa registrar configurações de hardware, versões de software, linguagem utilizada, compilador, sistema operacional, parâmetros dos algoritmos, bases de dados e critérios de medição. Esses detalhes são fundamentais para permitir que outras pessoas compreendam e, se possível, repliquem o experimento.

Depois da execução vem a **análise dos dados**. Nessa etapa, os resultados coletados são organizados e avaliados por meio de tabelas, gráficos e métodos estatísticos. O objetivo é verificar se as diferenças observadas são relevantes ou se podem ser explicadas por variações aleatórias. Por exemplo, se um algoritmo foi 2% mais rápido que outro em apenas uma execução, isso pode não ser suficiente para afirmar que ele é realmente melhor. Porém, se essa diferença aparece de forma consistente em várias repetições e sob diferentes condições, a conclusão se torna mais forte.

Por fim, há a **interpretação e comunicação dos resultados**. Nessa etapa, o pesquisador relaciona os dados obtidos com a pergunta inicial e com a hipótese formulada. Também é necessário apresentar limitações, ameaças à validade e condições em que os resultados podem ou não ser generalizados. Em um experimento de computação, por exemplo, não basta dizer que um modelo de machine learning teve melhor desempenho; é preciso explicar em qual base de dados, com quais métricas, em quais condições e se o ganho compensa o custo computacional.

Portanto, as etapas do método ajudam a garantir que a pesquisa experimental seja sistemática, controlada, verificável e reprodutível. Elas evitam que o pesquisador tire conclusões precipitadas a partir de testes isolados e permitem que o experimento tenha valor científico.

---

## Tipos de planejamento experimental

Neste slide, a ideia principal é mostrar que existem diferentes tipos de planejamento experimental, e que a escolha depende do objetivo da pesquisa.

Não existe um único tipo ideal para todos os casos. O pesquisador precisa considerar o que quer descobrir, quantos fatores serão analisados, quanto tempo e recurso estão disponíveis e qual nível de detalhe é necessário para interpretar os resultados.

Um primeiro tipo é o **planejamento comparativo**. Ele é usado quando queremos comparar alternativas. Em computação, isso pode acontecer quando comparamos dois algoritmos, duas bibliotecas ou duas versões de uma ferramenta. Por exemplo: queremos saber se o algoritmo A é mais rápido que o algoritmo B. Esse tipo é simples e direto, mas não explica muito bem quais fatores causaram a diferença se houver muitas variáveis envolvidas.

Outro tipo é o **planejamento de triagem**, também chamado de *screening*. Ele é usado quando existem muitos fatores possíveis e ainda não sabemos quais realmente influenciam o resultado. Em vez de testar tudo em profundidade, fazemos uma primeira seleção dos fatores mais importantes. Em computação, isso pode ser usado para descobrir quais hiperparâmetros mais afetam a acurácia de um modelo de aprendizado de máquina, ou quais configurações mais influenciam o desempenho de um sistema.

Também temos o **planejamento fatorial completo**. Nesse caso, todas as combinações entre fatores e níveis são testadas. Ele é útil quando temos poucos fatores e queremos observar não só o efeito de cada um separadamente, mas também as interações entre eles. Por exemplo, podemos testar ao mesmo tempo o algoritmo usado, o compilador e o tamanho da entrada. A vantagem é que ele gera bastante informação, mas a desvantagem é que o número de testes cresce muito rápido.

Quando o fatorial completo fica caro ou demorado demais, podemos usar o **planejamento fatorial fracionário**. Ele testa apenas uma parte das combinações possíveis. Isso reduz custo e tempo, mas exige mais cuidado na interpretação, porque alguns efeitos podem ficar misturados com outros. Em computação, isso é útil quando há muitas configurações de hardware, software ou parâmetros de sistema.

Outro tipo importante é a **metodologia de superfície de resposta**. Ela é usada quando o objetivo é otimizar uma resposta. Ou seja, não queremos apenas comparar alternativas, mas encontrar a melhor configuração possível. Em computação, isso pode ser aplicado para escolher o número ideal de threads, o tamanho de buffer ou a taxa de aprendizado de um modelo.

O **planejamento robusto**, associado ao método de Taguchi, busca encontrar configurações que funcionem bem mesmo quando existem variações externas. A ideia não é apenas ter bom desempenho em uma situação ideal, mas manter estabilidade mesmo com ruído. Em computação, isso pode ser útil para avaliar sistemas sob diferentes cargas de uso, variações de rede ou diferenças de hardware.

Por fim, existe o **planejamento de misturas**, usado quando os fatores representam proporções de um todo. Ele é mais comum em áreas como química e engenharia, mas pode ser adaptado para computação quando queremos avaliar a distribuição proporcional de recursos, como CPU, memória e armazenamento.

Então, resumindo: se o objetivo é comparar alternativas, usamos um planejamento comparativo. Se há muitos fatores, usamos triagem. Se queremos testar todas as combinações, usamos fatorial completo. Se queremos reduzir custo, usamos fatorial fracionário. Se queremos otimizar uma resposta, usamos superfície de resposta. Se buscamos estabilidade, usamos planejamento robusto. E, quando os fatores são proporções, usamos planejamento de misturas.

---

## Interpretação dos resultados

A interpretação dos resultados é uma das partes mais importantes do método experimental, porque é nela que os dados deixam de ser apenas números e passam a responder à pergunta de pesquisa. Um erro comum é interpretar os resultados apenas olhando qual valor foi maior ou menor. No entanto, em um experimento científico, é necessário analisar se a diferença observada é confiável, relevante e coerente com o contexto.

O primeiro ponto a observar é a **magnitude do efeito**. Isso significa avaliar o tamanho da diferença entre os tratamentos. Em computação, por exemplo, um algoritmo pode ser mais rápido que outro, mas a diferença pode ser muito pequena. Se um sistema reduz o tempo de execução de 10 segundos para 9,9 segundos, talvez a melhoria não justifique a troca, principalmente se o novo método for mais complexo ou consumir mais memória. Por outro lado, uma redução de 10 segundos para 4 segundos pode representar um ganho prático significativo.

O segundo ponto é a **variabilidade dos dados**. Resultados experimentais podem mudar por causa de fatores externos, como carga do sistema operacional, uso de memória, variações na rede, diferenças entre entradas ou comportamento não determinístico de alguns algoritmos. Por isso, repetir o experimento é fundamental. Se o resultado aparece apenas uma vez, ele pode ser fruto de acaso. Se aparece de forma consistente em várias execuções, a conclusão se torna mais confiável.

A interpretação também deve considerar a **incerteza estatística**. Em muitos experimentos, utiliza-se média, mediana, desvio padrão, intervalo de confiança e testes estatísticos para verificar se as diferenças observadas são significativas. A média mostra uma tendência geral, mas pode ser influenciada por valores extremos. A mediana pode ser mais robusta quando há outliers. O desvio padrão ajuda a entender se os resultados são estáveis ou muito dispersos. Já o intervalo de confiança indica uma faixa provável para o valor real do efeito observado.

Outro elemento importante é a **visualização dos dados**. Gráficos podem revelar padrões que tabelas não mostram claramente. Em experimentos computacionais, gráficos de barras, boxplots, linhas de tendência e gráficos de dispersão são úteis para comparar desempenho, identificar outliers e observar interações entre fatores. Por exemplo, um gráfico pode mostrar que um algoritmo é melhor para entradas pequenas, mas pior para entradas grandes. Essa informação seria perdida se a análise considerasse apenas uma média geral.

A interpretação dos resultados também precisa avaliar as **ameaças à validade**. A validade interna está relacionada à pergunta: “o efeito observado foi realmente causado pelo tratamento?”. Por exemplo, se um algoritmo parece mais rápido, mas foi testado em uma máquina menos carregada que o outro, a validade interna está comprometida. A validade externa pergunta se os resultados podem ser generalizados para outros contextos. Um modelo de aprendizado de máquina pode funcionar bem em uma base específica, mas não necessariamente em outras. A validade de construto avalia se as métricas usadas realmente medem aquilo que se deseja investigar. Por exemplo, medir apenas acurácia pode ser insuficiente em problemas com classes desbalanceadas. A validade de conclusão está ligada ao uso correto dos métodos estatísticos e à consistência das inferências feitas.

Outro cuidado é separar **significância estatística** de **relevância prática**. Um resultado pode ser estatisticamente significativo, mas pouco importante na prática. Em uma base de dados muito grande, diferenças pequenas podem aparecer como estatisticamente relevantes, mesmo sem impacto real. Por isso, a interpretação precisa considerar o contexto da aplicação. Em sistemas críticos, uma melhoria pequena em segurança pode ser muito importante. Já em sistemas simples, um ganho mínimo de desempenho pode não compensar o aumento de complexidade.

Em computação, também é importante interpretar os resultados considerando **trade-offs**. Um método pode melhorar uma métrica e piorar outra. Um algoritmo pode ser mais rápido, mas consumir mais memória. Um modelo pode ter maior acurácia, mas exigir muito mais tempo de treinamento. Uma técnica de segurança pode aumentar a proteção, mas reduzir desempenho. Assim, a conclusão não deve ser simplificada como “método A é melhor que método B”, mas sim explicar em quais condições e para quais objetivos ele é melhor.

Portanto, interpretar resultados exige mais do que apresentar números. É necessário relacionar os dados com a hipótese, avaliar a confiabilidade das medições, considerar limitações e explicar o significado prático dos resultados.

---

## Aplicações em computação

O Planejamento e Execução de Experimentos tem várias aplicações em computação, porque muitas pesquisas da área envolvem comparar técnicas, medir desempenho, avaliar ferramentas ou verificar se uma proposta realmente melhora algum aspecto de um sistema.

Uma das aplicações mais comuns está na **análise de algoritmos**. Experimentos podem ser usados para comparar tempo de execução, uso de memória, escalabilidade e comportamento em diferentes tamanhos de entrada. Embora a análise teórica seja importante, ela nem sempre mostra todos os efeitos práticos. Dois algoritmos com mesma complexidade assintótica podem ter desempenhos diferentes na prática por causa de cache, linguagem de programação, implementação, paralelismo ou características dos dados. O DoE ajuda a organizar esses testes e evitar conclusões baseadas em poucos casos isolados.

Outra aplicação importante está em **sistemas computacionais**. Em áreas como sistemas operacionais, redes, bancos de dados e sistemas distribuídos, é comum avaliar métricas como latência, throughput, consumo de CPU, uso de memória, consumo de energia e tolerância a falhas. Por exemplo, ao comparar duas configurações de banco de dados, o pesquisador pode variar fatores como tamanho da base, número de usuários simultâneos, tipo de consulta e configuração de cache. O planejamento experimental permite identificar quais fatores mais influenciam o desempenho e quais combinações produzem melhores resultados.

Na **engenharia de software**, o DoE pode ser usado para avaliar métodos, ferramentas e práticas de desenvolvimento. Por exemplo, é possível comparar uma ferramenta de detecção de code smells com uma abordagem manual, avaliar se testes automatizados reduzem defeitos, ou verificar se uma técnica de refatoração melhora a manutenibilidade do código. Quando há participação de desenvolvedores ou estudantes, o planejamento precisa considerar fatores humanos, como experiência, familiaridade com a linguagem e tempo disponível.

Em **aprendizado de máquina**, o DoE é especialmente útil porque modelos dependem de muitos fatores: algoritmo escolhido, hiperparâmetros, tamanho da base, técnica de pré-processamento, divisão entre treino e teste, métrica de avaliação e características dos dados. Um experimento mal planejado pode levar a conclusões erradas, como achar que um modelo é melhor apenas porque foi testado em uma divisão de dados mais favorável. O DoE permite comparar modelos de forma mais justa, usando métricas adequadas, repetições, validação cruzada e controle das condições de teste.

Na área de **segurança da informação e criptografia**, experimentos podem avaliar desempenho, robustez e viabilidade prática de técnicas de proteção. Por exemplo, ao implementar um algoritmo criptográfico pós-quântico em uma arquitetura específica, é possível medir ciclos de clock, uso de memória, área em hardware, consumo de energia e tempo de execução. Nesse caso, o DoE ajuda a comparar diferentes implementações ou configurações de compilação, permitindo entender quais fatores afetam o desempenho e a segurança.

Em **interação humano-computador**, experimentos são usados para avaliar interfaces, usabilidade e experiência do usuário. Por exemplo, pode-se comparar duas versões de uma interface medindo tempo para concluir tarefas, quantidade de erros, taxa de sucesso e satisfação dos usuários. Nessa área, o planejamento experimental é importante para evitar vieses, como diferença de experiência entre participantes ou ordem de apresentação das interfaces.

Também há aplicações em **otimização de software e configuração de sistemas**. Muitos sistemas possuem parâmetros ajustáveis, como tamanho de buffer, número de threads, política de cache, nível de compressão ou parâmetros de compilação. Testar todas as possibilidades manualmente pode ser inviável. O DoE permite selecionar combinações relevantes e identificar quais fatores têm maior impacto no resultado.

Além disso, o DoE se relaciona com outros métodos de pesquisa usados em computação. Ele pode complementar uma **revisão bibliográfica**, quando a literatura indica técnicas que precisam ser comparadas experimentalmente. Pode complementar um **estudo de caso**, quando um sistema real é avaliado em uma organização ou contexto específico. Também se relaciona com **Design Science**, pois muitas pesquisas em computação constroem artefatos, como algoritmos, ferramentas, modelos ou arquiteturas, e depois precisam avaliá-los de forma rigorosa.

De modo geral, o DoE é aplicável sempre que a pesquisa em computação envolve uma pergunta do tipo: “qual técnica funciona melhor?”, “quais fatores influenciam o desempenho?”, “a nova proposta melhora a solução existente?” ou “em quais condições esse método é mais adequado?”. Sua principal contribuição é permitir que essas perguntas sejam respondidas de maneira sistemática, reduzindo improviso, vieses e conclusões frágeis.

Por isso, em computação, o Planejamento e Execução de Experimentos não serve apenas para medir resultados. Ele apoia decisões científicas e técnicas, ajudando o pesquisador a escolher métodos, comparar alternativas, justificar conclusões e indicar limitações de forma transparente.

