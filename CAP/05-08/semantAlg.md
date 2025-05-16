## Revisão semantica comando de repetição

##### For
```txt
for i <- *valorInicial* to *valorFinal* step(incremento/decremento)
    ...
end for
- Usar quando ja sabe o n de repetições, (valorFinal - valorInicial + 1)

Exemplo de uso:

for i <- 0 to nAlunos-1
    read notas[i]
end for
```

##### While
```txt
while condição do

    0 ou +vezes(opcional)

end while
- Não necessariamente tem uma nota

Exemplo de uso:

while not achou(true) do
    enquanto nao achou eu faço

end while

```


##### Repeat
```txt
repeat 

    1 ou +vezes

until condição
-Necesariamente tem uma nota

Exemplo de uso:

repeat
    repita ate achar

until achou

```
