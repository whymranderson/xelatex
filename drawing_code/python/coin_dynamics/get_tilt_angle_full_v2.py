import numpy as np
#import matplotlib as mpl
#mpl.use('pgf')
from matplotlib import pyplot
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import matplotlib.cm as mplcm
import matplotlib.colors as colors
#from matplotlib import rc
#rc('text', usetex=True)


def coinEOMgeneral(wi,torquei_along_body):
    InerTen = np.array([[Ix,0,0],[0,Iy,0],[0,0,Iz]])
    angL=np.dot(InerTen,wi)
    crossprod = np.cross(wi,angL)
    fderiv = torquei_along_body - crossprod
    fderiv = np.dot(np.array([[1/Ix,0,0],
                              [0,1/Iy,0],
                              [0,0,1/Iz]]), fderiv)
    return fderiv

def topRK(wi,torquei,h):
    K1 = h*coinEOMgeneral(wi,torquei)
    K2 = h*coinEOMgeneral(wi+K1/2,torquei)
    K3 = h*coinEOMgeneral(wi+K2/2,torquei)
    K4 = h*coinEOMgeneral(wi+K3,torquei)
    nextw = wi + (K1+2*K2+2*K3+K4)/6
    return nextw

def rotation_matrix(axis,theta):
    axis = axis/np.sqrt(np.dot(axis,axis))
    a = np.cos(theta/2)
    b,c,d = axis*np.sin(theta/2)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])

def GetSteadyStatePara(g,theta0,rho,R):
    psid = np.sqrt(4*g/np.tan(theta0)/(R*np.cos(theta0)+6*rho))
    phid = -(rho/R+np.cos(theta0))*psid
    return psid,phid    

def eulerW2bodyW_Ginsberg(psi, psid, theta, thetad, phi, phid):
    # Follow z-y-z axis rotate convention
    euler_angles_Ginsberg = [psi, psid, theta, thetad, phi, phid]
    w_body_Ginsberg = np.zeros(3)
    w_body_Ginsberg[0] = euler_angles_Ginsberg[1]*np.sin(euler_angles_Ginsberg[2])*np.cos(
        euler_angles_Ginsberg[4]) + euler_angles_Ginsberg[3]*np.sin(euler_angles_Ginsberg[4])
    w_body_Ginsberg[1] = euler_angles_Ginsberg[1]*np.sin(euler_angles_Ginsberg[2])*np.sin(
        euler_angles_Ginsberg[4]) + euler_angles_Ginsberg[3]*np.cos(euler_angles_Ginsberg[4])
    w_body_Ginsberg[2] = euler_angles_Ginsberg[1]*np.cos(euler_angles_Ginsberg[2])+euler_angles_Ginsberg[5]
    return w_body_Ginsberg

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
    
xx = 5
R = 5.0*np.sqrt(2)
#orien = np.array([-np.pi/8,0,0]) # beta
ncp = 30 # number of 'new' CP, not including origin
onetheta = 30.0 # in degrees
angles = np.arange(0,360+onetheta,onetheta)                               #[0,2,...,360]
theta = np.array(angles) * np.pi / 180                 #in radians
C = np.zeros((ncp+1,3,3))

g = 9.8
m = 1.0
Ix = 0.25*m*R*R + m*R*R
Iy = 0.25*m*R*R
Iz = 0.5*m*R*R + m*R*R


# Set the orientation of z w.r.t lab_z
leananl=np.pi/5.0
C[0,:,:] = np.dot(rotation_matrix(np.array([1,0,0]),leananl),np.eye(3))
Cprime = np.zeros((ncp+1,3,3))
CM = np.zeros((ncp+1,3))                                #CM position vector array
CM[0,:]= R*C[0,:,1]    #CM(t0)
CMprime = np.zeros((ncp+1,3))
z = np.array([0,0,1])

cirCP = np.zeros((len(angles),3,ncp))                   #circle of the coin

rotheta = onetheta*np.pi/180                                   # theta

CP = np.zeros((ncp+1,3))
CPprime = np.zeros((ncp+1,3))
lowerangle = -np.radians(np.linspace(0,ncp,ncp)/ncp)
#print(np.linspace(0,ncp,ncp)/ncp)
omega_z = np.zeros(ncp+1)           #for tracking a fix point on coin
dtarray = np.zeros(ncp)


# Numerically solve the generic euler eqs.
w = np.zeros((ncp+1,3))

# From Ginsberg initial euler angles get the steady state body angular velocity
psi0=-np.pi/2
theta0 = np.pi/2-leananl
phi0=np.pi/2
rho=R

psid0,phid0 = GetSteadyStatePara(g,theta0,rho,R)
#print(psid0,phid0)
w_body_Ginsberg = eulerW2bodyW_Ginsberg(psi0, psid0, theta0, 0, phi0, phid0)
#print(w_body_Ginsberg)
#w[0,:]=w_body_Ginsberg

w[0,2]=-0.001
w[0,1]=0.001
w[0,0]=-0.001

#w[:,2]=w[:,2]+0.0005
#w[:,1]=w[:,1]+0.001
#w[:,0]=w[:,0]-0.0005
#print(omega_z)

# The position of the fix point cirCP0 on the coin
arcvec = np.zeros((ncp+1,3))

for j in range(ncp):
    
    betaj=np.pi/2 - np.arccos(np.dot(C[j,:,1],z))
#    print(np.degrees(betaj))
    alphaangl = np.arcsin(np.sin(rotheta/2)/np.cos(betaj))
#    print(alphaangl)
    kappaj = 2*alphaangl
    phi = np.arccos(np.cos(alphaangl)/np.cos(np.radians(onetheta/2)))
#    print(np.degrees(phi))
    twodt=2*phi/w[j,1] #phi/wy
    dtarray[j]=twodt
    print(twodt)
    Avecinspace = np.dot(rotation_matrix(z,kappaj/2),
                         C[j,:,0]*R*np.sin(rotheta/2)*2)

    Cprime[j,:,:] = np.dot(rotation_matrix(z,kappaj),C[j,:,:])
    C[j+1,:,:] = np.dot(rotation_matrix(Cprime[j,:,0],w[j+1,0]*twodt),Cprime[j,:,:])

#    activerotmat = np.transpose(rotation_matrix(z,j*kappa))
#    activerotmat1 = np.transpose(rotation_matrix(z,(j+1)*kappa))
#    xprime[j,:] =np.dot(activerotmat1,x)    #next space x-axis unit vector
#    CM[j+1,:] = CM[j,:]+ C[j,:,0]*5   #CM's translational motion
    CPprime[j,:] = CP[j,:] +Avecinspace
    CP[j+1,:] = CPprime[j,:] - Cprime[j,:,0]*w[j,2]*twodt*R
#    print(w[j+1,2]*twodt*R)
    CMprime[j,:]=CM[j,:] - Cprime[j,:,0]*w[j,2]*twodt*R
    CM[j+1,:] = CP[j+1,:] + C[j+1,:,1]*R
#    axis[j+1,:] = np.cross(xprime[j,:],-CP[j+1,:]+CM[j+1,:])   #next coin-z-body-axis
#    axis[j+1,:] = axis[j+1,:]/np.linalg.norm(axis[j+1,:])
    #print(np.linalg.norm(axis[j+1,:]))
    #print(np.dot(axis[j+1,:],-CP[j+1,:]+CM))
    omega_z[j+1] = omega_z[j] - w[j,2]*twodt
    for i in range(len(angles)):
        cirCP[i,:,j] = np.dot(rotation_matrix(C[j,:,2],
                              theta[i] - omega_z[j]- j*np.radians(onetheta)),CP[j,:]-CM[j,:]) + CM[j,:]

    
    # Calculate Tau_b
    Tau_s_j = np.cross(R*C[j,:,1],np.array([0,0,-m*g]))
    Tau_b_j = np.dot(C[j,:,:],Tau_s_j)
#    print(Tau_b_j)
    
    w[j+1,:] = topRK(w[j,:],Tau_b_j,twodt)
#    print(w[j,:])

#saving for plotting
np.savez('alphaphidata',CP=CP,
                        CPprime=CPprime,
                        CM=CM,
                        R=R,
                        onetheta=onetheta,
                        cirCP = cirCP,
                        C=C,
                        Cprime=Cprime,
                        )
                        #temp_variable=[R*np.tan(np.radians(onetheta)),0,0],
                        #temp_variable1=[cirCP[1,:,0]   ,[0,0,0]            ],
                        #temp_variable2=[CPprime[0,:]        ,[0,0,0]            ],
#end of saving

#1down
fig1 = pyplot.figure(1)#,figsize=(2,2))
#fig1 = pyplot.figure(1)
ax = p3.Axes3D(fig1)
ax.view_init(elev=35, azim=-45)

cm = pyplot.get_cmap('binary')
cNorm  = colors.Normalize(vmin=-1, vmax=len(angles)-1)
scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)
ax.set_color_cycle([scalarMap.to_rgba(i) for i in range(len(angles))])

def update_line(x, line, cirCP, lcp,lcmcp, CP):
    for lcpi,angx in zip(lcp,range(len(angles))): #must keep the angles part for zip to work and rip the first element
        lcpi.set_data([CM[x,0],cirCP[0,0,x]],[CM[x,1],cirCP[0,1,x]])
        lcpi.set_3d_properties([CM[x,2],cirCP[0,2,x]])
    for indl, linein in enumerate(line):
        for li, angx1 in zip(linein,range(len(angles))):    #linein has only one instance so angx1 is zero
#            print(li)
#            print(getp(li,'color'))           
            li.set_data(cirCP[indl:2+indl,0,x],cirCP[indl:2+indl,1,x])
            li.set_3d_properties(cirCP[indl:2+indl,2,x])
#            colori = (float(indl)/float(len(angles)))
#            print(colori)
#            li.set_color([colori,colori,1-0.835164835165])
#            setp(li,color = [colori,colori,1-0.835164835165])
#            print(getp(li,'color'))               
    for lcmcpi, nouse in zip(lcmcp,lcmcp):
        lcmcpi.set_data([CM[x,0],CP[x,0]],[CM[x,1],CP[x,1]])
        lcmcpi.set_3d_properties([CM[x,2],CP[x,2]])        
    return line, lcp
        
#lines = [ax.scatter(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data] does not work

#colormap = pyplot.cm.gist_ncar
#pyplot.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, ncp)])
#the rolling circle
line = [ax.plot(*[cirCP[j:j+2,i,0] for i in range(3)]) for j in range(len(angles))]
#setp(line,lw=7) # deprecated
#line = [ax.plot(cirCP[0:2,0,0],cirCP[0:2,1,0],cirCP[0:2,2,0],color = [0,0,1])[0] for i in angles]
#the line from CM to a point on circle
lcp = [ax.plot([CM[0,0],CP[0,0]],[CM[0,1],CP[0,1]],[CM[0,2],CP[0,2]],'k')[0] for i in angles]
#the line from CM to ground
lcmcp = ax.plot([CM[0,0],CP[0,0]],[CM[0,1],CP[0,1]],[CM[0,2],CP[0,2]],'ko')
#cptrace = [ax.plot(*[ CP[i:i+2,j] for j in range(3) ]) for i in range(ncp)]
#setp(cptrace,c='b')
#setp(cptrace,lw=7)

#the CP trace
#cptrace = ax.plot(CP[0:2,0],CP[0:2,1],CP[0:2,2],'k')
#ax.set_xlim3d([-10.0, 25.0])
#ax.set_ylim3d([-10.0, 25.0])
#ax.set_zlim3d([0.0, 35.0])              
ax.set_xbound(-10,10)
ax.set_ybound(0,20)
ax.set_zbound(0,10)
#print(line)
#         ax.scatter(cirCP[1,0,1],cirCP[1,1,1],cirCP[1,2,1])]


#animation
movie = raw_input('see movie?(yes/no)')
if movie == 'yes':
    line_ani = animation.FuncAnimation(fig1, update_line, range(0,ncp,1), fargs=(line,cirCP,lcp,lcmcp,CP),
                              interval=10, blit=False,repeat=True)

    #line_ani.save('3Dcoinroll.mp4',writer = 'ffmpeg',fps='24')

    pyplot.show()
#1up

'''#draw coin roll logo
ax.set_axis_off()
ax.set_xlim([-10,10])
ax.set_ylim([2,9])
ax.set_zlim([1,8])
pyplot.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\coinlogo.pgf')
'''

'''#velocitydown
velocity = np.sum(np.square(cirCP[4,:,:-1]-cirCP[4,:,1:]),axis=0)/np.absolute(dtarray[:-1])
fig2 = pyplot.figure(2)
pyplot.plot(velocity)
pyplot.show()
'''#velocityup

'''#2down
### Turn off the perspective/orthogonal viewing effect (it works but has some side problems)
from mpl_toolkits.mplot3d import proj3d
def orthogonal_proj(zfront, zback):
    a = (zfront+zback)/(zfront-zback)
    b = -2*(zfront*zback)/(zfront-zback)
    return np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,a,b],
                        [0,0,0,zback]])
proj3d.persp_transformation = orthogonal_proj
###

### Draw fancy arrows

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
###

#### The plotting of a vector-based graphics using the above points location information.
fig2 = pyplot.figure(2,figsize=(3.5, 4),dpi=100)
ax2 = p3.Axes3D(fig2)
ax2.view_init(elev=35, azim=305)
ax2.set_color_cycle('b')

linex, = ax2.plot([0,5],[0,0],[0,0])
linex.set_linewidth(1)
ax2.text(5,0,0, r'$\hat x_0, x_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
linex.set_color('k')
liney, = ax2.plot([0,0],[0,6],[0,0])
liney.set_linewidth(1)
liney.set_color('k')
ax2.text(0,6,0, r'$y_s$', fontsize=18,verticalalignment='top', horizontalalignment='left')
linez, = ax2.plot([0,0],[0,0],[0,6])
linez.set_linewidth(1)
linez.set_color('k')
ax2.text(0,0,6, r'$z_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')

# [line_end_vec1,line_end_vec2],[same]
lineswidth2 = np.array([[CP[0,:]        ,CM[0,:]            ],
                        [CPprime[0,:]        ,CM[0,:]            ],
                        [CM[0,:]        ,[R*np.tan(np.radians(onetheta)),0,0]],
                        [cirCP[1,:,0]   ,[0,0,0]            ],
                        [CPprime[0,:]        ,[0,0,0]            ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
                        ])
(mm,nn,pp)=np.shape(lineswidth2)
for k in range(mm):
    tempk, = ax2.plot(*np.transpose(lineswidth2[k,:,:]))
    tempk.set_linewidth(2)

# plot dash lines
dashlines = np.array([[CM[0,:],[CM[0,0],CM[0,1],0]],
                      [CPprime[0,:],[CM[0,0],CM[0,1],0]]])
(mmd,nnd,ppd)=np.shape(dashlines)
for kd in range(mmd):
    tempkd,=ax2.plot(*np.transpose(dashlines[kd,:,:]),linestyle='--')
    tempkd.set_linewidth(1)
    
CP1 = np.dot(C[0,:,1],CPprime[0,:])*C[0,:,1]
line8, = ax2.plot([CPprime[0,0],CP1perpen[0]],[CPprime[0,1],CP1perpen[1]],[CPprime[0,2],CP1perpen[2]],':')
line8.set_linewidth(2)
line9, = ax2.plot([cirCP[1,0,0],CP1perpen[0]],[cirCP[1,1,0],CP1perpen[1]],[cirCP[1,2,0],CP1perpen[2]],':')
line9.set_linewidth(2)

####
arrow1 = Arrow3D([CPprime[0,0]-C[1,0,0]*1,CPprime[0,0]+C[1,0,0]],
            [CPprime[0,1]-C[1,1,0]*1,CPprime[0,1]+C[1,1,0]],
            [CPprime[0,2]-C[1,2,0]*1,CPprime[0,2]+C[1,2,0]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow1)
ax2.text(CPprime[0,0]+C[1,0,0],CPprime[0,1]+C[1,1,0],CPprime[0,2]+C[1,2,0], r'$\hat x_1$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='left')

arrow2 = Arrow3D([0,2*C[0,0,1]],
                 [0,2*C[0,1,1]],
                 [0,2*C[0,2,1]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow2)
ax2.text(2*C[0,0,1],2*C[0,1,1],2*C[0,2,1], r'$\hat y_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')

arrow3 = Arrow3D([0,2*C[0,0,2]],
                 [0,2*C[0,1,2]],
                 [0,2*C[0,2,2]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow3)
ax2.text(2*C[0,0,2],2*C[0,1,2],2*C[0,2,2], r'$\hat z_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')
         
arrow4 = Arrow3D([CPprime[0,0],CPprime[0,0]+2*Cprime[0,0,1]],
                 [CPprime[0,1],CPprime[0,1]+2*Cprime[0,1,1]],
                 [CPprime[0,2],CPprime[0,2]+2*Cprime[0,2,1]], mutation_scale=18, lw=4, arrowstyle="-|>", color="r")
ax2.add_artist(arrow4)
ax2.text(CPprime[0,0]+2*C[1,0,1],CPprime[0,1]+2*C[1,1,1],CPprime[0,2]+2*C[1,2,1], r'$\/\hat y_1$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='left')

# plot the point dots
dots = ax2.plot([0,CM[0,0],CPprime[0,0],cirCP[1,0,0],R*np.tan(np.radians(onetheta)),CP1perpen[0]],
                [0,CM[0,1],CPprime[0,1],cirCP[1,1,0],0,CP1perpen[1]],
                [0,CM[0,2],CPprime[0,2],cirCP[1,2,0],0,CP1perpen[2]], marker='o',color = 'k', lw=0 ,markersize=5,alpha=1)
dots2 = ax2.plot([CM[0,0]],
                 [CM[0,1]],
                 [0], marker='.',color = 'k', lw=0 ,markersize=10,alpha=1)
                   



arc1 = 2*circle_arc([0,0,1],[1,0,0],CPprime[0,:]-CP[0,:],10)
larc1, = ax2.plot(arc1[:,0],arc1[:,1],arc1[:,2],'k')
ax2.text(arc1[4,0],arc1[4,1],arc1[4,2], r'$\alpha$', fontsize=16,verticalalignment='center', horizontalalignment='left')
arc2 = 2*circle_arc(C[0,:,2],-CM[0,:],cirCP[1,:,0]-CM[0,:],10)+CM[0,:]
larc2, = ax2.plot(arc2[:,0],arc2[:,1],arc2[:,2],'k')
ax2.text(arc2[4,0],arc2[4,1],arc2[4,2], r'$\theta$', fontsize=16,verticalalignment='top', horizontalalignment='left')
arc3 = 1*circle_arc(C[0,:,1],cirCP[1,:,0]-CP1perpen,CPprime[0,:]-CP1perpen,10)+CP1perpen
larc3, = ax2.plot(arc3[:,0],arc3[:,1],arc3[:,2],'k')
ax2.text(arc3[-1,0],arc3[-1,1],arc3[-1,2], r'$\/\phi$', fontsize=15,
         verticalalignment='bottom', horizontalalignment='left')
arc4 = 2.5*circle_arc([-1,0,0],CM[0,:],[0,1,0],10)
larc4, = ax2.plot(arc4[:,0],arc4[:,1],arc4[:,2],'k')
ax2.text(arc4[4,0],arc4[4,1],arc4[4,2], r'$\beta$', fontsize=16,verticalalignment='bottom', horizontalalignment='left')

# perpendicular sign in the vicinity of phi
rec1 = 0.3*circle_arc(C[0,:,2],cirCP[1,:,0]-CP1perpen,C[0,:,1],2)
rec1[1,:]=rec1[1,:]*1.414
rec1 = rec1+CP1perpen
lrec1, = ax2.plot(rec1[:,0],rec1[:,1],rec1[:,2],'k')

# perp sign at CPprime[0,:]
rec2 = 0.3*circle_arc(C[1,:,2],C[1,:,0],C[1,:,1],2)
rec2[1,:]=rec2[1,:]*1.414
rec2 = rec2 + CPprime[0,:]
lrec2, = ax2.plot(rec2[:,0],rec2[:,1],rec2[:,2],'k')

# perp sign of vertical line of CM[0,:]
rec3 = 0.5*circle_arc(C[0,:,0],[0,0,1],[0,-1,0],2)
rec3[1,:]=rec3[1,:]*1.414
rec3 = rec3 + np.array([CM[0,0],CM[0,1],0])
lrec3, = ax2.plot(rec3[:,0],rec3[:,1],rec3[:,2],'k')


ax2.text(0,0,-0.5, r'$CP_0$', fontsize=13,
         verticalalignment='top', horizontalalignment='center')
ax2.text(CM[0,0],CM[0,1],CM[0,2], r'$\/CM_0$', fontsize=13,
         verticalalignment='bottom', horizontalalignment='left')
ax2.text(CPprime[0,0],CPprime[0,1],CPprime[0,2], r'$\/CP_1$', fontsize=13,
         verticalalignment='top', horizontalalignment='left')
ax2.text(cirCP[1,0,0],cirCP[1,1,0],cirCP[1,2,0], r'$\/cirCP_1$', fontsize=10,
         verticalalignment='top', horizontalalignment='left')

#print(np.linalg.norm(CM[0,:]-CP[1,:]))                   

#axis1.Axis(ax2,'r')
ax2.autoscale_view()
#ax2.pbaspect= [1,1,0.5]
#ax2.auto_scale_xyz()
#ax2.set_xlim3d([-3, 8])
#ax2.set_ylim3d([-3,8])
#ax2.set_zlim3d([-3,8])
ax2.set_xlim([-0.5,3.7])
ax2.set_ylim([-0.5,3.7])
ax2.set_zlim([0,6])
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_zticks([])
ax2.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
ax2.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax2.w_zaxis.line.set_color([0,0,0,0])
#ax2.spines['left'].set_color('b') didn't work on 3D
ax2.set_axis_off()  #-> this can turn off the background curtain
#ax2.axhline(y=1,xmin=0,xmax=1)
#ax2.set_frame_on(True)
#ax2.set_axis_bgcolor('b')
#ax2.set_position() #set the bbox of the whole axes
#ax2.set_zbound()
pyplot.show()
pyplot.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\alphaphi.pgf')

'''#2UP

'''#3down
########
fig3 = pyplot.figure(3,figsize=(5, 4))
ax3 = p3.Axes3D(fig3)
ax3.view_init(elev=30, azim=10)
ax3.set_color_cycle('b')
########

########
line3x, = ax3.plot([0,8],[0,0],[0,0])
line3x.set_linewidth(2)
ax3.text(8,0,0, r'$\hat x_0, x_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
line3x.set_color('k')
line3y, = ax3.plot([0,0],[0,8],[0,0])
line3y.set_linewidth(2)
line3y.set_color('k')
ax3.text(0,8,0, r'$y_s$', fontsize=18,verticalalignment='top', horizontalalignment='left')
line3z, = ax3.plot([0,0],[0,0],[0,4])
line3z.set_linewidth(2)
line3z.set_color('k')
ax3.text(0,0,4, r'$z_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
########


########
# [line_end_vec1,line_end_vec2],[same]
f3lineswidth2 = np.array([[CP[0,:]        ,CM[0,:]            ],
                        [CPprime[0,:]        ,CM[0,:]            ],
                        [CPprime[0,:]   ,CP[0,:]            ],
                        [CMprime[0,:]        ,CM[0,:]            ],
                        [CP[1,:]        ,CPprime[0,:]            ],
                        [CMprime[0,:]        ,CP[1,:]         ],
                        [CMprime[0,:]        ,CM[1,:]         ],
                        [CM[1,:]        ,CP[1,:]         ],
                        [CM[1,:]        ,CPprime[1,:]         ],
                        [CM[1,:]        ,CMprime[1,:]         ],
                        [CP[2,:]        ,CPprime[1,:]         ],
                        [CP[2,:]        ,CMprime[1,:]         ],
                        [CP[1,:]        ,CPprime[1,:]         ],
                        [CP[2,:]        ,CM[2,:]         ],
                        [CM[2,:]        ,CPprime[2,:]         ],
                        [CM[2,:]        ,CMprime[1,:]         ],
                        [CP[2,:]        ,CPprime[2,:]         ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
#                        [CP[0,:]        ,3*C[0,:,2]         ],
                        ])
#print(np.dot(CM[1,:]-CMprime[0,:],CM[0,:]-CMprime[0,:]))                        
                        
(mm,nn,pp)=np.shape(f3lineswidth2)
print(np.transpose(f3lineswidth2[0,:,:]))
#test3, = ax3.plot([ 0.   ,       0.        ],
#         [ 0.   ,       6.12372436],
#         [ 0.   ,       3.53553391])
#test3.set_linewidth(2)

for k in range(mm):
    ax3.plot(*np.transpose(f3lineswidth2[k,:,:]))

# plot dash lines
f3dashlines = np.array([[CM[0,:]        ,[CM[0,0],CM[0,1],0]    ],
                       [CPprime[0,:]    ,[CM[0,0],CM[0,1],0]    ],
                       [CMprime[0,:]    ,[CMprime[0,0],CMprime[0,1],0]],
                       [CMprime[1,:]    ,[CMprime[1,0],CMprime[1,1],0]],
                       [[CM[0,0],CM[0,1],0],[CMprime[0,0],CMprime[0,1],0]],
                       [CP[1,:]         ,[CM[1,0],CM[1,1],0]],
                       [CM[1,:]         ,[CM[1,0],CM[1,1],0]],
                       [CPprime[1,:]    ,[CM[1,0],CM[1,1],0]],
                       [CP[2,:]         ,[CM[2,0],CM[2,1],0]],
                       [CPprime[2,:]    ,[CM[2,0],CM[2,1],0]],
                       [CM[2,:]         ,[CM[2,0],CM[2,1],0]],
                       [[CM[1,0],CM[1,1],0],[CMprime[1,0],CMprime[1,1],0]],
#                       [[CM[0,0],CM[0,1],0],[CMprime[0,0],CMprime[0,1],0]],
                         ])
(mmd,nnd,ppd)=np.shape(f3dashlines)
for kd in range(mmd):
    ax3.plot(*np.transpose(f3dashlines[kd,:,:]),linestyle='--')
#######

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

#######
f3arrowy0 = Arrow3D([CP[0,0]-C[0,0,1]*0,CP[0,0]+C[0,0,1]],
                   [CP[0,1]-C[0,1,1]*0,CP[0,1]+C[0,1,1]],
                   [CP[0,2]-C[0,2,1]*0,CP[0,2]+C[0,2,1]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowy0)
ax3.text(CP[0,0]+C[0,0,1],CP[0,1]+C[0,1,1],CP[0,2]+C[0,2,1], r'$\hat y_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')

f3arrowz0 = Arrow3D([CP[0,0]-C[0,0,1]*0,CP[0,0]+C[0,0,2]],
                   [CP[0,1]-C[0,1,1]*0,CP[0,1]+C[0,1,2]],
                   [CP[0,2]-C[0,2,1]*0,CP[0,2]+C[0,2,2]], mutation_scale=12, lw=2, arrowstyle="-|>", color="r")
ax3.add_artist(f3arrowz0)
ax3.text(CP[0,0]+C[0,0,2],CP[0,1]+C[0,1,2],CP[0,2]+C[0,2,2], r'$\hat z_0$', fontsize=16,
         verticalalignment='bottom', horizontalalignment='right')

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
ax3.text(CPprime[0,0]+Cprime[0,0,1],
         CPprime[0,1]+Cprime[0,1,1],
         CPprime[0,2]+Cprime[0,2,1], r'$\hat y_0^\prime$', fontsize=16,
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
ax3.text(CPprime[1,0]+Cprime[1,0,1],
         CPprime[1,1]+Cprime[1,1,1],
         CPprime[0,2]+Cprime[0,2,1], r'$\hat y_1^\prime$', fontsize=16,
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
         
###### f3text CMs CPs
ax3.text(0,0,0, r'$CP_0$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')
ax3.text(CM[0,0],CM[0,1],CM[0,2], r'$\/CM_0$', fontsize=11,
         verticalalignment='bottom', horizontalalignment='left')
ax3.text(CMprime[0,0],CMprime[0,1],CMprime[0,2], r'$\/CM_0^\prime$', fontsize=11,
         verticalalignment='bottom', horizontalalignment='left')
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


######
ax3.set_xlim(0,7)
ax3.set_zlim(0,4)
ax3.set_ylim(1,7)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_zticks([])
ax3.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
ax3.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax3.w_zaxis.line.set_color([0,0,0,0])
ax3.set_axis_off()
######
pyplot.show()
pyplot.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\cm0cm1cm2.pgf')

'''#3up

'''#4down
########
fig3 = pyplot.figure(3,figsize=(3, 3))
ax3 = p3.Axes3D(fig3)
ax3.view_init(elev=30, azim=-35)
ax3.set_color_cycle('b')
########

########
line3x, = ax3.plot([-8,8],[0,0],[0,0])
line3x.set_linewidth(2)
ax3.text(8,0,0, r'$x_s$', fontsize=18,verticalalignment='center', horizontalalignment='left')
line3x.set_color('k')
line3y, = ax3.plot([0,0],[0,8],[0,0])
line3y.set_linewidth(2)
line3y.set_color('k')
ax3.text(0,8,0, r'$y_s$', fontsize=18,verticalalignment='top', horizontalalignment='left')
line3z, = ax3.plot([0,0],[0,0],[0,16])
line3z.set_linewidth(2)
line3z.set_color('k')
ax3.text(0,0,16, r'$z_s$', fontsize=18,verticalalignment='bottom', horizontalalignment='left')
########

linecir = ax3.plot(cirCP[:,0,0],cirCP[:,1,0],cirCP[:,2,0])

#radial lines
for ri in range(len(angles)):
    ax3.plot([CM[0,0],cirCP[ri,0,0]],
             [CM[0,1],cirCP[ri,1,0]],
             [CM[0,2],cirCP[ri,2,0]])

ax3.text(CM[0,0],CM[0,1],CM[0,2], r'$\/CM_0$', fontsize=11,
         verticalalignment='top', horizontalalignment='left')
ax3.text(cirCP[1,0,0],cirCP[1,1,0],cirCP[1,2,0], r'$\/cirCP_1$', fontsize=11,
         verticalalignment='top', horizontalalignment='left')
ax3.text(CP[0,0],CP[0,1],CP[0,2], r'$CP_0$', fontsize=11,
         verticalalignment='top', horizontalalignment='right')

dots3 = ax3.plot([CM[0,0],cirCP[1,0,0]],
                 [CM[0,1],cirCP[1,1,0]],
                 [CM[0,2],cirCP[1,2,0]], marker='.',color = 'b', lw=0 ,markersize=10,alpha=1)

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

rec1 = 1.6*circle_arc(C[0,:,2],C[0,:,0],C[0,:,1],2)
rec1[1,:]=rec1[1,:]*1.414
lrec1, = ax3.plot(rec1[:,0],rec1[:,1],rec1[:,2],'k')


######
ax3.set_zlim(0,11)
ax3.set_ylim(0,7)
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_zticks([])
ax3.w_xaxis.line.set_visible(False) #turn off axis visibility
#ax2.w_xaxis.line.set_color([0,0,0,0])
ax3.w_yaxis.line.set_color([0,0,0,0]) # change the color of axis
ax3.w_zaxis.line.set_color([0,0,0,0])
ax3.set_axis_off()
######
'''#4up

#pyplot.show()
#matplotlib.use('pgf')
#from matplotlib.backends.backend_agg import FigureCanvasAgg
#fig3.set_canvas(FigureCanvasAgg(fig3))
#from matplotlib.backends.backend_pgf import FigureCanvasPgf
#matplotlib.backend_bases.register_backend('pdf', FigureCanvasPgf)
#pyplot.savefig(r'C:\Documents and Settings\user\My Documents\tony\2014\Xelatexfolder\circleCP.pgf')
