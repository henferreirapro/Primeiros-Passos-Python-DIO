"""
  Podemos ler os valores com a função input e mostrar
  com a função print.

  Na função print podemos passar os parametros e também
  utilizar mais dois parametros, são eles o end=" " e o
  sep=" "

  Com o end podemos add alguma função ou texto ao final
  do que será exibido pelo print.

  Já o sep podemos adicionar algo entre os espaços dos
  parametros normais chamados.
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

# forma padrão
print(nome, idade)

# utilizando end
print(nome, idade, end=" anos \n")

#utilizando sep
print(nome, idade,  sep=", minha idade é ")

# Utilizando end e sep
print(nome, idade, sep=", eu tenho ", end=" anos de idade. \n")

print(f"Meu nome é {nome}", idade, sep=", eu tenho ", end=" anos de idade.")