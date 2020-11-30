import numpy as np
import sys
sys.path.append('../3D_geometry_annotate_program')
from annotate_program import CK
from annotate_program import project_a_point_to_a_plane
from annotate_program import plot_front
from annotate_program import plot_back
from annotate_program import draw_xyz_coordinate_unit_vectors

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
import datetime

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


class earth_sun_relation:

    omega_CM = 2*np.pi/365/24/60/60
    omega_fast = 2*(np.pi+np.pi/365)/24/60/60
    longitude = 22.98333/180*np.pi
    latitude = 120.183333
    sun_distance= 1.4773e11
    earth_radius=6.37e6
    current_time = 12*60*60 +1*60
    date = 21*24*60*60+current_time
    hour8to5 = np.array([8,9,10,11,12,13,14,15,16,17])
    Jan_15_8to5 = 14*24*60*60 + hour8to5*60*60
    earth_ax =np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0])) 
    taiwan_x = np.array([0,0,-1])
    taiwan_y = np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0]))
    taiwan_z = np.dot(CK(longitude*np.array([0,0,-1])),np.array([-1,0,0]))

    def __init__(self, datepara=datetime.datetime(2020,3,12,9,1)):
        self.datepara = datepara 
        self.dt = ( self.datepara - datetime.datetime(2020,1,1,0,1)).total_seconds()

    def get_current_relation(self):
        self.sun_vec = np.dot(CK(self.omega_CM*self.dt*np.array([0,1,0])),np.array([-1,0,0]))
        self.taiwan_current_x = np.dot(CK((self.omega_fast*self.dt)*self.earth_ax),self.taiwan_x)
        self.taiwan_current_y = np.dot(CK((self.omega_fast*self.dt)*self.earth_ax),self.taiwan_y)
        self.taiwan_current_z = np.dot(CK((self.omega_fast*self.dt)*self.earth_ax),self.taiwan_z)
        self.taiwan_position = self.sun_distance*self.sun_vec + self.earth_radius*self.taiwan_current_z #scale down the earth-sun distance to better illustrate
        self.z_shadow_vec = 1/np.dot(self.taiwan_current_z,self.sun_vec)*self.sun_vec
        self.sun2ground_vec= -1/np.dot(self.taiwan_current_z,self.sun_vec)*self.sun_vec

    def __str__(self): 
        return "({0}, {1})".format(self.datepara, self.dt)

    def plotting(self,ax2):
        ## Plot tainan local axes at a certain datetime
        taiwan_current_x =self.taiwan_current_x 
        taiwan_current_y =self.taiwan_current_y
        taiwan_current_z =self.taiwan_current_z
        taiwan_position  =5*self.earth_radius*self.sun_vec + self.earth_radius*self.taiwan_current_z #scale down the earth-sun distance to better illustrate 
        z_shadow_vec     =self.z_shadow_vec
        sun2ground_vec   =self.sun2ground_vec

        plot_earth_center= 5*self.earth_radius*self.sun_vec #scale down the earth-sun distance to better illustrate
        plot_front(ax2,plot_earth_center[0],plot_earth_center[1],plot_earth_center[2],self.earth_radius)
        plot_back(ax2, plot_earth_center[0],plot_earth_center[1],plot_earth_center[2],self.earth_radius)
        #draw_xyz_coordinate_unit_vectors(ax2)
        
        earth_x_arrow = Arrow3D([taiwan_position[0],taiwan_position[0]+6e6*taiwan_current_x[0]],
                                [taiwan_position[1],taiwan_position[1]+6e6*taiwan_current_x[1]],
                                [taiwan_position[2],taiwan_position[2]+6e6*taiwan_current_x[2]], 
                            mutation_scale=8,
                          #lw=4,
                          arrowstyle="-|>", color="b")
        ax2.add_artist(earth_x_arrow)
        #ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)
        
        earth_z_arrow = Arrow3D([taiwan_position[0],taiwan_position[0]+6e6*taiwan_current_z[0]],
                                [taiwan_position[1],taiwan_position[1]+6e6*taiwan_current_z[1]],
                                [taiwan_position[2],taiwan_position[2]+6e6*taiwan_current_z[2]], 
                            mutation_scale=8,
                          #lw=4,
                          arrowstyle="-|>", color="b")
        ax2.add_artist(earth_z_arrow)
        #ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)
        
        earth_ax_arrow = Arrow3D([plot_earth_center[0],plot_earth_center[0]+8e6*self.earth_ax[0]],
                                 [plot_earth_center[1],plot_earth_center[1]+8e6*self.earth_ax[1]],
                                 [plot_earth_center[2],plot_earth_center[2]+8e6*self.earth_ax[2]], 
                            mutation_scale=8,
                          #lw=4,
                          arrowstyle="-|>", color="k")
        ax2.add_artist(earth_ax_arrow)
        #ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)
        
        sun2ground_vec_arrow = Arrow3D([taiwan_position[0]+6e6*taiwan_current_z[0],taiwan_position[0]+6e6*taiwan_current_z[0] +6e6*sun2ground_vec[0]],
                                       [taiwan_position[1]+6e6*taiwan_current_z[1],taiwan_position[1]+6e6*taiwan_current_z[1] +6e6*sun2ground_vec[1]],
                                       [taiwan_position[2]+6e6*taiwan_current_z[2],taiwan_position[2]+6e6*taiwan_current_z[2] +6e6*sun2ground_vec[2]], 
                            mutation_scale=8,
                          #lw=4,
                          arrowstyle="-|>", color="r")
        ax2.add_artist(sun2ground_vec_arrow)
        #ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)
        
        ground_vec = taiwan_current_z + sun2ground_vec
        
        ground_vec_arrow = Arrow3D([taiwan_position[0],taiwan_position[0] +6e6*ground_vec[0]],
                                   [taiwan_position[1],taiwan_position[1] +6e6*ground_vec[1]],
                                   [taiwan_position[2],taiwan_position[2] +6e6*ground_vec[2]], 
                            mutation_scale=8,
                          #lw=4,
                          arrowstyle="-|>", color="k")
        ax2.add_artist(ground_vec_arrow)
        #ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)


date1 = datetime.datetime(2020,1,1,00,02)
date2 = datetime.datetime(2020,4,1,12,01)
date3 = datetime.datetime(2020,7,1,12,01)
date4 = datetime.datetime(2020,10,1,12,01)
esr1 = earth_sun_relation(date1)
esr1.get_current_relation()
esr2 = earth_sun_relation(date2)
esr2.get_current_relation()
esr3 = earth_sun_relation(date3)
esr3.get_current_relation()
esr4 = earth_sun_relation(date4)
esr4.get_current_relation()

print esr1
print esr2


fig2 = plt.figure(2,figsize=(5, 5),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=180, azim=-90)
#ax2.view_init(elev=90, azim=-90)
#ax2.view_init(elev=0, azim=-0)
#ax2.view_init(elev=120, azim=-90)
#ax2.view_init(elev=0, azim=-90)
ax2.set_color_cycle('b')

esr1.plotting(ax2)
esr2.plotting(ax2)
esr3.plotting(ax2)
esr4.plotting(ax2)
draw_xyz_coordinate_unit_vectors(ax2,8e6)

Xt,Yt,Zt = zip(+5*esr1.earth_radius*np.array([1,0,0]),
               +5*esr1.earth_radius*np.array([0,1,0]),
               +5*esr1.earth_radius*np.array([0,0,1]),
               -5*esr1.earth_radius*np.array([0,1,0]),
               -5*esr1.earth_radius*np.array([0,0,1]),
               -5*esr1.earth_radius*np.array([1,0,0]),)
X = np.array(Xt)
Y = np.array(Yt)
Z = np.array(Zt)

max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.6

mid_x = (X.max()+X.min()) * 0.5
mid_y = (Y.max()+Y.min()) * 0.5
mid_z = (Z.max()+Z.min()) * 0.5 - 0.4
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

plt.show()
