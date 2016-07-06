#Este trabalho está licenciado sob a Licença Creative Commons Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-nc-sa/4.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

pdf: main.tex
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

dvi: main.tex
	latex main
	bibtex main
	latex main
	latex main

.PHONY: clean

clean:
	rm -f *.aux *.log *.out *.toc *.bbl
