# -*- coding: utf-8 -*-
import re
import codecs
import os

def dashrepl(matchobj): 
    return unichr(int(matchobj.group(1),16)) # python 2.7 use unichr, 
    # for python 3.3 use chr()

#f1 = open('rotationV13.tex', 'r')
f1 = codecs.open('rotationV14.tex', "r", "utf-8")
f2 = codecs.open('rotationV14uni.tex', "w", "utf-8")

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

f3 = open('rotationV14uni.tex', 'r')
f4 = open('preamble_remove.tex', "w")

for ind,line in enumerate(f3):
    if ind < 9:
#        print(line)
        pass
    else:
        f4.write(line)
f3.close()
f4.close()

f5 = open('preamble_remove.tex', "r")
f6 = open('rotationV14upa.tex', 'w')

new_preamble = [
"\documentclass[12pt,twoside]{article}\n",
"%\documentclass[12pt,a4paper]{article}\n",
"\usepackage{amsmath}\n",
"\usepackage{fontspec}\n",
"\usepackage{xeCJK}\n",
"\setmainfont{Times New Roman}\n",
"\setsansfont{Verdana}\n",
"\setmonofont{Courier New}\n",
"\setCJKmainfont[AutoFakeBold=1.5]{微軟正黑體}\n",
"\setCJKfamilyfont{kai}{標楷體}\n",
"\\newcommand*{\kai}{\CJKfamily{kai}}\n",
"\usepackage[inner=1in,outer=0.6in,top=0.7in,bottom=1in]{geometry}\n",
"\usepackage{unicode-math}\n",
"\usepackage{graphicx}\n",
"\usepackage[usenames,dvipsnames]{xcolor}\n",
"\usepackage[hidelinks]{hyperref}\n",
"\usepackage{pgf}\n",
"\usepackage{pstricks,pst-node,pst-3dplot}\n",
"\usepackage{minted}\n",
"\usepackage{pdfpages}\n",
"\usepackage{mdframed}\n",
"\usepackage{fancyhdr}\n",
"\pagestyle{fancy}\n",
"\\fancyhf{}\n",
"\\fancyfoot[LE,RO]{\\thepart-\\thepage}\n",
"\\renewcommand{\\headrulewidth}{0pt}\n",
"\\def\\mycleardoublepage#1{%\n",
"\\clearpage\n",
"\\null\\vfill\\hfill\\includegraphics[scale=0.3]{#1}%\n",
"\\cleardoublepage}\n",
]

for i in range(len(new_preamble)):
    f6.write(new_preamble[i])
    
for ind,line in enumerate(f5):
    f6.write(line)
    
f5.close()
f6.close()

os.remove('preamble_remove.tex')
os.remove('rotationV14uni.tex')

