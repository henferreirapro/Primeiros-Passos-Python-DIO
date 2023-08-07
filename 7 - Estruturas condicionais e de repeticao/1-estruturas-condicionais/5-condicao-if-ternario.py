# Condicional if ternário
saldo = 500
saque = float(input("Quanto deseja sacar? \n"))

status = "Saque realizado com Sucesso!" if saldo >= saque else "Saldo insuficiente!"

print(f"Resultado da sua transação foi: \n {status}")

