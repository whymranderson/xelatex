# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:21:22 2014

Use GIT to restore and get previous cases figures.

@author: user
"""
import numpy as np
import matplotlib as mpl
mpl.use('pgf')
from matplotlib import pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.patches as pat
#from matplotlib.collections import PatchCollection

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
    
########
fig3 = plt.figure(3,figsize=(4, 2.6),dpi=100)
ax = plt.gca()

#line1, = plt.plot([0,0],[np.sqrt(3),0],[np.sqrt(3),1],[0,0])

pa = np.array([-0.5,0,0])
pb = np.array([0.5,0,0])
pc = (pa+pb)/2
pd = (pb+pc)/2
R=0.25
cm= np.array([0,R,0])

line1, = plt.plot([pa[0],pb[0]],[pa[1],pb[1]],'b')
line2, = plt.plot([pc[0],cm[0]],[pc[1],cm[1]],'k')
plt.text(0.5*cm[0],0.3*cm[1], r'$R$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')


angleb=np.array([0.7,1,0])

arc1 = (R+0.1)*circle_arc([0,0,-1],[0.01,0.1,0],angleb,10)+cm
larc1, = plt.plot(arc1[:,0],arc1[:,1],'k')
plt.text(2.2*cm[0]+0.1,2.2*cm[1]+0.05, r'$\alpha$', fontsize=20,verticalalignment='bottom', horizontalalignment='left')

arc2 = (R/2)*circle_arc([0,0,-1],[0,0.1,0],angleb,15)+cm
larc2, = plt.plot(arc2[:,0],arc2[:,1],'k')
plt.text(cm[0]+0.07,cm[1]+0.1, r'$\tau$', fontsize=20,verticalalignment='bottom', horizontalalignment='left')


cir2a = R*circle_arc([0,0,1],[1,0,0],[-1,0,0],20) + cm
larc2a, = plt.plot(cir2a[:,0],cir2a[:,1],'k') 
cir2b = R*circle_arc([0,0,1],[-1,0,0],[1,0,0],20) + cm
larc2b, = plt.plot(cir2b[:,0],cir2b[:,1],'k')
plt.text(cm[0],cm[1], r'$CM$', fontsize=14,verticalalignment='bottom', horizontalalignment='right')
plt.plot(cm[0],cm[1],'o')
plt.plot(pc[0],pc[1],'o')

vecfr = pd-pc
arrow1 = pat.FancyArrow(
    pc[0], pc[1], vecfr[0],vecfr[1], #increment
    width=0.018,        # Default
    head_width=0.08,    # Default: 3 * width
    head_length=0.09    # Default: 1.5 * head_width
)
ax.add_patch(arrow1)
plt.text(pd[0],pd[1]-0.05, r'$F_{fr}$', fontsize=20,verticalalignment='top', horizontalalignment='left')

arrow2 = pat.FancyArrow(
    cm[0], cm[1], pb[0]*2/3,0,#increment
    width=0.018,        # Default
    head_width=0.08,    # Default: 3 * width
    head_length=0.09,    # Default: 1.5 * head_width
    color = 'r'
)
ax.add_patch(arrow2)
plt.text(cm[0]+pb[0]*2/3,cm[1]-0.05, r'$a$', fontsize=20,verticalalignment='top', horizontalalignment='left',color='r')

anglebarrow = np.dot(rotation_matrix([0,0,-1],np.pi/2),(arc1[-1,:]-cm))/20
arrow3 = pat.FancyArrow(
    arc1[-1,0], arc1[-1,1], anglebarrow[0],anglebarrow[1],#increment
#    width=0.003,        # Default
    head_width=0.05,    # Default: 3 * width
    head_length=0.03,    # Default: 1.5 * head_width
    color = 'k'
)
ax.add_patch(arrow3)

arrow4 = pat.FancyArrow(
    arc2[-1,0], arc2[-1,1], anglebarrow[0],anglebarrow[1],#increment
#    width=0.003,        # Default
    head_width=0.05,    # Default: 3 * width
    head_length=0.03,    # Default: 1.5 * head_width
    color = 'k'
)
ax.add_patch(arrow4)



plt.axis('equal')
plt.axis('off')
########

########
plt.show()
fig3.savefig('case4b.pgf')#, facecolor=fig.get_facecolor(), edgecolor='none')