# Tuplas Aninhadas
pessoas = (
    ("Henrique", 28, "SP"),
    ("Gru", 20, "BSB",),
    ("Malaquias", "30", "RJ"),
)

# Formas de acessar
print(pessoas[0])

print(pessoas[2][1])

print(pessoas[-2])

print(f"""
Pessoa na posição 0:
  {pessoas[0]}

Item 1 da pessoa na posição 2:
{pessoas[2][1]}

Pessoa na posição -2:
  {pessoas[-2]}
""")

