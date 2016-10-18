#/usr/bin/bash

#make clean -C ..
#make html -B -C ..

rm -rf ./book_in_webpage/*
rm -rf ./tmp/*

cp ./book_in_html/*.png ./book_in_webpage/
cp ./book_in_html/*.css ./book_in_webpage/

#change encoding to utf-8
cd ./book_in_html
for file in *.html; do
    iconv -f iso-8859-1 -t utf8 $file -o ../tmp/$file
done

cd ..
ls
#python tbinsert.py
python tbinsert2.py



