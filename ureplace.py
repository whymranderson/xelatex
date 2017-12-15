import re
import codecs
#import sys
#sys.path.insert(0, './resume/')

def dashrepl(matchobj): 
    return unichr(int(matchobj.group(1),16)) # python 2.7 use unichr, 
    # for python 3.3 use chr()

f1 = open('./resume/Resume_AnthonyLiang_2015.tex', 'r')
f2 = codecs.open('./resume/Resume_AnthonyLiang_2015_uni.tex', "w", "utf-8")

#f1 = open('Chapter_Orientation_Estimation.tex', 'r')
#f2 = codecs.open('Chapter_Orientation_Estimation_uni.tex', "w", "utf-8")
#f1 = open('SimpleGyroDesignExample.tex', 'r')
#f2 = codecs.open('SimpleGyroDesignExample_uni.tex', "w", "utf-8")

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







