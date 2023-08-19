<h1 align="center">String com Multiplas Linhas.</h1>

  - Strings de multiplas linhas são definidas usando 3 aspas simples ou duplas na hora de criar a atribuição.
  - Elas podem usar varias linhas do código e todos os espaços em branco e quebras de linha são incluidos na string final.

  <h4>Código:</h4>
  <img src="img/1 - String com multiplas linhas.png">

  <h4>Retorno:</h4>
  <img src="img/1.1 - Retorno String com multiplas linhas.png">

  <h4>Código para copiar:</h4>
  <blockquote>

    nome = "Henrique"

    opcoes = ["Extrato", "Saque", "Sair"]

    # Exemplo com uma mensagem.
    mensagem = f"""Meu nome é {nome},
      tenha 28 anos.
          Essa mensagem tem espaçamento diferente."""


    # Exemplo de um menu.
    menu = f"""
    Escolha uma Opção:
      [1] {opcoes[0]}
      [2] {opcoes[1]}
      [3] {opcoes[2]}
    """

    print(mensagem)
    print(menu)
  
  </blockquote>