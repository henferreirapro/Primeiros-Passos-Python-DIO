<h1 align="center">Listas com Python</h1>

  - Listas podem armazenar qualquer tipo de objeto de forma sequencial.
  - Existem **3 formas** para criar uma lista em Python, utilizando o construtor **list**, a função **range** ou colocando valores separados por virgulas dentro de colchetes.
  - Lembrando que listas são **objetos mutaveis**, então podemos **alterar** os dados dentro dela.

<!-- Criando listas -->
<h2>Como Criar uma lista</h2>
  
  <h3>Exemplo:</h3>
  <img src="1-criando-acessando-listas/img/1-criando-listas.png">

  <h3>Retorno:</h3>
  <img src="1-criando-acessando-listas/img/1.1-criando-listas.png">

  <h3>Código para copiar:</h3>
  <blockquote>

    # Criando lista com Construtor list
    linguagens = list("Python")

    # Usando o metodo range junto com list
    numeros = list(range(10))
    # Retorno: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Criando com colchetes
    pessoa = ["Henrique", 28, 1995, "SP", True]
  
  </blockquote>
  <br>

<!-- Acessando listas diretamente -->
<h2>Como Acessar Listas Diretamente</h2>

  <h3>Exemplo:</h3>
  <img src="1-criando-acessando-listas/img/2-acessando-listas.png">

  <h3>Retorno:</h3>
  <img src="1-criando-acessando-listas/img/2.2-acessando-listas.png">

  <h3>Código para copiar:</h3>
  <blockquote>
  
    linguagens = ["Python", "JavaScript", "Ruby"]

    print("\n")
    print(linguagens[1])
    # Retorno: "JavaScript"

    # Indice Negativo acessam os itens do ultimo para o primeiro 
    print(linguagens[-3])
    # Retorno: "Python"
  
  </blockquote>
  <br>

<!-- Listas aninhadas -->
<h2>Como Criar e Acessar Listas Aninhadas</h2>
  - Listas aninhadas são listas dentro de listas.

  <h3>Exemplo:</h3>
  <img src="1-criando-acessando-listas/img/3-lista-aninhada.png">

  <h3>Retorno:</h3>
  <img src="1-criando-acessando-listas/img/3.3-lista-aninhada.png">

  <h3>Código para copiar:</h3>
  <blockquote>
  
    matriz = [
        [1, "a", 2], #Primeira lista - 0
        ["b", 3, 4], #Segunda lista - 1
        [5, 6, "c"]  #Terceira lista - 2
    ]

    # Dessa forma acessamos todos os itens da primeira lista.
    print(matriz[0])
    # Retorno: [1, 'a', 2]

    # Dessa forma acessamos o item 0 da segunda lista .
    print(matriz[1][0])
    # Retorno:  5

    # Dessa forma acessamos o penultimo item da ultima lista
    print(matriz[-1][-2])
    # Retorno: 6

  </blockquote>
  <br>

<!-- Fatiamento de Listas -->
<h2>Como Usar Fatiamento em Listas</h2>

  - Fatiamento de Listas serve para quando precisamos retornar alguns pedaços de uma lista.
  - Como no fatiamento de strings, o fatiamento de listas também podemos passar 3 parametros.
  - O item inicial(start), caso não adicionado será considerdo como iitem 0 da lista.
  - O item final(stop), será onde o fatiamento irá parar, ele sempre ignora o ultimo item, então se o número for 8, ele irá até o número 7 e ignorará o 8.
  - E o intervalo(step), que serve como uma opção para pular os itens de uma lista, exemplo se quisessemos pegar do item 0 ao 5 pulando de 2 em 2 itens.

  <h3>Exemplo:</h3>
  <img src="1-criando-acessando-listas/img/4-fatiamento-listas.png">

  <h3>Retorno:</h3>
  <img src="1-criando-acessando-listas/img/4.4-fatiamento-listas.png">

  <h3>Código para copiar:</h3>
  <blockquote>
  
    lista = ["j", "a", "v", "a", "s", "c", "r", "i", "p", "t"]

    # Retorna do item 2 até o fim da lista.
    print(lista[2:])
    # Retorno: ['v', 'a', 's', 'c', 'r', 'i', 'p', 't']

    # Retorna do item 0 até  o item 5, ignora o item 6
    print(lista[:6])
    # Retorno: ['j', 'a', 'v', 'a', 's', 'c']

    # Retorna do item 4 ao item 6, ignora item 7
    print(lista[4: 7])
    # Retorno: ['s', 'c', 'r']

    # Retorna do item 0 ao item 7 pulando de 3 em 3 ignora oo item 8
    print(lista[0:8:3])
    # Retorno: ['j', 'a', 'r']

    # Retorna todos os itens de uma lista
    print(lista[::])
    # Retorno: ['j', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

    # Retorna a lista de tras para frente
    print(lista[::-1])
    # Retorno: ['t', 'p', 'i', 'r', 'c', 's', 'a', 'v', 'a', 'j']

  </blockquote>
  <br>

<!-- Iterar/Percorrer listas -->
<h2>Como Percorrer uma Lista</h2>

  - Podemos percorrer uma lista usando o **for**, más também podemos usar o for com o comando **enumarate**.
  - O **enumerate** serve para quando precisamos **saber o indice** do item que estamos percorrendo, ele sempre começa com zero.

  <h3>Exemplo:</h3>
  <img src="1-criando-acessando-listas/img/5-percorrer-listas.png">

  <h3>Retorno:</h3>
  <img src="1-criando-acessando-listas/img/5.5-percorrer-listas.png">

  <h3>Código para copiar:</h3>
  <blockquote>
  
    linguagens = ["Kotlin", "JS", "Python"]

    print("\nRetorno do for:")
    for linguagem in linguagens:
        print(linguagem)

    print("".center(30,"_"))

    # Usando for com enumerate
    print("\nRetorno do for com enumerate:")
    for indice, linguagem in enumerate(linguagens):
        print(f"Item {indice}: {linguagem}")
  
  </blockquote>
  <br>

<!-- Comprensão de listas -->
