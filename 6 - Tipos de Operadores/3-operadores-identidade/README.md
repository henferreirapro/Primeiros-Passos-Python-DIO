<h1 align="center">Operadores de Identidade</h1>

São Operadores utiizados para comparar se os dois objetos testados ocupam as mesmas posições na memoria.

<h2>Operador is</h2>

  - Quando eu quero comparar se o objeto **A** ocupa o mesmo lugar que o objeto **B** eu uso o operador **is**.
  - Se o objeto **A** e **B** ocuparem o mesmo espaço de memoria o resultado será **True**, se não será **False**.

  Código para copiar:
  <blockquote>
    
    curso = "Curso de Python"
    nome_curso = curso
    saldo, limite = 200, 200

    print(curso is nome_curso)
    # Resultado: True

    print(saldo is limite)
    # Resultado: True

    print(curso is limite)
    # Resultado: False

  </blockquote>
  <img src="img/1 - Operador is.png">


<h2>Operador is not</h2>

  - Quando eu desejo saber se os objetos **A** e **B** não ocupam a mesma posição eu uso o operador **is not**.
  - Se utilizam a mesma memoria o resultado será **False**, se não utilizarem a mesma memoria o resultado será **True**.

  Código para copiar:
  <blockquote>
  
    curso = "Curso de Python"
    nome_curso = curso
    saldo, limite = 200, 200

    print(curso is not nome_curso)
    # Resultado: False

    print(saldo is not nome_curso)
    # Resultado: True

    print(saldo is not limite)
    # Resultado: False  
  
  </blockquote>
  <img src="img/2 - Operador is not.png">