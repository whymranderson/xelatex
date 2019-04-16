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

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(6, 6),dpi=100)
ax2 = p3.Axes3D(fig2)
#ax2.view_init(elev=10, azim=187)
ax2.view_init(elev=10, azim=-130)
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

pC = np.array([0,6,0])
pB = np.array([1,3.5,7])
pD = np.array([7,1.5,0])

#step 1, determine a sphere that insuscribed BCD
incenterBCD,inradiusBCD,normvecBCD, pE, pF, pN= incircle3D(pB,pC,pD)
pO = incenterBCD + 1.2*inradiusBCD*normvecBCD
sphereR = np.sqrt(np.square(1.2*inradiusBCD)+np.square(inradiusBCD))

#step 2, establish an somewhat arbitrary second incircle, with same tangent point N
#tempM = rotmat_from_A_2_B(incenterBCD-pO,pN-pO)
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
#lineIbcdO, = ax2.plot(*zip(pO,incenterBCD),linewidth = 1,color='b',linestyle=':')
incircleBCD = circle_full(normvecBCD,
                          (-incenterBCD+pB),
                            inradiusBCD,40) + incenterBCD
ax2.plot(*np.transpose(incircleBCD),linewidth=1,linestyle=':')
#plot_front(ax2,pO[0],pO[1],pO[2],sphereR)
#plot_back(ax2,pO[0],pO[1],pO[2],sphereR)
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*incenterBCD, s = r"$I_{BCD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
#ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 2
incircleABD = circle_full(incenterABD-pO, pN-incenterABD, np.linalg.norm(pN-incenterABD), 30) + incenterABD
#ax2.plot(*np.transpose(incircleABD),linewidth=1,linestyle=':')
#lineIabdO, = ax2.plot(*zip(pO,incenterABD),linewidth = 1,color='b',linestyle=':')
#lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
#lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
#ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='top', horizontalalignment='right')
#ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
#ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#ax2.text(*incenterABD, s = r"$I_{ABD}$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 3
circleHE = circle_full(np.cross(pB-pC,pB-pA), pH-centerHE, r_cirHE, 30) + centerHE
#ax2.plot(*np.transpose(circleHE),linewidth=1,linestyle=':',color='r')
#lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')

# graph step 4
#ax2.text(*pM, s = r"$M$", fontsize=12,verticalalignment='top', horizontalalignment='right')
incenterACD,inradiusACD,normvecACD, pp, ppp, pppp= incircle3D(pA,pC,pD)
incircleACD = circle_full(incenterACD-pO, pF-incenterACD, np.linalg.norm(pF-incenterACD), 30) + incenterACD
#ax2.plot(*np.transpose(incircleACD),linewidth=1,linestyle=':')
#ax2.text(*incenterACD, s = r"$I_{ACD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*centerHE, s = r"$I_{ABC}$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#lineIacdO, = ax2.plot(*zip(pO,incenterACD),linewidth = 1,color='b',linestyle=':')
#lineIabcO, = ax2.plot(*zip(pO,centerHE),linewidth = 1,color='b',linestyle=':')

#ax2.scatter3D(*zip(pJ,pK,pL,pI,pO,pM,pN,pH,pG,pE,pF))

#graph vertice and center connections
#lineHN, = ax2.plot(*zip(pH,pN),linewidth = 1,color='k')
#lineBIabd, = ax2.plot(*zip(pB,incenterABD),linewidth = 1,color='k')
#lineBO, = ax2.plot(*zip(pB,pO),linewidth = 1,color='k')
#lineHO, = ax2.plot(*zip(pH,pO),linewidth = 1,color='k')
#lineNO, = ax2.plot(*zip(pN,pO),linewidth = 1,color='k')
#lineNIabd, = ax2.plot(*zip(pN,incenterABD),linewidth = 1,color='k')
#lineHIabd, = ax2.plot(*zip(pH,incenterABD),linewidth = 1,color='k')

#planarization
angle1= np.arccos(np.dot((incenterABD-pO)/np.linalg.norm(incenterABD-pO),(incenterBCD-pO)/np.linalg.norm(incenterBCD-pO)))
pAp1 = pD + np.dot(rotation_matrix(pB-pD,angle1),pA-pD)
lineAp1B, = ax2.plot(*zip(pAp1,pB),linewidth = 2,color='b')
lineAp1D, = ax2.plot(*zip(pAp1,pD),linewidth = 2,color='b')
incenterABDp,inradiusABDp,normvecABDp, _, _, _= incircle3D(pB,pD,pAp1)
incircleABDp = circle_full(incenterBCD-pO, pN-incenterABDp, inradiusABDp, 60) + incenterABDp
ax2.plot(*np.transpose(incircleABDp),linewidth=1,linestyle=':')
ax2.text(*incenterABDp, s = r"$I'_{ABD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pAp1, s = r"$A'_1$", fontsize=12,verticalalignment='top', horizontalalignment='left')

incenterABC=centerHE
angle2= np.arccos(np.dot((incenterABC-pO)/np.linalg.norm(incenterABC-pO),(incenterBCD-pO)/np.linalg.norm(incenterBCD-pO)))
pAp2 = pC + np.dot(rotation_matrix(pB-pC,-angle2),pA-pC)
lineAp2B, = ax2.plot(*zip(pAp2,pB),linewidth = 2,color='b')
lineAp2C, = ax2.plot(*zip(pAp2,pC),linewidth = 2,color='b')
incenterABCp,inradiusABCp,normvecABCp, _, _, _= incircle3D(pB,pC,pAp2)
incircleABCp = circle_full(incenterBCD-pO, pE-incenterABCp, inradiusABCp, 60) + incenterABCp
ax2.plot(*np.transpose(incircleABCp),linewidth=1,linestyle=':')
ax2.text(*incenterABCp, s = r"$I'_{ABC}$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pAp2, s = r"$A'_2$", fontsize=12,verticalalignment='top', horizontalalignment='right')

angle3= np.arccos(np.dot((incenterACD-pO)/np.linalg.norm(incenterACD-pO),(incenterBCD-pO)/np.linalg.norm(incenterBCD-pO)))
pAp3 = pC + np.dot(rotation_matrix(pD-pC,angle3),pA-pC)
lineAp3B, = ax2.plot(*zip(pAp3,pD),linewidth = 2,color='b')
lineAp3C, = ax2.plot(*zip(pAp3,pC),linewidth = 2,color='b')
incenterACDp,inradiusACDp,normvecACDp, _, _, _= incircle3D(pC,pD,pAp3)
incircleACDp = circle_full(incenterBCD-pO, pE-incenterACDp, inradiusACDp, 60) + incenterACDp
ax2.plot(*np.transpose(incircleACDp),linewidth=1,linestyle=':')
ax2.text(*incenterACDp, s = r"$I'_{ACD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pAp3, s = r"$A'_3$", fontsize=12,verticalalignment='top', horizontalalignment='left')

ax2.scatter3D()

# Add transparent faces
#vt1 = [pA,pB,pD]
#tr1 = p3.art3d.Poly3DCollection([vt1],color = 'r', alpha=0.3)
#tr1.set_facecolor('r')
#ax2.add_collection3d(tr1)

#draw coordinate
#draw_xyz_coordinate_unit_vectors(ax2)


Xt,Yt,Zt = zip(pO,pA,pB,pC,pD,pAp1,pAp2,pAp3)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 3.0


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


