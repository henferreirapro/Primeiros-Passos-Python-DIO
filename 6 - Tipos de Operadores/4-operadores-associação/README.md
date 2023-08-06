<h1 align="center">Operadores de Associação</h1>

São operdores utilizados para verificar se um objeto esta ou não presente em uma sequencia, lista, etc...

<h2>Operador in</h2>

  - Quando eu quero saber se um determinado caracter como string ou número esta presente em um array eu uso o operador **in** para verificar, caso esteja teremos a resposta **True**, se não a resposta será **False**.

  Código para copiar:
  <blockquote>
  
    cidade = "São Paulo"
    doces = ["brigadeiro", "trufa", "kitkat"]
    saques = [200, 450]

    print("Paulo" in cidade)
    # Resposta: True

    print("bolo" in doces)
    # Resposta: False

    print(78 in saques)
    # Resposta: False
  
  </blockquote>
  <img src="img/1 - Operador in.png">


<h2>Operador not in</h2>

  - Quando precisamos saber se um determinado objeto como string ou numéro não esta presente em uma lista ou sequencia, usamos o operador **not in** para fazer a verificação, se não houver o objeto a resposta será **True**, caso tenha a resposta sera **False**.

  Código para copiar:
  <blockquote>

    curso = "Curso de JavaScript"
    doces = ["brigadeiro", "trufa", "kitkat"]
    saques = [200, 450]

    print("Python" not in curso)
    # Resposta: True

    print("kitkat" not in doces)
    # Resposta: False

    print(201 not in saques)
    # Resposta: True
  
  </blockquote>
  <img src="img/2 - Operador not in.png">


