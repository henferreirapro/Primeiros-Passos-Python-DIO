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