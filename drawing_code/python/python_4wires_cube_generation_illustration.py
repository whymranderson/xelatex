# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 17:05:48 2015

@author: The One
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
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

testout =  np.transpose(np.array([
                                     [1,1,1],
                                     [-1,1,1],
                                     [-1,1,-1],
                                     [-1,-1,-1],
                                     [-1,1,1],
                                     [-1,-1,1],
                                     [-1,-1,-1],
                                     [1,-1,-1],
                                     [-1,-1,1],
                                     [1,-1,1],
                                     [1,-1,-1],
                                     [1,1,-1],
                                     [1,-1,1],
                                     [1,1,1],
                                     [1,1,-1],
                                     [-1,1,-1],
                                    ]))
                                    
#for i in range(16): # translation
#    testout[:,i] = testout[:,i] 

#%% 3D figure context setup
fig2 = plt.figure(2,figsize=(6,6))
ax4 = p3.Axes3D(fig2)
ax4.set_axis_off()  #-> this can turn off the background curtain
ax4.tick_params(labelbottom='off', labeltop='off', labelleft='off', labelright='off')
ax4.view_init(elev=20, azim=-70) #python
#ax4.view_init(elev=135, azim=-89) #opengl
#factor = 1.1    
#ax4.set_xlim3d([-1*factor, 1*factor])
#ax4.set_ylim3d([-1*factor, 1*factor])
#ax4.set_zlim3d([-1*factor, 1*factor])

#%%

cubeinst1 = ax4.plot(*testout[:,0:4],c='black',linewidth=4)
cubeinst2 = ax4.plot(*testout[:,4:8],c='gray',linewidth=4)
cubeinst3 = ax4.plot(*testout[:,8:12],c='lightgray',linewidth=4)
cubeinst4 = ax4.plot(*testout[:,12:16],c='darkgray',linewidth=4)

#%% add vertex numbering index
text_array_ind = np.array([1,2,3,4,6,10,8,12])-1
text_array_val = ['1,14','2,5','3,16','4,7','6,9','10,13','8,11','12,15']
for i in range(8):
    ax4.text(*testout[:,text_array_ind[i]],s=text_array_val[i],fontsize=20)

#%% plot xyz axes
xyz_arrow_data = np.array([[1,0,0],[0,1.0,0],[0,0,1.0]])*1.2

x_arrow = Arrow3D([0,xyz_arrow_data[0,0]],
                   [0,0],
                   [0,0], 
                    mutation_scale=16, lw=4, arrowstyle="-|>", color="b")
ax4.add_artist(x_arrow)
ax4.text(xyz_arrow_data[0,0],
         xyz_arrow_data[0,1],
        xyz_arrow_data[0,2]+0.1,s="x",fontsize=24)

y_arrow = Arrow3D([0,0],
                   [0,xyz_arrow_data[1,1]],
                   [0,0], 
                    mutation_scale=16, lw=4, arrowstyle="-|>", color="b")
ax4.add_artist(y_arrow)
ax4.text(*xyz_arrow_data[1,:],s="y",fontsize=24)
z_arrow = Arrow3D([0,0],
                   [0,0],
                   [0,xyz_arrow_data[2,2]], 
                    mutation_scale=16, lw=4, arrowstyle="-|>", color="b")
ax4.add_artist(z_arrow)
ax4.text(*xyz_arrow_data[2,:],s="z",fontsize=24)