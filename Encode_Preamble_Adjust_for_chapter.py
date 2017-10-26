# -*- coding: utf-8 -*-
import re
import codecs
import os
import sys


def dashrepl(matchobj): 
    return unichr(int(matchobj.group(1),16)) # python 2.7 use unichr, 
    # for python 3.3 use chr()

filename = "Chapter_" + sys.argv[1]

print filename

#filename = 'Chapter_Program'
#filename = 'Chapter_Case_Study'
#filename = 'Chapter_Orientation_Estimation'

f1 = codecs.open( filename + ".tex", "r", "utf-8")
f2 = codecs.open(filename +"_uni" + ".tex", "w", "utf-8")

#f1 = open('coinrotationV1.tex', 'r')
#f2 = codecs.open('coinrotationV1uni.tex', "w", "utf-8")

#f1 = open('Taiwanese-English-dicV1.tex', 'r')
#f2 = codecs.open('Taiwanese-English-dicV1uni.tex', "w", "utf-8")



p= re.compile(r"\\U{([\w]{,4})}")
for line in f1:
    m = re.sub(p,dashrepl,line)
##    print(m)
    f2.write(m)
f1.close()
f2.close()


##def dashrepl(matchobj):
##    return chr(int(matchobj.group(1),16))
##
##p= re.compile(r"\\U{([\w]{,4})}")
##teststring =r"\U{9019}\U{88e1}\U{5c07}\U{9640}\U{87ba}\U{7684}\U{904b}\U{52d5}\U{5206}"
##
##m = re.sub(p,dashrepl,teststring)
##print(m)

f3 = open(filename +"_uni" + ".tex", 'r')
f4 = open('preamble_remove.tex', "w")

for ind,line in enumerate(f3):
    if ind < 2:
#        print(line)
        pass
    else:
        f4.write(line)

f4.write("\\end{document}")#for last line

f3.close()
f4.close()

f5 = open('preamble_remove.tex', "r")
f6 = open(filename +"_upa" + ".tex", 'w')

new_preamble = [
"\documentclass[12pt,twoside]{article}\n",
"\usepackage{gyro_chapter_style}\n",
"\\begin{document}\n",
]

for i in range(len(new_preamble)):
    f6.write(new_preamble[i])
    
for ind,line in enumerate(f5):
    f6.write(line)
    
f5.close()
f6.close()

os.remove('preamble_remove.tex')

print "***  Successfully create uni and upa files.  ***"
#os.remove(filename +"_uni" + ".tex")

