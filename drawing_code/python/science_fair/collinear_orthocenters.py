# -*- coding: utf-8 -*-

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
from annotate_program import triangle_area
from annotate_program import plot_front
from annotate_program import plot_back
from annotate_program import project_a_point_to_a_plane 
from annotate_program import incircle3D 
from annotate_program import circle_full
from annotate_program import four_points_circle
from annotate_program import return_orthocenter
from annotate_program import return_9point_circle_center
from annotate_program import draw_xyz_coordinate_unit_vectors

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(6, 6),dpi=100)
ax2 = p3.Axes3D(fig2)
#ax2.view_init(elev=10, azim=187)
ax2.view_init(elev=20, azim=7)
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
#pC = (pD+pC)/2

pJ = return_orthocenter(pB,pC,pD)
pE = project_a_point_to_a_plane(pD,np.cross(pB-pC,pD-pC),pB-pC,pC)
pF = project_a_point_to_a_plane(pB,np.cross(pC-pD,pB-pD),pC-pD,pD)
pN = return_third_point_on_a_triagle_under_Ceva_Theorem(pB,pD,pC,pF,pE)
#pA = pJ + 15 * np.cross(pB-pD,pC-pD)/np.linalg.norm(np.cross(pB-pD,pC-pD)) 
pA = pJ + 10 * np.cross(pB-pD,pC-pD)/np.linalg.norm(np.cross(pB-pD,pC-pD)) 
pH = project_a_point_to_a_plane(pD,np.cross(pA-pB,pD-pB),pA-pB,pB)
pG = return_third_point_on_a_triagle_under_Ceva_Theorem(pA,pD,pB,pN,pH)
pM = return_third_point_on_a_triagle_under_Ceva_Theorem(pA,pC,pB,pE,pH)


lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')


pK = return_intersection_under_Ceva_Theorem(pD,pB,pA,pH,pG)
pL = return_intersection_under_Ceva_Theorem(pC,pA,pD,pG,pF)
pI = return_intersection_under_Ceva_Theorem(pA,pC,pB,pE,pH)
pO = return_intersection_under_Ceva_Theorem(pC,pA,pN,pK,pJ)

lineCK, = ax2.plot(*zip(pC,pK),linewidth = 1,color='b')#,linestyle=':')
lineAJ, = ax2.plot(*zip(pA,pJ),linewidth = 1,color='b')#,linestyle=':')
lineBL, = ax2.plot(*zip(pB,pL),linewidth = 1,color='b')#,linestyle=':')
lineDI, = ax2.plot(*zip(pD,pI),linewidth = 1,color='b')#,linestyle=':')

#lineMN, = ax2.plot(*zip(pM,pN),linewidth = 1,color='b')
#lineGE, = ax2.plot(*zip(pG,pE),linewidth = 1,color='b')
#lineHF, = ax2.plot(*zip(pH,pF),linewidth = 1,color='b')

#Plot four insuscribed circles
npcenterBCD = return_9point_circle_center(pB,pC,pD)
normvecBCD = np.cross(pC-pB,pD-pB)/np.linalg.norm(np.cross(pC-pB,pD-pB))
npradiusBCD = np.linalg.norm(npcenterBCD-pE)
npcircleBCD = circle_full(normvecBCD,
                          (-npcenterBCD+pB),
                            npradiusBCD,40) + npcenterBCD
ax2.plot(*np.transpose(npcircleBCD),linewidth=1,linestyle=':')

npcenterBAD = return_9point_circle_center(pB,pA,pD)
normvecBAD = np.cross(pA-pB,pD-pB)/np.linalg.norm(np.cross(pA-pB,pD-pB))
npradiusBAD = np.linalg.norm(npcenterBAD-pN)
npcircleBAD = circle_full(normvecBAD,
                          (-npcenterBAD+pB),
                            npradiusBAD,40) + npcenterBAD
ax2.plot(*np.transpose(npcircleBAD),linewidth=1,linestyle=':')


#Plot the midsphere
cx,cy,cz, radius = four_points_circle(pE,pF,pN,pH)
plot_front(ax2,cx,cy,cz,radius)
plot_back(ax2,cx,cy,cz,radius)


ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pE + (pE-pJ)/10), s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='center')
ax2.text(*(pF + (pF-pN)/10), s = r"$F$", fontsize=12,verticalalignment='center', horizontalalignment='left')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*(pG+(pG-pE)/20), s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='center')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pJ, s = r"$J_\perp$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pK, s = r"$K_\perp$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pI, s = r"$I_\perp$", fontsize=12,verticalalignment='bottom', horizontalalignment='left')
ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pL, s = r"$L_\perp$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pM, s = r"$M$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')

ax2.scatter3D(*zip(pJ,pK,pL,pI,pO,pM,pN,pH,pG,pE,pF))
ax2.set_color_cycle('r')
ax2.scatter3D(*zip((pB+pC)/2,(pC+pD)/2,(pD+pB)/2,(pB+pA)/2,(pA+pD)/2))

# Add transparent faces
#vt1 = [pA,pB,pD]
#tr1 = p3.art3d.Poly3DCollection([vt1],color = 'r', alpha=0.3)
#tr1.set_facecolor('r')
#ax2.add_collection3d(tr1)
#
#vt2 = [pD,pB,pC]
#tr2 = p3.art3d.Poly3DCollection([vt2],color = 'y', alpha=0.3)
#tr2.set_facecolor('y')
#ax2.add_collection3d(tr2)

#draw_xyz_coordinate_unit_vectors(ax2)

Xt,Yt,Zt = zip(pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 3.9


mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5 +0.8 # minus to move window in -y direction w/o moving object
mid_z = (Z.max()+Z.min()) * 0.5 - 0.8 # minus move window doward, correct
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
#pyplot.savefig('./pgf_files/collinear_orthocenters.pgf')

pyplot.show()


