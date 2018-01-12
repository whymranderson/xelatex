# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:21:22 2014

@author: user
"""
import numpy as np
import matplotlib as mpl
mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
#import matplotlib.axis as axis1
from mpl_toolkits.mplot3d import proj3d

### Turn off the perspective/orthogonal viewing effect (it works but has some side problems)
#def orthogonal_proj(zfront, zback):
#    a = (zfront+zback)/(zfront-zback)
#    b = -2*(zfront*zback)/(zfront-zback)
#    return np.array([[1,0,0,0],
#                        [0,1,0,0],
#                        [0,0,a,b],
#                        [0,0,0,zback]])
#proj3d.persp_transformation = orthogonal_proj
###

# want a arrow for the above?
#draw a vector
from matplotlib.patches import FancyArrowPatch
#from mpl_toolkits.mplot3d import proj3d <- uncomment this, you need this

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

########
fig3 = pyplot.figure(3,figsize=(3, 3),dpi=100)
ax3 = p3.Axes3D(fig3)
ax3.view_init(elev=25, azim=25)
ax3.set_color_cycle('b')
########

########
line3x, = ax3.plot([0,9],[0,0],[0,0])
line3x.set_linewidth(2)
ax3.text(9,0,0, r'$x_{lab}$', fontsize=14,verticalalignment='top', 
         horizontalalignment='center')
line3x.set_color('k')
line3y, = ax3.plot([0,0],[0,8],[0,0])
line3y.set_linewidth(2)
line3y.set_color('k')
ax3.text(0,8,0, r'$y_{lab}$', fontsize=14,verticalalignment='center', 
         horizontalalignment='left')
line3z, = ax3.plot([0,0],[0,0],[0,8])
line3z.set_linewidth(2)
line3z.set_color('k')
ax3.text(0,0,8, r'$z_{lab}$', fontsize=14,verticalalignment='bottom', 
         horizontalalignment='center')
         
#line3w, = ax3.plot([0,4],[0,4],[0,5],':')
#line3w.set_linewidth(2)
#line3w.set_color('k')
#ax3.text(4,4,5, '$\omega$', fontsize=14,verticalalignment='bottom', 
#         horizontalalignment='center')

########

######
# plot dash lines
dashxyzt0 = 8*np.dot(rotation_matrix([1,1,1],np.radians(-30)),np.eye(3))
dashxyzt1 = 8*np.dot(rotation_matrix([1,1,1],np.radians(-45)),np.eye(3))
dashxyzt2 = 8*np.dot(rotation_matrix([1,1,1],np.radians(-60)),np.eye(3))
#print(dashxyz)
f3dashlines = np.array([[[0,0,0]        ,dashxyzt0[0,:]   ],
                        [[0,0,0]        ,dashxyzt0[1,:]   ],
                        [[0,0,0]        ,dashxyzt0[2,:]   ],
                        [[0,0,0]        ,dashxyzt1[0,:]   ],
                        [[0,0,0]        ,dashxyzt1[1,:]   ],
                        [[0,0,0]        ,dashxyzt1[2,:]   ],
                        [[0,0,0]        ,dashxyzt2[0,:]   ],
                        [[0,0,0]        ,dashxyzt2[1,:]   ],
                        [[0,0,0]        ,dashxyzt2[2,:]   ],
#                       #                       [[CM[0,0],CM[0,1],0],[CMprime[0,0],CMprime[0,1],0]],
                         ])
(mmd,nnd,ppd)=np.shape(f3dashlines)
for kd in range(mmd):
    ax3.plot(*np.transpose(f3dashlines[kd,:,:]),linestyle='-',color='k')
#######

########
ax3.text(dashxyzt0[0,0],dashxyzt0[0,1],dashxyzt0[0,2], r'$x_0(t_0)$', fontsize=14,
         verticalalignment='top', horizontalalignment='right')
ax3.text(dashxyzt0[1,0],dashxyzt0[1,1],dashxyzt0[1,2], r'$y_0(t_0)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(dashxyzt0[2,0],dashxyzt0[2,1],dashxyzt0[2,2], r'$z_0(t_0)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='right')
ax3.text(dashxyzt1[0,0],dashxyzt1[0,1],dashxyzt1[0,2], r'$x_0(t_1)$', fontsize=14,
         verticalalignment='top', horizontalalignment='center')
ax3.text(dashxyzt1[1,0],dashxyzt1[1,1],dashxyzt1[1,2], r'$y_0(t_1)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(dashxyzt1[2,0],dashxyzt1[2,1],dashxyzt1[2,2], r'$z_0(t_1)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='right')
ax3.text(dashxyzt2[0,0],dashxyzt2[0,1],dashxyzt2[0,2], r'$x_1(t_2)$', fontsize=14,
         verticalalignment='top', horizontalalignment='left')
ax3.text(dashxyzt2[1,0],dashxyzt2[1,1],dashxyzt2[1,2], r'$y_1(t_2)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(dashxyzt2[2,0],dashxyzt2[2,1],dashxyzt2[2,2], r'$z_1(t_2)$', fontsize=14,
         verticalalignment='bottom', horizontalalignment='right')

########

########
# [line_end_vec1,line_end_vec2],[same]
#f3lineswidth2 = np.array([[CP[0,:]        ,CM[0,:]            ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
#                        ])
#print(np.dot(CM[1,:]-CMprime[0,:],CM[0,:]-CMprime[0,:]))                        
                        
#(mm,nn,pp)=np.shape(f3lineswidth2)
#for k in range(mm):
#    ax3.plot(*np.transpose(f3lineswidth2[k,:,:]),linewidth='1')

# plot dash lines
'''#down
dashxyz = 8*np.dot(rotation_matrix([1,0,0],np.radians(-5)),np.eye(3))
print(dashxyz)
f3dashlines = np.array([[[0,0,0]        ,dashxyz[0,:]   ],
                        [[0,0,0]        ,dashxyz[1,:]   ],
                        [[0,0,0]        ,dashxyz[2,:]   ],
#                       [[CM[0,0],CM[0,1],0],[CMprime[0,0],CMprime[0,1],0]],
                         ])
(mmd,nnd,ppd)=np.shape(f3dashlines)
for kd in range(mmd):
    ax3.plot(*np.transpose(f3dashlines[kd,:,:]),linestyle='--',color='k')
'''#up
#######


f3arrowW1 = Arrow3D([0,4],
                   [0,5],
                   [0,6], mutation_scale=20, lw=2, arrowstyle="-|>")
ax3.add_artist(f3arrowW1)
ax3.text(4,5,6, '$\omega_{0}$', fontsize=12,
         verticalalignment='bottom', horizontalalignment='left')
f3arrowW2 = Arrow3D([0,4],
                   [0,4],
                   [0,6.5], mutation_scale=20, lw=2, arrowstyle="-|>")
ax3.add_artist(f3arrowW2)
ax3.text(4,4,6.5, '$\omega_{1}$', fontsize=12,
         verticalalignment='bottom', horizontalalignment='right')

xarrow1 = Arrow3D([0.8*dashxyzt0[0,0],0.8*dashxyzt1[0,0]],
                  [0.8*dashxyzt0[0,1],0.8*dashxyzt1[0,1]],
                  [0.8*dashxyzt0[0,2],0.8*dashxyzt1[0,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(xarrow1)
xarrow2 = Arrow3D([0.8*dashxyzt1[0,0],0.8*dashxyzt2[0,0]],
                  [0.8*dashxyzt1[0,1],0.8*dashxyzt2[0,1]],
                  [0.8*dashxyzt1[0,2],0.8*dashxyzt2[0,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(xarrow2)

yarrow1 = Arrow3D([0.8*dashxyzt0[1,0],0.8*dashxyzt1[1,0]],
                  [0.8*dashxyzt0[1,1],0.8*dashxyzt1[1,1]],
                  [0.8*dashxyzt0[1,2],0.8*dashxyzt1[1,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(yarrow1)
yarrow2 = Arrow3D([0.8*dashxyzt1[1,0],0.8*dashxyzt2[1,0]],
                  [0.8*dashxyzt1[1,1],0.8*dashxyzt2[1,1]],
                  [0.8*dashxyzt1[1,2],0.8*dashxyzt2[1,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(yarrow2)

zarrow1 = Arrow3D([0.8*dashxyzt0[2,0],0.8*dashxyzt1[2,0]],
                  [0.8*dashxyzt0[2,1],0.8*dashxyzt1[2,1]],
                  [0.8*dashxyzt0[2,2],0.8*dashxyzt1[2,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(zarrow1)
zarrow2 = Arrow3D([0.8*dashxyzt1[2,0],0.8*dashxyzt2[2,0]],
                  [0.8*dashxyzt1[2,1],0.8*dashxyzt2[2,1]],
                  [0.8*dashxyzt1[2,2],0.8*dashxyzt2[2,2]], mutation_scale=10, lw=1, arrowstyle="-|>")
ax3.add_artist(zarrow2)




'''#down
#######

f3arrowBz = Arrow3D([0,0],
                   [0,6],
                   [0,4], mutation_scale=16, lw=4, arrowstyle="-|>", color="b")
ax3.add_artist(f3arrowBz)
ax3.text(0,5,3, r'$b_z$ at time t+dt', fontsize=12,
         verticalalignment='top', horizontalalignment='left')

f3arrowx1 = Arrow3D([CP[1,0]-C[1,0,0]*1.5,CP[1,0]+C[1,0,0]],
                   [CP[1,1]-C[1,1,0]*1.5,CP[1,1]+C[1,1,0]],
                   [CP[1,2]-C[1,2,0]*1.5,CP[1,2]+C[1,2,0]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowx1)
ax3.text(CP[1,0]+C[1,0,0],CP[1,1]+C[1,1,0],CP[1,2]+C[1,2,0], r'$\hat x_0^\prime ,\hat x_1$', fontsize=16,
         verticalalignment='top', horizontalalignment='right')

f3arrowy0p = Arrow3D([CPprime[0,0]-C[1,0,0]*0,CPprime[0,0]+Cprime[0,0,1]],
                    [CPprime[0,1]-C[1,1,0]*0,CPprime[0,1]+Cprime[0,1,1]],
                    [CPprime[0,2]-C[1,2,0]*0,CPprime[0,2]+Cprime[0,2,1]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowy0p)
ax3.text(CPprime[0,0]+Cprime[0,0,1],CPprime[0,1]+Cprime[0,1,1],CPprime[0,2]+Cprime[0,2,1], r'$\haty_0^\prime$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')
         
f3arrowy1 = Arrow3D([CP[1,0]-C[1,0,0]*0,CP[1,0]+C[1,0,1]],
                   [CP[1,1]-C[1,1,0]*0,CP[1,1]+C[1,1,1]],
                   [CP[1,2]-C[1,2,0]*0,CP[1,2]+C[1,2,1]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowy1)
ax3.text(CP[1,0]+C[1,0,1],CP[1,1]+C[1,1,1],CP[1,2]+C[1,2,1], r'$\hat y_1$', fontsize=16,
         verticalalignment='top', horizontalalignment='left')

f3arrowy1p = Arrow3D([CPprime[1,0]-C[1,0,0]*0,CPprime[1,0]+Cprime[1,0,1]],
                    [CPprime[1,1]-C[1,1,0]*0,CPprime[1,1]+Cprime[1,1,1]],
                    [CPprime[1,2]-C[1,2,0]*0,CPprime[1,2]+Cprime[1,2,1]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowy1p)
ax3.text(CPprime[1,0]+Cprime[1,0,1],CPprime[1,1]+Cprime[1,1,1],CPprime[0,2]+Cprime[0,2,1], r'$\haty_1^\prime$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')
         
f3arrowy2 = Arrow3D([CP[2,0]-C[1,0,0]*0,CP[2,0]+C[2,0,1]],
                   [CP[2,1]-C[1,1,0]*0,CP[2,1]+C[2,1,1]],
                   [CP[2,2]-C[1,2,0]*0,CP[2,2]+C[2,2,1]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowy2)
ax3.text(CP[2,0]+C[2,0,1],CP[2,1]+C[2,1,1],CP[2,2]+C[2,2,1], r'$\hat y_2$', fontsize=16,
         verticalalignment='top', horizontalalignment='left')

f3arrowx2 = Arrow3D([CP[2,0]-C[2,0,0]*1.5,CP[2,0]+C[2,0,0]],
                   [CP[2,1]-C[2,1,0]*1.5,CP[2,1]+C[2,1,0]],
                   [CP[2,2]-C[2,2,0]*1.5,CP[2,2]+C[2,2,0]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowx2)
ax3.text(CP[2,0]+C[2,0,0],CP[2,1]+C[2,1,0],CP[2,2]+C[2,2,0], r'$\hat x_1^\prime ,\hat x_2$', fontsize=16,
         verticalalignment='top', horizontalalignment='left')
######
'''#up
         
###### f3text CMs CPs
#ax3.text(0,0,0, r'$CP_0$', fontsize=11,
#         verticalalignment='top', horizontalalignment='right')
'''
ax3.text(dashxyz[1,0],dashxyz[1,1],dashxyz[1,2], r'$b_y$', fontsize=18,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(dashxyz[2,0],dashxyz[2,1],dashxyz[2,2], r'$b_z$', fontsize=18,
         verticalalignment='bottom', horizontalalignment='right')
ax3.text(CM[1,0],CM[1,1],CM[1,2], r'$\/CM_1$', fontsize=11,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(CMprime[1,0],CMprime[1,1],CMprime[1,2], r'$\/CM_1^\prime$', fontsize=11,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(CM[2,0],CM[2,1],CM[2,2], r'$\/CM_2$', fontsize=11,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(CP[1,0],CP[1,1],CP[1,2], r'$\/CP_1$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
ax3.text(CPprime[0,0],CPprime[0,1],CPprime[0,2], r'$\/CP_0^\prime$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
ax3.text(CP[2,0],CP[2,1],CP[2,2], r'$\/CP_2$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
ax3.text(CPprime[1,0],CPprime[1,1],CPprime[1,2], r'$\/CP_1^\prime$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
ax3.text(CPprime[2,0],CPprime[2,1],CPprime[2,2], r'$\/CP_2^\prime$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
######
'''

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


#arc1 = 4*circle_arc(dashxyzt0[2,:],dashxyzt2[2,:],dashxyzt2[2,:],10)
#larc1, = ax3.plot(arc1[:,0],arc1[:,1],arc1[:,2],'k')
#ax3.text(arc1[-1,0],arc1[-1,1],arc1[-1,2], r'$\Omega \rightarrow d\Omega$', fontsize=14,
#         verticalalignment='bottom', horizontalalignment='right')

'''         
######
f3dots1 = np.array([CM[0,:],CMprime[0,:],CM[1,:],CMprime[1,:],CM[2,:],
                    CP[0,:],CPprime[0,:],CP[1,:],CPprime[1,:],CP[2,:],
                    CPprime[2,:],
                    [CM[0,0],CM[0,1],0],
                    [CMprime[0,0],CMprime[0,1],0],
                    [CM[1,0],CM[1,1],0],
                    [CMprime[1,0],CMprime[1,1],0],
                    [CM[2,0],CM[2,1],0],
                    ])
ax3.plot(f3dots1[:,0],f3dots1[:,1],f3dots1[:,2], marker='.',color = 'b', lw=0 ,markersize=6,alpha=0.8)
######
'''
######
#ax3.set_xticks([])
#ax3.set_yticks([])
#ax3.set_zticks([])
#ax3.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
#ax3.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
#ax3.w_zaxis.line.set_color([0,0,0,0])
######

ax3.set_axis_off()  #-> this can turn off the background curtain

ax3.tick_params(labelbottom='off', labeltop='off', labelleft='off', labelright='off')
ax3.set_xlim(0,9)
ax3.set_ylim(-1,9)
ax3.set_zlim(0,8)

xsize,ysize = fig3.get_size_inches()
#ax3.autoscale_view(tight=True)
#ax3.get_autoscale_on()
#pyplot.subplots_adjust(left = (1/25.4)/xsize, bottom = (1/25.4)/ysize, right = 1 - (1/25.4)/xsize, top = 1 - (1/25.4)/ysize)
pyplot.show()
#pyplot.savefig(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\Zt0Zt1.pgf')