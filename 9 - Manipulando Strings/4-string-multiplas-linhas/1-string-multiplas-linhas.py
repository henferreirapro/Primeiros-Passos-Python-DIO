# String com Multiplas Linhas
nome = "Henrique"

opcoes = ["Extrato", "Saque", "Sair"]

# Exemplo com uma mensagem.
mensagem = f"""Meu nome é {nome},
  tenha 28 anos.
      Essa mensagem tem espaçamento diferente."""


# Exemplo de um menu.
menu = f"""
Escolha uma Opção:
  [1] {opcoes[0]}
  [2] {opcoes[1]}
  [3] {opcoes[2]}
"""

print(mensagem)
print(menu)

