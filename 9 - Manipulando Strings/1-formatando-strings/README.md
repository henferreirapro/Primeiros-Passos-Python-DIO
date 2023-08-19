<h1 align="center">Manipulando Strings</h1>

<h2>Metodos de Formatação de Strings.</h2>
  
  - Metodo **upper( )** <br> 
  Deixa todas as letras em Maiúsculo.
  
  Codigo para copiar:
  <blockquote>
    
    curso = "jAVascrIpt"
    cursos = ["pYthOn", "jAVascrIpt", "ANgulAr"]

    # exemplo simples
    print(curso.upper())
    # Resposta: "JAVASCRIPT"

    # exemplo com lista
    for curso in cursos:
        print(curso.upper())
        # Resposta: "PYTHON" "JAVASCRIPT" "ANGULAR"
  </blockquote>
  <img src="img/1 - metodo upper( ).png">

  ___ 
  <br>

  - Metodo **lower( )** <br> 
  Deixa todas as letras em Minúsculo.

  Código para copiar:
  <blockquote>
  
    curso = "ANgulAr"
    cursos = ["pYthOn", "jAVascrIpt", "ANgulAr"]

    # exemplo simples
    print(curso.lower())
    # Resposta: "angular"

    # exemplo com lista
    for curso in cursos:
        print(curso.lower())
        # Resposta: "python" "javascript" "angular"
  </blockquote>
  <img src="img/2 - metodo lower( ).png">

  ___
  <br>

  - Metodo **title( )** <br> 
  Deixa a primera letra de todas as palavras em maiusculo como um titulo.

  Código para copiar:
  <blockquote>
  
    curso = "pYthOn"
    cursos = ["pYthOn", "jAVascrIpt", "ANgulAr"]

    # exemplo simples
    print(curso.title())
    # Resposta: "Python"

    # exemplo com lista
    for curso in cursos:
        print(curso.title())
        # Resposta: "Python" "Javascript" "Angular"
    
  </blockquote>
  <img src="img/3 - metodo title( ).png">


<h2>Metodos Para Eliminar Espaços em Branco.</h2>

  - Metodo **strip( )** <br>
  Retira os espaços a **esquerda** e a **direita** da String.

  Código para copiar:
  <blockquote>
  
    curso = "   Python  "

    print(curso.strip())
    # Resposta: "Python"

    # Metodo strip() ira retirar os espaçamentos dos dois lados da string
  
  </blockquote>
  <img src="img/4 - metodo strip( ).png">

  ___
  <br>

  - Metodo **lstrip( )** <br>
  Retira espaçamento apenas do lado esquerdo da string.

  Código para copiar:
  <blockquote>
  
    curso = "  Angular   "

    print(curso.lstrip())
    # Resposta: "Angular   "

    # Metodo lstrip() retira o espaçamento apenas do lado esquerdo da string.
  
  </blockquote>
  <img src="img/5 - metodo lstrip( ).png">

  ___
  <br>

  - Metodo **rstrip( )** <br> 
  Retira o espaçamento apenas do lado direito da string.

  Código para copiar:
  <blockquote>
  
    curso = "      JavaScript    "

    print(curso.rstrip())
    # Resposta: "      JavaScript"

    # Metodo rstrip() retira o espaçamento apenas do lado direito da string.
  
  </blockquote>
  <img src="img/6 - metodo rstrip( ).png">


<h2>Junções e Centralização de String</h2>

  - Metodo **center( )** <br>
  Metodo center é ma forma de junção para centralizar uma string. <br>
  Podemos determinar a quantidade de caracteres que serão usados para fazer a centraização, nesse caso foram 20, contando os caracteres das strings.

  Código para copiar:
  <blockquote>
  
    menu = "Python", "Java", "SQL"

    print(menu[0].center(20, "#"))
    # Resposta: #######Python#######

    print(menu[1].center(20, "#"))
    # Resposta: ########Java########

    print(menu[2].center(20, "#"))
    # Resposta: ########SQL#########
  
  </blockquote>
  <img src="img/7 - metodo center( ).png">

  ___
  <br>

  - Metodo **.join( )** <br>
  Serve para juntarmos um determinado caracter a nossa string.<br>
  Ele irá adicionar esse caracter entre cada letra da nossa string.

  Código para copiar:
  <blockquote>
  
    nome = "Henrique"
    numeros = "123456"

    print(".".join(nome))
    # Resposta: "H.e.n.r.i.q.u.e"

    print("-".join(numeros))
    # Resposta: "1-2-3-4-5-6"
  
  </blockquote>
  <img src="img/8 - metodo .join( ).png">

