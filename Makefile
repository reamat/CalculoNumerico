#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

CAP1=cap_aritmetica
CAP2=cap_derint
CAP3=cap_equacao1d
CAP4=cap_intro
CAP5=cap_linsis
CAP6=cap_nlinsis
CAP7=cap_pvi
CAP8=cap_scilab

pdf: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabtrue \isoctavefalse" > main.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main
	rm -f main.knd

slide: main.tex
	echo "\isbookfalse \isslidetrue \ishtmlfalse \isscilabtrue \isoctavefalse" > main.knd
	cp main.tex slide.tex
	pdflatex slide
	bibtex slide
	makeindex slide
	pdflatex slide
	pdflatex slide
	rm -f main.knd

dvi: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabtrue \isoctavefalse" > main.knd
	latex main
	bibtex main
	makeindex main
	latex main
	latex main
	rm -f main.knd

html: main.tex
	rm -f ./html/*
	echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabtrue \isoctavefalse" > main.knd
	latex main 
	bibtex main
	latex main
	latex main
	htlatex main "myconfig,html,3,notoc*,info" "" "-d./html/"
	rm -f main.knd

epub: ./html/main.html
	./html2epub.sh

pdf-oct: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	pdflatex main
	bibtex main
	makeindex main
	pdflatex main
	pdflatex main
	rm -f main.knd

slide-oct: main.tex
	echo "\isbookfalse \isslidetrue \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	cp main.tex slide.tex
	pdflatex slide
	bibtex slide
	makeindex slide
	pdflatex slide
	pdflatex slide
	rm -f main.knd

dvi-oct: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	latex main
	bibtex main
	makeindex main
	latex main
	latex main
	rm -f main.knd

html-oct: main.tex
	rm -f ./html/*
	echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabfalse \isoctavetrue" > main.knd
	latex main 
	bibtex main
	latex main
	latex main
	htlatex main "myconfig,html,3,notoc*,info" "" "-d./html/"
	rm -f main.knd

epub-oct: ./html/main.html
	./html2epub-oct.sh

all: main.tex
	make clean
	make pdf
	make clean
	make slide
	make clean
	make dvi
	make clean
	make html -B
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
	make html-oct -B
	make clean
	make epub-oct

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.bbl \
		*.idx *.ilg *.ind *.blg *.backup \
		*.4tc *.lg *.tmp *.xref *.png *.html
	rm -f ${CAP1}/*.aux ${CAP1}/*.log ${CAP1}/*.backup
	rm -f ${CAP2}/*.aux ${CAP2}/*.log ${CAP2}/*.backup
	rm -f ${CAP3}/*.aux ${CAP3}/*.log ${CAP3}/*.backup
	rm -f ${CAP4}/*.aux ${CAP4}/*.log ${CAP4}/*.backup
	rm -f ${CAP5}/*.aux ${CAP5}/*.log ${CAP5}/*.backup
	rm -f ${CAP6}/*.aux ${CAP6}/*.log ${CAP6}/*.backup
	rm -f ${CAP7}/*.aux ${CAP7}/*.log ${CAP7}/*.backup
	rm -f ${CAP8}/*.aux ${CAP8}/*.log ${CAP8}/*.backup
