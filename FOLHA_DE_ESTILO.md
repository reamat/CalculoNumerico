# Folha de estilo

Este documento contém informações sobre os padrões de estilo de escrita e organização do livro colaborativo. Antes de submeter uma colaboração, verifique que seu trabalho está de acordo com todos os pontos observados nesta folha de estilo.

Estamos muito mais interessados em melhorar o conteúdo do livro (tando em qualidade como em quantidade) e menos interessados em melhorar a sua estética. Portanto, busque manter o código LaTeX o mais simples possível buscando potencializar a colaboração de outras pessoas e de forma a se obter um resultado que permita uma leitura objetiva e agradável do livro.

Qualquer dúvida, escreva em nossa lista de discussão:

<livro_colaborativo@googlegroups.com>

## Regionalização e Estilo de Escrita

O livro está escrito em língua portuguesa, seguindo os costumes linguísticos brasileiros. Dá-se prioridade à ortografia prevista no Acordo Ortográfico de 1990.

### Capitalização de nomes de métodos

Deve-se usar maiúscula apenas em nomes próprios, ex: método de Newton, métodos dos mínimos quadrados.


## Código fonte LaTeX

O livro está escrito em [LaTex](https://latex-project.org/). O arquivo principal `main.tex` encontra-se no diretório principal `CalculoNumerico`. O código LaTeX de cada capítulo encontra-se em um subdiretório específico com nome `cap_abrev`, onde `abrev` é uma abreviação que lembre o conteúdo do capítulo. Por exemplo, o código do capítulo sobre técnicas numéricas para sistemas lineares está no subdiretório `cap_linsis`.

Para informações sobre como compilar o código fonte, leia o arquivo `README.md`.

### Compatibilidade

O código LaTeX do livro deve permitir sua compilação tanto com `latex` como com `pdflatex`, além de permitir a compilação nos formatos HTML e EPUB. Ao adicionar suas colaborações, certifique-se que elas são compatíveis testando a compilação definida no `Makefile`. Para testar a compilação, use:

    $ make

e

    $ make dvi

Para testar a compilação de todos os formatos disponíveis, digite:

    $ make all

ATENÇÃO: a compilação de todos os formatos pode levar vários minutos!

#### Instruções LaTeX não compatíveis

Fazemos a conversão do livro de código LaTeX para HTML usando o pacote [TeX4ht](https://www.tug.org/tex4ht/). Os ambientes matemáticos são convertidos para [MathMl](https://www.w3.org/Math/) e então renderizados usando [MathJax](https://www.mathjax.org/). Para que a conversão funcione de forma apropriada deve-se observar as seguintes questões:

* Não usar o ambiente `align`: no lugar use o ambiente `eqnarray` ou o `split` dentro de um ambiente `equation`.

* Não usar `array` para composição de tabelas. A alternativa é usar o ambiente `tabular`, por exemplo:

        \begin{center}
	  \begin{tabular}{r|c|c}
	    $h$ & $Df(1)$ & $|f'(1) - D_{+,h}F(1)|$ \\ \hline
            $10^{-1}$ & $-8,67062\E-01$ & $2,55909\E-02$\\
            $10^{-2}$ & $-8,44158\E-01$ & $2,68746\E-03$\\
            $10^{-14}$ & $-8,43769\E-01$ & $2,29851\E-03$ \\\hline
	  \end{tabular}
	\end{center}

* Não colocar `label` dentro de colchetes.

### Capítulos

Dentro de cada subdiretório de um capítulo, por exemplo  `cap_foo`, devem estar presentes todos os arquivos referentes ao texto deste. As imagens devem ser colocadas no subdiretório `cap_foo/pics` e os códigos computacionais em `cap_foo/codes`. De preferência, deve-se criar um subdiretório para cada figura e código computacional. Quando possível, as figuras devem ser acompanhadas de seu código fonte.

### Figuras

Os arquivos das figuras devem ser fornecidos em formato `EPS` e `PNG` sendo armazenados no subdiretório `cap_foo/pics`, onde `cap_foo` é o diretório do capítulo que a figura pertence. As figuras devem ser fornecidas no tamanho desejado para o livro, i.e. evite definir o tamanho da figura no código LaTeX. Para uma vizualização conformável em celulares, recomendamos que a figura tenha largura inferior a 320px.

A inclusão de uma figura no código LaTex deve ser feita da seguinte forma:

    \begin{figure}
        \centering
	    \includegraphics{cap_foo/pics/picfoo}
		\caption{Descrição da figura picfoo.}
		\label{pic:picfoo}
	\end{figure}

Não insira figuras dentro de outros ambientes como, por exemplo, `ex`, `teo`, `sol` e outros.

Sempre que possível, forneça o código fonte da figura armazenando-o na pasta `cap_foo/pics/picfoo`. Nesta mesma pasta, crie um arquivo README.md com uma descrição da figura e a linceça da mesma, a qual deve ser compatível com a CC-BY-SA 3.0.

Veja, por exemplo, `.cap_equacao1d/pics/ex_metodo_da_bissecao`.

### Códigos computacionais

O livro deve ser versátil o suficiente para não depender de qualquer pacote computacional em específico. Para tanto, textos envolvendo algum pacote (ou alguma linguagem) computacional devem ser encapsulados dentro de uma declaração `se ... então`. Por exemplo, o texto:

    No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.

deve ser inserido no livro como:

    \ifisscilab
      No Scilab, \verb+%eps+ fornece o $\epsilon$ de máquina.
    \fi

Em breve iremos disponibilizar mais informações sobre como gerar uma versão do livro com outras linguagens computacionais.

### Equações e símbolos matemáticos

As equações e símbolos matemáticos estão escritos usando a coleção de pacotes [AMS-LaTeX](http://www.ams.org/publications/authors/tex/amslatex).

#### Uso da vírgula

O livro usa o pacote LaTeX [`icomma`](https://www.ctan.org/pkg/icomma). Desta forma, para que um espaço apareça após uma vírgula é necessário por o espaço no código LaTeX. Por exemplo, o código LaTeX `$1,24$` produz o número 1,24, enquanto o código `$1, 24$` porduz os números 1 e 24 separados por uma vírgula e um espaço.

#### Números em notação científica

Números em notação científica podem ser representados, tando usando `$\times 10^$` como usando o macro `\E`, por exemplo:

    1,25673\times 10^{-13} = 1,25673\E-13.

### Exercícios

O livro conta com três tipos de exercícios, os chamados: Exercícios Resolvidos, Exercícios e Exercícios Finais.

#### Exercícios resolvidos

Exercícios resolvidos são exercícios com resolução completa. Eles devem ser colocados em subseção da seção a que se referem. A subseção deve ser não numerada e intitulada "Exercícios Resolvidos" , i.e.:

    \subsection*{Exercícios Resolvidos}

O enunciado de um exercício resolvido  deve ser colocado dentro de um ambiente `exeresol` como, por exemplo:

    \begin{exeresol}
	    Escreva aqui o enunciado do exercício resolvido.
    \end{exersol}

A resolução do exercício deve ser colocada dentro de um ambiente `resol`, colocado logo abaixo do `\end{exeresol}`, por exemplo:

    \begin{resol}
	    Escreva aqui a resolução completa (detalhada) do exercício.
	\end{resol}

#### Exercícios

Exercícios com resposta ou sem devem ser colocados em subseção da seção a que se referem. A subseção deve ser não numerada e intitulada "Exercícios", i.e.:

    \subsection*{Exercícios}

O enunciado de um exercício com resposta ou sem deve ser colocado dentro de um ambiente `exer` como, por exemplo:

    \begin{exer}
	   Escreva aqui o enunciado do exercício com resposta ou sem.
	\end{exer}

Caso o exercício tenha resposta (final, para resolução completa, veja a subsecção Exercícios Resolvidos) ela deve ser colocado em um ambiente `resp` logo abaixo do ambiente ao qual o exercício se refere como, por exemplo:

    \begin{resp}
	   Escreva aqui a resposta do exercício.
	\end{resp}
