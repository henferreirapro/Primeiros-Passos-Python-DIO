# Operador E (and)
saldo = 500
saque = 300
limite = 150

print(saldo >= saque and saque <= limite)
# >>> False


# Operador Ou (or)
saldo = 500
saque = 300
limite = 150

print(saldo >= saque or saque <= limite)
# True


# Operador de Negação (not)
print(not 1000 > 1500)
# Resultado: False, Resposta: True

print(not 500 < 1000)
# Resultado: True, Resposta: False

lista = [] #Lista vazia é considerado False
print(not lista)
# Resultado: False, Resposta: True

print(not "texto") #String com texto considerado True 
#Resultado: True, Resposta: False


# Usando Parenteses 
saldo = 1000
saque = 300
limite = 150
conta_especial = True

# Forma Incorreta / Ruins de ler
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
# Resposta True

# Forma correta, melhor para ler
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
# Resposta True
