# -*- coding: utf-8 -*-
"""
Created on Mon May 08 13:19:33 2017

The 3D vector drawing functions for basic elements in geometry.

Elements include: line, perpendicular sign, circle, label, 

@author: The One
"""
import numpy as np

def draw_perpendicular_sign(rot_vec,first_axis,second_axis,location_point,ax):
    '''Put a perpendicular symbol to a 90 degree corner. The rot_vec
    is a vector parralel to first_axis crosses seconde_axis. First and seconde_axis are the two sides of the perp sign. Location_point is where the sign goes. ax is the figure axes.'''
    data = 0.25*circle_arc(rot_vec,first_axis,second_axis,2)
    data[1,:]=data[1,:]*np.sqrt(2)
    data = data+location_point
    ldata, = ax.plot(data[:,0],data[:,1],data[:,2],'k')

def rotation_matrix(axis,theta):
    '''Return the rotation_matrix that actively rotate a vector.'''
    axis = axis/np.sqrt(np.dot(axis,axis))
    a = np.cos(theta/2)
    b,c,d = axis*np.sin(theta/2)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])
def circle_arc(axis,start_v,end_v,num_points):
    '''Return the data points of a circle. Axis is the center axis of the circle following right hand rules. Start_v is the vector of the starting point on the circle. End_v is the ending point on the circle. Num_points is the total number of points.'''
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

def project_a_point_to_a_plane(out_point, plane_vec1, plane_vec2,anypointonplane):
    '''Return a point which is projected normally to the plane by another point. in_point is a point on the plane. Vec1 cross Vec2 should go toward the out_point.'''
    plane_normal = np.cross(plane_vec1,plane_vec2)
    plane_normal = plane_normal/np.linalg.norm(plane_normal)
    projected = np.dot(-out_point+anypointonplane,-plane_normal)*(-plane_normal) + out_point#
    #projected = -2*plane_normal+out_point
    return projected

def return_third_point_on_a_triagle_under_Ceva_Theorem(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point F. See figure on https://en.wikipedia.org/wiki/Ceva%27s_theorem"""
    a = np.linalg.norm(pA-pE)
    b = np.linalg.norm(pC-pE)
    c = np.linalg.norm(pC-pD)
    d = np.linalg.norm(pB-pD)
    e_over_f = b*d/a/c #ace = bdf, 
    pF = (1/(1+1/e_over_f)*pA + 1/(e_over_f+1)*pB)
    return pF

def return_intersection_under_Ceva_Theorem(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point O. See figure below.
    
    .. image:: ./figures/lemma4_fig4.png
       :scale: 60 %
       :align: center

    Image By 4C - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=1054185"""
    ae = np.linalg.norm(pA-pE)
    ec = np.linalg.norm(pC-pE)
    cb = np.linalg.norm(pC-pB)
    bd = np.linalg.norm(pB-pD)
    do_over_oa = ec*bd/ae/cb #ae/ec * cb/bd * bo/oe = 1, 
    pO = (pA*do_over_oa /(1+do_over_oa) + pD/(1+do_over_oa ))#(pA*od + pD*oa)/(oa+od)
    return pO



#%% Turn off the perspective/orthogonal viewing effect (it works but has some side problems)
#from mpl_toolkits.mplot3d import proj3d
def orthogonal_proj(zfront, zback):
    a = (zfront+zback)/(zfront-zback)
    b = -2*(zfront*zback)/(zfront-zback)
    return np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,a,b],
                        [0,0,0,zback]])
#proj3d.persp_transformation = orthogonal_proj
###

#%% Draw fancy arrows
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


