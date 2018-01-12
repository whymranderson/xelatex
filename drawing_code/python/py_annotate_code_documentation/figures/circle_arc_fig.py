# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import proj3d

import sys
sys.path.append(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf_related\programming_drawing_in_3D_toolbox')
import vector_drawing_basic_geometry_3D as tool

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 3),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=40, azim=-40)
ax2.set_color_cycle('b')


po = np.array([0,0,0])#origin
px = np.array([1,0,0])
py = np.array([0,1,0])
pz = np.array([0,0,1])
pA = np.array([1,1,1])/2.0

#bb = 1.3
#plb = np.array([-0.1*bb,0,-0.1*bb])
#plt = np.array([-0.1*bb,0,5*bb])
#ptr = np.array([5*bb,0,5*bb])
#pbr = np.array([5*bb,0,-0.1*bb])

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
farrowA = tool.Arrow3D(*zip(po,pA),mutation_scale=16, lw=2, arrowstyle="-|>", 
                       color="k")
ax2.add_artist(farrowA)

n_vec = np.cross(px/np.linalg.norm(px),pA/np.linalg.norm(pA))
arc_alpha = 0.3*tool.circle_arc(n_vec,px,pA,20)
larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'r',lw=2)




ax2.text(*px, s = r'$x$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*py, s = r'$y$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pz, s = r'$z$', fontsize=14,verticalalignment='top', horizontalalignment='left')
ax2.text(*pA, s = r"$A$ at (0.5,0.5,0.5)", fontsize=14,verticalalignment='bottom', horizontalalignment='left')



#draw_perpendicular_sign(np.cross(pB-pQ,pE-pQ),pB-pQ,pE-pQ,pQ,ax2)


#axis1.Axis(ax2,'r')
#ax2.autoscale_view()
#ax2.pbaspect= [1,1,0.5]
#ax2.auto_scale_xyz()

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
#ax2.set_xlim3d([-3, 8])
#ax2.set_ylim3d([-3,8])
#ax2.set_zlim3d([-3,8])
#ax2.set_xlim([-0.5,3.7])
#ax2.set_ylim([-0.5,3.7])
#ax2.set_zlim([0,6])


#ax2.annotate(s = r'$x$',xy = tuple(proj3d.proj_transform(*px, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='top',ha='left')
#ax2.annotate(s = r'$y$',xy = tuple(proj3d.proj_transform(*py, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':8,'fill':None,'edgecolor':'None'},va='top',ha='right')
#ax2.annotate(s = r'$z$',xy = tuple(proj3d.proj_transform(*pz, M = ax2.get_proj()))[:2], fontsize = 14, bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='right')


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
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf_related\pgf\lemma4_fig4.pgf')

