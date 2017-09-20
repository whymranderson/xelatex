# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:32:24 2015

@author: http://whymranderson.blogspot.tw/
"""

import numpy as np
import matplotlib as mpl
mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
#import matplotlib.axis as axis1
from mpl_toolkits.mplot3d import proj3d
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

def circle_full(axis,start_v,radius,num_points):
    axis = axis/np.linalg.norm(axis)
    start_v = start_v/np.linalg.norm(start_v)
    theta = 2*np.pi
    theta_s = list(np.arange(0.0, theta + theta/num_points, theta/num_points))
    circle_vecs = np.zeros([len(theta_s),3])
    for i,thetai in enumerate(theta_s):
        makecir = rotation_matrix(axis,thetai)
        circle_vecs[i,:] = np.dot(makecir,start_v)
    return circle_vecs*radius

def four_points_circle(p1,p2,p3,p4):
    x2y2z2=0
    M = np.array([[x2y2z2,p1[0],p1[1],p1[2],1],
                  [np.sum(np.square(p1)),p1[0],p1[1],p1[2],1],
                  [np.sum(np.square(p2)),p2[0],p2[1],p2[2],1],
                  [np.sum(np.square(p3)),p3[0],p3[1],p3[2],1],
                  [np.sum(np.square(p4)),p4[0],p4[1],p4[2],1]])    
    M11 = M[1:,1:]
    M11d = np.linalg.det(M11)
    M12 = np.array([
                  [np.sum(np.square(p1)),p1[1],p1[2],1],
                  [np.sum(np.square(p2)),p2[1],p2[2],1],
                  [np.sum(np.square(p3)),p3[1],p3[2],1],
                  [np.sum(np.square(p4)),p4[1],p4[2],1]]) 
    M12d = np.linalg.det(M12)
    x0 = 0.5*M12d/M11d
    M13 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[2],1],
                  [np.sum(np.square(p2)),p2[0],p2[2],1],
                  [np.sum(np.square(p3)),p3[0],p3[2],1],
                  [np.sum(np.square(p4)),p4[0],p4[2],1]])    
    M13d = np.linalg.det(M13)
    y0 = -0.5*M13d/M11d

    M14 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[1],1],
                  [np.sum(np.square(p2)),p2[0],p2[1],1],
                  [np.sum(np.square(p3)),p3[0],p3[1],1],
                  [np.sum(np.square(p4)),p4[0],p4[1],1]])    
    M14d = np.linalg.det(M14)
    z0 = 0.5*M14d/M11d
    M15 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[1],p1[2]],
                  [np.sum(np.square(p2)),p2[0],p2[1],p2[2]],
                  [np.sum(np.square(p3)),p3[0],p3[1],p3[2]],
                  [np.sum(np.square(p4)),p4[0],p4[1],p4[2]]])    
    M15d = np.linalg.det(M15)
    R = np.sqrt(x0**2+y0**2+z0**2-M15d/M11d)
    return x0,y0,z0,R

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


########
fig3 = pyplot.figure(3,figsize=(6,6),dpi=100)
ax3 = p3.Axes3D(fig3)
ax3.view_init(elev=15, azim=15)
ax3.set_color_cycle('b')
########

########
pointA = np.array([0.5/np.sqrt(3.0)   ,.5     ,1.3])
pointB = np.array([0     ,1      ,0])
pointC = np.array([0.5*np.sqrt(3.0)     ,.5    ,0])
pointD = np.array([0     ,0      ,0])
########

########
lineAB = ax3.plot(*zip(pointA,pointB))
lineBC = ax3.plot(*zip(pointC,pointB))
lineDB = ax3.plot(*zip(pointD,pointB))
lineAC = ax3.plot(*zip(pointA,pointC))
lineCD = ax3.plot(*zip(pointC,pointD))
lineAD = ax3.plot(*zip(pointA,pointD))
########

########
ax3.text(0.5,.5,1.3,'A')
ax3.text(0     ,1      ,0,'B')
ax3.text(1     ,0.5    ,0,'C')
ax3.text(0     ,0      ,0,'D')
########

def incircle3D(point1,point2,point3):
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
    return incenter,inradius, normvec

########    
incenterABC,inradiusABC,normvecABC= incircle3D(pointA,pointB,pointC)
ax3.scatter(*incenterABC)
incircleABC = circle_full(normvecABC,
                          (-incenterABC+pointA),
                            inradiusABC,40) + incenterABC
ax3.plot(*np.transpose(incircleABC),linewidth=0.5)

incenterBCD,inradiusBCD,normvecBCD= incircle3D(pointB,pointC,pointD)
ax3.scatter(*incenterBCD)
incircleBCD = circle_full(normvecBCD,
                          (-incenterBCD+pointB),
                            inradiusBCD,40) + incenterBCD
ax3.plot(*np.transpose(incircleBCD),linewidth=0.5)

incenterACD,inradiusACD,normvecACD= incircle3D(pointA,pointC,pointD)
ax3.scatter(*incenterACD)
incircleACD = circle_full(normvecACD,
                          (-incenterACD+pointA),
                            inradiusACD,40) + incenterACD
ax3.plot(*np.transpose(incircleACD),linewidth=0.5)

incenterBAD,inradiusBAD,normvecBAD= incircle3D(pointB,pointA,pointD)
ax3.scatter(*incenterBAD)
incircleBAD = circle_full(normvecBAD,
                          (-incenterBAD+pointB),
                            inradiusBAD,40) + incenterBAD
ax3.plot(*np.transpose(incircleBAD),linewidth=0.5)
########

########
midspherex,midspherey,midspherez,midsphereR = four_points_circle(incircleABC[0,:],incircleABC[10,:],incircleABC[20,:],incircleBCD[10,:])

lineAin = ax3.plot(*zip(pointA,incenterBCD))
lineBin = ax3.plot(*zip(pointB,incenterACD))
lineDin = ax3.plot(*zip(pointD,incenterABC))
lineCin = ax3.plot(*zip(pointC,incenterBAD))

########
ax3.tick_params(labelbottom='off', labeltop='off', labelleft='off', labelright='off')
ax3.set_xlim(0,1)
ax3.set_ylim(0,1)
ax3.set_zlim(0,1)
########


plot_front(ax3,midspherex,midspherey,midspherez,midsphereR)
plot_back(ax3,midspherex,midspherey,midspherez,midsphereR)
########

ax3.scatter(midspherex,midspherey,midspherez,color='red')