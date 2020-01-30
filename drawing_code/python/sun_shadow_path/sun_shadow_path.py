import numpy as np

def CK(rotvec):
    '''Cayley-Klein parameters. Important: the built rotation matrix takes its right-hand-rule active sense.
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

omega_CM = 2*np.pi/365/24/60/60
current_time = 12*60*60 +1*60
date = 21*24*60*60+current_time
print date
sun_vec = np.dot(CK(omega_CM*date*np.array([0,0,1])),np.array([1,0,0]))
#print np.linalg.norm(sun_vec)
angle = np.arccos(np.dot(sun_vec,np.array([1,0,0])))
omega_fast = 2*np.pi/24/60/60
longitude = 22.98333/np.pi
latitude = 120.183333
taiwan = np.dot(CK(longitude*np.array([0,0,1])),np.array([1,0,0]))
#print np.linalg.norm(taiwan)
earth_ax =np.dot(CK(longitude*np.array([0,0,1])),np.array([0,1,0])) 
taiwan_current_vec = np.dot(CK((omega_fast*current_time)*earth_ax),taiwan)
print np.linalg.norm(taiwan_current_vec)
theory = np.degrees(np.arccos(np.dot(sun_vec,taiwan_current_vec)))
print 180-theory
exp = np.degrees(np.arctan(19/14.4))
print exp

Jan_15_8to5 = 14*24*60*60 + np.array([8,9,10,11,12,13,14,15,16,17])*60*60
print Jan_15_8to5
