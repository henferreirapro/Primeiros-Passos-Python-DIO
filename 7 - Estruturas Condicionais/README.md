<h1 align="center">Estruturas Condicionais</h1>

São condições que podemos criar para cada ação necessaria de algum item, assim quando um item atendem ou se enquadrar em um padrão já determinado ele executará um bloco de código para aquela ação.

<h2>Condicional if</h2>

  - Por padrão para criar uma estrutura condicional basica usamos a palavra reservadas **if**, ela se enquandra quando precisamos atender apenas uma condição.
  - Quando a condição do **if** é **verdadeira**, ele executará um **bloco de código**, caso não seja ele não será executado e o código continuará sem nenhuma ação feita.
 
  Código para copiar:
  <blockquote>
  
    # Condição if
    nome = "Henrique"
    idade = 28

    # esse bloco será executado sempre
    print(f"Olá {nome}.")

    # Esse bloco só será executado se idade for maior que 18
    if idade > 18:
        print("Você é maior de idade!")
  
  </blockquote>
  <img src="img/1 - Condição if.png">

<h2>Condicional else</h2>

  - Quando usamos apenas o **if**, nós só teremos uma ação caso a condição seja atendida, caso contrario não teremos nenhuma resposta.
  - Para isso foi feito a condição **else**, caso a condição **if** não seja atendida, nós temos a condição **else** para termos uma resposta.
  - A condição **else** é executada caso as condicionais **if** ou **elif** não sejam atendidas.

  Código para copiar:
  <blockquote>
  
    saldo = 1000.0
    saque = float(input("Informe o valor a ser secado: "))

    if saldo >= saque:
        # Será executado se o saque for menor que saldo.'
        print("Saque Realizado!")
    else:
        # Será executado se o if não for atendido.
        print("Você não possui saldo suficiente!")
  
  </blockquote>
  <img src="img/2 - Condição if e else.png">


<h2>Condicional elif</h2>
  
  - A condicional elif serve para quando precisamos verificar mais de duas condições, assim usamos o if, elif e else, nessas ordens.
  - O uso do elif não se limita a uma unica vez, podemos usa-lo mais de uma vez após o uso do if.

  Código para copiar:
  <blockquote>
  
    opcao = int(input("Qual Opção Deseja Acessar: \n [1] Sacar \n [2] Extrato \nDigite uma Opção: "))

    if opcao == 1:
        saque = float(input("Qual o Valor do Saque? "))
        print("Saque Realizado!")
    elif opcao == 2:
        print("Extrato sendo carregado...")
    else:
        print("Opção invalida! \nSessão Finalizada!")
  
  </blockquote>
  <img src="img/3 - Condição elif.png">


<h2>condicional if aninhado</h2>

  - A condicional if aninhado serve para quando precisamos criar blocos **if, elif e else** e cada um desses blocos possui condições **if, elif e else** para serem verificadas, resumo seria criar uma estrutura de blocos dentro de outra estrutura condicional.
  - Um bom exemplo seria um **banco** que possui dois tipos de contas bancarias, uma **conta corrente** e uma **conta universitaria**, a conta corrente tem acesso ao **saldo** e ao **cheque especial**, já a conta universitaria possui acesso apenas ao **saldo** disponivel na conta.

  Código para copiar:
  <blockquote>

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

  </blockquote>
  <img src="img/4 - Condição if aninhado.png">


<h2>Condicional if ternário</h2>

  - Essa condicional permite escrever uma condição em uma unica linha.
  - Ele é composto por 3 partes:
    - A primeira parté é retorno da condição **if** se a expressão for **True**.
    - A segunda parte é a execução da expressão.
    - A terceira parte é o retorno do **else** caso o **if** não seja executado.

  Código para copiar:
  <blockquote>
  
    # Condicional if ternário
    saldo = 500
    saque = float(input("Quanto deseja sacar? \n"))

    status = "Saque realizado com Sucesso!" if saldo >= saque else "Saldo insuficiente!"

    print(f"Resultado da sua transação foi: \n {status}")
  
  </blockquote>
  <img src="img/5 - Condição if ternario.png">


