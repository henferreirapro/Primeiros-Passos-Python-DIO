# Estrutura de Repetição while simples
opcao = int(input("Escolha uma das opções: \n [1]Sacar \n [2]Consultar extrato \n [0] Sair \n Qual serviço deseja acessar? "))

while opcao != 0:
    opcao = int(input("Escolha uma das opções: \n [1]Sacar \n [2]Consultar extrato \n [0] Sair \n Qual serviço deseja acessar? "))

    if opcao == 1:
        print("Saque feito com sucesso!")
    elif opcao == 2:
        print("Seu extrato esta sendo carregado!")


