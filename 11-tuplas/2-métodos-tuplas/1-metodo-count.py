# Método .count()
cores = ("vermelho", "azul", "preto", "azul",)

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("preto"))

print(f"""
Quantas vezes aparece a cor vermelho:
  Resposta {cores.count("vermelho")}

Quantas vezes aparece a cor azul:
  Resposta {cores.count("azul")}

Quantas vezes aparece a cor preto:
  Resposta {cores.count("preto")}
""")