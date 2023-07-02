# BOAS PRATICAS PARA DECLARAR CONSTANTES
"""
  Também usamos o padrão Snake Case.
  Constantes não existe uma palavra para ser declarada em Python,
  então para deixarmos claro que uma variavel é uma constante
  nós declaramos ela com todas as letras em maiusculo.

  Exemplo de constante: 
  * LIMITES_SAQUE_DIARIO
  * ESTADO
"""

ESTADOS = [
    "SP",
    "RJ"
]

LIMITE_SAQUE_DIARIO = 1000

nome_perfil = "Henrique"

print(f"Meu nome é {nome_perfil} e meu saque diario é de R$ {LIMITE_SAQUE_DIARIO}.")