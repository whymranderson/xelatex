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
import vector_drawing_basic_geometry_3D

#%% Plotting begins
# first set viewing angle in 3D space
elevate = 45
azimuthal = 0
# plot generation
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=elevate, azim=azimuthal)
ax2.set_color_cycle('b')


pA = np.array([0,0,0])
pB = np.array([1,0,0])
pC = np.array([0,1,0])
pD = np.array([0,0,1])

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
#lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
#lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
#lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

#pE = (pA + pD)/2
#pF = (2*pB + pD)/3
#pG = (2*pB+3*pC)/5
#pH = (4*pC+pA)/5
#pPhantom = pC+(pC-pD)

#lineCPhan, = ax2.plot(*zip(pC,pPhantom),linewidth = 1,color='b')
#lineEG, = ax2.plot(*zip(pE,pG),linewidth = 1,color='b')
#lineHF, = ax2.plot(*zip(pH,pF),linewidth = 1,color='b')

#pP = pH + 0.7*(pH-pE)
#pPprime = pG+1.5*(pG-pF)
# 
#linePE, = ax2.plot(*zip(pP,pE),linewidth = 1,color='b')
#lineFPprime, = ax2.plot(*zip(pF,pPprime),linewidth = 1,color='b')


    
ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$x$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')

#ax2.scatter3D(*zip(pK,pJ,pH))

#draw_perpendicular_sign(np.cross(pB-pQ,pE-pQ),pB-pQ,pE-pQ,pQ,ax2)

# correcting bug of unequal aspect ratio
Xt,Yt,Zt = zip(pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)
max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6
mid_x = (X.max()+X.min()) * 0.5
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
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\tetra_premise_4.pgf')

