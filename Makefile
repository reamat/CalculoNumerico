#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

CAP1=cap_aritmetica
CAP2=cap_derint
CAP3=cap_equacao1d
CAP4=cap_intro
CAP5=cap_linsis
CAP6=cap_nlinsis
CAP7=cap_pvi
CAP8=cap_scilab
CAP9=cap_interp
CAP10=cap_ajuste

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

html: main.html

main.html: main.tex
	rm -f ./html/*
	echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabtrue \isoctavefalse" > main.knd
	latex main
	bibtex main
	latex main
	latex main
	mk4ht htlatex main "myconfig,html,3,notoc*,info" "" "-d./html/"
	rm -f main.knd

epub: ./html/main.html
	./html2epub.sh

pdf-oct: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	cp main.tex main-oct.tex
	pdflatex main-oct
	bibtex main-oct
	makeindex main-oct
	pdflatex main-oct
	pdflatex main-oct
	rm -f main.knd

slide-oct: main.tex
	echo "\isbookfalse \isslidetrue \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	cp main.tex slide-oct.tex
	pdflatex slide-oct
	bibtex slide-oct
	makeindex slide-oct
	pdflatex slide-oct
	pdflatex slide-oct
	rm -f main.knd

dvi-oct: main.tex
	echo "\isbooktrue \isslidefalse \ishtmlfalse \isscilabfalse \isoctavetrue" > main.knd
	cp main.tex main-oct.tex
	latex main-oct
	bibtex main-oct
	makeindex main-oct
	latex main-oct
	latex main-oct
	rm -f main.knd

html-oct: main.tex
	mkdir -p ./html-oct
	rm -f ./html-oct/*
	echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabfalse \isoctavetrue" > main.knd
	latex main
	bibtex main
	latex main
	latex main
	mk4ht htlatex main "myconfig,html,3,notoc*,info" "" "-d./html-oct/"
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

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.bbl \
		*.idx *.ilg *.ind *.blg *.backup \
		*.4tc *.lg *.tmp *.xref *.png *.html \
		*.4ct *.css *.idv *.maf *.mtc *.mtc0 \
		*.xml
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
