<h1 align="center">Operadores Lógicos</h1>

Quando um operador de comparação é utilizado, ele retorna o resultado booleano, com isso podemos combinar operadores de comparação com operadores lógicos para ter um resultado melhor, por exemplo:

<h2>Operador E (and)</h2>
  
  - Para essa expressão ser True, os dois operadores precisão ser verdadeiros, caso um seja falso e o outro verdadeiro o resultado será False. 

  Código para copiar:
  <code>

    saldo = 500
    saque = 300
    limite = 150

    print(saldo >= saque and saque <= limite)

  </code>
  <img src="1 - Operador E (and).png">


<h2>Operador Ou (or)</h2>

   - Para a expressão ser True, um dos operadores precisa ser verdadeiro, caso nenhuma seja verdadeira, a expressão sera False.

  Código para copiar:
  <code>
  
    saldo = 500
    saque = 300
    limite = 150

    print(saldo >= saque or saque <= limite)
  
  </code>
  <img src="2 - Operador Ou (or).png">


<h2>Operador de Negação (not)</h2>
  - Operador de negação pega o resultado do operador e responde com o contrario desse resultado. <br>
  - Por exemplo, se o resultado for True o operador de negação dará a resposta False.

  Código para copiar:
  <code>

    print(not 1000 > 1500)
    # Resultado: False, Resposta: True

    print(not 500 < 1000)
    # Resultado: True, Resposta: False

    lista = [] #Lista vazia é considerado False
    print(not lista)
    # Resultado: False, Resposta: True

    print(not "texto") #String com texto considerado True 
    #Resultado: True, Resposta: False

  </code> 
  <img src="3 - Operador de Negação (not).png">


<h2>Forma de declarar:</h2>

 - Usamos o Parenteses para delimitar a ordem que será executado os operadores, assim fica uma forma melhor de ler e entender o código escrito.

  Código para copiar
  <code>

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
  
  </code>
  <img src="4 - Forma de declarar.png">