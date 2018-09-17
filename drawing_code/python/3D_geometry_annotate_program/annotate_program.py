# -*- coding: utf-8 -*-
"""
Created on Mon May 08 13:19:33 2017

3D vector drawing functions for basic elements in geometry.
"""
import numpy as np
from mpl_toolkits.mplot3d import proj3d


def offset_curve(curve, length):
    '''Translate the position of all points on a 3D curve
    according to each point's normal direction described below, by specified
    length in mm. This operation is in a 2D plane. The offset normal direction is
    right hand rule's palm direction, with four fingers point
    along the curve starting from the first point, and thumb
    pointing perpendicular to the 2D plane, normally opposing the viewing direction.
     
    .. image:: ./figures/tex_group_logo.pdf
       :scale: 20 %
       :align: center

'''

    newcurve = 0*curve
    for ind,x in enumerate(curve[:,0]):
        if ind == 0:
            tangent = curve[1,:]-curve[0,:]
            tangentn = tangent/np.linalg.norm(tangent)
            nvec = np.dot(rotation_matrix([0,0,1],np.pi/2),tangentn)
            newcurve[0,:] = curve[0,:]+length*nvec
            #print newcurve
        else:
            tangent = curve[ind,:]-curve[ind-1,:]
            tangentn = tangent/np.linalg.norm(tangent)
            nvec = np.dot(rotation_matrix([0,0,1],np.pi/2),tangentn)
            newcurve[ind,:]=curve[ind,:]+length*nvec
            #print curve[ind,:]+length*nvec
            #print newcurve[ind,:]
    return newcurve
            
        


def draw_xyz_coordinate_unit_vectors(ax4):
    '''Put xyz coordinate unit vectors with fancy arrows.'''
    xyz_arrow_data = np.array([[1.0,0,0],[0,1.0,0],[0,0,1.0]])

    x_arrow = Arrow3D([0,xyz_arrow_data[0,0]],
                       [0,0],
                       [0,0], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(x_arrow)
    ax4.text(*xyz_arrow_data[0,:],s="x",fontsize=12)

    y_arrow = Arrow3D([0,0],
                       [0,xyz_arrow_data[1,1]],
                       [0,0], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(y_arrow)
    ax4.text(*xyz_arrow_data[1,:],s="y",fontsize=12)
    z_arrow = Arrow3D([0,0],
                       [0,0],
                       [0,xyz_arrow_data[2,2]], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(z_arrow)
    ax4.text(*xyz_arrow_data[2,:],s="z",fontsize=12)

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
    '''Return the data points of a circle. Axis is the center axis of the circle following right hand rules. Start_v is the vector of the starting point on the circle. End_v is the ending point on the circle. Num_points is the total number of points on the arc. More points give a smoother arc. Vectors take the form like np.array([1,0,0]).
    
    .. image:: ./figures/circle_arc_fig.png
       :scale: 60 %
       :align: center
       
    .. code:: python
    
      px = np.array([1,0,0])
      pA = np.array([0.5,0.5,0.5])
      n_vec = np.cross(px/np.linalg.norm(px),pA/np.linalg.norm(pA))
      arc_alpha = 0.3*tool.circle_arc(n_vec,px,pA,20)
      larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'r',lw=2)

'''
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
    """Given points ABCDE, return point F.

    .. image:: ./figures/ceva_third_side_point.png
       :scale: 60 %
       :align: center
    """
    a = np.linalg.norm(pA-pE)
    b = np.linalg.norm(pC-pE)
    c = np.linalg.norm(pC-pD)
    d = np.linalg.norm(pB-pD)
    e_over_f = b*d/a/c #ace = bdf, 
    pF = (1/(1+1/e_over_f)*pA + 1/(e_over_f+1)*pB)
    return pF

def return_intersection_under_Ceva_Theorem(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point O. See figure below.
    
    .. image:: ./figures/ceva_intersection.png
       :scale: 60 %
       :align: center
    """
    ae = np.linalg.norm(pA-pE)
    ec = np.linalg.norm(pC-pE)
    cb = np.linalg.norm(pC-pB)
    bd = np.linalg.norm(pB-pD)
    do_over_oa = ec*bd/ae/cb #ae/ec * cb/bd * bo/oe = 1, 
    pO = (pA*do_over_oa /(1+do_over_oa) + pD/(1+do_over_oa ))#(pA*od + pD*oa)/(oa+od)
    return pO

def return_Menelaus_third_outer_point(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point F. See figure below.
    
    .. image:: ./figures/menelaus_outer_point.png
       :scale: 60 %
       :align: center
    """
    ae = np.linalg.norm(pA-pE)
    ec = np.linalg.norm(pC-pE)
    cd = np.linalg.norm(pC-pD)
    bd = np.linalg.norm(pB-pD)
    bf_over_fa = ec*bd/ae/cd #ae/ec * cb/bd * bf/fa = 1, 
    pF = pB + (pB-pA)* bf_over_fa/(1- bf_over_fa) #( -pA*bf + pB*fa)/(fa-bf)
    return pF

def triangle_area(pA,pB,pC):
    """Given points ABC, return area using Heron's Theorem."""
    la = np.linalg.norm(pA-pB)
    lb = np.linalg.norm(pB-pC)
    lc = np.linalg.norm(pA-pC)
    s = 0.5*(la+lb+lc)
    area =  np.sqrt(s*(s-la)*(s-lb)*(s-lc))
    return area


sphere_color = 'red'#'#FFDDDD'
sphere_alpha = 0.05
frame_color = 'darkgray'
frame_alpha = 0.4
frame_width = 1
sphere_grid = 40
wirestride = 3
def plot_front(axes,midspherex,midspherey,midspherez,midsphereR):
    '''plot the lucid sphere, front part'''
    u = np.linspace(-np.pi, 0, sphere_grid)
    v = np.linspace(0, np.pi, sphere_grid)
    x = midsphereR*np.outer(np.cos(u), np.sin(v))+midspherex
    y = midsphereR*np.outer(np.sin(u), np.sin(v))+midspherey
    z = midsphereR*np.outer(np.ones(np.size(u)), np.cos(v))+midspherez
    axes.plot_surface(x, y, z, rstride=2, cstride=2,
                           color=sphere_color, linewidth=0,
                           alpha=sphere_alpha)
    axes.plot_wireframe(x, y, z, rstride=wirestride, cstride=wirestride,
                             color=frame_color,
                             alpha=frame_alpha)


def plot_back(axes,midspherex,midspherey,midspherez,midsphereR):
    '''plot the lucid sphere, back part'''
    u = np.linspace(0, np.pi, sphere_grid)
    v = np.linspace(0, np.pi, sphere_grid)
    x = midsphereR*np.outer(np.cos(u), np.sin(v))+midspherex
    y = midsphereR*np.outer(np.sin(u), np.sin(v))+midspherey
    z = midsphereR*np.outer(np.ones(np.size(u)), np.cos(v))++midspherez
    axes.plot_surface(x, y, z, rstride=2, cstride=2,
                           color=sphere_color, linewidth=0,
                           alpha=sphere_alpha)
    axes.plot_wireframe(x, y, z, rstride=wirestride, cstride=wirestride,
                             color=frame_color,
                             alpha=frame_alpha)

def incircle3D(point1,point2,point3):
    """Return the insubscribed circle's position, radius and norm vec from a triangle(p1,p2,p3)"""
    dist12 = np.sqrt(np.sum(np.square(point1-point2)))
    dist23 = np.sqrt(np.sum(np.square(point2-point3)))
    dist13 = np.sqrt(np.sum(np.square(point1-point3)))
    incenter = (dist12*point3 + dist23*point1 + dist13*point2)/(dist12+dist23+dist13)
    inradius = 0.5*np.sqrt((dist12+dist23-dist13)*
                            (dist12-dist23+dist13)*
                            (-dist12+dist23+dist13)/
                            (dist12+dist23+dist13))    
    axisvec = np.cross(point1-point2,point1-point3)
    normvec = axisvec/np.linalg.norm(axisvec)  
    L_1t12 = np.sqrt(np.square(np.linalg.norm(point1-incenter)) - np.square(inradius))  
    t12 = point1 + L_1t12 * (point2-point1) / np.linalg.norm(point2-point1)
    L_2t23 = np.sqrt(np.square(np.linalg.norm(point2-incenter)) - np.square(inradius))  
    t23 = point2 + L_2t23 * (point3-point2) / np.linalg.norm(point3-point2)
    L_3t31 = np.sqrt(np.square(np.linalg.norm(point3-incenter)) - np.square(inradius))  
    t31 = point3 + L_3t31 * (point1-point3) / np.linalg.norm(point1-point3)
    return incenter,inradius, normvec, t12, t23, t31

def circle_full(axis,start_v,radius,num_points):
    """Return drawing data of a full circle, need a drawing here. start_v is the any vector 
    paralel to first data point."""
    axis = axis/np.linalg.norm(axis)
    start_v = start_v/np.linalg.norm(start_v)
    theta = 2*np.pi
    theta_s = list(np.arange(0.0, theta + theta/num_points, theta/num_points))
    circle_vecs = np.zeros([len(theta_s),3])
    for i,thetai in enumerate(theta_s):
        makecir = rotation_matrix(axis,thetai)
        circle_vecs[i,:] = np.dot(makecir,start_v)
    return circle_vecs*radius

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


