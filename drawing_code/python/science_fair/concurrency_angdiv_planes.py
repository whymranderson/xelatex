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

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(5, 5),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=15, azim=-20)
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

pA = np.array([0,0,0])
pC = np.array([0,6,0])
pB = np.array([1,3.5,7])
pD = np.array([7,1.5,0])

lineAC, = ax2.plot(*zip(pA,pC),linewidth = 2,color='b')
lineAB, = ax2.plot(*zip(pA,pB),linewidth = 2,color='b')
lineAD, = ax2.plot(*zip(pA,pD),linewidth = 2,color='b')
lineCB, = ax2.plot(*zip(pC,pB),linewidth = 2,color='b')
lineCD, = ax2.plot(*zip(pC,pD),linewidth = 2,color='b')
lineBD, = ax2.plot(*zip(pB,pD),linewidth = 2,color='b')

pE = (triangle_area(pA,pC,pD)*pB + triangle_area(pA,pB,pD) * pC)/(triangle_area(pA,pC,pD)+triangle_area(pA,pB,pD))
pF = (triangle_area(pA,pB,pC)*pD + triangle_area(pA,pB,pD) * pC)/(triangle_area(pA,pB,pC)+triangle_area(pA,pB,pD))
pN = (triangle_area(pA,pB,pC)*pD + triangle_area(pA,pC,pD) * pB)/(triangle_area(pA,pB,pC)+triangle_area(pA,pC,pD))
pH = (triangle_area(pD,pB,pC)*pA + triangle_area(pA,pC,pD) * pB)/(triangle_area(pD,pB,pC)+triangle_area(pA,pC,pD))
pG = (triangle_area(pA,pB,pC)*pD + triangle_area(pC,pB,pD) * pA)/(triangle_area(pA,pB,pC)+triangle_area(pC,pB,pD))
pM = (triangle_area(pD,pB,pC)*pA + triangle_area(pA,pB,pD) * pC)/(triangle_area(pD,pB,pC)+triangle_area(pA,pB,pD))

#lineDE, = ax2.plot(*zip(pD,pE),linewidth = 1,color='b',linestyle=':')
#lineBF, = ax2.plot(*zip(pB,pF),linewidth = 1,color='b',linestyle=':')
#lineDH, = ax2.plot(*zip(pD,pH),linewidth = 1,color='b',linestyle=':')
#lineBG, = ax2.plot(*zip(pB,pG),linewidth = 1,color='b',linestyle=':')


#lineCN, = ax2.plot(*zip(pC,pN),linewidth = 1,color='b',linestyle=':')
#lineAN, = ax2.plot(*zip(pA,pN),linewidth = 1,color='b',linestyle=':')
#lineAR, = ax2.plot(*zip(pA,pR),linewidth = 1,color='b')

pJ = return_intersection_under_Ceva_Theorem(pB,pD,pC,pF,pE)
pK = return_intersection_under_Ceva_Theorem(pD,pB,pA,pH,pG)
pL = return_intersection_under_Ceva_Theorem(pC,pA,pD,pG,pF)
pI = return_intersection_under_Ceva_Theorem(pA,pC,pB,pE,pH)
pO = return_intersection_under_Ceva_Theorem(pC,pA,pN,pK,pJ)

lineCK, = ax2.plot(*zip(pC,pK),linewidth = 1,color='b',linestyle=':')
lineAJ, = ax2.plot(*zip(pA,pJ),linewidth = 1,color='b',linestyle=':')
lineBL, = ax2.plot(*zip(pB,pL),linewidth = 1,color='b',linestyle=':')
lineDI, = ax2.plot(*zip(pD,pI),linewidth = 1,color='b',linestyle=':')

lineMN, = ax2.plot(*zip(pM,pN),linewidth = 1,color='b')
lineGE, = ax2.plot(*zip(pG,pE),linewidth = 1,color='b')
lineHF, = ax2.plot(*zip(pH,pF),linewidth = 1,color='b')

pO_on_BCD = project_a_point_to_a_plane(pO, pB-pD, pC-pD,pJ)
radius = np.linalg.norm(pO-pO_on_BCD)
plot_front(ax2,pO[0],pO[1],pO[2],radius)
plot_back(ax2,pO[0],pO[1],pO[2],radius)

lineO_BCD, = ax2.plot(*zip(pO,pO_on_BCD),linewidth = 1,color='r',linestyle=':')

ax2.text(*pA, s = r'$A$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pB, s = r'$B$', fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pC, s = r'$C$', fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pD, s = r"$D$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*(pE + (pE-pJ)/10), s = r"$E$", fontsize=12,verticalalignment='bottom', horizontalalignment='center')
ax2.text(*(pF + (pF-pN)/5), s = r"$F$", fontsize=12,verticalalignment='center', horizontalalignment='left')
ax2.text(*pH, s = r"$H$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*(pG+(pG-pE)/9), s = r"$G$", fontsize=12,verticalalignment='top', horizontalalignment='center')
ax2.text(*pN, s = r"$N$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pJ, s = r"$J$", fontsize=12,verticalalignment='top', horizontalalignment='left')
ax2.text(*pK, s = r"$K$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pI, s = r"$I$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pO, s = r"$O$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')
ax2.text(*pL, s = r"$L$", fontsize=12,verticalalignment='top', horizontalalignment='right')
ax2.text(*pM, s = r"$M$", fontsize=12,verticalalignment='bottom', horizontalalignment='right')

ax2.scatter3D(*zip(pJ,pK,pL,pI,pO,pM,pN,pH,pG,pE,pF))

Xt,Yt,Zt = zip(pA,pB,pC,pD)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6 +0.7


mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5 - 1
mid_z = (Z.max()+Z.min()) * 0.5
ax2.set_xlim3d(mid_x - max_range, mid_x + max_range)
ax2.set_ylim3d(mid_y - max_range, mid_y + max_range)
ax2.set_zlim3d(mid_z - max_range, mid_z + max_range)

#anotation of segment a
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pB, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pE, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.5",
                            ),
            )

pla = (pB+pE)/2
ax2.annotate(s = 'a\n ',xy = tuple(proj3d.proj_transform(*pla, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='center',color="0.5")

#annotation of segment b
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pE, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pC, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.5",
                            ),
            )

plb = (pE+pC)/2
ax2.annotate(s = 'b\n ',xy = tuple(proj3d.proj_transform(*plb, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='center',color="0.5")

#annotation of segment c
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pC, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pF, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.2",
                            ),
            )

plc = (pF+pC)/2
plc = plc + (plc-pB)/5
ax2.annotate(s = 'c',xy = tuple(proj3d.proj_transform(*plc, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='center',color="0.5")

#annotation of segment d
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pF, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pD, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.2",
                            ),
            )

pld = (pF+pD)/2
pld = pld + (pld-pA)/10
ax2.annotate(s = 'd',xy = tuple(proj3d.proj_transform(*pld, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='bottom',ha='center',color="0.5")

#annotation of segment e
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pD, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pG, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )

ple = (pD+pG)/2
ax2.annotate(s = ' \ne',xy = tuple(proj3d.proj_transform(*ple, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='top',ha='right',color="0.5")

#annotation of segment f
ax2.annotate("",
            xy=tuple(proj3d.proj_transform(*pG, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*pA, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )

plf = (pG+pA)/2
ax2.annotate(s = '\n\nf   ',xy = tuple(proj3d.proj_transform(*plf, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va='top',ha='right',color="0.5")


def segment_length_annotate(ax,p1,p2,radius,string,ver_a,hor_a,color):
    #annotation of segment f
    ax.annotate("",
            xy=tuple(proj3d.proj_transform(*p1, M = ax2.get_proj()))[:2], #xycoords='data',
            xytext=tuple(proj3d.proj_transform(*p2, M = ax2.get_proj()))[:2], #textcoords='data',
            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
                            color="0.5",
                            patchB=None,
                            shrinkB=0,
                            connectionstyle="arc3,rad=" + str(radius),
                            ),
            )

    plm = (p1+p2)/2
    ax.annotate(s = string,xy = tuple(proj3d.proj_transform(*plm, M = ax2.get_proj()))[:2],
             bbox={'pad':12,'fill':None,'edgecolor':'None'},va=ver_a,ha=hor_a,color=color)

segment_length_annotate(ax2,pA,pH,0.3,'g  \n\n','bottom','right','0.5')
segment_length_annotate(ax2,pH,pB,0.3,'h  \n\n','bottom','right','0.5')
    



ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.w_xaxis.line.set_visible(False) #turn off axis visibility
ax2.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax2.w_zaxis.line.set_color([0,0,0,0])
ax2.set_axis_off()  #-> this can turn off the background curtain
#pyplot.savefig('./pgf_files/concurrency_sidepoint_connections.pgf')

pyplot.show()


