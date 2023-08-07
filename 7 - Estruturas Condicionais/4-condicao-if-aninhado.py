# Condicional if aninhado
saldo = 1000
cheque_especial = 1500

# Usuario escolhe o tipo da conta
tipo_conta = int(input("Qual seu tipo de conta: \n [1]Conta Corrente \n [2]Conta Universitaria \nDigite o número da Conta: \n"))

if tipo_conta == 1:
    saque = float(input(f"Seu saldo é de R${saldo:.2f}. \n Quanto deseja sacar? \n"))
    
    # Caso valor seja menor ou igual ao saldo disponivel.
    if saldo >= saque:
        print(f"O valor de R${saque:.2f} foi sacado com sucesso!")
    
    # Se o saque menor que a soma do saldo + cheque especial.
    elif saque <= (saldo + cheque_especial):
        print(f"O valor de R${saque:.2f} foi sacado com sucesso com o uso o cheque especial.")

    # Caso nenhuma das duas a cima seja atendida.
    else:
        print(f"Saldo insuficiente, o valor disponivel na sua conta é de: \n Saldo na conta: R${saldo:.2f} \n Cheque especial: R${cheque_especial:.2f}.")
elif tipo_conta == 2:
    saque = float(input(f"Seu saldo é de R${saldo:.2f}. \n Quanto deseja sacar? \n"))

    # Se o saldo for maior ou igual ao saque.
    if saldo >= saque:
        print(f"O valor de R${saque:.2f} foi feito com sucesso!")
    
    # Caso a condição a cim a não seja atendida.
    else:
        print(f"Saldo indisponivel, seu saldo para saques atual é de: \n Saldo na conta: R${saldo:.2f}.")
else:
    print("Sistema não reconheceu seu tipo de conta, por favor escolha uma das opções a baixo:")

    # Gera uma nova opção para finalizar a sessão.
    tipo_conta = int(input("Qual seu tipo de conta: \n [1]Conta Corrente \n [2]Conta Universitaria \n [0] Se deseja sair \nDigite o número da Conta: \n"))
    if tipo_conta == 0:
        print("Sessão finalizada com sucesso!")


