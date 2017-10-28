# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:33:28 2017

@author: The One
"""
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter
from pygments.formatters import HtmlFormatter



import sys
sys.path.insert(0, '../../../Scripts/cordtrans/Physics_and_Animation_Modules_Library')
sys.path.insert(0, '../../../Scripts/cordtrans/Demo_Examples/spinning_top_gyroscope/four_classical_motions_demo/OpenGL_animation')

#fh = file('RBPlotFunc.html','w')
#fl = file('RBPlotFunc.tex','w')

fh = file('cusp_GL.html','w')
fl = file('cusp_GL.tex','w')


pyfile = file("../../../Scripts/cordtrans/Demo_Examples/spinning_top_gyroscope/four_classical_motions_demo/OpenGL_animation/cusp_GL.py")

code_list = pyfile.readlines()
code = "".join(code_list)
highlight(code,PythonLexer(),HtmlFormatter(),outfile=fh)
#highlight(code,PythonLexer(),LatexFormatter(full = True, docclass = 'standalone'),outfile=fl)
highlight(code,PythonLexer(),LatexFormatter(verboptions = 'fontsize=\\small, numbers = left, frame=bottomline'),outfile=fl)

# save style definitions
stylestr = LatexFormatter().get_style_defs()
#print stylestr
fs = file('cuspGLstyle.sty','w')
fs.write(stylestr)

fh.close()
fl.close()
fs.close()
