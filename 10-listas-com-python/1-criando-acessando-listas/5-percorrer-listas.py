# Percorrendo Listas
linguagens = ["Kotlin", "JS", "Python"]

print("\nRetorno do for:")
for linguagem in linguagens:
    print(linguagem)

print("".center(30,"_"))

# Usando for com enumerate
print("\nRetorno do for com enumerate:")
for indice, linguagem in enumerate(linguagens):
    print(f"Item {indice}: {linguagem}")

