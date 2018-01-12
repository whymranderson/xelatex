import re
import codecs

def dashrepl(matchobj): 
    return unichr(int(matchobj.group(1),16)) # python 2.7 use unichr, 
    # for python 3.3 use chr()

#f1 = open('ABC_play_chess.tex', 'r')
#f2 = codecs.open('ABC_play_chess_uni.tex', "w", "utf-8")

f1 = open('telephone.tex', 'r')
f2 = codecs.open('telephone_uni.tex', "w", "utf-8")


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







