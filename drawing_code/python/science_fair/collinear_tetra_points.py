# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import proj3d

import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import return_third_point_on_a_triagle_under_Ceva_Theorem
from annotate_program import return_intersection_under_Ceva_Theorem
from annotate_program import return_Menelaus_third_outer_point

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=15, azim=-95)
ax2.set_color_cycle('b')

pA = np.array([2.5,-1,3])
pB = np.array([4,0,0])
pD = np.array([0,0,0])
pC = np.array([1,-2.5,0])
pN = (0.6*pA + 0.4*pB)
pH = (0.7*pB + 0.3*pD)
pI = (0.45*pB + 0.55*pC)


pE = return_intersection_under_Ceva_Theorem(pA,pD,pB,pH,pN)
pF = return_intersection_under_Ceva_Theorem(pA,pC,pB,pI,pN)
pJ = return_third_point_on_a_triagle_under_Ceva_Theorem(pD,pC,pN,pF,pE)
pG = return_Menelaus_third_outer_point(pD,pC,pN,pF,pE)

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 1,color='b')
lineGE, = ax2.plot(*zip(pG,pE),linewidth = 1,color='b')
lineCG, = ax2.plot(*zip(pC,pG),linewidth = 1,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 1,color='b')
lineAH, = ax2.plot(*zip(pA,pH),linewidth = 1,color='b')
lineAI, = ax2.plot(*zip(pA,pI),linewidth = 1,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 1,color='b')
lineBC, = ax2.plot(*zip(pC,pB),linewidth = 1,color='b')
lineDB, = ax2.plot(*zip(pD,pB),linewidth = 1,color='b')
lineNC, = ax2.plot(*zip(pN,pC),linewidth = 1,color='b')
lineDC, = ax2.plot(*zip(pD,pC),linewidth = 1,color='b')
lineDN, = ax2.plot(*zip(pD,pN),linewidth = 1,color='b')


lineCE, = ax2.plot(*zip(pC,pE),linewidth = 1,color='b',linestyle=':')
lineNJ, = ax2.plot(*zip(pN,pJ),linewidth = 1,color='b',linestyle=':')
lineDF, = ax2.plot(*zip(pD,pF),linewidth = 1,color='b',linestyle=':')

ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right',linespacing=12)
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='left',linespacing=12)
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*(pE+(pA-pH)/20), s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#ax2.text(*(pI*1.02), s = r"$I$", fontsize=12,verticalalignment='center', horizontalalignment='left')
ax2.text(*(pJ+(pJ-pN)/20), s = r"$J$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='bottom', horizontalalignment='left',linespacing=12)
#ax2.text(*pL, s = r"$L$", fontsize=12,verticalalignment='top', horizontalalignment='left')

ax2.scatter3D(*zip(pE,pF,pG,pJ),color='k')



Xt,Yt,Zt = zip(pA,pB,pC,pG,pE)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6


mid_x = (X.max()+X.min()) * 0.5 - 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5
ax2.set_xlim3d(mid_x - max_range, mid_x + max_range)
ax2.set_ylim3d(mid_y - max_range, mid_y + max_range)
ax2.set_zlim3d(mid_z - max_range, mid_z + max_range)
#ax2.set_xlim3d([-3, 8])
#ax2.set_ylim3d([-3,8])
#ax2.set_zlim3d([-3,8])
#ax2.set_xlim([-0.5,3.7])
#ax2.set_ylim([-0.5,3.7])
#ax2.set_zlim([0,6])

'''
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pB, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pE, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.5",
                            ),
            )
'''


#pla = (pB+pE)/2
#ax2.text(*pla, s = r"$a$", fontsize=10,verticalalignment='bottom', horizontalalignment='left')#bbox={'pad':38,'fill':None,'edgecolor':'blue'})
#ax2.annotate(s = 'a',xy = tuple(proj3d.proj_transform(*pla, M = ax2.get_proj()))[:2], bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='left')


ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
ax2.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax2.w_zaxis.line.set_color([0,0,0,0])
#ax2.spines['left'].set_color('b') didn't work on 3D
ax2.set_axis_off()  #-> this can turn off the background curtain
#ax2.axhline(y=1,xmin=0,xmax=1)
#ax2.set_frame_on(True)
#ax2.set_axis_bgcolor('b')
#ax2.set_position() #set the bbox of the whole axes
#ax2.set_zbound()
pyplot.savefig('./pgf_files/collinear_tetra_points.pgf')
pyplot.show()

