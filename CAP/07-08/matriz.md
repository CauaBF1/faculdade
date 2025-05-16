# Vetor
Variavel composta: armazena varios valores
Homogenea: mesmo tipo de dados
arranjo unidimensional
---
# Matriz
Composta
Homogenea
arranjo Bidimensional
---



### Varredura completa de uma matriz inserindo em cada elemento e somando as colunas das linhas impares
```txt

|> Ler os elementos da matriz e realizar a soma dos impares
for i <- 0 to nLinhas-1 do
    soma[i] <- 0
    for j <- 0 to nColunas-1 do
        scanf elemento[i][j]
        if i % 2 <> 0 then
            soma[i] <- soma[i] + elemento[i][j]
        end if
    end for
end for

|> Escrever resultado
for i<- 0 to nLinhas-1 do 
    if i % 2 <> 0 then
        write soma[i]
    end if
end for
```
pode ser feito sem o if com j <- 1 com step2




### Agora calculando media por linha e media completa
```txt
|> Ler os elementos da matriz e realizar a soma de todos
somaElementos <- 0
read nLinhas, nColunas
for i<-0 to nLinhas-1 do
    for j <- 0 to nColunas-1 do
         scanf elemento[i][j]
         somaElementos <- somaElementos + elemento[i][j]
    end for
end for

mediaTotal <- somaElementos / (nLinhas * nColunas)


|> realizar a media de cada linha
for i <- 0 to nLinhas-1 do
    soma[i] <- 0 
    for j <- 0 to nColunas-1 do 
            soma[i] <- soma[i] + elemento[i][j] 
    end for
    
    mediaLinha[i] <- soma[i] / nColunas
end for

|> Escrever resultado das medias das linhas e da media total
for i<- 0 to nLinhas-1 do 
        write mediaLinha[i]
end for

write mediaTotal
```
