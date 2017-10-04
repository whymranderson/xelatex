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
from mpl_toolkits.mplot3d import proj3d

#%% Plotting begins
# first set viewing angle in 3D spoce
elevate = 90
azimuthal = -90
# plot generation
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=elevate, azim=azimuthal)
ax2.set_color_cycle('b')


po = np.array([0,0,0])#origin
px = np.array([1,0,0])
py = np.array([0,1,0])
pz = np.array([0,0,1])
plb = np.array([-0.3,-0.3,0])
ptr = np.array([1.3,1.3,0])

farrowx = tool.Arrow3D(*zip(po,px),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowx)
farrowy = tool.Arrow3D(*zip(po,py),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowy)
farrowz = tool.Arrow3D(*zip(po,pz),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowz)

arc_alpha = 0.1*tool.circle_arc(pz,px,py,20)
larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'k')

#draw_perpendicular_sign(np.cross(px-pQ,pE-pQ),px-pQ,pE-pQ,pQ,ax2)

# correcting bug of unequal aspect ratio
Xt,Yt,Zt = zip(po,px,py,pz,plb,ptr)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)
max_range = 0.5* np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
mid_x = (X.max()+X.min()) * 0.5 
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5 
ax2.set_xlim3d(mid_x - max_range, mid_x + max_range)
ax2.set_ylim3d(mid_y - max_range, mid_y + max_range)
ax2.set_zlim3d(mid_z - max_range, mid_z + max_range)

# Create Annotation
ax2.annotate(s = r'$x$',xy = tuple(proj3d.proj_transform(*px, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='top',ha='left')
ax2.annotate(s = r'$y$',xy = tuple(proj3d.proj_transform(*py, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='bottom',ha='left')
ax2.annotate(s = r'$z$',xy = tuple(proj3d.proj_transform(*pz, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='bottom',ha='left')

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
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\gl_coordinance.pgf')

