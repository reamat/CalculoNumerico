#Folha de Estilo

Este documento contém informações sobre os padrões de estilo de escrita e organização do livro colaborativo.

## Regionalização

O livro está escrito em língua portuguesa.

## Equações e símbolos matemáticos

As equações e símbolos matemáticos estão escritos usando a coleção de pacotes [AMS-LaTeX](http://www.ams.org/publications/authors/tex/amslatex). Para mais informações, recomendamos a leitura do seguinte documento:

ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf

## Organização do código fonte

O livro está escrito em [LaTex](https://latex-project.org/). O arquivo principal (`main.pdf`) escontra-se no diretório principal (`CalculoNumerico`). O código LaTeX de cada capítulo encontra-se em um subdiretório específico com nome `cap_abrev`, onde `abrev` é uma abreviação que lembre o conteúdo do capítulo. Por exemplo, o código do capítulo sobre técnicas numéricas para sistemas lineares está no subdiretório `cap_linsis`.

### Capítulos

Dentro de cada subdiretório de um capítulo, por exemplo, `cap_foo` devem estar presentes todos os arquivos referentes ao texto deste. As imagens devem ser colocadas em no subdiretório `cap_foo/pics` e os códigos computacionais em `cap_foo/codes`. De preferência, deve-se criar um subdiretório para cada figura e código computacional. Quando possível, as figuras devem ser acompanhadas de seu código fonte.

### Códigos computacionais

O livro deve ser versátil o suficiente para não depender de qualquer pacote computacional em específico. Para tanto, textos envolvendo algum pacote (ou alguma linguagem) computacional devem ser encapsulados dentro de uma declaração `se ... então`. Por exemplo, o texto:

    No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.

deve ser inserido no livro como:

    \ifiscilab
      No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.
    \fi

A declaração `isscilab` deve ser declarada como `True` ou `False` no preâmbulo (`preamble.tex`) do arquivo LaTeX principal `main.tex`. Por exemplo, para declará-la `True` temos:
    \newif\ifisscilab
    \isscilabtrue
