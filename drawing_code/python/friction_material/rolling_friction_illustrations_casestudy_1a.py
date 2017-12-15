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
fig3 = plt.figure(3,figsize=(3,3),dpi=100)
ax = plt.gca()

#line1, = plt.plot([0,0],[np.sqrt(3),0],[np.sqrt(3),1],[0,0])

pa = np.array([0,0,0])
pb = np.array([np.sqrt(3),0,0])
pc = np.array([np.sqrt(3),1,0])

line1, = plt.plot([0,np.sqrt(3)],[0,0],'b')
line2, = plt.plot([np.sqrt(3),np.sqrt(3)],[0,1],'b')
line3, = plt.plot([0,np.sqrt(3)],[0,1],'b')

arc1 = 0.1*circle_arc([0,0,1],[1,0,0],[np.sqrt(3),1,0],10)
larc1, = plt.plot(arc1[:,0],arc1[:,1],'k')
plt.text(arc1[0,0]+0.1,arc1[0,1], r'$\theta$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='left')

tangentp = pc/2
perpen = pc*3/4
po = perpen - pb
po = po/np.linalg.norm(po)
cm = tangentp + 0.4*po
cir2a = 0.4*circle_arc([0,0,1],[1,0,0],[-1,0,0],20) + cm
larc2a, = plt.plot(cir2a[:,0],cir2a[:,1],'k') 
cir2b = 0.4*circle_arc([0,0,1],[-1,0,0],[1,0,0],20) + cm
larc2b, = plt.plot(cir2b[:,0],cir2b[:,1],'k')
plt.text(cm[0],cm[1], r'$CM$', fontsize=14,verticalalignment='bottom', 
         horizontalalignment='right')
plt.plot(cm[0],cm[1],'o')
plt.plot(tangentp[0],tangentp[1],'o')

vecfr = 0.5*(pc-tangentp)
#arrow1 = pat.FancyArrow(
#    tangentp[0], tangentp[1], vecfr[0],vecfr[1], #increment
#    width=0.018,        # Default
#    head_width=0.08,    # Default: 3 * width
#    head_length=0.09    # Default: 1.5 * head_width
#)
#ax.add_patch(arrow1)
#plt.text((tangentp[0]+vecfr[0]),(tangentp[1]+vecfr[1]), r'$F_{fr}$', 
#         fontsize=14,verticalalignment='top', horizontalalignment='left')

arrow2 = pat.FancyArrow(
    cm[0], cm[1], 0,-cm[1]*2/3,#increment
    width=0.018,        # Default
    head_width=0.08,    # Default: 3 * width
    head_length=0.09    # Default: 1.5 * head_width
)
ax.add_patch(arrow2)
plt.text(cm[0],cm[1]/3, r'$mg$', fontsize=14,verticalalignment='top', 
         horizontalalignment='left')

arrow3p1 = cm + po/2
arrow3 = pat.FancyArrow(
    arrow3p1[0], arrow3p1[1], vecfr[0],vecfr[1],#increment
    width=0.05,        # Default
    head_width=0.2,    # Default: 3 * width
    head_length=0.12,    # Default: 1.5 * head_width
    color = 'r'
)
ax.add_patch(arrow3)
plt.text(arrow3p1[0]+vecfr[0],arrow3p1[1]+vecfr[1]+0.1, r'$a$', 
         fontsize=14,verticalalignment='bottom', horizontalalignment='left')

arrow4 = pat.FancyArrow(
    cm[0], cm[1], vecfr[0],vecfr[1], #increment
    width=0.018,        # Default
    head_width=0.08,    # Default: 3 * width
    head_length=0.09    # Default: 1.5 * head_width
)
ax.add_patch(arrow4)
plt.text((cm[0]+vecfr[0]),(cm[1]+vecfr[1]), r'$F_{p}$', 
         fontsize=14,verticalalignment='top', horizontalalignment='left')


plt.axis('off')
#plt.axis('image')
plt.axis([0,1.8,-0.2,1.6])
########

########
plt.show()
#fig3.savefig('friction_study1a.pgf')#, facecolor=fig.get_facecolor(), edgecolor='none')