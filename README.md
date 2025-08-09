# Python
Este repositório acomoda projetos desenvolvidos em python, exemplos e como usar algumas bibliotecas Pyton.

## EXEMPLOS DE SINTAXE
Veja a baixo alguns exemplos em Python:
 
![operadores](https://github.com/marcospontoexe/Python/blob/main/imagens/operadores.png)
 
1. [Manipulação de entrada e saida de dados](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/01-vari%C3%A1veis): Veja maneiras de manipular entrada e saida de dados usando com o monitor e o teclado, com variáveis int, float e strings.
2. [Manipulação de strings](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/02-string): Aprenda a manipular variáveis dotipo String.
3. [Uso de bibliotecas](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/03-bilioteca): Veja como usar algumas bibliotecas essenciais.
4. [Usando `if` e `elif`](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/04-if): Veja como usar o comando `if` e `elif` para criar blocos condicionais, e também operador ternário
5. [Colorindo saida de dados pelo monitor](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/05-cores): Veja como colorir a saida de dados no monitor.
6. [Usando o comando `for`](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/06-for): Veja como usar o comando `for` para criar estruturas de repetição.
7. [Usando o comando `while`](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/07-while): Veja como usar o comando `while` para criar estruturas de repetição.
8. [Controle de fluxo`](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/08-break): Às vezes, queremos forçar alguns comportamentos nos nossos laços de repetição. Isso pode ser uma interrupção das repetições ou forçar o código para ir para a próxima iteração, por exemplo.
    * **Break**:O comando break interrompe um laço no ponto onde estiver do código, passando a execução do programa para a linha imediatamente posterior ao final do laço.
    * **Continue**: O comando continue força uma nova iteração a partir do ponto em que o programa se encontra, não sendo executado o resto do laço.
    *  **Pas**: O comando pass preenche uma estrutura que, porventura, tenha de ficar vazia. Normalmente, é utilizado para testar códigos ainda não terminados. 
9. [Usando tuplas](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/09-tupla): Veja como usar tuplas para manipular dados.
10. [Usando listas](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/10-lista): Veja como usar tuplas para manipular listas.
     
| Método    | Descrição                                                        |
|-----------|------------------------------------------------------------------|
| append()  | Adiciona um elemento ao fim da lista.                            |
| extend()  | Adiciona todos os elementos de uma lista em outra.               |
| insert()  | Insere um elemento em determinado índice da lista.               |
| remove()  | Remove um elemento da lista.                                     |
| pop()     | Remove e retorna determinado elemento de um índice da lista.     |
| clear()   | Remove todos os elementos da lista.                              |
| index()   | Retorna o índice do primeiro elemento localizado na lista.       |
| count()   | Retorna a quantidade de um elemento na lista passado como argumento. |
| sort()    | Ordena os elementos de uma lista em ordem ascendente.            |
| reverse() | Inverte a ordem dos elementos de uma lista.                      |
| copy()    | Retorna uma cópia da lista.                                      |
| min()     |  retorna o menor valor dentro de uma lista.|
| max()     |  retorna o maior valor dentro de uma lista. |
| len()     |  retorna a quantidade de elementos de uma lista. |
| sorted()  | retorna a lista passada em ordem crescente, ordenação em ordem decrescente, por meio do parâmetro reverse.  sorted(lista, reverse=True)  |
| sum()     | retorna a soma de todos os elementos de uma lista.                                    |

11. [Usando dicionários](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/11-dicion%C3%A1rio): Veja como usar tuplas para manipular dicionários.

| Método         | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| `clear()`      | Remove todos os elementos de um dicionário.                               |
| `copy()`       | Retorna a cópia de um dicionário.                                         |
| `fromkeys()`   | Retorna um dicionário com chaves e valores específicos.                   |
| `get()`        | Retorna o valor de uma chave específica.                                  |
| `items()`      | Retorna uma lista contendo uma tupla para cada par chave-valor.           |
| `keys()`       | Retorna uma lista contendo as chaves de um dicionário.                    |
| `pop()`        | Remove um elemento de uma chave específica.                               |
| `popitem()`    | Remove o último elemento inserido no dicionário.                          |
| `setdefault()` | Retorna o valor de uma chave específica. Caso não exista, insere esse valor. |
| `update()`     | Adiciona um conjunto de pares chave-valor a um dicionário.                |
| `values()`     | Retorna a lista de valores de um dicionário.                              |


12. [Usando funções](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/12-fun%C3%A7%C3%B5es): Veja como usar funções.
 * **Parâmetros com valor-padrão**: Todos os parâmetros com valores-padrão ficam no final da lista de parâmetros na função.
 * **Parâmetros arbitrários**: Uma função que possa receber um número variável de parâmetros precisa declarar um parâmetro arbitrário.
 * **Retornos múltiplos (tuplas)**: Este retorno pode ser capturado como uma tupla, sendo os valores acessados de forma individual a partir de cada índice.
 *  **Documentando funções**: O desenvolvimento em Python é regido por alguns documentos de boas práticas, chamados Python Enhancement Proposals (PEPs). No caso da documentação, existe o padrão docstrings, registrado pelo PEP 257 – Docstring Conventions.
   ```python
   def delta(a: int, b: int, c: int) -> int:
       """
       Calcula o valor de delta utilizado no cálculo de raízes de polinômios de segundo grau.
    
       :param a: Valor do primeiro termo do polinômio.
       :param b: Valor do segundo termo do polinômio.
       :param c: Valor do termo independente do polinômio.
       :return: Retorna as raízes calculadas e um booleano, indicando se o cálculo foi bem-sucedido.
       """
       return b*b - 4*a*c
```
* **Sobre carga**: As funções em python não aceitam sobre carga.

**DICAS:**
* **Não use variáveis globais:**
 1. Tudo o que a função precisa para funcionar deve ser enviado nos parâmetros.
 2. Tudo o que a função precisa retornar deve estar no return.
 3. A dependência de estado global pode tornar seu código difícil de entender e propenso a bugs. Prefira passar variáveis como argumentos para suas funções.
* **Mantenha suas funções pequenas e focadas:** Cada função deve fazer uma coisa e fazer bem. Isso torna as funções mais fáceis de entender, testar e reutilizar.
* **Use nomes descritivos:** O nome da função deve indicar claramente o que ela faz. Prefira nomes mais longos e descritivos no lugar de nomes curtos e vagos.
* **Evite muitos parâmetros:** Se uma função tem muitos parâmetros, pode ser difícil entender e usar. Considere agrupar parâmetros parecidos em uma tupla ou dicionário.
* **Evite efeitos colaterais:** Uma função não deve modificar o estado global ou alterar seus argumentos de entrada, a menos que essa seja explicitamente sua finalidade.
* **Use comentários e documente o seu código:** Use comentários e documente o seu código para explicar partes complicadas do código para descrever o que a função faz, seus parâmetros e o que retorna.
* **Use a palavra-chave return explicitamente:** Mesmo que uma função não retorne um valor útil, considere usar **return None** explicitamente para tornar claro que a função é intencionalmente sem retorno.
13. **Manipulando arquivos:**.
  *  veja como abrir e salvar [arquivos **txt**](https://github.com/marcospontoexe/Python/blob/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/13-modulariza%C3%A7%C3%A3o/02-pacote(biblioteca)/biblioteca/arquivo/__init__.py).
  * Usando a palavra-chave reservada **with**, uma construção em Python que garante que o arquivo seja fechado corretamente após o seu uso:
```python
with open("dados.txt", "w") as arquivo: #maneira de abrir um arquivo txt
  arquivo.write("Counter-Strike é melhor do que Valorant.")
  arquivo.write("O correto é 'bolacha'.")
```
    
```python
with open("dados.txt", "r") as arquivo: #maneira de ler um arquivo txt
 linhas = arquivo.readlines() # retorna uma lista de strings, onde cada elemento da lista representa uma linha do arquivo
 print(linhas)
'''
Ler uma linha de cada vez: função readline().
Ler todo o conteúdo do arquivo em uma só string: função read().
Ler todo o conteúdo do arquivo separando linha por linha como strings em uma única lista: função readlines().
'''
```
* **JSON**: O JSON é baseado em uma estrutura de dados composta por pares de chave e valor. Esses pares são organizados em uma sintaxe simples e legível, permitindo representar informações de forma estruturada. A estrutura básica do JSON consiste em objetos e arrays (vetores, ou listas).

  * Objetos: são delimitados por chaves {} e consistem em uma coleção não ordenada de pares chave-valor. Cada chave é uma string única que identifica o valor associado a ela. Os pares chave-valor são separados por vírgulas.
  * Arrays: são delimitados por colchetes [] e podem conter uma lista ordenada de valores. Os valores em um array podem ser de qualquer tipo válido do JSON, incluindo strings, números e outros arrays. Os elementos do array são separados por vírgulas.
  ```python
  import json
  dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Curitiba",
    "frutas_favoritas": [
      "maçã",
      "banana",
      "laranja"
    ]
  }# abrindo um arquivo chamado “pessoa.json” em modo de escrita.
  ## encoding=”utf-8”. Definimos este parâmetro para garantir que caracteres especiais (como o “ã” e “ç”) sejam tratados corretamente.
  with open("pessoa.json", "w", encoding="utf-8") as arquivo: 
    #estamos usando a função json.dump() para escrever o conteúdo do dicionário dados no arquivo JSON aberto.
    #o parâmetro ensure_ascii=False para permitir a codificação correta de caracteres não-ASCII (caracteres que não façam parte do alfabeto da língua inglesa).
    # O código UTF-8 (Unicode) é mais amplo que o ASC-II. Ele é adequado para aplicações multilíngues e internacionais
    json.dump(dados, arquivo, ensure_ascii=False, ident=4)
    arquivo.close() # Fecha o arquivo 
  
  # lendo o conteúdo do arquivo pessoa.json em modo de leitura. 
  # Como poderemos ter caracteres especiais, usamos também o parâmetro encoding="utf-8" para evitarmos qualquer tipo de erro.  
  with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    #. A função load() carrega o conteúdo do arquivo JSON e converte-o em uma estrutura de dados Python, como um dicionário ou uma lista, dependendo do conteúdo do arquivo JSON.
    dados_lidos = json.load(arquivo)
    arquivo.close() # Fecha o arquivo 
  print(dados_lidos)
  ```

* Arquivo **binários**: Podemos usar o módulo **pickle** para ler e salvar variáveis sem passar por nenhum tipo de conversão.
  ```python
  import pickle
  
  dados = [1, 2, 3, 4, 5]
  
  with open("dados.pickle", "wb") as arquivo: #Abrimos o arquivo em modo de escrita binário ("wb”)
      pickle.dump(dados, arquivo) # pickle.dump() para armazenar uma variável "dados" dentro do arquivo binário "arquivo"
      arquivo.close() #fecha o arquivo binário
      '''
      O pickle permite que você armazene e recupere uma ampla variedade de objetos Python, incluindo listas, tuplas, conjuntos, classes personalizadas e muito mais. 
      Basta passar o objeto desejado como argumento para a função pickle.dump()
      '''
  
  with open("dados.pickle", "rb") as arquivo: #Abrimos o conteúdo do arquivo pickle no modo leitura binário (“rb”)
      variavel_lida = pickle.load(arquivo)    #"variavel_lida" recebe o conteúdo de "arquivo" 
      arquivo.close() #fecha o arquivo binário
  print(variavel_lida)
  ``` 
  
14. [Modularizando scripts](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/13-modulariza%C3%A7%C3%A3o): Veja como modularizar scripts e criar bibliotecas python.
15. [Tratamento de erros](https://github.com/marcospontoexe/Python/tree/main/exerc%C3%ADcios_curso%20em%20v%C3%ADdeo/tratamento%20de%20erros): Veja como deixar o script mais robusto a erros com os comandos `try`, `except`, e `finally`.
---

# POO (Object-Oriented Programming) no Python
A programação orientada a objetos tem o objetivo de aproximar o mundo digital do mundo real.  

## A evolução dos métodos de programação
Quando os computadores começaram a surgir, na década de 40, a programação era feita em **baixo nível**. Quem fornecia as instruções para o cumputador realizar uma ação eram os próprios engenheiros que construiam os computadores, e as instruções eram binárias ou decimais. Esse tipo de programação é chamada linguagem de máquina. Dando sequência aos métodos de programação, surgil a linguagem de alto nível tornando a **programação linear**, os comandos eram mais compreensíveis para humanos, mas ainda sem rotinas internas.

A evolução da programação linear deu origem à **programação estruturada** no final da década de 60, permitindo que pequenos pedações da programação linear  fosse executados fora da ordem natural, dando origem aos sistemas. Com o crescimento dos sistemas a programação estruturada começou a falhar em sua metodologia, e surgiu a **programação modular**, permitindo o desenvolvimento de softwares que envolve dividir um programa em partes menores e independentes chamadas módulos. Cada módulo tem uma responsabilidade bem definida e interage com outros módulos através de interfaces claramente definidas. Essa abordagem promove a reutilização de código, a facilidade de manutenção e a escalabilidade do software. Apliando os conceitos da programação modular, surgiu a **programação orientada a objetos**.

**Alan Kay**, o pai da POO, que era formado em biologia e matemática desenvolveu a POO baseado na forma natural de como as coisas se relacionam no mundo real. Veja a baixo o seu postulado:
> O computador ideal deve funcionar como um
> organismo vivo, isso é, cada célula se relaciona
> com outras a fim de alcançar um objetivo, mas
> cada uma funciona de forma autônoma. As
> células poderiam também reagrupar-se para
> resolver um outro problema ou desempenhar
> outras funções.

## Vantagens da POO
Todo software orientado a objetos é:
* **confiável**: O isolamento entre as parte gera software seguro. Ao alterar uma parte, nenhuma outra é afetada.
* **Oportuno**: Ao dividir tudo em partes, várias delas podem ser desenvolvidas em paralelo.
*  **Manutenível**: Atualizar um software é mais fácil. Uma pequena modificação vai beneficiar todas as partes que usarem o objeto.
*  **Extensível**: O software não é estático. Ele deve crescer para permanecer útil.
*  **Reutilizável**: Podemos usar o objeto de um sistema que criamos em outro sistema fulturo.
*  **Natural**: Mai fácil de entender. Você se preocupa mais na funcionalidade do que nos detalhes de implementação.

## O que é um objeto
Objeto é uma coisa material ou abstrata que pode ser percebido pelos sentidos e descrita por meios de suas características, comportamento e estado atual. Em programação os objetos são representados por classes, responsável por classificar características, comportamento e estado atual de um objeto.

Por exemplo, uma objeto "Carro" pode ter atributos como cor, modelo, métodos como acelerar e frear, e o estado atual como ligado ou desligado. 

### As características
Todo objeto possui pelo menos uma característica que descreve oque esse objeto tem, em programação essas características são chamadas de **atributos**.

Para criar atributo, deve-se começar com o prefixo **self.** e depois o nome da variável. 

Variáveis da classe são como variáveis globais para essa classe! O que isso significa? Isso significa que as variáveis podem ser usadas em qualquer método que pertença à classe. Este é um dos principais pontos de usar classes. Você não precisará usar variáveis globais que podem ser acessadas em qualquer parte do código, contribuindo para a construção de uma bagunça. Ao encapsular as variáveis dentro da classe, apenas os métodos da classe podem acessar essas variáveis, portanto, você tem menos chances de cometer erros.

### O comportamento do objeto
Objetos possuem comportamento responsável em realizar uma ação, em programação esses comportamentos são nomeados de **métodos**.
Todo método de classe deve passar como primeiro parâmetro, obrigatoriamente, o objeto **self**, que é uma referência à própria classe à qual o método pertence.

### Estado do objeto
Em programação o estado atual do objeto é manipulado por métodos acessores e modificadores **getter** e **setter**. O getter diz qual é o estado atual de um determinado atributo do objeto, e o setter altera o estado desse atributo. No entanto, a abordagem tradicional de usar métodos getter e setter não é tão comum em Python quanto em algumas outras linguagens de programação, como Java.

### Herança
Herança é quando classes herdam características de outras classes. 
[Veja nesse exemplo](https://github.com/marcospontoexe/Python/blob/main/POO/Heranca.py) que a classe "Forma" é uma classe base que contém os métodos que todas as outras classes irão herdar. A partir dela, foram criadas as subclasses "Circulo" e "Retangulo", cada uma com seus próprios métodos e atributos. Perceba que temos agora **class Circulo(Forma)** e **class Retangulo(Forma)**. Este **(Forma)** presente em ambos os casos é o que diz que estas duas classes são herdadas de Forma.

Não é necessário implementar todos os métodos da superclasse para todas as classes filhas. Se não implementarmos, a classe filha usará a mesma lógica implementada pela superclasse. Como não foi implementada a própria lógica de **calcular_area()** para Circulo e Retangulo e nem implementamos a nossa lógica de calcular_perimetro() para o Retangulo, o algoritmo usou a lógica que existia na superclasse.

### Polimorfismo
O polimorfismo permite que classes filhas herdem o mesmo métoda da superclasse mas com comportamento defirente para cada classe filha. [Veja um exemplo](https://github.com/marcospontoexe/Python/blob/main/POO/Polimorfismo.py).

## Criando objetos
Para criar um objeto, antes é necessário planejar o seu molde. A partir desse molde é possível criar inúmeros objetos.
Esse molde é chamado de **classe** e possui todas as características e comportamento (os atributos e métodos) do objeto a ser criado.

O nome dado ao processo de criação de um objeto a partir de uma classe existente se chama **instanciar** um objeto. Com objeto instanciado (criado) é possível saber qual é o estado atual desse objeto e alterar esse estado, antes disso o estado do objeto é inexistem, pois ainda não foi instanciado.

### Modificadores de acesso
Indicam o nível de acesso aos atributos e métodos de uma classe, permintindo encapsular um objeto. No entanto em Python, não há modificadores de acesso tradicionais, como "public", "private" e "protected", como em algumas outras linguagens de programação orientada a objetos. 

Porém ainda sim é possível garantir uma proteção aos dados internos da classe, pode-se definir um escopo **privado** para eles. Ou seja, os dados só podem ser alterados pelo código interno da classe, e não por uma chamada externa sem controle. Essa implementação é feita colocando dois underscores **(_)** antes do nome do parâmetro. A partir deste momento, o acesso aos atributos privados devem ser feito a partir de métodos públicos da classe.

Para tornar um **método privado**, basta adicionar dois underscores antes de seu nome. Isso indica que o método deve ser utilizado internamente pela classe e não deve ser acessado externamente.

### Método construtor
É um método da classe usado para configurar os atributos e estado de um objeto no momento em que é instanciado, garantindo que o objeto esteja em um estado válido e utilizável. O método construtor tem o seguinte nome `__init__` e pode, ou não, receber parâmetros para criar um objeto.

Caso não seja implementado um construtor em uma classe, o compilador fornece um construtor padrão sem parâmetros em qualquer classe que não inclui explicitamente um construtor.

Ao contrário de outras linguagens de programação, o Python não permite a criação de diversos construtores. Por outro lado, conforme as regras de funções é possível dar valores-padrão para os parâmetros do construtor.

[Clique aqui](https://github.com/marcospontoexe/Python/tree/main/POO) para ver um exemplo de objeto em Python. Nesse exemplo a classe "Main.py" instancia dois objetos da classe "Jedi".

Veja nesse [outro exemplo](https://github.com/marcospontoexe/Python/blob/main/POO/Televisao.py) uma classe Televisao, em que o usuário é capaz de trocar de canais, aumentar ou diminuir o volume. O limite de canais válidos vai de 1 a 15 e o limite de volume válido vai de 0 a 10. No caso de um canal inválido, é definido como padrão o canal 1.
---

# BIBLIOTECAS
Veja como usar algumas bibliotecas Python
## Tk interface
A biblioteca Tkinter é uma ferramenta comumente usada com interface gráfica para programas em Python, e faz parte do kit de ferramentas Tcl/Tk GUI. Tanto o Tk quanto o tkinter estão disponíveis na maioria das plataformas Unix, incluindo macOS, bem como em sistemas Windows.
### Gerenciador de layouts
O gerenciador de layout é um widget responsável por gerenciar o posicionamento de outros widget dentro de um container. 
É recomendado usar apenas um único gerenciador de layout em cada container, porém podemos usar um container dentro de outro container.
No pacote Tkinter existem três gerenciadores de layouts distintos (place, pack, grid).
* [Place](https://github.com/marcospontoexe/Python/tree/main/tkinter/01-gerenciador%20de%20layout/01-place): O gerenciador de layout **Place** posiciona os widgets no plano cartesiano (x, y).
* [Pack](https://github.com/marcospontoexe/Python/tree/main/tkinter/01-gerenciador%20de%20layout/02-Pack): O gerenciador de layout **PACK** empacota os widgets, alinhando na direção horizontal ou vertical a partir do atributo "side" (TOP, BOTTOM, LEFT ou RIGHT).
* [GRID](https://github.com/marcospontoexe/Python/tree/main/tkinter/01-gerenciador%20de%20layout/03-grid): O gerenciador de layout **GRID** usa linhas e colunas para posicionar os widgets, usando o conceito de planilha para o posicionamento dos widgets.
### Widgets
Nessa sessão estão disponíveis alguns widgets da biblioteca Tkinter. 
* [Menu](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/01-menu): O Widget menu disponibiliza opções de menus e submenus na barra superior da GUI.
* [Radio Button](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/02-radio_button): Esse widget cria radio buttons para selecionar opcões.
* [Option Menu](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/03-option_menu): De maneira similar ao Radio Buttom, selecione opções de com Option Menu.
* [Message Box](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/04-message_box): Imprima informação na GUI com o Message box, com esse widget também é possível solicitar informações como *sim* e *não* do usuário.
* [Frame](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/05-frame): Cria uma janela do tipo **frame**.
* [Label Frame](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/06-label%20frame):  Cria uma janela do tipo **frame** com um Label de informação relacionado à janela frame.
* [Image](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/07-image): Imprima imagens na GUI com este widget.
* [Check Button](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/08-checkButton): Diferendo do **Radiobutton** e do **Optionmenu**, que permitem selecionar apenas uma opção, o **Checkbutton** permite selecionar várias opções.
* [Entry](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/09-senha): Receba parâmetro de entrada pela GUI com o este widget.
* [Combo Box](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/10-comboBox): Este widget permite selecionar opções ja exixtentes ou que o usuário digite novas opções.
* [List Box](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/11-listBox): Semelhante ao **Combobox**, o **Listbox** permite que o usuário inclua uma nova opção a lista de seleção, porém o menu de opções mostra todas as opções possíveis.
* [Spin Box](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/12-spinbox): Selecione valores predefinidos.
* [Scale](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/13-scale): Selecione valores a partir de uma barra de rolagem horizontal. 
* [Note Book](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/14-notebook): O **Notebook** permite criar um Widget semelhante a um gerenciador de Layouts.
* [Progress Bar](https://github.com/marcospontoexe/Python/tree/main/tkinter/02-WidGets/15-progressBar): O **Progressbar** imprime uma barra de progresso na GUI.
### Eventos
Eventos podem ser chamados com o método [`bind()`](https://github.com/marcospontoexe/Python/tree/main/tkinter/03-eventos/01-bind), atribuido à uma tecla.
## Pandas
Pandas é uma biblioteca para manipulação de dados.

A biblioteca cria uma data frame, que é uma tabela contendo linhas e colunas.
As **colunas**, chamadas de *séries*, são do tipo *lista* e pode ter apenas um tipo de variável (float, int, boleana...).
As **linhas**, chamadas de *registros* ou *amostras*. São do tipo *dicionário* e podem conter vários tipos de variáveis (float, int, boleana...).

Ocabeçalho da tabela é chamado de *features*, *atributo* ou *variável*.

![pandas](https://github.com/marcospontoexe/Python/blob/main/Pandas/imagens/pandas-componentes-principais.png)

DataFrames e Series são muito semelhantes, pois muitas operações podem ser feitas com uma ou com a outra (e.g., preencher valores nulos, calcular a média).

* [Criando Dataframes](https://github.com/marcospontoexe/Python/tree/main/Pandas/01-gerando%20arquivos): Veja alguns exemplos para criação de um dataframe. Veja também como inserir e apagar *séries* e *registros*, e salvar o dataframe como um arquivo ".CSV" ou ".XLSX".
* [Abrindo um dataframe](https://github.com/marcospontoexe/Python/tree/main/Pandas/02-abrir_arquivos): Veja como gerar um dataframe a partir de um arquivo ".CSV" ou ".XLSX", e ver a quantidade de *séries* com o metodo `shape`, *registros*, dados contidos no dataframe e seus tipos com os métodos `size` e `info()`. 
* [Explorando o dataframe](https://github.com/marcospontoexe/Python/tree/main/Pandas/03-explorando%20o%20arquivo): Veja como usar alguns métodos para análise dos dados, como `value_counts()`, `unique()`, `isnull()`, `loc()`, `iloc()`, `isnull()`. Veja também alguns métodos para conversão de dataframe; `to_datetime()`, `to_numeric()`.
* [Manipulando dados](https://github.com/marcospontoexe/Python/tree/main/Pandas/04-manipulando%20valores): Veja como manipular dados.
* [filtrando valores](https://github.com/marcospontoexe/Python/tree/main/Pandas/05-filtrando%20valores): O `filter()` permite realizar busca mais avançada.
* [Agrupamento de dados](https://github.com/marcospontoexe/Python/tree/main/Pandas/06-agrupamento): Faça um agrupamento de dados do o método `groupby()`, ou usando funções de agrupamento; `sum()`, `mean()`, `max()`, `min()`, `describe()`...

## Win32com
O win32com é uma biblioteca que fornece acesso a muitas funcionalidades do Windows através da tecnologia COM (Component Object Model). Permite interagir com aplicativos Windows e manipular arquivos do sistema, para controlar aplicativos e processos.


[Nesse exemplo](https://github.com/marcospontoexe/Python/tree/main/Pandas%20e%20e-mail) o win32com é usado para enviar um dataframe tratado por e-mail através do *Microsoft Outlook*.

## re
A biblioteca **re** em Python é utilizada para **trabalhar com expressões regulares (regex)** — uma poderosa ferramenta para **buscar, verificar, extrair, substituir e dividir strings com base em padrões de texto**.

### O que são expressões regulares?

Expressões regulares são **sequências de caracteres especiais que definem um padrão de busca**. Por exemplo:

* `\d` → qualquer dígito (0–9)
* `\w` → qualquer caractere alfanumérico (a–z, A–Z, 0–9, \_)
* `.` → qualquer caractere (exceto nova linha)
* `*` → repete zero ou mais vezes
* `+` → repete uma ou mais vezes
* `^` → início da string
* `$` → fim da string

As expressões regulares foram inicialmente propostas como um sistema de notações de álgebra de conjuntos regulares usado na busca de padrões em textos. Essas notações foram, anos mais tarde, implementadas em diversas linguagens de programação, como Perl, Python, PHP e JavaScript.​​​​​​​

Você poderá fazer uso de expressões regulares nas mais diversas situações em que precise localizar ou extrair padrões em meio ao texto (e.g., encontrar CEPs de endereço no texto, obter os preços de produtos de uma listagem). Você pode usar expressões regulares em linguagens de programação e editores de texto por exemplo.

Sempre que possível, use **raw strings** (prefixo `r""`) para evitar que o Python interprete barras invertidas como escapes:

```python
re.search(r"\d+", "ano 2025")
```
### Definir para qual funcionalidade o padrão RegEx será utilizado
Você pode usar um padrão para:

* Buscar padrões/valores no texto (i.e., **search**, **match**, **findall**)
* Quebrar texto em sub-textos (i.e., **split**)
* Substituir dados no texto (i.e., **sub**)

texto = "clássico é clássico e vice-versa"

```python
# A função search() retorna um objeto caso encontre o padrão no texto
if re.search(padrao, texto):
  print("Encontrou")
else:
  print("Não encontrou")
```

### `re.search(pattern, string)`

Busca o **primeiro match** do padrão em qualquer lugar da string.

```python
match = re.search(r"clássico", "clássico é clássico e vice-versa")  # <re.Match object; span=(0, 8), match='clássico'>
# Mostra o objeto/match da busca - caso não encontre o padrão retorna None
match
```

```python
re.search(r"\d+", "Hoje é dia 01 de agosto")  # Match: '01'
```

### `re.match(pattern, string)`
Verifica se o padrão **ocorre no início da string**.

```python
match = re.match(r"clássico", "clássico é clássico e vice-versa")
# Mostra o objeto/match da busca - caso não encontre o padrão retorna None

# Caso queira mostrar o trecho de texto encontrado usar a função group()
#match.group()

# Caso queira obter a posição de início e fim do texto encontrado
#match.start()
#match.end()
```

```python
m = re.match(r"teste", "Este é um teste de regex.")
print(m)    # None
```

```python
re.match(r"\d+", "2025 é o ano")  # Match: '2025'
```

### `re.findall(pattern, string)`

Retorna **todas as ocorrências** do padrão na string.

```python
re.findall(r"\d+", "Dias: 01, 02, 03")  # ['01', '02', '03']
```

```python
match = re.findall(r"clássico", "clássico é clássico e vice-versa") # ['clássico', 'clássico']
```

### `re.sub(pattern, replacement, string)`

Substitui todas as ocorrências do padrão por outro valor.

```python
re.sub(r"\d+", "XX", "Dia 01 de agosto")  # 'Dia XX de agosto'
```

```python
r = re.sub(r"gato", "cachorro", "Este é meu gato Thomas. Eu adoro ter um gato em casa.")  #Este é meu cachorro Thomas. Eu adoro ter um cachorro em casa.
```

### `re.split(pattern, string)`

Divide o texto toda vez que encontrar a ocorrência do padrão dado.

```python
re.split(r",\s*", "maçã, banana, uva")  # ['maçã', 'banana', 'uva']
```

```python
partes = re.split(r"/", "10/05/1999") # ['10', '05', '1999']
```

### Como escrever padrões mais complexos?

Agora que você sabe utilizar as principais funções da biblioteca re, podemos criar padrões de busca mais complexos e poderosos. Existe uma série de caracteres especiais que podem lhe ajudar a construir os padrões de texto desejados. Não é preciso decorá-los, apenas saber como utilizá-los. A seguir uma tabela de referência com vários destes caracteres.

![regex](https://github.com/marcospontoexe/Python/blob/main/imagens/regex-cheat-sheet.png)

**DICA IMPORTANTE**: Você também pode testar as expressões regulares a seguir no site [**Pythex**](https://pythex.org/), que tem uma interface bem interessante para visualizar e testar suas expressões regulares.

### Metacaracteres

#### Metacaracteres Representantes (ou de Classe de Caracteres)

**Para que servem:** Eles definem **quais** caracteres podem aparecer em uma determinada posição. São como "curingas" ou "moldes" para um único caractere.

| Metacaractere | Nome | O que faz | Exemplo Prático |
| :--- | :--- | :--- | :--- |
| **`.`** | Ponto (Curinga) | Corresponde a **qualquer caractere único**, exceto quebra de linha. | A regex `c.sa` encontrará "casa", "cosa", "cisa", "c#sa", etc. |
| **`[]`** | Lista (ou Conjunto) | Corresponde a **qualquer um dos caracteres** listados dentro dos colchetes. | A regex `gr[ae]y` encontrará "gray" e "grey", mas não "groy". |
| **`[^]`** | Lista Negada | Corresponde a qualquer caractere que **NÃO** esteja na lista. | A regex `[^abc]` encontrará "d", "x", "5", mas não "a", "b" ou "c". |
| **`\w`** | Alfanumérico | Corresponde a qualquer caractere de palavra (letras `a-z`, `A-Z`, números `0-9` e `_`). | A regex `\w\w\w` encontrará "gato", "Rua", "123", mas não "R$!". |
| **`\d`** | Dígito | Corresponde a qualquer dígito numérico (`0` a `9`). | A regex `CEP: \d\d\d\d\d-\d\d\d` encontrará "CEP: 12345-678". |
| **`\s`** | Espaço em Branco | Corresponde a qualquer caractere de espaçamento (espaço, tabulação `\t`, nova linha `\n`). | A regex `Olá\sMundo` encontrará "Olá Mundo". |

---

#### Metacaracteres Quantificadores

**Para que servem:** Eles definem **quantas vezes** o caractere, grupo ou classe anterior pode se repetir. Eles nunca aparecem sozinhos, sempre modificam o item que vem imediatamente antes deles.

| Metacaractere | Nome | O que faz | Exemplo Prático |
| :--- | :--- | :--- | :--- |
| **`*`** | Asterisco | Corresponde ao item anterior **zero ou mais** vezes. | A regex `go*l` encontrará "gl" (zero 'o'), "gol" (um 'o') e "goooool" (vários 'o'). |
| **`+`** | Mais | Corresponde ao item anterior **uma ou mais** vezes. | A regex `go+l` encontrará "gol" e "goooool", mas **não** "gl". |
| **`?`** | Interrogação | Corresponde ao item anterior **zero ou uma** vez (torna o item opcional). | A regex `honou?r` encontrará "honor" (versão americana) e "honour" (versão britânica). |
| **`{n}`** | Chaves (Exato) | Corresponde ao item anterior exatamente **n** vezes. | A regex `\d{3}` encontrará "123", "987", mas não "12" ou "1234". |
| **`{n,}`** | Chaves (Mínimo) | Corresponde ao item anterior **no mínimo n** vezes. | A regex `\d{2,}` encontrará "12", "123" e "1234", mas não "1". |
| **`{n,m}`** | Chaves (Intervalo) | Corresponde ao item anterior **no mínimo n** e **no máximo m** vezes. | A regex `\w{3,5}` encontrará "gato" e "cinco", mas não "eu" ou "paralelepípedo". |

---

#### Metacaracteres Âncoras (ou de Posição)

**Para que servem:** Eles não correspondem a um caractere, mas a uma **posição** específica na string (início, fim, ou fronteira de palavra). Eles garantem que o padrão seja encontrado apenas em um determinado local.

| Metacaractere | Nome | O que faz | Exemplo Prático |
| :--- | :--- | :--- | :--- |
| **`^`** | Circunflexo | Corresponde ao **início** da string ou da linha. | A regex `^Olá` encontrará "Olá" em "Olá mundo", mas não em "Diga Olá mundo". |
| **`$`** | Cifrão | Corresponde ao **fim** da string ou da linha. | A regex `mundo$` encontrará "mundo" em "Olá mundo", mas não em "mundo cruel". |
| **`\b`** | Borda de Palavra | Corresponde à posição entre um caractere de palavra (`\w`) e um não-palavra (`\W`). | A regex `\bato\b` encontrará "ato" em "um ato de coragem", mas não em "gato" ou "trator". É perfeito para encontrar palavras inteiras. |

---

#### Metacaracteres de Agrupamento e Alternância

**Para que servem:** Eles permitem criar sub-padrões mais complexos, agrupar partes de uma expressão ou definir alternativas.

| Metacaractere | Nome | O que faz | Exemplo Prático |
| :--- | :--- | :--- | :--- |
| **`()`** | Parênteses | **Agrupa** uma parte da expressão para aplicar um quantificador a todo o grupo. Também "captura" o texto correspondente para uso posterior. | A regex `(ha)+` encontrará "ha", "haha", "hahaha". Sem os parênteses, `ha+` encontraria "ha", "haa", "haaa". |
| **`|`** | Barra Vertical (OU) | Funciona como um operador **OU**, correspondendo à expressão da esquerda **ou** à da direita. | A regex `gato|cachorro` encontrará "gato" ou "cachorro". |
| **`\`** | Barra Invertida (Escape) | **Escapa** um metacaractere, ou seja, remove sua função especial e o trata como um caractere literal. | Para encontrar um ponto final de verdade, você usa `\.`. A regex `site\.com` encontrará "site.com" e não "siteXcom". |

Entender essas quatro categorias e como elas se combinam é o que permite construir expressões regulares para resolver praticamente qualquer problema de busca e manipulação de texto.

### Groups & Ranges


### Classes de caracteres
* `\s` - Obtém todos espaços (white-space)
* `\S` - Obtém todos NÃO espaços (white-space)

```python
re.findall(r"\s", "Conseguimos pegar o que não é espaço?")  # [' ', ' ', ' ', ' ', ' ', ' ']
```

### Ancoras
* `^` - Indica início de texto

```python
# Faz match apenas se a palavra clássico estiver no início do texto
match = re.findall(r"^clássico", "clássico é clássico e vice-versa")    # ['clássico']
```

```python
# Faz match apenas se a palavra clássico estiver no início do texto
match = re.findall(r"^clássico", "Este jogo é um clássico") # []
```

* `$` - Indica fim de texto

```python
# Faz match apenas se a palavra clássico estiver no fim do texto
match = re.findall(r"clássico$", "Este jogo é um clássico")   # ['clássico']
```

```python
# Faz match apenas se a palavra clássico estiver no fim do texto
match = re.findall(r"clássico$", "clássico é clássico e vice-versa")   # []
```

### Quantificadores
Em alguns momentos você pode querer quantificar a quantidade de vezes que um determinado padrão aparece.

```python
# Padrão que encontra dois números em sequencia
match = re.findall(r"[0-9]{2}", "João tem 5 laranjas, enquanto Maria tem 25.")  # ['25']
```

```python
# Padrão que encontra de um a cinco números em sequencia
match = re.findall(r"[0-9]{1,5}", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")  # ['5', '25', '10000']
```

```python
# Padrão que encontra um ou mais numeros em sequencia
match = re.findall(r"[0-9]{1,}", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")   #  ['5', '25', '10000']
```

* `*` - Zero ou mais ocorrências

```python
# Padrão que encontra de um a cinco números em sequencia
match = re.findall(r"[a-zA-Z]{1,} x* [a-zA-Z]{1,}", "Vasco x Palmeiras - Corinthians x Santos - Portuguesa xxx Guarani")  # ['Vasco x Palmeiras', 'Corinthians x Santos', 'Portuguesa xxx Guarani']
```

* `+` - Uma ou mais ocorrências

```python
# Padrão que encontra um ou mais numeros em sequencia
match = re.findall(r"[0-9]+", "João tem 5 laranjas, enquanto Maria tem 25. Já Henrique possui 10000.")  # ['5', '25', '10000']
```

* `?` - Zero ou uma ocorrência

```python
# Padrão que encontra 9 numeros, seguidos ou não por um hífen, seguidos de dois números
match = re.findall(r"[0-9]{9}-?[0-9]{2}", "RG: 8122691-8 CPF: 064555874-90 / RG: 81623338 CPF: 06454357320 ") # ['064555874-90', '06454357320']
```

### Exemplo 
Vamos fazer uma expressão regular para obter endereços de e-mail no texto

```python
texto = "Lucas Oliveira: lucas.oliveira@pucpr.br \n maria-silva@gmail.com \n jobs@apple.com "
re.findall(r"[a-z]+@[a-z]+", texto)   # ['oliveira@pucpr', 'silva@gmail', 'jobs@apple']
```

O padrão acima obtém as letras, porém, ignora o hífen e o ponto final. Para resolver podemos criar um RANGE adicionando estes caracteres.

```python
re.findall(r"[a-z-.]+@[a-z-.]+", texto)   # ['lucas.oliveira@pucpr.br', 'maria-silva@gmail.com', 'jobs@apple.com']
```

###  EXTRAÇÃO DE GRUPO
Você pode realizar o que chamamos de EXTRAÇÃO DE GRUPO usando as expressões regulares. Basta agrupar os sub-padrões que você deseja extrair separadamente com os parênteses.

```python
re.findall(r"([a-z-.]+)@([a-z-.]+)", texto)   
"""
[('lucas.oliveira', 'pucpr.br'),
('maria-silva', 'gmail.com'),
('jobs', 'apple.com')]
"""
```

texto do linkDigamos que você queira remover todos os e-mails do texto por questões de privacidade.

```python
re.sub(r"[a-z-.]+@[a-z-.]+", "-CONFIDENCIAL-", texto)   # Lucas Oliveira: -CONFIDENCIAL- \n -CONFIDENCIAL- \n -CONFIDENCIAL- 
```

É possível ainda utilizar os agrupamentos para efetuar substituições mais complexas. Por exemplo, imagine que queiramos apenas substituir o servidor de e-mail, mas mantendo o nome de usuário.

```python
# Nesse caso podemos usar os agrupamentos da expressão regular
# \1 indica a informação obtida no primeiro agrupamento - neste caso o nome do usuário
# \2 indica a informação obtida no segundo agrupamento - neste caso o servidor do e-mail
re.sub(r"([a-z-.]+)@([a-z-.]+)", r"\1@regex.com", texto)    # Lucas Oliveira: lucas.oliveira@regex.com \n maria-silva@regex.com \n jobs@regex.com
```

### CARACTER DE ESCAPE
E quando eu quero procurar algum caractere que já representa algo em expressões regulares? (e.g., ponto final, interrogação). Nesse caso podemos usar o que chamamos de CARACTER DE ESCAPE, representado pelo caracter `\`.

Exemplo: Quero obter todas perguntas presentes em um texto
```python
texto = """Este é um texto de exemplo.
Mas será que ele é confiável?
Além dos questionamentos acima há outras questões a serem levantadas.
Você está gostando de aprender expressões regulares?
PLN é uma área de seu interesse?"""

# Obtém qualquer sequencia de caracteres (exceto quebra de linha)
re.findall(r".+", texto)  
"""
['Este é um texto de exemplo.',
 'Mas será que ele é confiável?',
 'Além dos questionamentos acima há outras questões a serem levantadas.',
 'Você está gostando de aprender expressões regulares?',
 'PLN é uma área de seu interesse?']
"""
```

Neste caso, o ponto de interrogação é considerado um quantificador de Expressão Regular, portanto, é interpretado como tal. Para fazermos com que ele seja interpretado como um caracter comum, usamos o escape `\`.

```python
re.findall(r".+\?", texto)  
"""
['Mas será que ele é confiável?',
 'Você está gostando de aprender expressões regulares?',
 'PLN é uma área de seu interesse?']
"""
```
---




Com certeza! Os **metacaracteres** são o coração das Expressões Regulares (Regex). Eles são caracteres que não representam a si mesmos, mas sim uma ideia, uma regra ou um conceito. É o que transforma uma busca de texto simples em uma busca por padrões poderosa.

Vamos dividir os metacaracteres em quatro categorias principais, explicando para que servem e com exemplos práticos.

---

