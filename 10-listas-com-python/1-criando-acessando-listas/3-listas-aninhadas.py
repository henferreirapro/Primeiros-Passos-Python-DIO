# Listas Aninhadas
matriz = [
    [1, "a", 2], #Primeira lista - 0
    ["b", 3, 4], #Segunda lista - 1
    [5, 6, "c"]  #Terceira lista - 2
]

# Dessa forma acessamos todos os itens da primeira lista.
print(matriz[0])
# Retorno: [1, 'a', 2]

# Dessa forma acessamos o item 0 da segunda lista .
print(matriz[1][0])
# Retorno:  5

# Dessa forma acessamos o penultimo item da ultima lista
print(matriz[-1][-2])
# Retorno: 6

print(f"""
Itens da lista 0D
{matriz[0]}

Primeiro item da lista 2
{matriz[1][0]}

Penultimo item da lista 2
{matriz[-1][-2]}

""")