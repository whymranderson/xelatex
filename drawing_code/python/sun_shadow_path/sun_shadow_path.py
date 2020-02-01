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
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)


omega_CM = 2*np.pi/365/24/60/60
omega_fast = 2*np.pi/24/60/60
longitude = 22.98333/np.pi
latitude = 120.183333
sun_distance= 1.4773e11
earth_radius=6.37e6
current_time = 12*60*60 +1*60
date = 21*24*60*60+current_time
Jan_15_8to5 = 14*24*60*60 + np.array([8,9,10,11,12,13,14,15,16,17])*60*60
earth_ax =np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0])) 

def shadow_position(timeinsec):

    sun_vec = np.dot(CK(omega_CM*timeinsec*np.array([0,0,1])),np.array([1,0,0]))
    #print np.linalg.norm(sun_vec)
    angle = np.arccos(np.dot(sun_vec,np.array([1,0,0])))
    taiwan = np.dot(CK(longitude*np.array([0,0,1])),np.array([1,0,0]))
    #print np.linalg.norm(taiwan)
    earth_ax =np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0])) 
    taiwan_current_vec = np.dot(CK((omega_fast*timeinsec)*earth_ax),taiwan)
    print np.linalg.norm(taiwan_current_vec)
    theory_angle = np.degrees(np.arccos(np.dot(sun_vec,taiwan_current_vec)))
    print 180-theory_angle
    #exp = np.degrees(np.arctan(19/14.4))
    #print exp
    return theory_angle


Jan_15_angs_degree = []
Jan_15_angs = []
for x in Jan_15_8to5:
    x_ang = shadow_position(x)
    Jan_15_angs_degree.append(180 - x_ang) 
    Jan_15_angs.append((180 - x_ang)*np.pi/180) 

print Jan_15_angs_degree
pen_length = 0.15
print pen_length*np.tan(Jan_15_angs)

def sun_projection(timeinsec):
    # coordinate setup need a figure, sun at (0,0,0), x-axis at new year eve!, y is along big rotation
    taiwan_x = np.array([0,0,-1])
    taiwan_y = np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0]))
    taiwan_z = np.dot(CK(longitude*np.array([0,0,1])),np.array([1,0,0]))

    taiwan_current_x = np.dot(CK((omega_fast*timeinsec)*earth_ax),taiwan_x)
    taiwan_current_y = np.dot(CK((omega_fast*timeinsec)*earth_ax),taiwan_y)
    taiwan_current_z = np.dot(CK((omega_fast*timeinsec)*earth_ax),taiwan_z)
    sun_vec = np.dot(CK(omega_CM*timeinsec*np.array([0,0,1])),np.array([1,0,0]))
    taiwan_position = sun_distance*sun_vec + earth_radius*taiwan_current_z
    print np.linalg.norm(taiwan_current_y)
    sun_proj = project_a_point_to_a_plane(np.array([0,0,0]),
                                          taiwan_current_x,
                                          taiwan_current_y,
                                          taiwan_position)
    print sun_proj
    return np.dot(sun_proj/np.linalg.norm(sun_proj),taiwan_current_y)

Jan_15_shadows_cos = []
for y in Jan_15_8to5:
    Jan_15_shadows_cos.append(sun_projection(y))

print Jan_15_shadows_cos
#def shadow_angle(timeinsec):
    
pen_shadow_vecs =[]
for z in range(10):
    print z
    pen_shadow_vecs.append([pen_length*np.tan(Jan_15_angs[z])*Jan_15_shadows_cos[z],
                            pen_length*np.tan(Jan_15_angs[z])*np.sqrt(1-np.square(Jan_15_shadows_cos[z]))])

for q in range(10):
    print pen_shadow_vecs[q]

fig2 = plt.figure(2,figsize=(6, 6),dpi=100)
ax2 = p3.Axes3D(fig2)
#ax2.view_init(elev=10, azim=187)
#ax2.view_init(elev=20, azim=7)
ax2.set_color_cycle('b')


## Plot tainan local axes at a certain datetime

dt = 0.1
sun_vec = np.dot(CK(omega_CM*dt*np.array([0,0,1])),np.array([1,0,0]))
plot_earth_center= sun_distance*sun_vec
plot_front(ax2,plot_earth_center[0],plot_earth_center[1],plot_earth_center[2],earth_radius)
plot_back(ax2, plot_earth_center[0],plot_earth_center[1],plot_earth_center[2],earth_radius)
#draw_xyz_coordinate_unit_vectors(ax2)

taiwan_x = np.array([0,0,-1])
taiwan_y = np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0]))
taiwan_z = np.dot(CK(longitude*np.array([0,0,1])),np.array([1,0,0]))
taiwan_current_x = np.dot(CK((omega_fast*dt)*earth_ax),taiwan_x)
taiwan_current_y = np.dot(CK((omega_fast*dt)*earth_ax),taiwan_y)
taiwan_current_z = np.dot(CK((omega_fast*dt)*earth_ax),taiwan_z)
taiwan_position = sun_distance*sun_vec + earth_radius*taiwan_current_z
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

sun_vec_overhead = Arrow3D([taiwan_position[0]+6e6*taiwan_current_z[0],taiwan_position[0]+6e6*taiwan_current_z[0] +9e6*sun_vec[0]],
                           [taiwan_position[1]+6e6*taiwan_current_z[1],taiwan_position[1]+6e6*taiwan_current_z[1] +9e6*sun_vec[1]],
                           [taiwan_position[2]+6e6*taiwan_current_z[2],taiwan_position[2]+6e6*taiwan_current_z[2] +9e6*sun_vec[2]], 
                    mutation_scale=8,
                  #lw=4,
                  arrowstyle="-|>", color="r")
ax2.add_artist(sun_vec_overhead)
#ax2.text(*xyz_arrow_data[2,:],s="z",fontsize=12)



Xt,Yt,Zt = zip(plot_earth_center+2*earth_radius*np.array([1,0,0]),
               plot_earth_center+2*earth_radius*np.array([0,1,0]),
               plot_earth_center+2*earth_radius*np.array([0,0,1]),
               plot_earth_center-2*earth_radius*np.array([0,1,0]),
               plot_earth_center-2*earth_radius*np.array([0,0,1]),
               plot_earth_center-2*earth_radius*np.array([1,0,0]),)
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
