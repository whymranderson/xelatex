# -*- coding: utf-8 -*-
"""
Created on Mon May 08 13:19:33 2017

The initial figure creation commands and fig saving commands are:

from matplotlib import pyplot as plt
    
fig3 = plt.figure(3,figsize=(4, 4),dpi=100)
ax = plt.gca()

line1, = plt.plot([0,1],[0,0],'b')

plt.axis('equal')
plt.axis('off')
#fig3.savefig('case1b.pgf')#, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

3D vector drawing functions for basic elements in geometry.

"""
import numpy as np
from mpl_toolkits.mplot3d import proj3d


def offset_curve(curve, length):
    '''Translate the position of all points on a 3D curve
    according to each point's normal direction described below, by specified
    length in mm. This operation is in a 2D plane. The offset normal direction is
    right hand rule's palm direction, with four fingers point
    along the curve starting from the first point, and thumb
    pointing perpendicular to the 2D plane, normally opposing the viewing direction.
     
    .. image:: ./figures/tex_group_logo.pdf
       :scale: 20 %
       :align: center

'''

    newcurve = 0*curve
    for ind,x in enumerate(curve[:,0]):
        if ind == 0:
            tangent = curve[1,:]-curve[0,:]
            tangentn = tangent/np.linalg.norm(tangent)
            nvec = np.dot(rotation_matrix([0,0,1],np.pi/2),tangentn)
            newcurve[0,:] = curve[0,:]+length*nvec
            #print newcurve
        else:
            tangent = curve[ind,:]-curve[ind-1,:]
            tangentn = tangent/np.linalg.norm(tangent)
            nvec = np.dot(rotation_matrix([0,0,1],np.pi/2),tangentn)
            newcurve[ind,:]=curve[ind,:]+length*nvec
            #print curve[ind,:]+length*nvec
            #print newcurve[ind,:]
    return newcurve
            
        


def draw_xyz_coordinate_unit_vectors(ax4):
    '''Put xyz coordinate unit vectors with fancy arrows. See figure in circle_arc.'''
    xyz_arrow_data = np.array([[1.0,0,0],[0,1.0,0],[0,0,1.0]])

    x_arrow = Arrow3D([0,xyz_arrow_data[0,0]],
                       [0,0],
                       [0,0], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(x_arrow)
    ax4.text(*xyz_arrow_data[0,:],s="x",fontsize=12)

    y_arrow = Arrow3D([0,0],
                       [0,xyz_arrow_data[1,1]],
                       [0,0], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(y_arrow)
    ax4.text(*xyz_arrow_data[1,:],s="y",fontsize=12)
    z_arrow = Arrow3D([0,0],
                       [0,0],
                       [0,xyz_arrow_data[2,2]], 
                        mutation_scale=8,
                      #lw=4,
                      arrowstyle="-|>", color="b")
    ax4.add_artist(z_arrow)
    ax4.text(*xyz_arrow_data[2,:],s="z",fontsize=12)

def draw_perpendicular_sign(rot_vec,first_axis,second_axis,location_point,ax,size):
    '''Put a perpendicular symbol to a 90 degree corner. The rot_vec
    is a vector parralel to first_axis crosses seconde_axis. First and seconde_axis are the two sides of the perp sign. Location_point is where the sign goes    . ax is the figure axes. size is the length of one side of the size.

    .. image:: ./figures/perp_sign.png
       :scale: 60 %
       :align: center

    '''
    data = size*circle_arc(rot_vec,first_axis,second_axis,2)
    data[1,:]=data[1,:]*np.sqrt(2)
    data = data+location_point
    ldata, = ax.plot(data[:,0],data[:,1],data[:,2],'k')

def rotation_matrix(axis,theta_rad):
    '''Return the rotation_matrix that actively rotate a vector.'''
    axis = axis/np.sqrt(np.dot(axis,axis))
    a = np.cos(theta_rad/2)
    b,c,d = axis*np.sin(theta_rad/2)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])

def rotmat_from_A_2_B(A,B):
    '''Return the active r.h. rotation matrix constructed from rotation vector :math:`C=A\\times B`. This matrix rotates any object in the world frame using rotation vector C.'''
    rotunit = np.cross(A, B)
    rotunit = rotunit/np.linalg.norm(rotunit)
    thetarot = np.arccos(np.dot(A/np.linalg.norm(A),B/np.linalg.norm(B)))
    rotmat = CK(thetarot*rotunit)
    return rotmat

def CK(rotvec):
    '''Cayley-Klein parameters. Important: the built rotation matrix is with its couterclockwise active sense.
    This is basically the Rodriguez rotation formula in a matric form.
    '''
    amp = np.sqrt(np.dot(rotvec,rotvec))
    if amp == 0:
        ret = np.eye(3)
    else:
        axis = rotvec/amp
        phi = amp % (2*np.pi)
        a = np.cos(phi/2)
        b,c,d = axis*np.sin(phi/2)
        ret =  np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])
    return ret


def circle_arc(axis,start_v,end_v,num_points):
    '''Return the data points of a circle. Axis is the center axis of the circle following right hand rules. Start_v is the vector of the starting point on the circle. End_v is the ending point on the circle. Num_points is the total number of points on the arc. More points give a smoother arc. Vectors take the form like np.array([1,0,0]).
    
    .. image:: ./figures/circle_arc_fig.png
       :scale: 60 %
       :align: center
       
    .. code:: python
    
      px = np.array([1,0,0])
      pA = np.array([0.5,0.5,0.5])
      n_vec = np.cross(px/np.linalg.norm(px),pA/np.linalg.norm(pA))
      arc_alpha = 0.3*tool.circle_arc(n_vec,px,pA,20)
      larc_alpha, = ax2.plot(arc_alpha[:,0],arc_alpha[:,1],arc_alpha[:,2],'r',lw=2)

'''
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

def project_a_point_to_a_plane(out_point, plane_vec1, plane_vec2,anypointonplane):
    '''Return a point which is projected normally to the plane by another point. in_point is a point on the plane. Vec1 cross Vec2 should go toward the out_point.

    .. image:: ./figures/point_projection.png
       :scale: 60 %
       :align: center

    '''
    plane_normal = np.cross(plane_vec1,plane_vec2)
    plane_normal = plane_normal/np.linalg.norm(plane_normal)
    projected = np.dot(-out_point+anypointonplane,-plane_normal)*(-plane_normal) + out_point#
    #projected = -2*plane_normal+out_point
    return projected

def return_third_point_on_a_triagle_under_Ceva_Theorem(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point F.

    .. image:: ./figures/ceva_third_side_point.png
       :scale: 60 %
       :align: center

    Also works when O is outside.
    """
    a = np.linalg.norm(pA-pE)
    b = np.linalg.norm(pC-pE)
    c = np.linalg.norm(pC-pD)
    d = np.linalg.norm(pB-pD)
    e_over_f = b*d/a/c #ace = bdf, 
    pF = (1/(1+1/e_over_f)*pA + 1/(e_over_f+1)*pB)
    return pF

def return_intersection_under_Ceva_Theorem(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point O. See figure below.
    
    .. image:: ./figures/ceva_intersection.png
       :scale: 60 %
       :align: center

    This function also works for the following case where O is outside of triangle ABC. See fig. Image generated by ceva_third_point.py.
    """
    ae = np.linalg.norm(pA-pE)
    ec = np.linalg.norm(pC-pE)
    cb = np.linalg.norm(pC-pB)
    bd = np.linalg.norm(pB-pD)
    do_over_oa = ec*bd/ae/cb #ae/ec * cb/bd * bo/oe = 1, 
    pO = (pA*do_over_oa /(1+do_over_oa) + pD/(1+do_over_oa ))#(pA*od + pD*oa)/(oa+od)
    return pO

def return_Menelaus_third_outer_point(pA,pB,pC,pD,pE):
    """Given points ABCDE, return point F. See figure below.
    
    .. image:: ./figures/menelaus_outer_point.png
       :scale: 60 %
       :align: center
    """
    ae = np.linalg.norm(pA-pE)
    ec = np.linalg.norm(pC-pE)
    cd = np.linalg.norm(pC-pD)
    bd = np.linalg.norm(pB-pD)
    bf_over_fa = ec*bd/ae/cd #ae/ec * cb/bd * bf/fa = 1, 
    pF = pB + (pB-pA)* bf_over_fa/(1- bf_over_fa) #( -pA*bf + pB*fa)/(fa-bf)
    return pF

def return_Menelaus_third_outer_point_2nd(pA,pB,pC,pD,pF):
    """Given points ABCDF, return point E. See figure above.
    
    """
    cd = np.linalg.norm(pC-pD)
    bd = np.linalg.norm(pB-pD)
    bf = np.linalg.norm(pB-pF)
    fa = np.linalg.norm(pF-pA)
    ec_over_ae = cd/bd * bf/fa #ae/ec * cb/bd * bf/fa = 1, 
    pE = (pA*ec_over_ae + pC)/(ec_over_ae +1 )#( -pA*bf + pB*fa)/(fa-bf)
    return pE


def triangle_area(pA,pB,pC):
    """Given points ABC, return area using Heron's Theorem."""
    la = np.linalg.norm(pA-pB)
    lb = np.linalg.norm(pB-pC)
    lc = np.linalg.norm(pA-pC)
    s = 0.5*(la+lb+lc)
    area =  np.sqrt(s*(s-la)*(s-lb)*(s-lc))
    return area

def solve_four_circles_on_sphere(r1,r2,r3,c):
    '''Given the radia of three mutually tangent circles (on the outside) on a midsphere, and tetra's c length (refer to the fig in the note), return length a. Following the steps described in the note, one can get r4.'''
    p = [(r2**2)*c**3 + (r2**2)*(r3**2)*c + (r1**2)*(r2**2)*c - (r1**2)*(r3**2)*c,
            -(2*(r1**2)*(r3**2)*c**2 + 2*(r1**2)*(r2**2)*(r3**2)),
            -((r1**2)*(r3**2)*c**3 + (r1**2)*(r2**2)*(r3**2)*c),]
# if c is known instead of a
#    p = [(r4**2)*(b**2)-(r2**2)*(r1**2),-(2*(r2**2)*(r1**2)*b),
#            (r4**2)*(r1**2)*(b**2) + (r2**2)*(r4**2)*(b**2) - (r2**2)*(r1**2)*(b**2) - (r2**2)*(r4**2)*(r1**2),
#            -2*(r2**2)*(r4**2)*(r1**2)*b]
    two_a = np.roots(p)
    two_b = (r1**2)*(two_a+c)/(two_a*c - (r1**2))
    two_d = (r3**2)*(two_a+c)/(two_a*c - (r3**2))
    r4 = np.sqrt((two_a*two_b*two_d)/(two_a+two_b+two_d))
    return two_a,two_b,two_d,r4



sphere_color = 'red'#'#FFDDDD'
sphere_alpha = 0.05
frame_color = 'darkgray'
frame_alpha = 0.4
frame_width = 1
sphere_grid = 40
wirestride = 3
def plot_front(axes,midspherex,midspherey,midspherez,midsphereR):
    '''plot the lucid sphere, front part. Used together with plot_back.

    .. image:: ./figures/lucid_sphere.png
       :scale: 80 %
       :align: center

    '''
    u = np.linspace(-np.pi, 0, sphere_grid)
    v = np.linspace(0, np.pi, sphere_grid)
    x = midsphereR*np.outer(np.cos(u), np.sin(v))+midspherex
    y = midsphereR*np.outer(np.sin(u), np.sin(v))+midspherey
    z = midsphereR*np.outer(np.ones(np.size(u)), np.cos(v))+midspherez
    axes.plot_surface(x, y, z, rstride=2, cstride=2,
                           color=sphere_color, linewidth=0,
                           alpha=sphere_alpha)
    axes.plot_wireframe(x, y, z, rstride=wirestride, cstride=wirestride,
                             color=frame_color,
                             alpha=frame_alpha)


def plot_back(axes,midspherex,midspherey,midspherez,midsphereR):
    '''plot the lucid sphere, back part'''
    u = np.linspace(0, np.pi, sphere_grid)
    v = np.linspace(0, np.pi, sphere_grid)
    x = midsphereR*np.outer(np.cos(u), np.sin(v))+midspherex
    y = midsphereR*np.outer(np.sin(u), np.sin(v))+midspherey
    z = midsphereR*np.outer(np.ones(np.size(u)), np.cos(v))++midspherez
    axes.plot_surface(x, y, z, rstride=2, cstride=2,
                           color=sphere_color, linewidth=0,
                           alpha=sphere_alpha)
    axes.plot_wireframe(x, y, z, rstride=wirestride, cstride=wirestride,
                             color=frame_color,
                             alpha=frame_alpha)

def cylinder(ax2,c1,c2,radius):
    ''' Plot from cylinder's both end circle's centers c1 and c2 and radius.'''
    length = np.linalg.norm((c2-c1))/2
    x=np.linspace(-1*radius, 1*radius, 100)
    z=np.linspace(-1*length, 1*length, 100)
    Xc, Zc=np.meshgrid(x, z)
    Yc = np.sqrt(np.square(radius) - np.square(Xc))
    cmm,cnn = np.shape(Yc)
    mat_zn2omega = rotmat_from_A_2_B(np.array([0,0,1]),(c2-c1)/length)
    Xcu,Ycu,Zcu =np.zeros((100,100)),np.zeros((100,100)),np.zeros((100,100))     
    Xcm,Ycm,Zcm =np.zeros((100,100)),np.zeros((100,100)),np.zeros((100,100))   
    for i in range(cmm):
        for j in range(cnn):
            Xcu[i,j],Ycu[i,j],Zcu[i,j] = np.dot(mat_zn2omega,
            np.array([Xc[i,j],Yc[i,j],Zc[i,j]])) 
    for i in range(cmm):
        for j in range(cnn):
            Xcm[i,j],Ycm[i,j],Zcm[i,j] = np.dot(mat_zn2omega,
            np.array([Xc[i,j],-Yc[i,j],Zc[i,j]])) 
    # Translate
    distance = (c2-c1)/2 + c1
    # Draw parameters
    rstride = 3
    cstride = 20
    ax2.plot_surface(Xcu+distance[0], Ycu+distance[1], Zcu+distance[2], alpha=0.3, rstride=rstride, cstride=cstride)
    ax2.plot_surface(Xcm+distance[0], Ycm+distance[1], Zcm+distance[2], alpha=0.3, rstride=rstride, cstride=cstride)
    #ax2.plot_surface(Xc+distance[0], Yc+distance[1], Zc+distance[2], alpha=0.9, rstride=rstride, cstride=cstride)
    #ax2.plot_surface(Xc+distance[0], Yc+distance[1], Zc+distance[2], alpha=0.9, rstride=rstride, cstride=cstride)


def incircle3D(point1,point2,point3):
    """Return the insubscribed circle's center's position pO, radius r and norm vec nv and 
    three Ceva sidepoints p12,p23,p31 from a triangle(p1,p2,p3). If you only need a partial results,
    put dummy or _ or use foo()[0,3,4].

    .. image:: ./figures/incircle_triangle.png
       :scale: 60 %
       :align: center
       
    .. code:: python

       pO,r,nv,p12,p23,p31 = incircle3D(p1,p2,p3)
       pO,r, _,p12,p23,p31 = incircle3D(p1,p2,p3)
       pO,r, _,dummy1,dummy2,dummy3 = incircle3D(p1,p2,p3)
       p12,p23,p31 = incircle3D(p1,p2,p3)[3,4,5]

       """
    dist12 = np.sqrt(np.sum(np.square(point1-point2)))
    dist23 = np.sqrt(np.sum(np.square(point2-point3)))
    dist13 = np.sqrt(np.sum(np.square(point1-point3)))
    incenter = (dist12*point3 + dist23*point1 + dist13*point2)/(dist12+dist23+dist13)
    inradius = 0.5*np.sqrt((dist12+dist23-dist13)*
                            (dist12-dist23+dist13)*
                            (-dist12+dist23+dist13)/
                            (dist12+dist23+dist13))    
    axisvec = np.cross(point1-point2,point1-point3)
    normvec = axisvec/np.linalg.norm(axisvec)  
    L_1t12 = np.sqrt(np.square(np.linalg.norm(point1-incenter)) - np.square(inradius))  
    t12 = point1 + L_1t12 * (point2-point1) / np.linalg.norm(point2-point1)
    L_2t23 = np.sqrt(np.square(np.linalg.norm(point2-incenter)) - np.square(inradius))  
    t23 = point2 + L_2t23 * (point3-point2) / np.linalg.norm(point3-point2)
    L_3t31 = np.sqrt(np.square(np.linalg.norm(point3-incenter)) - np.square(inradius))  
    t31 = point3 + L_3t31 * (point1-point3) / np.linalg.norm(point1-point3)
    return incenter,inradius, normvec, t12, t23, t31

def four_points_circle(p1,p2,p3,p4):
    """ Return center and radius of a sphere suscribing four points p1~4. """
    x2y2z2=0
    M = np.array([[x2y2z2,p1[0],p1[1],p1[2],1],
                  [np.sum(np.square(p1)),p1[0],p1[1],p1[2],1],
                  [np.sum(np.square(p2)),p2[0],p2[1],p2[2],1],
                  [np.sum(np.square(p3)),p3[0],p3[1],p3[2],1],
                  [np.sum(np.square(p4)),p4[0],p4[1],p4[2],1]])    
    M11 = M[1:,1:]
    M11d = np.linalg.det(M11)
    M12 = np.array([
                  [np.sum(np.square(p1)),p1[1],p1[2],1],
                  [np.sum(np.square(p2)),p2[1],p2[2],1],
                  [np.sum(np.square(p3)),p3[1],p3[2],1],
                  [np.sum(np.square(p4)),p4[1],p4[2],1]]) 
    M12d = np.linalg.det(M12)
    x0 = 0.5*M12d/M11d
    M13 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[2],1],
                  [np.sum(np.square(p2)),p2[0],p2[2],1],
                  [np.sum(np.square(p3)),p3[0],p3[2],1],
                  [np.sum(np.square(p4)),p4[0],p4[2],1]])    
    M13d = np.linalg.det(M13)
    y0 = -0.5*M13d/M11d

    M14 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[1],1],
                  [np.sum(np.square(p2)),p2[0],p2[1],1],
                  [np.sum(np.square(p3)),p3[0],p3[1],1],
                  [np.sum(np.square(p4)),p4[0],p4[1],1]])    
    M14d = np.linalg.det(M14)
    z0 = 0.5*M14d/M11d
    M15 = np.array([
                  [np.sum(np.square(p1)),p1[0],p1[1],p1[2]],
                  [np.sum(np.square(p2)),p2[0],p2[1],p2[2]],
                  [np.sum(np.square(p3)),p3[0],p3[1],p3[2]],
                  [np.sum(np.square(p4)),p4[0],p4[1],p4[2]]])    
    M15d = np.linalg.det(M15)
    R = np.sqrt(x0**2+y0**2+z0**2-M15d/M11d)
    return x0,y0,z0,R

def return_orthocenter(p1,p2,p3):
    """Return orthocenter by first finding two points of foot of perpendicular then using Ceva Theorem."""
    perp23 = project_a_point_to_a_plane(p1,np.cross(p3-p2,p1-p2),p3-p2,p2)
    perp13 =project_a_point_to_a_plane(p2,np.cross(p1-p3,p2-p3),p1-p3,p3)
    ortho = return_intersection_under_Ceva_Theorem(p1,p2,p3,perp23,perp13)
    return ortho

def return_centroid(p1,p2,p3):
    """Return centroid by using Ceva Theorem."""
    m23 = (p2+p3)/2
    m13 = (p1+p3)/2
    centroid = return_intersection_under_Ceva_Theorem(p1,p2,p3,m23,m13)
    return centroid

def return_circumcenter(p1,p2,p3):
    """Return circumcenter using centroid and orthocenter and the Euler's line of a triangle. Another keyword: 9-point circle. Fig here."""
    circumcenter = (3 * return_centroid(p1,p2,p3) - return_orthocenter(p1,p2,p3))/2
    return circumcenter

def return_9point_circle_center(p1,p2,p3):
    """Return 9-points center using Euler's line."""
    ninepcenter = ( return_orthocenter(p1,p2,p3) + return_circumcenter(p1,p2,p3) )/2
    return ninepcenter

def circle_full(axis,start_v,radius,num_points):
    """Return drawing data of a full circle centered on origin, need a drawing here. start_v is the any vector 
    paralel to first data point. The plot command is needed to make circle visible. see code. To
    move the circle remember to add circle center. See code.

    .. code:: python
    
       v1 = np.array([1,0,0])
       n_vec = np.array([0,0,1])
       circle1 = circle_full(n_vec,v1,0.3,20) + circle_center
       circle1, = ax2.plot(circle1[:,0],circle1[:,1],circle1[:,2],'r',lw=2)
    """
    axis = axis/np.linalg.norm(axis)
    start_v = start_v/np.linalg.norm(start_v)
    theta = 2*np.pi
    theta_s = list(np.arange(0.0, theta + theta/num_points, theta/num_points))
    circle_vecs = np.zeros([len(theta_s),3])
    for i,thetai in enumerate(theta_s):
        makecir = rotation_matrix(axis,thetai)
        circle_vecs[i,:] = np.dot(makecir,start_v)
    return circle_vecs*radius


def showing_usage_of_dot_datapoints():
    ''' ax2.scatter3D(*zip(pJ,pK,pL,pI,pO,pM,pN,pH,pG,pE,pF)) what about color?'''
    

def third_seg_incircled(x,y,r):
    """Return z following the relation of the xyz lengths bisect by incircle and the r radius.
    :math:`r=\\sqrt{\\frac{xyz}{x + y + z}}`

    .. image:: ./figures/third_seg_incircled.png
       :scale: 60 %
       :align: center
       
    The py script to generate this fig is the same as the script that generates the fig in the
    incircle3D funtion, the incircle_triangle.py, but in a different git commit, tagged
    xyzr_thir_sed.
    """
    z = np.square(r)*(x+y)/(x*y-np.square(r))
    return z

def plot_body_space_cone(ax,height_vec,side_vec,location_tip):
    '''
    Plot a cone with the specified parameters.
    '''
    # Set up the grid in polar coordinate theta, radius
    zn = height_vec/np.linalg.norm(height_vec)
    omegavec =side_vec
    cone_theta = np.linspace(0,2*np.pi,90)
    bcone_radius = np.linalg.norm(height_vec - side_vec) 
    bcone_len = np.linalg.norm(height_vec) 
    
    cone_r = np.linspace(0,bcone_radius,15)
    c1T, c1R = np.meshgrid(cone_theta, cone_r)
    # Then calculate X, Y, and Z
    c1X = c1R * np.cos(c1T)
    c1Y = c1R * np.sin(c1T)
    c1Z = np.sqrt(c1X**2 + c1Y**2)/bcone_radius*bcone_len
    cmm,cnn = np.shape(c1Z)
    mat_zn2omega = rotmat_from_A_2_B(np.array([0,0,1]),zn)
    for i in range(cmm):
        for j in range(cnn):
            c1X[i,j],c1Y[i,j],c1Z[i,j] = np.dot(mat_zn2omega,
            np.array([c1X[i,j],c1Y[i,j],c1Z[i,j]]))

    ax.plot_surface(c1X+location_tip[0],
                    c1Y+location_tip[1],
                    c1Z+location_tip[2],rstride=5, cstride=5,linewidth=0,alpha=0.16,color = 'black')    
    
#def length_annotation_arc_style(ax2,p1,p2,style_str="arc3,rad=0.5",va_str,ha_str):
#    ''' testing, '''
#    p1perp=tuple(proj3d.proj_transform(*p1, M = ax2.get_proj()))[:2], 
#    p2perp=tuple(proj3d.proj_transform(*p2, M = ax2.get_proj()))[:2], 
#    p12p = p2perp - p1perp 
#    pO = 1.0/np.sqrt(3)*0.5*np.dot(rotation_matrix(np.array([0,0,-1]),np.pi/2),np.array([p12p[0],p12p[1],0))+ (p1perp+p2perp)/2 
#    circle_arc(np.array([0,0,-1]),start_v,end_v,num_points)
#
#def length_annotation(ax2,p1,p2,style_str="arc3,rad=0.5",va_str,ha_str):
#    ''' Text location problem unsovled....
#    style_str = "arc3,rad=0.5"
#    usage length_annotation(ax2,p1,p2,"arc3,rad=0.5",top,right)
#    The arc will be on the left side of vector p12
#    '''
#    ax2.annotate("",
#            xy=tuple(proj3d.proj_transform(*p1, M = ax2.get_proj()))[:2], #xycoords='data',
#            xytext=tuple(proj3d.proj_transform(*p2, M = ax2.get_proj()))[:2], #textcoords='data',
#            arrowprops=dict(arrowstyle="-", #linestyle="dashed",
#                            color="0.5",
#                            patchB=None,
#                            shrinkB=0,
#                            connectionstyle=style_str,
#                            ),
#            )
#    pla = (p1+p2)/2
#    ax2.annotate(s = 'a\n ',xy = tuple(proj3d.proj_transform(*pla, M = ax2.get_proj()))[:2],
#             bbox={'pad':12,'fill':None,'edgecolor':'None'},va=va_str,ha=ha_str,color="0.5")

def just2show_length_annotaion_usage():
    '''
    To indicate equal lengthes by putting symbols on line segments.

    .. code:: python

       mar_a = mpl.markers.MarkerStyle(marker='_')
       mar_a._transform = mar_a.get_transform().rotate_deg(-30) # Rotate counterclockwise
       ax2.scatter3D(*zip(pointA,),marker=mar_a,s=90,color='k')
       
       mar2 = mpl.markers.MarkerStyle(marker='$||$')
       mar2._transform = mar2.get_transform().rotate_deg(-5) # Rotate ccw
       ax2.scatter3D(*zip(pointB,),marker=mar2,s=80,color='k')

       mar1 = mpl.markers.MarkerStyle(marker='$|||$')
       mar1._transform = mar1.get_transform().rotate_deg(-15)
       ax2.scatter3D(*zip(pointC,),marker=mar1,s=100,color='k')

    .. image:: ./alphaphi.png
       :scale: 40 %
       :align: center
    
    .. code:: python

       ax2.scatter3D(*zip(point1,),marker='o',s=64,edgecolors='k',facecolor="None")
       ax2.scatter3D(*zip(point2,),marker='s',s=64,edgecolors='k',facecolor="None")
       ax2.scatter3D(*zip(point3,),marker='$=$',s=64,edgecolors='k',facecolor="None")

    .. image:: ./figures/spherical_triangles_patches_inspired.png
       :scale: 50 %
       :align: center


    '''


#%% Turn off the perspective/orthogonal viewing effect (it works but has some side problems)
#from mpl_toolkits.mplot3d import proj3d
def orthogonal_proj(zfront, zback):
    a = (zfront+zback)/(zfront-zback)
    b = -2*(zfront*zback)/(zfront-zback)
    return np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,a,b],
                        [0,0,0,zback]])
#proj3d.persp_transformation = orthogonal_proj
###

#%% Draw fancy arrows
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


