# -*- coding: utf-8 -*-

#Start from a traigle BCD, all three vertice known. Assume we are given a vector CA but we
#don't know the position of A, but we know the direction of CA. We can construct one and only one 
#sphere that tangents to three segments of BCD and CA then from this sphere we will find segs 
#BA and DA that tangents the shpere and determine the position of A.

import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
from mpl_toolkits.mplot3d import proj3d

import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import return_third_point_on_a_triagle_under_Ceva_Theorem
from annotate_program import return_intersection_under_Ceva_Theorem
from annotate_program import return_Menelaus_third_outer_point
from annotate_program import triangle_area
from annotate_program import plot_front
from annotate_program import plot_back
from annotate_program import project_a_point_to_a_plane 
from annotate_program import incircle3D 
from annotate_program import circle_full
from annotate_program import four_points_circle
from annotate_program import rotmat_from_A_2_B
from annotate_program import CK
from annotate_program import circle_full
from annotate_program import third_seg_incircled
from annotate_program import rotation_matrix
from annotate_program import draw_xyz_coordinate_unit_vectors
from annotate_program import draw_perpendicular_sign
from annotate_program import solve_four_circles_on_sphere
from annotate_program import return_vertex_under_ceva

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(5, 5),dpi=100)
ax2 = p3.Axes3D(fig2)
#ax2.view_init(elev=10, azim=187)
ax2.view_init(azim=-67,elev=3)
#ax2.view_init(azim=23,elev=-18)#very_long_tetra_inscribed_possible_3.png
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
pA = np.array([2,0,0])
pC = np.array([-1,-1.732,0])
pD = np.array([-1,1.732,0])
pB = np.array([0,0,1]) 

#lineBA = ax2.plot(*zip(pB,pA),linewidth = 2,color='b')
#lineBC = ax2.plot(*zip(pB,pC),linewidth = 2,color='b')
#lineDB = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

#step 1, determine vector BO
#first determine a segment length BN, or fix a N
len_a = 1
pN = pB + len_a*(pD-pB)/np.linalg.norm(pD-pB)
# this will fix E and H
pH = pB + len_a*(pA-pB)/np.linalg.norm(pA-pB)
pE = pB + len_a*(pC-pB)/np.linalg.norm(pC-pB)
#to find Htemp1,2, first find incenter
midHN = (pN + pH)/2
n_BmidHN = (midHN-pB)/np.linalg.norm(midHN-pB)
amp_BIabd=np.linalg.norm(pN-pB) * np.linalg.norm(pB-pN)/np.linalg.norm(midHN-pB)
incenterABD = pB + amp_BIabd*n_BmidHN
midHE = (pE + pH)/2
n_BmidHE = (midHE-pB)/np.linalg.norm(midHE-pB)
amp_BIabc=np.linalg.norm(pE-pB) * np.linalg.norm(pB-pE)/np.linalg.norm(midHE-pB)
incenterABC = pB + amp_BIabc*n_BmidHE
midNE = (pE + pN)/2
n_BmidNE = (midNE-pB)/np.linalg.norm(midNE-pB)
amp_BIbcd=np.linalg.norm(pE-pB) * np.linalg.norm(pB-pE)/np.linalg.norm(midNE-pB)
incenterBCD = pB + amp_BIbcd*n_BmidNE
# to find O, first find Htemp
r1 = incenterABD-pH
r1n = r1/np.linalg.norm(r1)
r2 = incenterABC-pH
r2n = r2/np.linalg.norm(r2)
cos_alpha = np.dot(r1n,r2n)
pHtemp1 = pH + (np.linalg.norm(r1)/cos_alpha)*r2n
pHtemp2 = pH + (np.linalg.norm(r2)/cos_alpha)*r1n
# if IabdHIabc>90 degree, can't use the following, have to use similar triangle to find O
# if < 90, fine
#pO =return_intersection_under_Ceva_Theorem(pHtemp2,pHtemp1,pH,incenterABC,incenterABD)
ampOH1 = np.linalg.norm(incenterABC-pHtemp1)*np.linalg.norm(pH-pHtemp1)/np.linalg.norm(incenterABD-pHtemp1)
pO = pHtemp1 + (incenterABD-pHtemp1)/np.linalg.norm(incenterABD-pHtemp1)*ampOH1

plot_front(ax2,pO[0],pO[1],pO[2],np.linalg.norm(pO-pH))
plot_back(ax2,pO[0],pO[1],pO[2],np.linalg.norm(pO-pH))

#graph step 1
#lineIabdO = ax2.plot(*zip(incenterABD,pO),linewidth = 2,color='b')
#lineIabcO = ax2.plot(*zip(incenterABC,pO),linewidth = 2,color='b')

#ax2.text(*pH, s = r'$H$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pO, s = r'$O$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*pN, s = r'$N$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*pE, s = r'$E$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*incenterABC, s = r'$I_{abc}$', fontsize=12,verticalalignment='bottom', horizontalalignment='left')
#ax2.text(*incenterABD, s = r'$I_{abd}$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#draw_perpendicular_sign(np.cross(r1,r2), -r2, pHtemp2-incenterABC, incenterABC, ax2, 0.2)
#draw_perpendicular_sign(np.cross(r1,r2),pHtemp1-incenterABD, -r1, incenterABD, ax2, 0.2)

ax2.scatter3D(*zip(pO))

incircleABD = circle_full(incenterABD-pO, pN-incenterABD, np.linalg.norm(pN-incenterABD), 30) + incenterABD
ax2.plot(*np.transpose(incircleABD),linewidth=1,linestyle=':')
incircleABC = circle_full(incenterABC-pO, pH-incenterABC, np.linalg.norm(pH-incenterABC), 30) + incenterABC
ax2.plot(*np.transpose(incircleABC),linewidth=1,linestyle=':')
incircleBCD = circle_full(incenterBCD-pO, pN-incenterBCD, np.linalg.norm(pN-incenterBCD), 30) + incenterBCD
ax2.plot(*np.transpose(incircleBCD),linewidth=1,linestyle=':')

r1 = np.linalg.norm(pH-incenterABD)
r2 = np.linalg.norm(pH-incenterABC)
r3 = np.linalg.norm(pN-incenterBCD)
c = np.linalg.norm(pH-pB)

a_roots, _, _,_ =  solve_four_circles_on_sphere(r1,r3,r2,c)
print a_roots
a = 3.4367153
b = (r1**2)*(a+c)/(a*c-(r1**2))
d = (r2**2)*(a+c)/(a*c-(r2**2))
r4 = np.sqrt(d*a*b/(d+a+b))

pDD = pN + b * (pN-pB)/np.linalg.norm(pN-pB)
pAA = pH + a * (pH-pB)/np.linalg.norm(pH-pB)
pCC = pE + d * (pE-pB)/np.linalg.norm(pE-pB)
lineAADD = ax2.plot(*zip(pAA,pDD),linewidth = 2,color='b')
lineAACC = ax2.plot(*zip(pAA,pCC),linewidth = 2,color='b')
lineDDCC = ax2.plot(*zip(pDD,pCC),linewidth = 2,color='b')
lineBCC = ax2.plot(*zip(pB,pCC),linewidth = 2,color='b')
lineBAA = ax2.plot(*zip(pB,pAA),linewidth = 2,color='b')
lineBDD = ax2.plot(*zip(pB,pDD),linewidth = 2,color='b')
ax2.text(*pCC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pDD, s = r'$D$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pAA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')

incenterACD, _, _,pF,_,_ = incircle3D(pDD,pCC,pAA) 
incircleACD = circle_full(incenterACD-pO, pF-incenterACD, np.linalg.norm(pF-incenterACD), 30) + incenterACD
ax2.plot(*np.transpose(incircleACD),linewidth=1,linestyle=':')
# Add transparent faces
#vt1 = [pA,pB,pD]
#tr1 = p3.art3d.Poly3DCollection([vt1],color = 'r', alpha=0.3)
#tr1.set_facecolor('r')
#ax2.add_collection3d(tr1)

#draw coordinate
#draw_xyz_coordinate_unit_vectors(ax2)


Xt,Yt,Zt = zip(pO,pA,pB,pC,pD)
#Xt,Yt,Zt = zip(pH,pHtemp1,pHtemp2,pB)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 1.6


mid_x = (X.max()+X.min()) * 0.5 - 0.25
mid_y = (Y.max()+Y.min()) * 0.5 
mid_z = (Z.max()+Z.min()) * 0.5 - 0.5
ax2.set_xlim3d(mid_x - max_range, mid_x + max_range)
ax2.set_ylim3d(mid_y - max_range, mid_y + max_range)
ax2.set_zlim3d(mid_z - max_range, mid_z + max_range)


ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.w_xaxis.line.set_visible(False) #turn off axis visibility
ax2.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax2.w_zaxis.line.set_color([0,0,0,0])
ax2.set_axis_off()  #-> this can turn off the background curtain
#pyplot.savefig('./pgf_files/tetra_midsphere.pgf')

pyplot.show()


