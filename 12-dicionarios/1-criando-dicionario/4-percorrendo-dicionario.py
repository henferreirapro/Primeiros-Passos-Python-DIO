# Percorrendo um dicionario com for
pessoas = {
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "99999-9999"},
    "ferreira@gmail.com": {"nome": "ferreira", "telefone": "99999-1234"},
    "silva@gmail.com": {"nome": "silva", "telefone": "99999-6789"},
}

print("\nUtilizando for:")
for usuario in pessoas:
    print(f"Os dados do usuario {usuario} é {pessoas[usuario]}")

# usando o for com items
print("\nUtilizando for com items:")
for usuario, dados in pessoas.items():
    print(f"Os dados do usuario {usuario} é {dados}")
    
