# Criando função sem parametros definidos
def mensagem():
    print("Olá Mundo!")


# Criando função com parametro obrigatório.
nome = "Henrique" #passando parametro

def mensagem_parametro(nome):
    print(f"Olá {nome}, espero que esteja bem!")


# Criando Função com parametro opcional
def mensagem_opcional(nome="Anônimo"):
    print(f"Seja bem vindo(a) {nome}.")

print("\nRetorno da Função mensagem:")
# Função sem parametro definido
mensagem()

print("\nRetorno da Função mensagem_parametro:")
# Função com parametro definido
mensagem_parametro(nome)
mensagem_parametro("Ferreira")

print("\nRetorno da Função mensagem_opcional:")
# Função Sem passar um parametro
mensagem_opcional() #ira exibir o parametro pré definido na função
mensagem_opcional(nome="João")

