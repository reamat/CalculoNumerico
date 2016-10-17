#/usr/bin/bash

make clean -C ..
make html -B -C ..

mkdir -p ./book_in_html
mkdir -p ./.tmp

rm -rf ./book_in_html/*
rm -rf ./.tmp/*

cp ../html/*.png ./book_in_html/
cp ../html/*.css ./book_in_html/

cd ../html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../webpage/.tmp/$file
done
cd ../webpage
python tbinsert.py



