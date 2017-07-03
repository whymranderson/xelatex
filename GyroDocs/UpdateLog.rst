Updates and changelog
=====================

2017/6
   The two gyro's animation methods, mplot3D and OpenGL, probably should be split up into two separate programs. Now they are tangled and very hard to maintain. Not sure how to design the GUI window layout because there are too many drawing parameters with mplot3D and OpenGL combined. Separating them may be a good idea. Already have 4-5 versions of GUI layout, and am still not satisfied.

2017/5
   py2exe finally clinched. A windows executable mems gyro program is made to easy survey the demo. Still need to make the program cleaner by removing unwanted modules, or including only the needed modules. Added chatter ring and fidget gyro turning faster upon tilting discussion.

2017/5
   Built a rotational platform to test mems gyro's accuracy. This verifies that rotation ocurring in one fix direction (x axis of gyro?) is quite accurate. Need to verify the y and z direction. And then move onto any axis. And then move on to general motion of a moving rotational axis. Also recorded a video and shared it on my blog.

2017/4
   Improving GUI window, make it easier to use. Not done yet. Try to come up with an orgainized scheme for all the demos I want to put into the program, for users and me to use the program intuitively and handily. Designing the layout of the GUI windows. Made TKinter window creation functions more modulized.

2017/4
   Documentation page numbering fix. Previously the page number of the pdf generated has a problem during printing. Automized the work pipeline of LYX to html generation, learned, logged, and blogged about the new skills. Automized the pipeline of SW to html generation. The pevious two automizations mainly invovles LaTeX math handling (MathJax), and some graphics handling. Typeseted a science fair work as a show off to the skill of our workshop.

2017/1
   Completed the 3D virtual reality demo using OpenGL. Created a 3D snenary in which one can change his angle of view with ASUS tablet, exploiting the gyro sensor inside. Also implemented our orientation algorithm. This is a suplementing example to my material to show how orientation algorithm (or more basically, body angular velocity) is applied to the rotational control in VR.

2016/12
   Fixing and upgrading the two old noise-included orien estimation demos. Meanwhile clean up some slow code and make code more modulized. Documentation code correction on case 16 and program chapter. Gyrodoc overfull line correction.

2016/11
   Added a section of graphic user interface creation using Tkinter. A digression, created a CSGO database using Django and sqlite on my second website. whymrandersonwhy.pythonanywhere.com. Unlike some big CSGO websites lacking the basic ability to show schedules by team (that is when you go to a team's page you won't see their upcoming schedule they are attending.), our database model has this scoop funtionality. It is considered during the design phase, day one, when building the Entity-Relation database table model.

2016/11
   Mission accomplished on ASUS pad rotation visualization on OpenGL. Really hyped. The result is actually quite good. Best app communication speed setting is medium. OpenGL movie plays so smooth. And drift error or accuracy is actually not bad at all. Use high(game) speed will have some lagging occured, will look into it later.

2016/10
   GUI program underwent major upgrade. Need more elaboration here...

2016/8/26
   Progress on OpenGL ASUS gyro sensor animation. Completed the integration of socket receiving angular velocity data to OpenGL animation module. Also completed animation on gyro_ring_test.py where Asus pad is displayed on the same OpenGL gyroscope platform animation we already had, only in this case the cube is replaced with a slab.

2016/8/3
   Adding OpenGL animation to the ASUS gyro case study. This includes making a OpenGL slab to represent the ASUS pad. This also takes the concept of a state machine.

2016/8/3
   Succesfully incoporate LYX to editing doc workflow and exporting doc to LaTeX file that TeXLive(XeLaTeX) can compile. Only minute adjustment is needed and it can be done automatically with python (remove all \\string"). Doc can be exported to HTML as well thanks to LYX versital abilities, which I will be using to generate my product page on my website. This means all editing can be done on LYX. To generate high quality pdf typeset docs and a html landing page one simply just push export button and LYX will handle the rest.

2016/7/21
   Now OpenGL animation can be saved into a mp4 movie by making savePNGYesNo = 
   True in the cubegyro_opengl_animation_1.py file, default to False. Remeber to
   change it back to False after you are done with saving.
   Movie's play speed can be adjusted, e.g., to slow down
   the play speed to better observe the gyroscopic motion. See more in the 
   description/docstring of the function ``savePNG`` in the software manual under
   the OpenGL animation module.

2016/7/13
   Major rearrangement on program files. Remove all unnessesary. Move gyrodoc
   folder eslewhere. Major reorganization of the contents, e.g. the orders of
   the paragraphs, of pdf document material.

2016/6/11
   Added two demo example with animations to GUI_v3 user interface as two 
   simple-enough push buttons. First one is Hercules flywheel demonstration. 
   The second one is real time ASUS pad rotational control using mems gyro 
   sensor.

2016/6/6
   Finally completed 3D visualization and animation of ASUS pad's rotation 
   control on our python simulation program in real time. This will be added 
   as a presentation demo to teach students how to use the C method we brought 
   in to apply to orientation control.

2016/5/21
   Exploit my gyro's contact force simulaiton to explain a Hercules' flywheel 
   example film on youtube, where the authos stumble on the explanation why its
   easy to hphold a flywheel on a long bar. This can be perfectly explained by 
   the contact force needed to hold the flywheel on a bar. But somehow contact 
   force failed to appear in conversation. The discussion is added in case 
   study chapter and 3D demonstration is built as a demo case in the simulation 
   program. The youtube video link can be found in the study case. 

2016/5/14
   Finally succeed to let python receive data from gyro sensor in real time on 
   the ASUS pad. Thanks to an android app written by J Zwiener, which enable 
   gyro data to be transmited over wifi. Then pick up the data on python side 
   on a computer using his suggested code too! Hmm ... stumbled here for quite 
   some time, hmmmm, but same thing went with OpenGL too. What can I say? They 
   are really not my field.

2016/3/28
   New version GS_version_3 available at GitHub! 
   https://github.com/whymranderson/cordtrans/tree/GS_version_3

2016/2/25
   Use my 3D gyroscope simulation to explain a common mistake people have on 
   angular momentom. Most people, including me, thought that the trajectory 
   of L is a circle, and the amplitude of L is a constant. The thing is L 
   does not line up with body Z (the spinning axis) as time progresses! See 
   the explaination on my webpage. Will make this into a case study soon. 

2016/2/20
   OpenGL 3D animation has been improved in appearance. Added the lucid sphere. 
   The physical size of the cube has been made to match those of python's 
   result, so no more scaling is required, which was a drawback because of 
   previous eager-fast-and-lawssy putting together. Label animation for physical 
   quantities like :math:`\omega` is being successfully tested, to be wrapped 
   up and finished later. 

2016/1/10
   Use Django to create a website on pythonanywhere.com. For two reasons. 
   First is to have better image/text transfer machenizm than those offered by 
   blogger.com. Second is to dodge the ubiquity of google and be independent. 
   If something is for free explicitly usually it is the most expensive 
   implicitly, I think.

2015/12/10
   Added OpenGL animation creation module documentation to the software manual.

2015/12/04
   GS Simulation attended Taiwan-Japan companies matchmaking fair put together 
   by ITRI, at Tainan's Shangri-La's Far Eastern Plaza Hotel.

2015/11/22
   Successfully verified my C method, orientation estimation method, can be 
   used with a MEMS gyroscope sensor to create mobile device's rotational 
   motion with my ASUS tablet. Next step is to add filtering because 
   InvenSense's gyro sensor has tons of noise. Also need to put this into an 
   example in the manuscript, and make into a slide. 

2015/11/03
   Testing a design of an angular rate sensor to it's simplest form, and added 
   as a case study to this document in the orientation estimation chapter. A 
   animation is available on my blog under title ``DIY simple angular rate 
   sensor``. This example serves as the concept paradigm of a generic angular 
   rate sensor or gyro sensor. It also proves what rate sensor measures is 
   body angular velocity.

2015/10/21
   Expanded Prof. Hasbun's Matlab code ``top_V2.m`` so that when run in Matlab 
   it will show the body xyz axes motion. It used the ``euler2space.m`` 
   function to convert from body to space frame.

2015/10/10
   Successfully utilized OpenGL to achieve real-time gyroscope 3D motion animation.

2015/8/11
   The contact force acting on the gyroscope is added to the animation. The derivation of the contact force is explained in the case study in part 3 of the manuscript.

2015/7/25
   Work presented at Meetup's Python Tainan User Group in Tainan's isrlab x Hackerspace.

2015/7/16
   Fix a bug in program where I used absolute link instead of relative link to reference modules. Previously distributed program may not work due to this reason. Now program should be able to run on all computers.

2015/7/11
   Git version control implemented to program. The reason is two-fold. First is because git makes backup very easy and ease-of-mind. No need to worry about old data overwriting new ones while copy and paste are performed. Second is because one can record the history of files and go back in time to recover an earlier version. GS version_2 is made in this way. It is an earlier version. The most-up-to-date developing version is constantly under revision. 

2015/7/11
   The logo has been artfully recrafted to resemble the gyroscope from the film "Inception". A motion trail of the gyroscope's locus is projected and mapped onto the surface of the gyroscope.

2015/7/1
   Work presented to the group of Dr. Tsao in Research Center for Information Technology Innovation(CITI) at Academia Sinica.

2015/6/25
   A demo example is added to the GUI to graph angular velocity trail observed from the body frame or world. Both angular velocities calculated from A or B method can be plotted to compare their deviation. ``Demo - Angular Velocity Trail in the body frame``

2015/6/17
   A simple GUI (graphic user interface) is built to let users better survey the demo examples.

2015/5/27
   Angular vector as a function of time, :math:`\omega_{lab}(t)/\omega_{lab}(t_{0})`, nomalized to t0 value, from B method Lagrange method using Hasbun rewritten code, is now added as an option and can be animated in 3D. Set DrawOption['B_Angular Velocity Vector (normalized to t0 value)'] = True to activate when using the B method ``HasbunEulerEquationODEsolve()``. This is seen as the true and correct angular velocity vector and can be used to compared with angular velocity calculated from A method. This way one can compare the differences and accuracy of A method, the rotation vector integration method, to other method, by looking at and comparing rotational axis.

2015/5/25
   The materials here are presented in a advanced mechanics class at NCKU mechanical engineering department. Thanks for Professor Chao-Chieh Lan's setup, feedbacks and discussion.

2015/5/20
   Sphinx, the auto documenting module, has a glitch over its ``autoclass`` function not properly showing attribute' docstrings. But one can always resort to the basic directives, ``..attribute:``. Now documentation shows rigid body object's adjustable parameters.

2015/5/11
   Comparison example to Professor Hasbun's Matlab program added. This is to ensure that our B method produced the same result as its ancestor matrix. Prof Hasbun's original Matlab code is also conveniently included in the program but to run it of course you need Matlab.

2015/4/22
   3D Cube animation accomplished and upgraded. Now animation shows a 3D rotating cube together with vectors of its physical observables and multiple trails. Run file ``Gyroscope-testCubeAnimation-2.py``. A few small loose-ends need to be tighten. Add link here?

2015/4/5
   A cube is added to represent the rotating mass. It is a static plot which means it can only show in one frame and will not show in a animation. Animating cube will be upgraded in the future.

2015/3/10
   Comparison to Christian Wolfgang's simulation of gyroscope is added. The example file to run is ``Gyroscope_Christian_Wolfgang_compared.py``. 

2013/3/5
   Rotation vector approximation J-cycle added to ``EulerDCMiter()`` as an option.

2015/2/26
   Space cone and body cone plotting function added. Function's name is ``plot_body_space_cone()``. It is a static plot. 3D animating cone will need to be integrated in the future.

2015/2/10
   Method A now has a option to use Python ODE solver instead of the RK's method I wrote. The accuracy is arguably the same. But using Python ODE solver can lower the sampling rate a lot.

2014/12/29
   C method noise-included still case added.


**Manufacture Pipeline** 

.. image:: develope_process.png
   :width: 100 %
