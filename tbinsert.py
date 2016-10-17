#/usr/bin/python

import os
from os import walk
import numpy as np

sdirname = "./tmp/"

lfiles = []
for (dirpath, dirnames, filenames) in walk (sdirname):
    lfiles.extend (filenames)
    break

for index, f in enumerate (lfiles):
    lfiles[index] = os.path.splitext(f)[0]
print "Source files: ", lfiles

for index, f in enumerate (lfiles):
    print ("Changing %s file." % (f))
    ifile = open("./tmp/"+f+".html", "r")
    headfile = open("head_aux.html", "r")
    bottomfile = open("bottom_aux.html", "r")
    ofile = open("./book_in_webpage/"+f+".html", "w")
    atTop = False
    atBottom = False

    #insert head
    for line in headfile:
        ofile.write (line)
    ofile.write("\n")
    ofile.write("\n")

    write1 = False
    write2 = False
    for line in ifile:
        if (write2):
            if (line[0:14] == "</body></html>"):
                break
            else:
                ofile.write (line)
        if (write1):
            write2 = True
        if (line[0:12] == "</head><body"):
            write1 = True

    for line in bottomfile:
        ofile.write (line)
        
    ifile.close ()
    ofile.close ()
    headfile.close ()
    bottomfile.close ()

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
