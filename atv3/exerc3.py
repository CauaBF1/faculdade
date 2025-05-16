def not_eat(estudantes, sanduiches):
    while estudantes and sanduiches:
        if estudantes[0] == sanduiches[0]:
            estudantes.pop(0)
            sanduiches.pop(0)
        else:
            # coloca o estudante no final da fila
            estudantes.append(estudantes.pop(0))
            
            # ninguem pegou um sanduiche no loop
            if estudantes.count(sanduiches[0]) == 0:
                break

    return len(estudantes)


estudantes = [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]
sanduiches = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
print(not_eat(estudantes, sanduiches))

# Estudantes
'''
1, 1, 1, 0, 0, 1, 0, 0, 0, 1*
1, 1, 0, 0, 1, 0, 0, 0, 1*, 1*
1, 0, 0, 1, 0, 0, 0, 1*, 1*, 1*
0, 0, 1, 0, 0, 0, 1*, 1*, 1*, 1*
0, 1, 0, 0, 0, 1*, 1*, 1*, 1*
1, 0, 0, 0, 1*,1*, 1*, 1*, 0*
0, 0, 0, 1*,1*, 1*, 1*, 0*
0, 0, 1*,1*, 1*, 1*, 0*
0, 1*,1*, 1*, 1*, 0*,0*
1*,1*, 1*, 1*, 0*,0*,0*
1*,1*, 1*, 0*,0*,0*
1* 0*,0*,0*
0*,0*,0*, 1*
0*,0*, 1*
0*, 1*
1*
'''

# Sanduiches
'''
0, 1, 0, 1, 1, 1, 0, 0, 0, 0*
1, 0, 1, 1, 1, 0, 0, 0, 0*
0, 1, 1, 1, 0, 0, 0, 0*
1, 1, 1, 0, 0, 0, 0*
1, 1, 0, 0, 0, 0*
1, 0, 0, 0, 0*
0, 0, 0, 0*
0, 0, 0*
0, 0*
0*
'''