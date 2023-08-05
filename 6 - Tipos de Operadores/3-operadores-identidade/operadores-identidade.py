# Operador is
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)
# Resultado: True

print(saldo is limite)
# Resultado: True

print(curso is limite)
# Resultado: False


# Operador is not
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is not nome_curso)
# Resultado: False

print(saldo is not nome_curso)
# Resultado: True

print(saldo is not limite)
# Resultado: False

