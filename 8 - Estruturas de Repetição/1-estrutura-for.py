# Estruturar de repetição for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Para cada letra em texto, execute o abaixo.
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"No texto: {texto}, temos a vogal: {letra}. \n")


# Podemos usar o  else no final do laço se necessario
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"No texto: {texto}, temos a vogal: {letra}. \n")
else:
    print("Nenhum texto ou palavra digitado!")


# Exemplo de for com números
contador = [1, 2, 3, 4, 5]

for numero in contador:
    print(f"Número: {numero}")


