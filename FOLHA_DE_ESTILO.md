#Folha de Estilo

Este documento contém informações sobre os padrões de estilo de escrita e organização do livro colaborativo.

## Regionalização

O livro está escrito em língua portuguesa, seguindo os costumes linguísticos brasileiros. Dá-se prioridade à ortografia prevista no Acordo Ortográfico de 1990.

## Equações e símbolos matemáticos

As equações e símbolos matemáticos estão escritos usando a coleção de pacotes [AMS-LaTeX](http://www.ams.org/publications/authors/tex/amslatex). Para mais informações, recomendamos a leitura do seguinte documento:

ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf

## Organização do código fonte

O livro está escrito em [LaTex](https://latex-project.org/). O arquivo principal (`main.pdf`) escontra-se no diretório principal (`CalculoNumerico`). O código LaTeX de cada capítulo encontra-se em um subdiretório específico com nome `cap_abrev`, onde `abrev` é uma abreviação que lembre o conteúdo do capítulo. Por exemplo, o código do capítulo sobre técnicas numéricas para sistemas lineares está no subdiretório `cap_linsis`.

### Compatibilidade

O código fonte do livro deve perimitir sua compilação tanto com `latex` como com `pdflatex`. Ao adicionar suas colaborações, certifique-se que elas são compatíveis testando a compilação definida no `Makefile`. Para testar a compilação, use:

    $ make

e

    $ make dvi

### Capítulos

Dentro de cada subdiretório de um capítulo, por exemplo, `cap_foo` devem estar presentes todos os arquivos referentes ao texto deste. As imagens devem ser colocadas em no subdiretório `cap_foo/pics` e os códigos computacionais em `cap_foo/codes`. De preferência, deve-se criar um subdiretório para cada figura e código computacional. Quando possível, as figuras devem ser acompanhadas de seu código fonte.

### Figuras

Os arquivos das figuras devem ser fornecidos em formato `EPS` e armazenados no subdiretório `cap_foo/pics`, onde `cap_foo` é o diretório do capítulo que a figura pertence. As figuras devem ser fornecidas no tamanho desejado para o livro, i.e. evite definir o tamanho da figura no código LaTeX.


### Códigos computacionais

O livro deve ser versátil o suficiente para não depender de qualquer pacote computacional em específico. Para tanto, textos envolvendo algum pacote (ou alguma linguagem) computacional devem ser encapsulados dentro de uma declaração `se ... então`. Por exemplo, o texto:

    No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.

deve ser inserido no livro como:

    \ifisscilab
      No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.
    \fi

A declaração `isscilab` deve ser declarada como `True` ou `False` no preâmbulo (`preambulo.tex`) do arquivo LaTeX principal `main.tex`. Por exemplo, para declará-la `True` temos:

    \newif\ifisscilab
    \isscilabtrue
