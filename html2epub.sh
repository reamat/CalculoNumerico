#/usr/bin/bash

mkdir -p ./.tmp1
rm -rf ./.tmp1/*

latex main 
bibtex main
latex main
latex main
htlatex main "ebook_config,html,2,notoc*" "" "-d./.tmp1/"
#rm -f main.knd


ebook-convert ./.tmp1/main.html $1 \
	      --title="Cálculo Numérico - Um Livro Colaborativo - Versão com Octave" \
	      --authors="Todos os Colaboradores"\
	      --cover="./rosto/cover-scilab.png"\
	      --comments="Para mais informações sobre este livro visite  http://www.ufrgs.br/numerico"




