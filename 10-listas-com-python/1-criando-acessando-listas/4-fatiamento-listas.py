# Fatiamento de Listas
lista = ["j", "a", "v", "a", "s", "c", "r", "i", "p", "t"]

# Retorna do item 2 até o fim da lista.
print(lista[2:])
# Retorno: ['v', 'a', 's', 'c', 'r', 'i', 'p', 't']

# Retorna do item 0 até  o item 5, ignora o item 6
print(lista[:6])
# Retorno: ['j', 'a', 'v', 'a', 's', 'c']

# Retorna do item 4 ao item 6, ignora item 7
print(lista[4: 7])
# Retorno: ['s', 'c', 'r']

# Retorna do item 0 ao item 7 pulando de 3 em 3 ignora oo item 8
print(lista[0:8:3])
# Retorno: ['j', 'a', 'r']

# Retorna todos os itens de uma lista
print(lista[::])
# Retorno: ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

# Retorna a lista de tras para frente
print(lista[::-1])
# Retorno: ['t', 'p', 'i', 'r', 'c', 's', 'a', 'v', 'a', 'j']

print(f"""
# Retorna do item 2 até o fim da lista.
{lista[2:]}

# Retorna do item 0 até  o item 5, ignora o item 6
{lista[:6]}

# Retorna do item 4 ao item 6, ignora item 7
{lista[4: 7]}

# Retorna do item 0 ao item 7 pulando de 3 em 3 ignora oo item 8
{lista[0:8:3]}

# Retorna todos os itens de uma lista
{lista[::]}

# Retorna a lista de tras para frente
{lista[::-1]}
""")

