# Acessando um item de uma lista
linguagens = ["Python", "JavaScript", "Ruby"]

print("\n")
print(linguagens[1])
# Retorno: "JavaScript"

# Indice Negativo acessam os itens do ultimo para o primeiro 
print(linguagens[-3])
# Retorno: "Python"


print(f"""
item 1 da lista
{linguagens[1]}

item -3 da lista
{linguagens[-3]}
""")