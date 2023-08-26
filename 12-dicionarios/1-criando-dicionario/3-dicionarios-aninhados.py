# Criando um dicionario aninhado
pessoas = {
    "henrique@gmail.com": {"nome": "Henrique", "telefone": "99999-9999"},
    "ferreira@gmail.com": {"nome": "ferreira", "telefone": "99999-1234"},
    "silva@gmail.com": {"nome": "silva", "telefone": "99999-6789"},
}

# Como acessar os dados
print(pessoas["ferreira@gmail.com"]["telefone"])

print(f"""
O contato da pessoa ferreira@gmail.com é: 
  Contato: {pessoas['ferreira@gmail.com']["telefone"]}.
""")

