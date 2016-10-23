#/usr/bin/bash

make clean

mkdir -p ./.tmp1
rm -rf ./.tmp1/*

#mkdir -p ./.tmp2
#rm -rf ./.tmp2/*

latex main 
bibtex main
latex main
latex main
htlatex main "ebook_config,html,3,notoc*,info" "" "-d./.tmp1/"

##change encoding to utf-8
#cd ./.tmp1
#for file in *.html; do
#    iconv -f iso-8859-1 -t utf8 $file -o ../.tmp2/$file
#done

#cd ../
#cp ./.tmp1/*.png ./.tmp2/
#cp ./.tmp1/*.css ./.tmp2/

ebook-convert ./.tmp1/main.html main.epub \
	      --title="Cálculo Numérico - Um Livro Colaborativo" \
	      --authors="Todos os Colaboradores"\
	      --cover="./rosto/cover.png"\
	      --comments="Para mais informações sobre este livro visite  http://www.ufrgs.br/numerico"




