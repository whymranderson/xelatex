# -*- coding: utf-8 -*-

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import proj3d

import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import incircle3D
from annotate_program import circle_full


#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=90, azim=-90)
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
pB = np.array([3,0,0])
pC = np.array([2,2.5,0])
pO,r,nv,p12,p23,p31 = incircle3D(pA,pB,pC)

circle1 = circle_full(nv,p12-pO,r,50) +pO
circle1, = ax2.plot(circle1[:,0],circle1[:,1],circle1[:,2],'r',lw=2)

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineBA, = ax2.plot(*zip(pB,pA),linewidth = 2,color='b')
lineBC, = ax2.plot(*zip(pB,pC),linewidth = 2,color='b')
liner, = ax2.plot(*zip(pO,p12),linewidth = 2,color='b')

#lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
#lineBE, = ax2.plot(*zip(pB,pE),linewidth = 2,color='b')



#ax2.text(*pA, s = r'$p1$', fontsize=12,verticalalignment='bottom', horizontalalignment='right',linespacing=12)
#ax2.text(*pB, s = r'$p2$', fontsize=12,verticalalignment='bottom', horizontalalignment='left',linespacing=12)
#ax2.text(*pC, s = r'$p3$', fontsize=12,verticalalignment='bottom', horizontalalignment='left')
#ax2.text(*pO, s = r'$O$', fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*(pO+p12)/2,   s = r'$r$', fontsize=14,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*((p12+pA)/2), s = r"$x$", fontsize=14,verticalalignment='top', horizontalalignment='left')
ax2.text(*((p23+pB)/2), s = r"$y$", fontsize=14,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*((p31+pC)/2), s = r"$z$", fontsize=14,verticalalignment='bottom', horizontalalignment='right')


ax2.scatter3D(*zip(p12,p23,p31,pO),c = ['blue'])

Xt,Yt,Zt = zip(pA,pB,pC)
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
#pyplot.savefig('./pgf_files/incircle_triangle.pgf')
pyplot.show()

