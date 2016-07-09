.. GyroSoft documentation documentation master file, created by
   sphinx-quickstart on Wed Jan 07 11:49:35 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Funtional Descriptions of equation of motion of top
===================================================

.. automodule:: RGCordTransV15
   :members: CK, euler2space

----

RigidBodyOjbect class

Class Functions and default parameters (with it default numerical values shown) :

.. autoclass:: RGCordTransV15.RigidBodyObject
   :members:
   :member-order: groupwise


----

All available variables accessible after functions HasbunEulerEquationODEsolve(), EulerDCMiter(), and directDCMiter() are executed.

.. class:: RGCordTransV15.RigidBodyObject

   .. attribute:: F = 9.8

      gravity force

   .. attribute:: N = round(t_n-t_0)*samplerate

      number of solved steps 

   .. attribute:: h = (tn-t0)/N

      time step interval

   .. attribute:: tlist = np.linspace(t0,tn,N+1)

      a list of all time steps

   .. attribute:: w

      A method's body angular velocity, size(N+1 x 3)

   .. attribute:: w_lab

      A method's angular velocity in lab frame, size(N+1 x 3)

   .. attribute:: w_lab_hasbun

      B method's angular velocity in lab frame, size(N+1 x 3)

   .. attribute:: theta0

      euler angle's theta[t0] in rad, this is the tilt angle of gyroscope's body z from space z axis.

   .. attribute:: b=-(Iz-Iy)/Ix*w[0,2]

      asymetric constant in the Euler-Newton equation

   .. attribute:: cordvec

      Solved gyro body xyz data. Body xyz axes vectors at all N+1 time steps in the lab frame, cordvec's array size is :math:`(N+1) \times 3 \times (3+4+3+3)`. Fist size axis N+1 is the time steps, corresponding to tlist. The second size axis 3 indicated each axis-vector's xyz components in the lab frame, the last 3+4+3+3 size axis consists of first three 0-1-2: A-method's xyz axis vectors, next four 3-4-5-6: four rectangle vertices constructed from A-methods body xyz for animation, next three 7-8-9: three hasbun/B-method's xyz axis vectors, last four 10-11-12: three C-method's xyz axis vector.

   .. attribute:: Tau_lab_t0

      initial torque produced by gravity

   .. attribute:: TrackMat_t0

      initial orientation CK matrix :math:`CK(\Omega_{0})`

   .. attribute:: L_b_t0

      initial total angular momentum in t0 body frame

   .. attribute:: L_lab

      solved A-method's total angular momentum in lab frame, size(N+1 x 3)

   .. attribute:: linesarg

      line drawing object and motional information. Need more elaboration here..

   .. attribute:: UsePY_ODE = 1   

      Instead of using the Runge Kutta method I wrote, use python ode solver library

   .. attribute:: use_Jcycle=0  

      use J-cycle rotation vector approximation

   .. attribute:: F_cp

      contact force vector in the lab frame, normalized in a way that gravity vector is half unit vector for easy observation.



