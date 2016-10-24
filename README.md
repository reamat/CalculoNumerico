# Cálculo Numérico: Um Livro Colaborativo

Este é um livro colaborativo sobre tópicos de métodos e análise numérica normalmente estudados em cursos de graduação das áreas exatas e da terra na disciplina de cálculo numérico.

Caso queira colaborar, escreva para:

livro_colaborativo@googlegroups.com

Fork us on GitHub! O código fonte do livro está disponível no repositório GitHub:

https://github.com/livroscolaborativos/CalculoNumerico

## Licença
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## Sobre o código fonte
O código fonte está escrito em Latex e as referências bibliográficas em BibTex, testados em computador Linux com o pacote TexLive. O texto está em formatação **utf-8**.

## Compilando
O código LaTeX pode ser compilado com:

    $ make

Isto gera o livro em formato PDF (main.pdf), o qual é o formato principal. Também, o código pode ser compilado em formato DVI:

    $ make dvi

Alguma vezes a compilação pode gerar erros devido a incompatibilidade com antigos arquivos temporários. Para limpar os arquivos temporários gerados durante a compilação, digite:

    $ make clean

Alternativamente, o livro pode ser compilado com os comandos usuais `latex main`, `bibtex main`, `pdflatex main`, `makeindex main`. Lembrando que `main.tex` é o arquivo LaTeX principal.

### Outros formatos
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

## Colaborações
Todos são convidados a colaborarem na escrita deste livro. Caso esteja interessado, entre em contato conosco escrevendo para:

livro_colaborativo@googlegroups.com

### Fork us on GitHub
Colabore editando diretamente o código fonte disponível no repositório GitHub:

https://github.com/livroscolaborativos/CalculoNumerico

### Folha de estilo
Para colaborar de forma efetiva, leia nossa [folha de estilo](https://github.com/livroscolaborativos/CalculoNumerico/blob/master/FOLHA_DE_ESTILO.md).
