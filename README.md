# Cálculo Numérico: Um Livro Colaborativo

Este é um livro colaborativo sobre tópicos de métodos e análise numérica normalmente estudados em cursos de graduação das áreas exatas e da terra na disciplina de cálculo numérico.

Caso queira colaborar, escreva para:

<livro_colaborativo@googlegroups.com>

Fork us on GitHub! O código fonte do livro está disponível no repositório GitHub:

<https://github.com/livroscolaborativos/CalculoNumerico>

Também disponibilizamos o e-mail de contato:

<livroscolaborativos@gmail.com>

## Licença
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite <https://creativecommons.org/licenses/by-sa/3.0/> ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## Sobre o código fonte
O código fonte está escrito em [Latex](https://latex-project.org/) e as referências bibliográficas em [BibTex](http://www.bibtex.org/), testado em computador Linux com o pacote [TexLive](http://www.tug.org/texlive/). O texto está em formatação **utf-8**.

## Compilando

### Em computador Linux
O código LaTeX está testado em computador [Linux](https://pt.wikipedia.org/wiki/Linux) com o pacote [TexLive](https://www.tug.org/texlive/) instalado. O livro pode ser compilado com:

    $ make

Isto gera o livro em formato PDF (main.pdf) na versão [Scilab](http://www.scilab.org/). Também, o código pode ser compilado em formato DVI:

    $ make dvi

Alguma vezes a compilação pode gerar erros devido a incompatibilidade com antigos arquivos temporários. Para limpar os arquivos temporários gerados durante a compilação, digite:

    $ make clean

Alternativamente, o livro pode ser compilado com os comandos usuais `latex main`, `bibtex main`, `pdflatex main`, `makeindex main`. Lembrando que `main.tex` é o arquivo LaTeX principal.

#### Outros formatos
O livro também pode ser compilado em formato slides, HTML e EPUB, digitando:

- Slides:

		$ make slide

Este comando cria o arquivo `slides.pdf` contendo o livro em formato de slides.

- HTML:

		$ make html

Este comando cria a pasta `./html` onde todo os arquivos da versão HTML do livro são colocados.

- EPUB:

		$ make epub

Este comando cria o arquivo `main.epub` contendo o livro em formato EPUB.

#### Outras versões

Atualmente, o livro também conta com versão [GNU Octave](https://www.gnu.org/software/octave/) e versão [Python](https://www.python.org/).

Para compilar o formato PDF da versão **GNU Octave** basta digitar:

    $ make pdf-oct

Similarmente, para compilar o formato PDF da versão **Python** basta digitar:

    $ make pdf-py

Use o comando análogo para compilar em outros formatos.

### Outros sistemas operacionais
O código LaTeX pode ser compilado em outros sistemas operacionais.

Em primeiro lugar, deve-se editar o arquivo de configuração `main.knd`. Este arquivo contém instruções TeX para controlar o formato e a versão do livro. Por exemplo, para setar o formato do livro em PDF na versão Scilab, garanta que este arquivo contenha o seguinte texto:

    \isbooktrue \isslidefalse \ishtmlfalse \isscilabtrue \isoctavefalse \ispythonfalse

Por fim, o livro pode ser compilado com a seguinte sequência de comandos:

    pdflatex main
    bibtex main
    makeindex main
    pdflatex main
    pdflatex main


## Colaborações
Há várias maneiras de colaborar com a escrita do livro. Toda a colaboração é bem vinda, seja ela um aviso de erro de digitação, uma reformulação de uma parte do livro, uma nova figura, uma nova seção ou um novo capítulo.

### Obtenha a sua versão
O código [LaTeX](http://www.latex-project.org/) livro está disponível no repositório GitHub:

<https://github.com/livroscolaborativos/CalculoNumerico>

No GitHub você pode fazer sua própria cópia do repositório, editá-la e, então, sugerir que sua cópia seja incorporada a versão oficial do projeto.

### Envie sua colaboração
Antes de requerer que sua colaboração seja incorporada a versão oficial do livro, verifique se ela está de acordo com nossa [folha de estilo](https://github.com/livroscolaborativos/CalculoNumerico/blob/master/FOLHA_DE_ESTILO.md).

Então, para requerer que suas contribuições no livro sejam incorporadas a versão oficial, faça um "New pull request" do seu "fork" do projeto no GitHub. Ao recebermos seu requerimento, o corpo de organizadores do livro irá analisar e decidir por incorporar por completo, parcialmente ou de forma modificada suas colaborações.

Os organizadores também podem decidir por negar por completo seu pedido de incorporação de suas contribuições na versão oficial do livro. Observe que mesmo neste caso, você construirá de posse de sua versão do livro e poderá usá-la e distribuí-la, dentro do previsto na licença CC-BY-SA 3.0 (veja a [licença](https://creativecommons.org/licenses/by-sa/3.0/)).

Observamos que somente será incorporado à versão oficial do livro material sob licença CC-BY-SA 3.0 (ou equivalente). Isto é, todo o material que deseja incorporar a versão oficial não poderá conter material sob violação de copyright e você deverá explicitamente declarar que está de acordo que seu material seja colocado sob a licença CC-BY-SA 3.0 (veja a [licença](https://creativecommons.org/licenses/by-sa/3.0/)).

Nós só poderemos incorporar suas colaborações à versão oficial do livro após você assinar os termos CLA. As instruções para assinatura dos termos será exibida na lista de discussão referente ao seu "Pull Request". Leia atentamente os termos. Qualquer dúvida sobre estes termos entre em contato pelo e-mail: <livroscolaborativos@gmail.com>

### Outras formas de colaboração
Toda a colaração é bem vinda! Caso tenha encontrado algum erro, imprecisão ou tenha alguma sugestão a fazer, escreva para nossa lista de e-mails:

<https://groups.google.com/forum/#!forum/livro_colaborativo>

Alternativamente, entre em contato pelo e-mail:

<livroscolaborativos@gmail.com>

### Aviso de violação de copyright
Caso encontre qualquer violação de copyright em qualquer parte do material do livro, por favor, nos informe pelo e-mail:

<livroscolaborativos@gmail.com>

ou pela lista de e-mails:

<https://groups.google.com/forum/#!forum/livro_colaborativo>

Iremos cuidar para analisar seu aviso o mais prontamente possível e removeremos o material que não esteja de acordo com a licença [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
