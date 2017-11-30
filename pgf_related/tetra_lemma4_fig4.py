# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import matplotlib.cm as mplcm
import matplotlib.colors as colors
import sys
sys.path.append('./programming_drawing_in_3D_toolbox')
from programming_drawing_in_3D_toolbox.vector_drawing_basic_geometry_3D import return_third_point_on_a_triagle_under_Ceva_Theorem
from programming_drawing_in_3D_toolbox.vector_drawing_basic_geometry_3D import return_intersection_under_Ceva_Theorem


#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=21, azim=-22)
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

pA = np.array([0,0,0])
pC = np.array([0,6,3])
pB = np.array([1,3.5,4])
pD = np.array([6,1.5,0])

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

pE = (pB + pC)/2
pF = (pC + pD)/2
pH = (pA + pB)/2
pG = (0.4*pA + 0.6*pD)

lineDE, = ax2.plot(*zip(pD,pE),linewidth = 1,color='b')
lineBF, = ax2.plot(*zip(pB,pF),linewidth = 1,color='b')
lineDH, = ax2.plot(*zip(pD,pH),linewidth = 1,color='b')
lineBG, = ax2.plot(*zip(pB,pG),linewidth = 1,color='b')

pN = return_third_point_on_a_triagle_under_Ceva_Theorem(pB,pD,pC,pF,pE)
pNp = return_third_point_on_a_triagle_under_Ceva_Theorem(pD,pB,pA,pH,pG)

lineCN, = ax2.plot(*zip(pC,pN),linewidth = 1,color='b')
lineANp, = ax2.plot(*zip(pA,pNp),linewidth = 1,color='b')
#lineAR, = ax2.plot(*zip(pA,pR),linewidth = 1,color='b')

pJ = return_intersection_under_Ceva_Theorem(pB,pD,pC,pF,pE)
pK = return_intersection_under_Ceva_Theorem(pD,pB,pA,pH,pG)

lineCK, = ax2.plot(*zip(pC,pK),linewidth = 1,color='b')
lineAJ, = ax2.plot(*zip(pA,pJ),linewidth = 1,color='b')

ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pNp, s = r"$N'$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pJ, s = r"$J$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pK, s = r"$K$", fontsize=12,verticalalignment='top', horizontalalignment='left')


#draw_perpendicular_sign(np.cross(pB-pQ,pE-pQ),pB-pQ,pE-pQ,pQ,ax2)


#axis1.Axis(ax2,'r')
#ax2.autoscale_view()
#ax2.pbaspect= [1,1,0.5]
#ax2.auto_scale_xyz()

Xt,Yt,Zt = zip(pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6


mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5 - 1
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
pyplot.show()
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\tetra_premise_2.pgf')

