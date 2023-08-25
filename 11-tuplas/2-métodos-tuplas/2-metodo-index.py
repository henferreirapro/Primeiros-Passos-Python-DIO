# Método .index()
linguagens = ("python", "js", "ruby",)

print(linguagens.index("ruby"))

print(linguagens.index("python"))

for indice, linguagem in enumerate(linguagens):
    print(f"A linguagem {linguagem} esta no indice {indice}.\n")


