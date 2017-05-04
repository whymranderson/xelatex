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

def rotation_matrix(axis,theta):
    axis = axis/np.sqrt(np.dot(axis,axis))
    a = np.cos(theta/2)
    b,c,d = axis*np.sin(theta/2)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])
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
#proj3d.persp_transformation = orthogonal_proj
###

### Draw fancy arrows

from matplotlib.patches import FancyArrowPatch

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
###

def project_a_point_to_a_plane(out_point, plane_vec1, plane_vec2,in_point):
    '''Return a point which is projected normally to the plane by another point. in_point is a point on the plane. Vec1 cross Vec2 should go toward the out_point.'''
    plane_normal = np.cross(plane_vec1,plane_vec2)
    plane_normal = plane_normal/np.linalg.norm(plane_normal)
    projected = np.dot(-out_point+in_point,-plane_normal)*(-plane_normal) + out_point#
    #projected = -2*plane_normal+out_point
    return projected
    
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

pB = np.array([0,0,0])
pD = np.array([0,6,0])
pA = np.array([1,3.5,4])
pC = np.array([6,2.5,0])

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

pE = (pB + pD)/2

lineCE, = ax2.plot(*zip(pC,pE),linewidth = 2,color='b')
lineAE, = ax2.plot(*zip(pA,pE),linewidth = 2,color='b')

pQ = project_a_point_to_a_plane(pE, pA-pB, pC-pB,pA)
pP = project_a_point_to_a_plane(pE, pC-pD, pA-pD,pA)
pR = project_a_point_to_a_plane(pA, pD-pC, pB-pC,pD)

lineEQ, = ax2.plot(*zip(pE,pQ),linewidth = 1,color='b')
lineEP, = ax2.plot(*zip(pE,pP),linewidth = 1,color='b')
lineAR, = ax2.plot(*zip(pA,pR),linewidth = 1,color='b')
    
ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pQ, s = r"$Q_\perp$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pP, s = r"$P_\perp$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pR, s = r"$R_\perp$", fontsize=12,verticalalignment='top', horizontalalignment='left')

ax2.scatter3D(*zip(pQ,pP,pR))


def draw_perpendicular_sign(rot_vec,first_axis,second_axis,location_point,ax):
    '''Put a perpendicular symbol to a 90 degree corner.'''
    data = 0.25*circle_arc(rot_vec,first_axis,second_axis,2)
    data[1,:]=data[1,:]*np.sqrt(2)
    data = data+location_point
    ldata, = ax.plot(data[:,0],data[:,1],data[:,2],'k')


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
#pyplot.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\alphaphi.pgf')

