# Fatiamento de Tuplas
tupla = ("p", "y", "t", "h", "o", "n",)


print(tupla[2:])
print(tupla[:3])
print(tupla[1:5])
print(tupla[0:5:2])
print(tupla[::])
print(tupla[::-1])

print(f"""
Retorna do item 2 em diante:
  {tupla[2:]}

Retorna do item 0 ao 2, ignorando o item 3:
  {tupla[:3]}

Retorna do item 1 ao item 4, ignorando o item 5:
  {tupla[1:5]}

Retorna do item 0 ao item 4, pulando de 2 em 2:
  {tupla[0:5:2]}

Retorna todos os itens:
  {tupla[::]}

Retorna todos itens de tras para frente:
  {tupla[::-1]}
""")

