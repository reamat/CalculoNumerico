#/usr/bin/python

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
    
    #include on head
    head_aux_file = open("head_aux.html", "r")
    head_include = head_aux_file.read()
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
