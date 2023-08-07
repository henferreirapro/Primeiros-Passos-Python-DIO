# Condicional if, elif e else
opcao = int(input("Qual Opção Deseja Acessar: \n [1] Sacar \n [2] Extrato \nDigite uma Opção: "))

if opcao == 1:
    saque = float(input("Qual o Valor do Saque? "))
    print("Saque Realizado!")
elif opcao == 2:
    print("Extrato sendo carregado...")
else:
    print("Opção invalida! \nSessão Finalizada!")


