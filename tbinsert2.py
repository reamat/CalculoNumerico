#/usr/bin/python
# -*- coding: utf-8 -*-

import os
from os import walk
import numpy as np
import string

sdirname = "./tmp/"

lfiles = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    lfiles.extend (filenames)
    break

for index, f in enumerate (lfiles):
    lfiles[index] = os.path.splitext(f)[0]
print("Source files: ", lfiles)

for index, f in enumerate (lfiles):
    print ("Changing %s file." % (f))
    ifile = open("./tmp/"+f+".html", "r")
    ofile = open("./book_in_webpage/"+f+".html", "w")

    text = ifile.read()

    #replace meta charset
    text = text.replace("iso-8859-1","utf-8")
    
    #include head
    head_aux_file = open("head_aux.html", "r")
    head_include = head_aux_file.read()
    
    #get chapterHead or sectionHead to include in <meta> keywords
    s=-1
    e=-1
    s = text.find('<h2 class="chapterHead">')
    if (s != -1):
        auxText = text[s:]
        s = auxText.find('</a>')+4
        e = auxText.index('</h2>')
        kw = auxText[s:e]
    else:
        s = text.find('<h3 class="sectionHead">')
        if (s != -1):
            auxText = text[s:]
            s = auxText.find('</a>')+4
            e = auxText.index('</h3>')
            kw = auxText[s:e]
        else:
            kw = []
    head1 = "<meta name='keywords' content='"
    head1 += "Livro, Cálculo Numérico, Métodos, Análise"
    if (len(kw) != 0):
        head1 += ", " + kw 
    head1 += "'>\n"
    head_include = head1 + head_include;
    
    text = text.replace("</head><body \n>", head_include)

    #include on bottom
    bottom_aux_file = open("bottom_aux.html", "r")
    bottom_include = bottom_aux_file.read()
    text = text.replace("</body></html>", bottom_include)

    ofile.write(text)
    ifile.close ()
    ofile.close ()
    head_aux_file.close()
    bottom_aux_file.close()

#change main.css
ifile = open("./book_in_webpage/main.css",'r')
bookfile = open("book.css",'r')
ofile = open("./book_in_webpage/new_main.css",'w')

for line in bookfile:
    ofile.write (line)
for line in ifile:
    ofile.write (line)

ifile.close ()
bookfile.close ()
ofile.close ()
