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
from annotate_program import solve_four_circles_on_sphere

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(6, 6),dpi=100)
ax2 = p3.Axes3D(fig2)
#ax2.view_init(elev=10, azim=187)
ax2.view_init(elev=10, azim=-130)
ax2.set_color_cycle('b')

pC = np.array([0,6,0])
pB = np.array([1,3.5,7])
pD = np.array([7,1.5,0])

#step 1, determine a sphere that insuscribed BCD
incenterBCD,inradiusBCD,normvecBCD, pE, pF, pN= incircle3D(pB,pC,pD)
pO = incenterBCD + 1.2*inradiusBCD*normvecBCD
sphereR = np.sqrt(np.square(1.2*inradiusBCD)+np.square(inradiusBCD))

#step 2, establish an somewhat arbitrary second incircle, with same tangent point N
#from incenterABD find pH and pG
angle = 69
tempM = rotation_matrix(pD-pN,np.radians(angle))
direction = np.dot(tempM,(pN-pO))*np.cos(np.radians(angle))
incenterABD = pO+direction#/np.linalg.norm(direction)*np.linalg.norm(incenterBCD-pO)+ pO
M4pH = rotmat_from_A_2_B(pN-incenterABD,pB-incenterABD)
pH = incenterABD + np.dot(M4pH,pB-incenterABD)/np.linalg.norm(pB-incenterABD)*np.linalg.norm(pN-incenterABD)
M4pG = rotmat_from_A_2_B(pN-pD,incenterABD-pD)
pG = pD + np.dot(M4pG,incenterABD-pD)/np.linalg.norm(pD-incenterABD)*np.linalg.norm(pN-pD)
##calculate third seg using x,y,z,r relation on wiki (Chu's resulte)
x,y,r = np.linalg.norm(pB-pH),np.linalg.norm(pN-pD),np.linalg.norm(pN-incenterABD)
z = third_seg_incircled(x,y,r)
pA = (pH-pB)/np.linalg.norm(pH-pB)*z + pH 
# realized AC will go through sphere. So there are restrictions here. Maybe sphereR has to be smaller than
# both incircle radius? or the angle between two triangles has to be greater than sphereR. Or combined.
# Should comeback and examine later. Restiction is four triangles formed by tangent points obtuse.

#from pE pH find inplane tangent circle
M90 = rotation_matrix(np.cross(pB-pC,pB-pA),np.pi/2)
cHE_pH = np.dot(M90,pB-pH)
n_cHE_pH = cHE_pH/np.linalg.norm(cHE_pH)
bb = np.linalg.norm(pB-pH)
aa = np.linalg.norm(pE-pH)/2
r_cirHE = bb/np.sqrt(np.square(bb/aa)-1)
centerHE = n_cHE_pH * r_cirHE + pH 

#find point M
pM = return_third_point_on_a_triagle_under_Ceva_Theorem(pA,pC,pB,pE,pH)
incenterACD,inradiusACD,normvecACD, pp, ppp, pppp= incircle3D(pA,pC,pD)

#lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
#lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
#lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')

# graph step one
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')
lineIbcdO, = ax2.plot(*zip(pO,incenterBCD),linewidth = 1,color='b',linestyle=':')
incircleBCD = circle_full(normvecBCD,
                          (-incenterBCD+pB),
                            inradiusBCD,40) + incenterBCD
ax2.plot(*np.transpose(incircleBCD),linewidth=1,linestyle='-')
plot_front(ax2,pO[0],pO[1],pO[2],sphereR)
plot_back(ax2,pO[0],pO[1],pO[2],sphereR)
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*incenterBCD, s = r"$I_{BCD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 2
incircleABD = circle_full(incenterABD-pO, pN-incenterABD, np.linalg.norm(pN-incenterABD), 30) + incenterABD
ax2.plot(*np.transpose(incircleABD),linewidth=1,linestyle='-')
lineIabdO, = ax2.plot(*zip(pO,incenterABD),linewidth = 1,color='b',linestyle=':')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*incenterABD, s = r"$I_{ABD}$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 3
circleHE = circle_full(np.cross(pB-pC,pB-pA), pH-centerHE, r_cirHE, 30) + centerHE
ax2.plot(*np.transpose(circleHE),linewidth=1,linestyle='-',color='b')
lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')

# graph step 4
ax2.text(*pM, s = r"$M$", fontsize=12,verticalalignment='top', horizontalalignment='right')
incenterACD,inradiusACD,normvecACD, pp, ppp, pppp= incircle3D(pA,pC,pD)
incircleACD = circle_full(incenterACD-pO, pF-incenterACD, np.linalg.norm(pF-incenterACD), 30) + incenterACD
ax2.plot(*np.transpose(incircleACD),linewidth=1,linestyle='-')#:')
ax2.text(*incenterACD, s = r"$I_{ACD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*centerHE, s = r"$I_{ABC}$", fontsize=12,verticalalignment='top', horizontalalignment='left')
lineIacdO, = ax2.plot(*zip(pO,incenterACD),linewidth = 1,color='b',linestyle=':')
lineIabcO, = ax2.plot(*zip(pO,centerHE),linewidth = 1,color='b',linestyle=':')

lineIabcE, = ax2.plot(*zip(pE,   centerHE),linewidth = 1,color='k',linestyle=':')
lineIabdN, = ax2.plot(*zip(pN,incenterABD),linewidth = 1,color='k',linestyle=':')
lineIbcdN, = ax2.plot(*zip(pN,incenterBCD),linewidth = 1,color='k',linestyle=':')
lineIabcG, = ax2.plot(*zip(pG,incenterACD),linewidth = 1,color='k',linestyle=':')

ax2.text(*(pE+   centerHE)/2, s = r"$r_1$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pN+incenterABD)/2, s = r"$r_4$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pN+incenterBCD)/2, s = r"$r_2$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pG+incenterACD)/2, s = r"$r_3$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pA+pG)/2, s = r"$a$", fontsize=12,verticalalignment='top', horizontalalignment='left',color='r')
ax2.text(*(pB+pN)/2, s = r"$b$", fontsize=12,verticalalignment='bottom', horizontalalignment='left',color='r')
ax2.text(*(pC+pE)/2, s = r"$c$", fontsize=12,verticalalignment='bottom', horizontalalignment='right',color='r')
ax2.text(*(pD+pG)/2, s = r"$d$", fontsize=12,verticalalignment='top', horizontalalignment='left',color='r')
#ax2.scatter3D(*zip(pJ,pK,pL,pI,pO,pM,pN,pH,pG,pE,pF))

# solve two roots
r3 = inradiusACD
r4 = np.linalg.norm(pN-incenterABD)
r2 = inradiusBCD
r1 = np.linalg.norm(pH-centerHE)
c = np.linalg.norm(pA-pG)
two_a, two_b, two_d, two_r2= solve_four_circles_on_sphere(r1, r3, r4, c)

pC2nd = pM - two_b[1]*(pA-pM)/np.linalg.norm(pA-pM)
pB2nd = pH - two_a[1]*(pA-pH)/np.linalg.norm(pA-pH)
pD2nd = pG - two_d[1]*(pA-pG)/np.linalg.norm(pA-pG)

lineCB2nd, = ax2.plot(*zip(pC2nd,pB2nd),linewidth = 2,color='r')#,linestyle=':')
lineDB2nd, = ax2.plot(*zip(pD2nd,pB2nd),linewidth = 2,color='r')#,linestyle=':')
lineCD2nd, = ax2.plot(*zip(pC2nd,pD2nd),linewidth = 2,color='r')#,linestyle=':')
incenter2ndr2,inradius2ndr2,normvec2ndr2, pCD2ndmid, _, _= incircle3D(pC2nd,pD2nd,pB2nd)
incircle2ndr2 = circle_full(normvec2ndr2,
                          (-incenter2ndr2+pB2nd),
                            inradius2ndr2,40) + incenter2ndr2
ax2.plot(*np.transpose(incircle2ndr2),linewidth=1.5,linestyle=':',color='r')
line2ndr2, = ax2.plot(*zip(incenter2ndr2, pCD2ndmid),linewidth = 1,color='r',linestyle=':')
ax2.text(*(incenter2ndr2+ pCD2ndmid)/2, s = r"$r^*_2$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*incenter2ndr2, s = r"$I_{2nd}$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')

#draw coordinate
#draw_xyz_coordinate_unit_vectors(ax2)


Xt,Yt,Zt = zip(pO,pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 4.0


mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5 + 0.6
mid_z = (Z.max()+Z.min()) * 0.5 - 0.6
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


