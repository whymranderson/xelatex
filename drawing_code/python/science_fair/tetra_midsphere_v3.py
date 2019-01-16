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
fig2 = pyplot.figure(2,figsize=(6,6),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=2, azim=106)
#ax2.view_init(elev=10, azim=-130)
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

#find division circle


#lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
#lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
#lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')

# graph step one
#lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
#lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
#lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')
#lineIbcdO, = ax2.plot(*zip(pO,incenterBCD),linewidth = 1,color='b',linestyle=':')
incircleBCD = circle_full(normvecBCD,
                          (-incenterBCD+pB),
                            inradiusBCD,40) + incenterBCD
#ax2.plot(*np.transpose(incircleBCD),linewidth=1,linestyle=':')
plot_front(ax2,pO[0],pO[1],pO[2],sphereR)
plot_back(ax2,pO[0],pO[1],pO[2],sphereR)
#ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='right')
#ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='top', horizontalalignment='right')
#ax2.text(*pE, s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
#ax2.text(*pF, s = r"$F$", fontsize=12,verticalalignment='top', horizontalalignment='right')
#ax2.text(*incenterBCD, s = r"$I_{BCD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 2
incircleABD = circle_full(incenterABD-pO, pN-incenterABD, np.linalg.norm(pN-incenterABD), 30) + incenterABD
ax2.plot(*np.transpose(incircleABD),linewidth=2,linestyle='-')
#lineIabdO, = ax2.plot(*zip(pO,incenterABD),linewidth = 1,color='b',linestyle=':')
#lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
#lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
#ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
#ax2.text(*pG, s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*incenterABD, s = r"$I_{ABD}$", fontsize=12,verticalalignment='top', horizontalalignment='left')

# graph step 3
circleHE = circle_full(np.cross(pB-pC,pB-pA), pH-centerHE, r_cirHE, 30) + centerHE
ax2.plot(*np.transpose(circleHE),linewidth=2,linestyle='-',color='b')
#lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')

# graph step 4
#ax2.text(*pM, s = r"$M$", fontsize=12,verticalalignment='top', horizontalalignment='right')
incenterACD,inradiusACD,normvecACD, pp, ppp, pppp= incircle3D(pA,pC,pD)
incircleACD = circle_full(incenterACD-pO, pF-incenterACD, np.linalg.norm(pF-incenterACD), 30) + incenterACD
#ax2.plot(*np.transpose(incircleACD),linewidth=1,linestyle='-')#:')
#ax2.text(*incenterACD, s = r"$I_{ACD}$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*centerHE, s = r"$I_{ABC}$", fontsize=12,verticalalignment='top', horizontalalignment='left')
#lineIacdO, = ax2.plot(*zip(pO,incenterACD),linewidth = 1,color='b',linestyle=':')
#lineIabcO, = ax2.plot(*zip(pO,centerHE),linewidth = 1,color='b',linestyle=':')


# graph diabeter of two circles connecting H
pH1 = pH+2*(incenterABD-pH)
pH2 = pH+2*(centerHE-pH)
lineHdiaIabd, = ax2.plot(*zip(pH,pH+2*(incenterABD-pH)),linewidth = 1,color='g')
lineHdiaIabc, = ax2.plot(*zip(pH,pH+2*(centerHE-pH)),linewidth = 1,color='g')
bigcHperp = circle_full(np.cross(incenterABD-pO,centerHE-pO),
                        pH-pO, np.linalg.norm(pH-pO), 40) + pO
ax2.plot(*np.transpose(bigcHperp),linewidth=1,linestyle='-',color='g')#:')

pHmid = (pH1-pO+pH2-pO)/2
pHmid = pHmid/np.linalg.norm(pHmid)
pHmid = pO + np.linalg.norm(pH-pO)*pHmid

ax2.text(*pH1, s = r"$H_1$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pH2, s = r"$H_2$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pHmid, s = r"$H_{mid}$", fontsize=12,verticalalignment='top', horizontalalignment='right')

lineOH, = ax2.plot(*zip(pO,pH),linewidth = 1,color='b')
lineOH1, = ax2.plot(*zip(pO,pH1),linewidth = 1,color='b')
lineOH2, = ax2.plot(*zip(pO,pH2),linewidth = 1,color='b')
lineOHmid, = ax2.plot(*zip(pO,pHmid),linewidth = 1,color='b')

dt_ABD = pO + np.linalg.norm(pH-pO)*(incenterABD-pO)/np.linalg.norm(incenterABD-pO)#doom top
dt_ABC = pO + np.linalg.norm(pH-pO)*(centerHE-pO)/np.linalg.norm(centerHE-pO)#doom top
linedtABD, = ax2.plot(*zip(pO,dt_ABD),linewidth = 1,color='b',linestyle=':')
linedtABC, = ax2.plot(*zip(pO,dt_ABC),linewidth = 1,color='b',linestyle=':')

ax2.text(*dt_ABD, s = r"$t_{ABD}$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*dt_ABC, s = r"$t_{ABC}$", fontsize=12,verticalalignment='top', horizontalalignment='right')

ax2.scatter3D(*zip(pH,pH1,pH2,pHmid,pO,centerHE,incenterABD,dt_ABD,dt_ABC,))

#graph division circle
divCircle = circle_full(pHmid-pO+pH-pO,pHmid-pH,
                        np.linalg.norm(pHmid-pH)/2,  40) + (pHmid+pH)/2
ax2.plot(*np.transpose(divCircle),linewidth=1,linestyle='-',color='k')#:')
#draw coordinate
#draw_xyz_coordinate_unit_vectors(ax2)


Xt,Yt,Zt = zip(pO,pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 5.0


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


