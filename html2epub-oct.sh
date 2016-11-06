#/usr/bin/bash

make clean

mkdir -p ./.tmp1
rm -rf ./.tmp1/*


#echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabfalse \isoctavetrue" > main.knd
cat main-oct.knd > main.knd
latex main 
bibtex main
latex main
latex main
htlatex main "ebook_config,html,2,notoc*,info" "" "-d./.tmp1/"
rm -f main.knd


ebook-convert ./.tmp1/main.html main-oct.epub \
	      --title="Cálculo Numérico - Um Livro Colaborativo" \
	      --authors="Todos os Colaboradores"\
	      --cover="./rosto/cover-oct.png"\
	      --comments="Para mais informações sobre este livro visite  http://www.ufrgs.br/numerico"




