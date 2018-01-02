import os

fname = 'Commongeometrydrawingfunctionsin3D.tex'


def replace_word(infile,old_word,new_word):
    if not os.path.isfile(infile):
        print ("Error on replace_word, not a regular file: "+infile)
        sys.exit(1)

    f1=open(infile,'r').read()
    #f1=open(infile,'r').readline()
    f2=open(infile,'w')
    m=f1.replace(old_word,new_word)
    f2.write(m)
    
replace_word(fname,r'\begin{tikzpicture}','')
replace_word(fname,r'\end{tikzpicture}','')
