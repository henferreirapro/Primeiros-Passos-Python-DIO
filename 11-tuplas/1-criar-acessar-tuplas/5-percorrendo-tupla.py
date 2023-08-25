# Percorrendo Tupla com for
carros = ("Corsinha", "Celta", "Fox",)

print("\nRetorno do for:")
for carro in carros:
    print(carro)

print("\nRetorno do for com enumerate:")
# Usando enumerate com for
for indice, carro in enumerate(carros):
    print(f"Itens {indice}: {carro}.")

