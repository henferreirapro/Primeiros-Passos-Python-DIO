<h1 aling="center">Estruturas Condicionais</h1>

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

<h2>Condicional if e else</h2>

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