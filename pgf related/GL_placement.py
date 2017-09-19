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
import vector_drawing_basic_geometry_3D as tool

#%% Plotting begins
# first set viewing angle in 3D spoce
elevate = 30
azimuthal = -60
# plot generation
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=elevate, azim=azimuthal)
ax2.set_color_cycle('b')


po = np.array([0,0,0])#origin
px = np.array([1,0,0])
py = np.array([0,1,0])
pz = np.array([0,0,1])
pup = np.array([0,-1,0])
pz0 = np.array([0.6,0,0.3])
pz0_xy = tool.project_a_point_to_a_plane(pz0, px, py, po)
pz0_yz = tool.project_a_point_to_a_plane(pz0, py, pz, po)

farrowx = tool.Arrow3D(*zip(po,px),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowx)
farrowy = tool.Arrow3D(*zip(po,py),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowy)
farrowz = tool.Arrow3D(*zip(po,pz),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowz)

linepuppo, = ax2.plot(*zip(pup,po-np.array([0,0.05,0])),linewidth = 1,color='b',linestyle=':')

farrow_defaultview = tool.Arrow3D(*zip(pup,(pup*2.0+po)/3.0),mutation_scale=16, lw=3, arrowstyle="-|>", color="r")
ax2.add_artist(farrow_defaultview)

farrow_omega0 = tool.Arrow3D(*zip(po,py*0.66),mutation_scale=16, lw=3, arrowstyle="-|>", color="r")
ax2.add_artist(farrow_omega0)

farrow_raise = tool.Arrow3D(*zip(pup+pz,(pup+pz)*0.66), mutation_scale=16, lw=3, arrowstyle="-|>", color="r")
ax2.add_artist(farrow_raise)

linepuppraise, = ax2.plot(*zip(pup,pup+pz),linewidth = 1,color='b',linestyle=':')
linepraisepo, = ax2.plot(*zip(pup+pz,po),linewidth = 1,color='b',linestyle=':')

farrow_z0 = tool.Arrow3D(*zip(po,pz0), mutation_scale=16, lw=1, arrowstyle="-|>", color="m")
ax2.add_artist(farrow_z0)
linepz0pz0_xy, = ax2.plot(*zip(pz0,pz0_xy),linewidth = 1,color='b',linestyle=':')
linepz0pz0_yz, = ax2.plot(*zip(pz0,pz0_yz),linewidth = 1,color='b',linestyle=':')

arc_alpha = 0.5*tool.circle_arc(-px,pup+pz,pz,20)
larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'k')


#lineAB, = ax2.plot(*zip(po,px),linewidth = 2,color='b')
#lineAD, = ax2.plot(*zip(po,pz),linewidth = 2,color='b')

#pE = (po + pz)/2
#pF = (2*px + pz)/3
#pG = (2*px+3*py)/5
#pH = (4*py+po)/5
#pPhantom = py+(py-pz)

#lineCPhan, = ax2.plot(*zip(py,pPhantom),linewidth = 1,color='b')
#lineEG, = ax2.plot(*zip(pE,pG),linewidth = 1,color='b')
#lineHF, = ax2.plot(*zip(pH,pF),linewidth = 1,color='b')

#pP = pH + 0.7*(pH-pE)
#pPprime = pG+1.5*(pG-pF)
# 
#linePE, = ax2.plot(*zip(pP,pE),linewidth = 1,color='b')
#lineFPprime, = ax2.plot(*zip(pF,pPprime),linewidth = 1,color='b')

ax2.annotate(s = r'$A$',xy = (0,0), bbox={'pad':8},va='top')
#ax2.text(*po, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*px, s = r'$x$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')

#ax2.scatter3D(*zip(pK,pJ,pH))

#draw_perpendicular_sign(np.cross(px-pQ,pE-pQ),px-pQ,pE-pQ,pQ,ax2)

# correcting bug of unequal aspect ratio
Xt,Yt,Zt = zip(po,px,py,pz,pup)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)
max_range = 0.5* np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5 -0.2
mid_y = (Y.max()+Y.min()) * 0.5 - 0.3
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
pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\gl_coordinance.pgf')

