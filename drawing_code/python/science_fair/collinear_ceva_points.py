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


#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=35, azim=-105)
ax2.set_color_cycle('b')

'''
linex, = ax2.plot([0,6],[0,0],[0,0])
linex.set_linewidth(1)
linex.set_color('k')
liney, = ax2.plot([0,0],[0,6],[0,0])
liney.set_linewidth(1)
liney.set_color('k')
linez, = ax2.plot([0,0],[0,0],[0,3])
linez.set_linewidth(1)
linez.set_color('k')
ax2.text(0,0,6, r'$z_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
'''

pB = np.array([2.5,-0.1,1.5])
pC = np.array([4,0,0])
pA = pB + pB - pC
pG = np.array([0,0,0])
pE = np.array([1,-3.5,0])

pD = (0.6*pE + 0.4*pC)
pH = (0.3*pG + 0.7*pC)

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineBG, = ax2.plot(*zip(pB,pG),linewidth = 2,color='b')
lineBE, = ax2.plot(*zip(pB,pE),linewidth = 2,color='b')
lineGE, = ax2.plot(*zip(pG,pE),linewidth = 2,color='b')
lineCG, = ax2.plot(*zip(pC,pG),linewidth = 2,color='b')
lineCE, = ax2.plot(*zip(pC,pE),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineAH, = ax2.plot(*zip(pA,pH),linewidth = 2,color='b')

pI = return_intersection_under_Ceva_Theorem(pA,pE,pC,pD,pB)
pK = return_intersection_under_Ceva_Theorem(pA,pG,pC,pH,pB)

lineGI, = ax2.plot(*zip(pG,pI),linewidth = 1,color='b',linestyle=':')
lineEK, = ax2.plot(*zip(pE,pK),linewidth = 1,color='b',linestyle=':')
lineGD, = ax2.plot(*zip(pG,pD),linewidth = 1,color='b',linestyle=':')
lineHE, = ax2.plot(*zip(pH,pE),linewidth = 1,color='b',linestyle=':')

pJ = return_intersection_under_Ceva_Theorem(pG,pE,pB,pI,pK)
pL = return_intersection_under_Ceva_Theorem(pG,pE,pC,pD,pH)

pF = return_third_point_on_a_triagle_under_Ceva_Theorem(pG,pE,pB,pI,pK)

lineCF, = ax2.plot(*zip(pC,pF),linewidth = 1,color='b',linestyle=':')
lineBF, = ax2.plot(*zip(pB,pF),linewidth = 1,color='b',linestyle=':')
lineAL, = ax2.plot(*zip(pA,pL),linewidth = 1,color='b')

ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right',linespacing=12)
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='left',linespacing=12)
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*(pI*1.02), s = r"$I$", fontsize=12,verticalalignment='center', horizontalalignment='left')
ax2.text(*(pJ*0.9), s = r"$J$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pK, s = r"$K$", fontsize=12,verticalalignment='bottom', horizontalalignment='center',linespacing=12)
ax2.text(*pL, s = r"$L$", fontsize=12,verticalalignment='top', horizontalalignment='left')



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
pyplot.savefig('./pgf_files/collinear_ceva_points.pgf')
pyplot.show()

