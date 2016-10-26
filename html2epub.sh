#/usr/bin/bash

make clean

mkdir -p ./.tmp1
rm -rf ./.tmp1/*

echo "\isbookfalse \isslidefalse \ishtmltrue \isscilabtrue \isoctavefalse" > main.knd
latex main 
bibtex main
latex main
latex main
htlatex main "ebook_config,html,3,notoc*,info" "" "-d./.tmp1/"
rm -f main.knd


ebook-convert ./.tmp1/main.html main.epub \
	      --title="Cálculo Numérico - Um Livro Colaborativo" \
	      --authors="Todos os Colaboradores"\
	      --cover="./rosto/cover.png"\
	      --comments="Para mais informações sobre este livro visite  http://www.ufrgs.br/numerico"




