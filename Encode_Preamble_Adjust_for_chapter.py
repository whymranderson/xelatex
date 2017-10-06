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
"%\documentclass[12pt,a4paper]{article}\n",
"\usepackage{amsmath}\n",
#"\usepackage{fontspec}\n",
"\usepackage{standalone}\n",

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
"\usepackage[hidelinks,colorlinks]{hyperref}\n",
"\usepackage{pgf}\n",
"\usepackage{pstricks,pst-node,pst-3dplot}\n",
"\usepackage{minted}\n",
"\usepackage{pdfpages}\n",
"\usepackage{mdframed}\n",

"\usepackage{everyshi}\n",
"\\newcounter{xpage}\stepcounter{xpage}\n",
"\EveryShipout{\stepcounter{xpage}}\n",

"\usepackage{fancyhdr}\n",
"\pagestyle{fancy}\n",
"\\fancyhf{}\n",
#"\\newcounter{partpage}[part]\n",
"\\fancyfoot[LE,RO]{\\thepart-\\thepage}\n",
"\\renewcommand{\\headrulewidth}{0pt}\n",
"\\def\\mycleardoublepage#1{%\n",
"\\cleardoublepage}\n",
"\\makeatletter\n",
"\\def\\emptypage@emptypage{%\n",
"    \\hbox{}%\n",
"     \\vspace*{\\fill}\n",
"     \\begin{center}\n",
"     \\includegraphics[width=0.5\\textwidth]{./figs/two_gyro_logo.png}\n",
"     \\end{center}\n",
"     \\vspace{\\fill}\n",
"     \\newpage%    \n",
"}%\n",
"\\def\\cleardoublepage{%\n",
"        \\clearpage%\n",
"        \\if@twoside%\n",
"            \\ifodd\\c@page%\n",
"                % do nothing\n",
"            \\else%\n",
"                \\emptypage@emptypage%\n",
"            \\fi%\n",
"        \\fi%\n",
"    }%\n",
"\\makeatother\n",
"\\setcounter{secnumdepth}{0}",
"\\newtheorem{theorem}{Theorem}\n",
"\\newtheorem{case}[theorem]{Case}\n",
"\\newtheorem{remark}[theorem]{Remark}\n",
"\\definecolor{bg}{rgb}{0.95,0.95,0.95}\n",
"\\input{tcilatex}\n",
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

