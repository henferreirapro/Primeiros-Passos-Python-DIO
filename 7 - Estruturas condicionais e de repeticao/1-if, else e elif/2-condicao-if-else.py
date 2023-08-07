# Condicional if e else
saldo = 1000.0
saque = float(input("Informe o valor a ser secado: "))

if saldo >= saque:
    # Será executado se o saque for menor que saldo.'
    print("Saque Realizado!")
else:
    # Será executado se o if não for atendido.
    print("Você não possui saldo suficiente!")


