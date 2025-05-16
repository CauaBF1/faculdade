## Questão 1
Menor valor entre 7 numeros inteiros:

```txt
// Receber os 7 números
for i <-  0 to 6 do
    read n[i]
end for

// Inicializar o menor valor com o primeiro elemento
vmenor <- n[0]

// Calcular qual o menor dos 7 números
for i <- 0 to 6 do
    if n[i] < vmenor then
        vmenor <- n[i]
end for

// Exibir o menor número
write vmenor

```



## Questão 2
Mostrar nome preço e tipo do vinho mais caro
```txt
// Ler os dados dos vinhos
while true do

    // Ler o nome do vinho
    read nome

    // Verificar se o nome é "FIM" para encerrar a entrada de dados
    if nome <- "FIM" then
        break

    // Ler o preço e o tipo do vinho
    read preco
    read tipo

    // Atualizar o vinho mais caro se o preço atual for maior que o vinho mais caro conhecido
    if preco > vinhoMaisCaroPreco then
        vinhoMaisCaroNome <- nome
        vinhoMaisCaroPreco <- preco
        vinhoMaisCaroTipo <- tipo

    // Exibir os dados do vinho mais caro
    write "Vinho mais caro:"
    write "Nome: ", vinhoMaisCaroNome
    write "Preço: R$", vinhoMaisCaroPreco
    write "Tipo: ", vinhoMaisCaroTipo
end while
```

## Questão 3
10 Equações de 2 grau

```txt
for i <-  0 to 9
    read a, b, c
    
    // Verificar se é uma equação do segundo grau
    if a != 0 then
        // Calcular o discriminante
        discriminante <- b**2 - 4*a*c
        
    // Verificar a natureza das raízes com base no discriminante
        if discriminante < 0 then
            write "Não possui raízes reais"
        
        else if discriminante == 0 then
            write "Possui raízes reais idênticas"
            res <- -b / (2*a)
            write "Raiz: ", res
        
        else if discriminante > 0 then
            write "Possui raízes reais distintas"
            raiz1 <- (-b + discriminante**(1/2)) / (2*a)
            raiz2 <- (-b - discriminante**(1/2)) / (2*a)
            write "Raiz 1: ", raiz1
            write "Raiz 2: ", raiz2
    
    else
        write "Equação não válida (a = 0)"
end for
```




