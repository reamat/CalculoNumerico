#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite https://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

########################################
#
# ATENÇÃO
#
# POR SEGURANÇA, NÃO EDITE ESTE ARQUIVO.
#
########################################

CAP1=cap_aritmetica
CAP3=cap_equacao1d
CAP4=cap_intro
CAP5=cap_linsis
CAP6=cap_nlinsis
CAP7=cap_pvi
CAP8=cap_scilab
CAP9=cap_interp
CAP10=cap_ajuste
CAP11=cap_derivacao
CAP12=cap_integracao
CAP13=cap_pvc
CAP14=cap_python
CAP15=cap_octave

########################################
# FORMATO LIVRO PDF
########################################

pdf: main.tex
	cp config-pdf-sci.knd config.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main

pdf-sci: main.tex
	cp config-pdf-sci.knd config.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main

pdf-py: main.tex
	cp config-pdf-py.knd config.knd
	cp main.tex main-py.tex
	pdflatex main-py
	bibtex main-py
	makeindex main-py
	pdflatex main-py
	pdflatex main-py
	cp config-pdf-sci.knd config.knd

pdf-oct: main.tex
	cp config-pdf-oct.knd config.knd
	cp main.tex main-oct.tex
	pdflatex main-oct
	bibtex main-oct
	makeindex main-oct
	pdflatex main-oct
	pdflatex main-oct
	cp config-pdf-sci.knd config.knd

########################################
# FORMATO LIVRO DVI
########################################

dvi: main.tex
	cp config-pdf-sci.knd config.knd
	latex main
	bibtex main
	makeindex main
	latex main
	latex main
	cp config-pdf-sci.knd config.knd

dvi-py: main.tex
	cp config-pdf-py.knd config.knd
	cp main.tex main-py.tex
	latex main-py
	bibtex main-py
	makeindex main-py
	latex main-py
	latex main-py
	cp config-pdf-sci.knd config.knd

dvi-oct: main.tex
	cp config-pdf-oct.knd config.knd
	cp main.tex main-oct.tex
	latex main-oct
	bibtex main-oct
	makeindex main-oct
	latex main-oct
	latex main-oct
	cp config-pdf-sci.knd config.knd


########################################
# FORMADO SLIDES PDF
########################################

slide: main.tex
	cp config-slide-sci.knd config.knd
	cp main.tex slide.tex
	pdflatex slide
	bibtex slide
	makeindex slide
	pdflatex slide
	pdflatex slide
	cp config-pdf-sci.knd config.knd

slide-oct: main.tex
	cp config-slide-oct.knd config.knd
	cp main.tex slide-oct.tex
	pdflatex slide-oct
	bibtex slide-oct
	makeindex slide-oct
	pdflatex slide-oct
	pdflatex slide-oct
	cp config-pdf-sci.knd config.knd

slide-py: main.tex
	cp config-slide-py.knd config.knd
	cp main.tex slide-py.tex
	pdflatex slide-py
	bibtex slide-py
	makeindex slide-py
	pdflatex slide-py
	pdflatex slide-py
	cp config-pdf-sci.knd config.knd


########################################
# FORMATO HTML
########################################

html: main-sci.html

html-oct: main-oct.html

html-py: main-py.html

main-sci.html: main.tex
	cp config-html-sci.knd config.knd
	mkdir -p ./html-sci
	rm -f ./html-sci/*
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "myconfig,3,notoc*" " -cunihtf" "-d./html-sci/"
#	mk4ht htlatex main "myconfig,3,notoc*" "" "-d./html/"
	cp config-pdf-sci.knd config.knd

main-oct.html: main.tex
	cp config-html-oct.knd config.knd
	mkdir -p ./html-oct
	rm -f ./html-oct/*
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "myconfig,3,notoc*" " -cunihtf" "-d./html-oct/"
#	mk4ht htlatex main "myconfig,3,notoc*" "" "-d./html-oct/"
	cp config-pdf-sci.knd config.knd

main-py.html: main.tex
	cp config-html-py.knd config.knd
	mkdir -p ./html-py
	rm -f ./html-py/*
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "myconfig,3,notoc*" " -cunihtf" "-d./html-py/"
	mk4ht htlatex main "myconfig,3,notoc*" "" "-d./html-py/"
	cp config-pdf-sci.knd config.knd

########################################
# FORMATO EPUB
########################################

epub: main.tex
	mkdir -p ./.tmp1
	rm -rf ./.tmp1/*
	cp config-html-sci.knd config.knd
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "ebook_config,html,2,notoc*" "" "-d./.tmp1/"
	cp config-pdf-sci.knd config.knd


	ebook-convert ./.tmp1/main.html main.epub \
	      --authors="Todos os Colaboradores"\
              --cover=./rosto/cover-scilab-epub.png\
	      --comments="Para mais informações sobre este livro visite  https://www.ufrgs.br/reamat/CalculoNumerico"

epub-oct: main.tex
	mkdir -p ./.tmp1
	rm -rf ./.tmp1/*
	cp config-html-oct.knd config.knd
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "ebook_config,html,2,notoc*" "" "-d./.tmp1/"
	cp config-pdf-sci.knd config.knd


	ebook-convert ./.tmp1/main.html main-oct.epub \
	      --authors="Todos os Colaboradores"\
	      --comments="Para mais informações sobre este livro visite  https://www.ufrgs.br/reamat/CalculoNumerico"

epub-py: main.tex
	mkdir -p ./.tmp1
	rm -rf ./.tmp1/*
	cp config-html-py.knd config.knd
	latex main
	bibtex main
	latex main
	latex main
	htlatex main "ebook_config,html,2,notoc*" "" "-d./.tmp1/"
	cp config-pdf-sci.knd config.knd


	ebook-convert ./.tmp1/main.html main-py.epub \
	      --authors="Todos os Colaboradores"\
              --cover=./rosto/cover-python-epub.png\
	      --comments="Para mais informações sobre este livro visite  https://www.ufrgs.br/reamat/CalculoNumerico"


########################################
# TODOS AS VERSÕES EM FORMATO PDF
########################################

all-pdf: main.tex
	make clean
	make pdf
	make clean
	make pdf-py
	make clean
	make pdf-oct

########################################
# TODOS AS VERSÕES EM FORMATO Slide
########################################

all-slide: main.tex
	make clean
	make slide
	make clean
	make slide-py
	make clean
	make slide-oct

########################################
# TODOS OS FORMATOS
########################################

all: main.tex
	make clean
	make pdf
	make clean
	make slide
	make clean
	make dvi
	make clean
	make html
	make clean
	make epub

all-oct: main.tex
	make clean
	make pdf-oct
	make clean
	make slide-oct
	make clean
	make dvi-oct
	make clean
	make html-oct
	make clean
	make epub-oct

all-py: main.tex
	make clean
	make pdf-py
	make clean
	make slide-py
	make clean
	make dvi-py
	make clean
	make html-py
	make clean
	make epub-py

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.bbl \
		*.idx *.ilg *.ind *.blg *.backup \
		*.4tc *.lg *.tmp *.xref *.png *.html \
		*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
		*.xml main-oct.tex main-py.tex
	rm -f ${CAP1}/*.aux ${CAP1}/*.log ${CAP1}/*.backup
	rm -f ${CAP2}/*.aux ${CAP2}/*.log ${CAP2}/*.backup
	rm -f ${CAP3}/*.aux ${CAP3}/*.log ${CAP3}/*.backup
	rm -f ${CAP4}/*.aux ${CAP4}/*.log ${CAP4}/*.backup
	rm -f ${CAP5}/*.aux ${CAP5}/*.log ${CAP5}/*.backup
	rm -f ${CAP6}/*.aux ${CAP6}/*.log ${CAP6}/*.backup
	rm -f ${CAP7}/*.aux ${CAP7}/*.log ${CAP7}/*.backup
	rm -f ${CAP8}/*.aux ${CAP8}/*.log ${CAP8}/*.backup
	rm -f ${CAP9}/*.aux ${CAP9}/*.log ${CAP9}/*.backup
	rm -f ${CAP10}/*.aux ${CAP10}/*.log ${CAP10}/*.backup
	rm -f ${CAP11}/*.aux ${CAP11}/*.log ${CAP11}/*.backup
	rm -f ${CAP12}/*.aux ${CAP12}/*.log ${CAP12}/*.backup
	rm -f ${CAP13}/*.aux ${CAP13}/*.log ${CAP13}/*.backup
	rm -f ${CAP14}/*.aux ${CAP14}/*.log ${CAP14}/*.backup
	rm -f ${CAP15}/*.aux ${CAP15}/*.log ${CAP15}/*.backup


########################################
# 	EXTRAI EXERCÍCIOS
########################################


exer-sci:
	make clean
	cp config-pdf-sci.knd config.knd
	python3 extrai_exercicios.py sci
	latex main
	latex exercicios-sci
	latex exercicios_resolvidos-sci
	latex exercicios_todos-sci
	pdflatex exercicios-sci
	pdflatex exercicios_resolvidos-sci
	pdflatex exercicios_todos-sci

exer-py:
	make clean
	cp config-pdf-py.knd config.knd
	python3 extrai_exercicios.py py
	latex main
	latex exercicios-py
	latex exercicios_resolvidos-py
	latex exercicios_todos-py
	pdflatex exercicios-py
	pdflatex exercicios_resolvidos-py
	pdflatex exercicios_todos-py

exer-oct:
	make clean
	cp config-pdf-oct.knd config.knd
	python3 extrai_exercicios.py oct
	latex main
	latex exercicios-oct
	latex exercicios_resolvidos-oct
	latex exercicios_todos-oct
	pdflatex exercicios-oct
	pdflatex exercicios_resolvidos-oct
	pdflatex exercicios_todos-oct
