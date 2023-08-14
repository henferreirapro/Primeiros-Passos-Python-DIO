# Estrutura de Repetição while com break

while True:
    opcoes = int(input("Escolha uma das opções: \n [1]Sacar \n [2]Consultar extrato \n [0] Sair \n Qual serviço deseja acessar? "))

    if opcoes == 1:
        valor = float(input("Qual valor desejado? "))
        print(f"O valor de R${valor:.2f} foi sacado com sucesso! \n")
    elif opcoes == 2:
        print("Carregando seu extrato... \n")
    elif opcoes == 0:
        print("Obrigado por usar nossos serviços! \n")
        break
    

