<h1 align="center">Estruturas de Repetição</h1>

- São estruturas usadas para **repetir** um **bloco de código** determinado. 
- Esse número de **repetições/Loops** pode ser pré determinado ou pode ser atrelado a uma determinada resposta recebida na execução do **Loop**.


<h2>Estrutura de Repetição for</h2>

  - É utilizado quando precisamos **percorrer** uma estrutura como listas, objetos ou outros tipos de dados.
  - É recomendado o uso do for quando **sabemos a quantidade exatas de vezes** que um bloco de código precisa ser executado ou quando **precisamos percorrer uma lista inteira**, por exemplo.

  Código para copiar:
  <blockquote>

    # Estruturar de repetição for
    texto = input("Informe um texto: ")
    VOGAIS = "AEIOU"

    # Para cada letra em texto, execute o abaixo.
    for letra in texto:
        if letra.upper() in VOGAIS:
            print(f"No texto: {texto}, temos a vogal: {letra}. \n")


    # Podemos usar o  else no final do laço se necessario
    for letra in texto:
        if letra.upper() in VOGAIS:
            print(f"No texto: {texto}, temos a vogal: {letra}. \n")
    else:
        print("Nenhum texto ou palavra digitado!")


    # Exemplo de for com números
    contador = [1, 2, 3, 4, 5]

    for numero in contador:
        print(f"Número: {numero}")
  
  </blockquote>
  <img src="img/1 - Estrutura de Repetição for.png">

<h2>Estrutura de Repetição for in range</h2>

  - O **range** é uma **função do python** criada para **produzir** uma sequencia de números com inicio e fim determinados.
  - Por padrão ele começará com número 0 caso não tenha um inicio especificado.
  - O range **possui 3 argumentos**, **stop** que é obrigatório, **start** e **step** que são opcionais.
  - O **stop** é o número que fara a execução parar, nesse caso se queremos que seja executado uma contagem de números até 10 o nosso stop seria o número 11, assim o código seria executado 10 vezes e pararia na 11ª execução.
  - O **start** é o número que ira iniciar a execução, você pode escolher um número ou deixar o zero, ele irá começar a execução do código por esse número.
  - O **step** seria meio que um  intervalo, ele seria por exemplo para a execução de uma tabuada ou para pular uma quantidade de números na execução, **por exemplo um código que conte de 0 a 20 pulando de 2 em 2 números**.

  - Irei deixar um exemplo simples de contagem com range e um exemplo de uma tabuada com range.
  - Na tabuada o start começa com o número 0, o stop seria o número 51 e o step número 5.
  - Então o código iria executar a contagem a partir do 0 e pular de 5 em 5 casas, mostrando esses resultados igual a tabuada do 5.

  Código para copiar:
  <blockquote>

    for numero in range(0, 11):
        print(numero, end=" ")

    # exibir uma tabuada usando as os argumentos start, stop e step
    contador = 0
    for numero in range(0, 51, 5):
        print(f"5 x {contador} = {numero}")
        contador += 1

  </blockquote>
  <img src="img/2 - Estrutura de Repetição for in range.png">


<h2>Estrutura de Repetição while</h2>

  - O while é utilizado para executar um código quando não o número exatos de repetição que aquele bloco de código precisa ser executado.
  - Com o while podemos executar um bloco de código varias vezes até uma determinada opção ou padrãoo seja atendiido.
  - Para parar a execução podemos usar a função break, com ela se a resposta ou condição for atendida o código irá parar.

  Exemplo de um while simples sem uso da função break. <br>
  Código  para copiar:
  <blockquote>

    opcao = int(input("Escolha uma das opções: \n [1]Sacar \n [2]Consultar extrato \n [0] Sair \n Qual serviço deseja acessar? "))

    while opcao != 0:
      opcao = int(input("Escolha uma das opções: \n [1]Sacar \n [2]Consultar extrato \n [0] Sair \n Qual serviço deseja acessar? "))

      if opcao == 1:
          print("Saque feito com sucesso!")
      elif opcao == 2:
          print("Seu extrato esta sendo carregado!")
  
  </blockquote>
  <img src="img/3 - Estrutura de Repetição while.png">

  Exemplo de while com uso do break. <br>
  Código para copiar:
  <blockquote>
  
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
  
  </blockquote>
  <img src="img/4 - Estrutura de Repetição while com break.png">


