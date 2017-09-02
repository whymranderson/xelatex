# -*- coding: utf-8 -*-
"""
Created on Wed May 03 19:41:33 2017

@author: The One
"""
import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import matplotlib.cm as mplcm
import matplotlib.colors as colors
import vector_drawing_basic_geometry_3D as vlib

#%% Plotting begins
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=21, azim=-22)
ax2.set_color_cycle('b')


pB = np.array([0,0,0])
pD = np.array([0,6,0])
pA = np.array([1,3.5,5])
pC = np.array([6,2.5,0])

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

pE = (pB + pD)/2
pI = (pA + 2*pE)/3

lineCE, = ax2.plot(*zip(pC,pE),linewidth = 1.5,color='b')
lineAE, = ax2.plot(*zip(pA,pE),linewidth = 1.5,color='b')

pK = vlib.project_a_point_to_a_plane(pI, pA-pB, pC-pB,pA)
pJ = vlib.project_a_point_to_a_plane(pI, pD-pA, pC-pA,pA)
pH = vlib.project_a_point_to_a_plane(pI, pC-pB, pD-pB,pD)

lineIK, = ax2.plot(*zip(pI,pK),linewidth = 1,color='b',linestyle=':')
lineIJ, = ax2.plot(*zip(pI,pJ),linewidth = 1,color='b',linestyle=':')
lineIH, = ax2.plot(*zip(pI,pH),linewidth = 1,color='b',linestyle=':')
lineID, = ax2.plot(*zip(pI,pD),linewidth = 1,color='b')
lineIB, = ax2.plot(*zip(pI,pB),linewidth = 1,color='b')
lineIC, = ax2.plot(*zip(pI,pC),linewidth = 1,color='b')
    
ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pK, s = r"$K_\perp$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pJ, s = r"$J_\perp$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pH, s = r"$H_\perp$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pI, s = r"$I$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')

ax2.scatter3D(*zip(pK,pJ,pH))




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
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\tetra_premise_3.pgf')

