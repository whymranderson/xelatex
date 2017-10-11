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

fh = file('RBPlotFunc.html','w')
fl = file('RBPlotFunc.tex','w')

RBplot_f = file("../../../Scripts/cordtrans/Physics_and_Animation_Modules_Library/RBPlotFunctionV5.py")

code_list = RBplot_f.readlines()
code = "".join(code_list)
highlight(code,PythonLexer(),HtmlFormatter(),outfile=fh)
highlight(code,PythonLexer(),LatexFormatter(full = True),outfile=fl)

fh.close()
fl.close()
