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
elevate = 0
azimuthal = -90
# plot generation
fig2 = pyplot.figure(2,figsize=(3, 3),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=elevate, azim=azimuthal)
ax2.set_color_cycle('b')


po = np.array([0,0,0])#origin
px = np.array([1,0,0])
py = np.array([0,1,0])
pz = np.array([0,0,1])
bb = 1.3
plb = np.array([-bb,0,-bb])
plt = np.array([-bb,0,bb])
ptr = np.array([bb,0,bb])
pbr = np.array([bb,0,-bb])

cr = 0.1*np.sqrt(2)/2
pctr = np.array([cr,0,cr])
pcbl = np.array([-cr,0,-cr])
pctl = np.array([-cr,0,cr])
pcbr = np.array([cr,0,-cr])

farrowx = tool.Arrow3D(*zip(po,px),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowx)
farrowy = tool.Arrow3D(*zip(po,py),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowy)
farrowz = tool.Arrow3D(*zip(po,pz),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="b")
ax2.add_artist(farrowz)
#ax2.scatter(0,0,0)

line1, = ax2.plot(*zip(plb,plt),linewidth = 1,color='b',linestyle='-')
line2, = ax2.plot(*zip(plt,ptr),linewidth = 1,color='b',linestyle='-')
line3, = ax2.plot(*zip(ptr,pbr),linewidth = 1,color='b',linestyle='-')
line4, = ax2.plot(*zip(pbr,plb),linewidth = 1,color='b',linestyle='-')
linec1, = ax2.plot(*zip(pctr,pcbl),linewidth = 1,color='k',linestyle='-')
linec2, = ax2.plot(*zip(pctl,pcbr),linewidth = 1,color='k',linestyle='-')

arc_alpha = 0.1*tool.circle_arc(-py,px,-px,20)
larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'k')
arc_alpha2 = 0.1*tool.circle_arc(-py,-px,px,20)
larc_alpha2, = ax2.plot(arc_alpha2[:,0],arc_alpha2[:,1],arc_alpha2[:,2],'k')


#arc_alpha = 0.05*tool.circle_arc(pz,px,-px,20)
#larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'k')
#arc_alpha2 = 0.05*tool.circle_arc(pz,-px,px,20)
#larc_alpha2, = ax2.plot(arc_alpha2[:,0],arc_alpha2[:,1],arc_alpha2[:,2],'k')

#draw_perpendicular_sign(np.cross(px-pQ,pE-pQ),px-pQ,pE-pQ,pQ,ax2)

# correcting bug of unequal aspect ratio
Xt,Yt,Zt = zip(po,px,py,pz,1.2*plb,1.2*ptr,1.2*plt,1.2*pbr)
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
ax2.annotate(s = r'$y$',xy = tuple(proj3d.proj_transform(*pcbl, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='top',ha='right')
ax2.annotate(s = r'$z$',xy = tuple(proj3d.proj_transform(*pz, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='right')
ax2.annotate(s = 'window',xy = (0.07,0.05), textcoords = 'axes fraction', fontsize = 14, bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='left')
#pyplot.axhline(y= 0.06, xmin=0.15, xmax=0.85)
#pyplot.axvline(x= 0.15, ymin=0.15, ymax=0.85)
#
#pyplot.axhspan(ymin=0,ymax= 0.06, xmin=0.15, xmax=0.85) doesn't work


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
#proj3d.persp_transformation = tool.orthogonal_proj

pyplot.show()
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf_related\pgf\gl_adjusted_view.pgf')

