#Generate a gyro logo with white background, with thicker thumb handle
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3

nop = 160
a0 = 1.0
xx = np.linspace(2.3 ,12.5, nop)
rotate_angle = 0
choose = 2


def hydrogenN3l2(x):
    if choose == 1:
        f = 1.0/81/np.sqrt(6*np.pi)/np.power(a0,1.5)*x*x/a0/a0*np.exp(-x/3/a0)   
    else:
        f = 1/((x-8)**2+1) # Lorentz function
    return f

def gfunc(xx):
    gout = hydrogenN3l2(xx)
    return gout
def rotation_matrix(axis,theta):
    axis = axis/np.sqrt(np.dot(axis,axis))
    a = np.cos(theta/2)
    b,c,d = axis*np.sin(theta/2)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])

#%% Figure setup

#fig4=plt.figure(4)
#plt.plot(roundtopx,roundtopy)



fig3 = plt.figure(3)#,figsize=(1.5,2))#,dpi=200)
ax3 = p3.Axes3D(fig3)
ax3.view_init(elev=0, azim=-10)
#ax3.set_axis_bgcolor('black')
#ax3.set_color_cycle('b')

#print(fig3.get_dpi())
#print(fig3.get_size_inches())

#%% no use
markersizearray =  hydrogenN3l2(xx)

grx = np.array([8.5,12.0])
grr = hydrogenN3l2(grx)
gyroZvec = np.dot(rotation_matrix((-1,0,0),np.radians(rotate_angle)),[0,1,0])
#arc2unrotated = grr[0]*circle_arc([0,1,0],[0,0,grr[0]],[0.001,0,-grr[0]],60) + grx[0]*np.array([0,1,0])
#arc2 = np.dot(rotation_matrix((-1,0,0),np.radians(100)),np.transpose(arc2unrotated)) 
#ax3.scatter(arc2[0,:],arc2[1,:],arc2[2,:],alpha=0.2,s = markersizearray[::-1]*0.65)

#arc3 = grr[1]*circle_arc([0,1,np.sqrt(3)],[0,-np.sqrt(3),1],[0.01,np.sqrt(3),-1],20) + grx[1]*np.array([0,1,np.sqrt(3)])/2
#larc3, = ax3.plot(arc3[:,0],arc3[:,1],arc3[:,2],'k',lw=4)
#ax3.text(0,15,17,r'',fontsize=28,verticalalignment='top')

#ax3.plot(*gyrovec2[:,:50],linewidth=7,color='k',alpha=0.4)
#ax3.plot(*gyrovec,linewidth=6,color='k')

#%% the wave shape from z axis motion of gyroscope

linedata=[]
for i in [1,2,3]:
    Z_vec_array = 2*np.transpose(np.load('../outfile'+str(i)+'.npy'))
    mmZ,nnZ = np.shape(Z_vec_array)
    #print mmZ,nnZ
    for nnZi in range(nnZ):
        Z_vec_array[:,nnZi] = np.dot(rotation_matrix([1,0,0],np.radians(90)),
                                Z_vec_array[:,nnZi])
    # translate ring along Z direction (up and down)
    Z_vec_array[1,:] = Z_vec_array[1,:] + 8.3  
    
    # shrink in the xz plane to match top
    for nnZii in range(nnZ):
        shrink_factor =1/np.sqrt(np.square(Z_vec_array[0,nnZii])+
                                 np.square(Z_vec_array[2,nnZii]))*5*gfunc(Z_vec_array[1,nnZii])
        Z_vec_array[:,nnZii] = np.array([Z_vec_array[0,nnZii]*shrink_factor,
                                         Z_vec_array[1,nnZii],
                                         Z_vec_array[2,nnZii]*shrink_factor])
        Z_vec_array[:,nnZii] = np.dot(rotation_matrix([-1,0,0],np.radians(rotate_angle)),
                                Z_vec_array[:,nnZii])
    linedata.append(Z_vec_array)

#%% fixing the tips of the top so that they are round and smooth. Before it's sharp.
v = np.linspace(0, np.pi, 20) # theta angle from the zy plane

roundnumber = 11
roundtopx= np.linspace(0.001,0.9999,roundnumber,endpoint=True)
roundtopy=np.sqrt(1-np.square(roundtopx))
lucidy = gfunc(xx) + 0.03

for i in range(roundnumber):
    lucidy[-(roundnumber-i)]=lucidy[-(roundnumber)]*roundtopy[i]
    lucidy[i-1]=lucidy[roundnumber]*roundtopy[-i]
    
#Smoothing
for j in range(10):
    lucidy[-roundnumber+5-j]=np.sum(lucidy[-roundnumber+5-j-5:-roundnumber+5-j+5])/10

#making a groove
#gloc = 70
#lucidy[gloc:gloc+2] = lucidy[gloc:gloc+2]*0
#%% checking the 2D profile outline shape
plt.figure(2)
plt.plot(xx,lucidy)

maxi = np.argmax(lucidy)

profiley = np.zeros(2*maxi)
profiley[:maxi] = -lucidy[maxi:0:-1]
profiley[maxi:2*maxi] = lucidy[0:maxi]
profilex = np.zeros(2*maxi)
profilex[:maxi] = xx[maxi:0:-1]
profilex[maxi:2*maxi] =xx[:maxi]

plt.figure(4)
plt.plot(profilex,profiley)
databf=zip(1.18*profilex,5*profiley)
dataaf=np.array(databf)

np.savetxt(r'C:\Documents and Settings\The One\My Documents\tony\2014\xelatexfolder\otherstuff\data_text_files\logoprofile.txt',dataaf, fmt='%.4f', delimiter=' ', newline='\n', header='', footer='', comments='# ')


gx = np.outer(5*lucidy, np.sin(v))
print np.shape(gx), 'gx'
gz = np.outer(5*lucidy, np.cos(v))
gy = np.outer(xx,np.ones(np.size(v)))
gxl = gx.flatten()
gzl = gz.flatten()
gyl = gy.flatten()
glrotatedvec = np.dot(rotation_matrix([-1,0,0],np.radians(rotate_angle)),
                      np.array([gxl,gyl,gzl]))
gxlr = np.reshape(glrotatedvec[0,:],(nop,20))
gylr = np.reshape(glrotatedvec[1,:],(nop,20))
gzlr = np.reshape(glrotatedvec[2,:],(nop,20))
ax3.plot_surface(gxlr, gylr, gzlr, rstride=1, cstride=1,
                       color='w', linewidth=0,)
                       #alpha=0.1)
# wireframe
ax3.plot_wireframe(gxlr, gylr,gzlr, rstride=2, cstride=2,
                         color='w',
                         alpha=1)




#ax3.scatter(*gyrovec,s=markersizearray*0.8,color='w',alpha=1)
#ax3.plot(*gyrovec,color='w',linewidth=2)#,s=markersizearray)
#Z_vec_array
ax3.plot(*linedata[0],color='red',linewidth=2)#,s=markersizearray*0.05)#, color='b')
ax3.plot(*linedata[1],color='yellow',linewidth=2)#,s=markersizearray*0.05)#, color='b')
ax3.plot(*linedata[2],color='magenta',linewidth=2)#,s=markersizearray*0.05)#, color='b')

ax3.set_axis_off()  #-> this can turn off the background curtain

ax3.tick_params(labelbottom='off', labeltop='off', labelleft='off', labelright='off')
ax3.set_xlim(0,10)
ax3.set_ylim(-7,7)
#ax3.set_zlim(-13,-3)
ax3.w_xaxis.set_pane_color((0.0, 0.0, 1.0, 0.0))


#print(fig3.get_size_inches())

plt.show()
#plt.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\gyrologo6.pgf')
