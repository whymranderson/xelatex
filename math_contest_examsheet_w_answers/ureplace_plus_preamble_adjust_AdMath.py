# -*- coding: utf-8 -*-
import re
import codecs
import os

def dashrepl(matchobj): 
    return unichr(int(matchobj.group(1),16)) # python 2.7 use unichr, 
    # for python 3.3 use chr()
    
file = 'combine.tex'
file_uni = 'combine_uni.tex'
file_upa = 'combine_upa.tex'

#f1 = open('rotationV13.tex', 'r')
f1 = open(file, 'r')
f2 = codecs.open(file_uni, "w", "utf-8")

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

f3 = open(file_uni, 'r')
f4 = open('temp_preamble_remove.tex', "w")

for ind,line in enumerate(f3):
    if ind < 36:
#        print(line)
        pass
    else:
        f4.write(line)
f3.close()
f4.close()

f5 = open('temp_preamble_remove.tex', "r")
f6 = open(file_upa, 'w')

new_preamble = [
"\documentclass[12pt]{article}\n",
"\usepackage[inner=0.75 in,outer=0.75in]{geometry}\n",
"\usepackage{xeCJK}\n",
"\setmainfont{Times New Roman}\n",
"\setsansfont{Verdana}\n",
"\setmonofont{Courier New}\n",
"\setCJKmainfont{微軟正黑體}\n",
"\usepackage{eso-pic}\n",
"\usepackage{graphicx}\n",
"\usepackage{lipsum}\n",
"\usepackage{color}\n",
"\usepackage{pstricks}\n",
#"\usepackage[colorlinks]{hyperref}\n",
]

for i in range(len(new_preamble)):
    f6.write(new_preamble[i])
    
for ind,line in enumerate(f5):
    f6.write(line)
    
f5.close()
f6.close()

os.remove('temp_preamble_remove.tex')
os.remove(file_uni)

