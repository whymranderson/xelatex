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
#import get_tilt_angle_full_v2.rotation_matrix
#import get_tilt_angle_full_v2.circle_arc
import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import draw_perpendicular_sign


#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=55, azim=-6)
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
pC = np.array([0,6,0])
pB = np.array([2,4,6])
pAp = np.array([10,2.5,0])
pO = (pA + pAp)/3
pD = pO + ((pB-pO) + (pC-pO))/4

DOunit = (pD-pO)/np.linalg.norm(pD-pO)
pE = np.dot(-pO,DOunit)*DOunit + pO
pF= np.dot(pAp-pO,DOunit)*DOunit + pO

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineAAp, = ax2.plot(*zip(pA,pAp),linewidth = 2,color='b')
lineBAp, = ax2.plot(*zip(pB,pAp),linewidth = 2,color='b')
lineCAp, = ax2.plot(*zip(pC,pAp),linewidth = 2,color='b')
lineAE, = ax2.plot(*zip(pA,pE),linewidth = 1,color='b',linestyle=':')
lineApF, = ax2.plot(*zip(pAp,pF),linewidth = 1,color='b',linestyle=':')
lineDF, = ax2.plot(*zip(pO + ((pB-pO) + (pC-pO))/2,pF),linewidth = 1,color='b',linestyle=':')

for vertex in [pA,pB,pC,pAp]:
    ax2.plot(*zip(pD,vertex),linewidth = 1,color='b')
    
ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pAp, s = r"$A'$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pF, s = r"$E'$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.scatter(*pO, marker='o',color = 'k')


draw_perpendicular_sign(np.cross(DOunit,-pO),-pE,-pD+pO,pE,ax2,0.3)
draw_perpendicular_sign(np.cross(DOunit,-pO),pAp-pF,DOunit,pF,ax2,0.3)

#axis1.Axis(ax2,'r')
#ax2.autoscale_view()
#ax2.pbaspect= [1,1,0.5]
#ax2.auto_scale_xyz()

Xt,Yt,Zt = zip(pA,pB,pC,pAp)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6

# i think what u want is set all axes equal aspect,
# then rotate to a desired view angle, then transform
# all data to screen coordinate, then calculate xyz limits
# and set xyz limit, and then set figure figaspect ratio??
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
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\pgf related\pgf\tetra_premise_1.pgf')
def save(filepath, fig=None):
    '''Save the current image with no whitespace
    Example filepath: "myfig.png" or r"C:\myfig.pdf" 
    '''
    import matplotlib.pyplot as plt
    if not fig:
        fig = plt.gcf()

    plt.subplots_adjust(0,0,1,1,0,0)
    for ax in fig.axes:
        ax.axis('off')
        ax.margins(0,0)
        ax.xaxis.set_major_locator(plt.NullLocator())
        ax.yaxis.set_major_locator(plt.NullLocator())
    fig.savefig(filepath, pad_inches = 0, bbox_inches='tight')
#pyplot.savefig('./pgf_files/tetra_premise_1.pgf')
#pyplot.savefig('./pgf_files/tetra_premise_1.png',bbox_inches = 'tight', pad_inches = 0)
save('./pgf_files/tetra_premise_1.png',fig2)
pyplot.show()
