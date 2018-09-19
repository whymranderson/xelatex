# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import proj3d

import sys
sys.path.append(r'C:\Users\user\Desktop\xelatex_Transend\drawing_code\python\3D_geometry_annotate_program')
import annotate_program as tool

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 3),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=40, azim=-40)
ax2.set_color_cycle('b')


po = np.array([0,0,0])#origin
px = np.array([1,0,0])
py = np.array([0,1,0])
pz = np.array([0,0,1])
pA = np.array([0.3,0.3,1])

#xyz axes
farrowx = tool.Arrow3D(*zip(po,px),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowx)
farrowy = tool.Arrow3D(*zip(po,py),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowy)
farrowz = tool.Arrow3D(*zip(po,pz),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowz)
#farrowA = tool.Arrow3D(*zip(po,pA),mutation_scale=16, lw=2, arrowstyle="-|>", 
#                       color="k")
#ax2.add_artist(farrowA)


ax2.text(*(1.1*px), s = r'$x$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*py, s = r'$y$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*(1.1*pz), s = r'$z$', fontsize=14,verticalalignment='top', horizontalalignment='left')
#ax2.text(*pA, s = r"$A$ at (0.3,0.3,1)", fontsize=14,verticalalignment='bottom', horizontalalignment='left')

midspherex,midspherey,midspherez,midsphereR = 0.5,0.5,0.5,0.5

tool.plot_front(ax2,midspherex,midspherey,midspherez,midsphereR)
tool.plot_back(ax2,midspherex,midspherey,midspherez,midsphereR)


ff = 0.75
Xt,Yt,Zt = zip(po,px,py,pz,pA)#,ff*plb,ff*ptr,ff*plt,ff*pbr)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0


mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5 
mid_z = (Z.max()+Z.min()) * 0.5
ax2.set_xlim3d(mid_x - max_range, mid_x + max_range)
ax2.set_ylim3d(mid_y - max_range, mid_y + max_range)
ax2.set_zlim3d(mid_z - max_range, mid_z + max_range)

ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
ax2.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax2.w_zaxis.line.set_color([0,0,0,0])
#ax2.spines['left'].set_color('b') didn't work on 3D
ax2.set_axis_off()  #-> this can turn off the background curtain
pyplot.show()
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf_related\pgf\lemma4_fig4.pgf')

