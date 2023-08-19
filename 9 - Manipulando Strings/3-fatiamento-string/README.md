<h1 align="center">Fatiamento de Strings</h1>

  - É uma tecnica utilizada para retornar substrings, partes da string original.
  - Para fazer isso informamos o inicio(start), fim(stop) e o passo(step) dentro de conchetes.
  
  Código: <br>
  <img src="img/1 - Fatiamento de strings.png">

  Retorno: <br>
  <img src="img/1.1 - Retorno de Fatiamento de strings.png">

  Código para copiar:
  <blockquote>
  
    nome = "Henrique Ferreira"

    # Retorna o caracter 0 apenas.
    print(nome[0])
    # Retorna: "H"

    # Retorna do caracter 0 até o 7.
    print(nome[:8])
    # Retorna: "Henrique"

    # Retorna do caracter 9 em diante.
    print(nome[9:])
    # Retorna: "Ferreira"

    # Retorna do caracter 5 ao 13.
    print(nome[5:14])
    # Retorna: "que Ferre"

    # Retornado caracter 9 ao 15 pulando de 2 em 2 casas.
    print(nome[9:16:2])
    # Retorna: "Frer"

    # Retorna a string inteira
    print(nome[:])
    # Retorna: "Henrique Ferreira"

    # Espelha a string(Mostra de tras para frente)
    print(nome[::-1])
    # Retorna: "arierreF euqirneH"
  
  </blockquote>

___

