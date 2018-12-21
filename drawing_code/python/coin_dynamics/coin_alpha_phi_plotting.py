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
from tempfile import TemporaryFile
import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import rotation_matrix
from annotate_program import Arrow3D

#2down
### Turn off the perspective/orthogonal viewing effect (it works but has some side problems)
from mpl_toolkits.mplot3d import proj3d
def orthogonal_proj(zfront, zback):
    a = (zfront+zback)/(zfront-zback)
    b = -2*(zfront*zback)/(zfront-zback)
    return np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,a,b],
                        [0,0,0,zback]])
proj3d.persp_transformation = orthogonal_proj
###



#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(4*1.5, 4*1.5),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=40, azim=300)
ax2.set_color_cycle('b')

linex, = ax2.plot([0,5],[0,0],[0,0])
linex.set_linewidth(1)
ax2.text(5,0,0, r'$\hat x_0, x_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
linex.set_color('k')
liney, = ax2.plot([0,0],[0,6],[0,0])
liney.set_linewidth(1)
liney.set_color('k')
ax2.text(0,6,0, r'$y_s$', fontsize=18,verticalalignment='top', horizontalalignment='left')
linez, = ax2.plot([0,0],[0,0],[0,6])
linez.set_linewidth(1)
linez.set_color('k')
ax2.text(0,0,6, r'$z_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')

# load coin data
npzfile = np.load('alphaphidata.npz')
CP = npzfile['CP']
CM = npzfile['CM']
CPprime = npzfile['CPprime']
R = npzfile['R']
onetheta = npzfile['onetheta']
cirCP = npzfile['cirCP']
C = npzfile['C']
Cprime = npzfile['Cprime']

# [line_end_vec1,line_end_vec2],[same]
lineswidth2 = np.array([[CP[0,:]        ,CM[0,:]            ],
                        [CPprime[0,:]   ,CM[0,:]            ],
                        [CM[0,:]        ,[R*np.tan(np.radians(onetheta)),0,0]],
                        [cirCP[1,:,0]   ,[0,0,0]            ],
                        [CPprime[0,:]        ,[0,0,0]            ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
                        ])
(mm,nn,pp)=np.shape(lineswidth2)
for k in range(mm):
    tempk, = ax2.plot(*np.transpose(lineswidth2[k,:,:]))
    tempk.set_linewidth(2)

# plot dash lines
dashlines = np.array([[CM[0,:],[CM[0,0],CM[0,1],0]],
                      [CPprime[0,:],[0,CPprime[0,1],0]],
                      [CPprime[0,:],[CPprime[0,0],0,0]]]
                      )
(mmd,nnd,ppd)=np.shape(dashlines)
for kd in range(mmd):
    tempkd,=ax2.plot(*np.transpose(dashlines[kd,:,:]),linestyle='--')
    tempkd.set_linewidth(1)
    
CP1perpen = np.dot(C[0,:,1],CPprime[0,:])*C[0,:,1]
line8, = ax2.plot([CPprime[0,0],CP1perpen[0]],[CPprime[0,1],CP1perpen[1]],[CPprime[0,2],CP1perpen[2]],':')
line8.set_linewidth(2)
line9, = ax2.plot([cirCP[1,0,0],CP1perpen[0]],[cirCP[1,1,0],CP1perpen[1]],[cirCP[1,2,0],CP1perpen[2]],':')
line9.set_linewidth(2)

####
arrow1 = Arrow3D([CPprime[0,0]-C[1,0,0]*1,CPprime[0,0]+C[1,0,0]],
            [CPprime[0,1]-C[1,1,0]*1,CPprime[0,1]+C[1,1,0]],
            [CPprime[0,2]-C[1,2,0]*1,CPprime[0,2]+C[1,2,0]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow1)
ax2.text(CPprime[0,0]+C[1,0,0],CPprime[0,1]+C[1,1,0],CPprime[0,2]+C[1,2,0], r'$\hat x_1$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='left')

arrow2 = Arrow3D([0,2*C[0,0,1]],
                 [0,2*C[0,1,1]],
                 [0,2*C[0,2,1]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow2)
ax2.text(2*C[0,0,1],2*C[0,1,1],2*C[0,2,1], r'$\hat y_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')

arrow3 = Arrow3D([0,2*C[0,0,2]],
                 [0,2*C[0,1,2]],
                 [0,2*C[0,2,2]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow3)
ax2.text(2*C[0,0,2],2*C[0,1,2],2*C[0,2,2], r'$\hat z_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')
         
arrow4 = Arrow3D([CPprime[0,0],CPprime[0,0]+2*Cprime[0,0,1]],
                 [CPprime[0,1],CPprime[0,1]+2*Cprime[0,1,1]],
                 [CPprime[0,2],CPprime[0,2]+2*Cprime[0,2,1]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow4)
ax2.text(CPprime[0,0]+2*C[1,0,1],CPprime[0,1]+2*C[1,1,1],CPprime[0,2]+2*C[1,2,1], r'$\/\hat y_1$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='left')

# plot the point dots
dots = ax2.plot([0,CM[0,0],CPprime[0,0],cirCP[1,0,0],R*np.tan(np.radians(onetheta)),CP1perpen[0]],
                [0,CM[0,1],CPprime[0,1],cirCP[1,1,0],0,CP1perpen[1]],
                [0,CM[0,2],CPprime[0,2],cirCP[1,2,0],0,CP1perpen[2]], marker='o',color = 'k', lw=0 ,markersize=5,alpha=1)
dots2 = ax2.plot([CM[0,0]],
                 [CM[0,1]],
                 [0], marker='.',color = 'k', lw=0 ,markersize=10,alpha=1)
                   

def circle_arc(axis,start_v,end_v,num_points):
    axis = axis/np.linalg.norm(axis)
    start_v = start_v/np.linalg.norm(start_v)
    end_v = end_v/np.linalg.norm(end_v)
    theta = np.arccos(np.dot(start_v,end_v))
    theta_s = list(np.arange(0.0, theta + theta/num_points, theta/num_points))
    circle_vecs = np.zeros([len(theta_s),3])
    for i,thetai in enumerate(theta_s):
        makecir = rotation_matrix(axis,thetai)
        circle_vecs[i,:] = np.dot(makecir,start_v)
    return circle_vecs


arc1 = 2*circle_arc([0,0,1],[1,0,0],CPprime[0,:]-CP[0,:],10)
larc1, = ax2.plot(arc1[:,0],arc1[:,1],arc1[:,2],'k')
ax2.text(arc1[4,0],arc1[4,1],arc1[4,2], r'$\alpha$', fontsize=16,verticalalignment='center', horizontalalignment='left')
arc2 = 2*circle_arc(C[0,:,2],-CM[0,:],cirCP[1,:,0]-CM[0,:],10)+CM[0,:]
larc2, = ax2.plot(arc2[:,0],arc2[:,1],arc2[:,2],'k')
ax2.text(arc2[4,0],arc2[4,1],arc2[4,2], r'$\theta$', fontsize=16,verticalalignment='top', horizontalalignment='left')
arc3 = 1*circle_arc(C[0,:,1],cirCP[1,:,0]-CP1perpen,CPprime[0,:]-CP1perpen,10)+CP1perpen
larc3, = ax2.plot(arc3[:,0],arc3[:,1],arc3[:,2],'k')
ax2.text(arc3[-1,0],arc3[-1,1],arc3[-1,2], r'$\/\phi$', fontsize=15,
         verticalalignment='bottom', horizontalalignment='left')
arc4 = 2.5*circle_arc([-1,0,0],CM[0,:],[0,1,0],10)
larc4, = ax2.plot(arc4[:,0],arc4[:,1],arc4[:,2],'k')
ax2.text(arc4[4,0],arc4[4,1],arc4[4,2], r'$\beta$', fontsize=16,verticalalignment='bottom', horizontalalignment='left')

# perpendicular sign in the vicinity of phi
rec1 = 0.3*circle_arc(C[0,:,2],cirCP[1,:,0]-CP1perpen,C[0,:,1],2)
rec1[1,:]=rec1[1,:]*1.414
rec1 = rec1+CP1perpen
lrec1, = ax2.plot(rec1[:,0],rec1[:,1],rec1[:,2],'k')

# perp sign at CPprime[0,:]
rec2 = 0.3*circle_arc(C[1,:,2],C[1,:,0],C[1,:,1],2)
rec2[1,:]=rec2[1,:]*1.414
rec2 = rec2 + CPprime[0,:]
lrec2, = ax2.plot(rec2[:,0],rec2[:,1],rec2[:,2],'k')

# perp sign of vertical line of CM[0,:]
rec3 = 0.5*circle_arc(C[0,:,0],[0,0,1],[0,-1,0],2)
rec3[1,:]=rec3[1,:]*1.414
rec3 = rec3 + np.array([CM[0,0],CM[0,1],0])
lrec3, = ax2.plot(rec3[:,0],rec3[:,1],rec3[:,2],'k')


ax2.text(0,0,-0.5, r'$CP_0$', fontsize=13,
         verticalalignment='top', horizontalalignment='center')
ax2.text(CM[0,0],CM[0,1],CM[0,2], r'$\/CM_0$', fontsize=13,
         verticalalignment='bottom', horizontalalignment='left')
ax2.text(CPprime[0,0],CPprime[0,1],CPprime[0,2], r'$\/CP_1$', fontsize=13,
         verticalalignment='top', horizontalalignment='left')
ax2.text(cirCP[1,0,0],cirCP[1,1,0],cirCP[1,2,0], r'$\/cirCP_1$', fontsize=10,
         verticalalignment='top', horizontalalignment='left')

#print(np.linalg.norm(CM[0,:]-CP[1,:]))                   

#axis1.Axis(ax2,'r')
ax2.autoscale_view()
#ax2.pbaspect= [1,1,0.5]
#ax2.auto_scale_xyz()
#ax2.set_xlim3d([-3, 8])
#ax2.set_ylim3d([-3,8])
#ax2.set_zlim3d([-3,8])
ax2.set_xlim([-0.5,3.7])
ax2.set_ylim([-0.5,3.7])
ax2.set_zlim([0,6])
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
#pyplot.savefig('alphaphi.png')
pyplot.show()

