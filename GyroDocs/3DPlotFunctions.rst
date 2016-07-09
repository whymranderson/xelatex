3D plotting and animation functions
==================================================

.. automodule:: RBPlotFunctionV5
   :members:

----

The following objects are available for viewing. Turn on the corresponding 
objects by setting ``Drawoption['A_axes'] = True``, to make the belonging 
physical observables visible in a 3D animation. These data are processed in 
the ``AnimationFrameSetup()`` function in the ``RBPlotFunctionVxx`` module.

.. literalinclude:: ..\Physics_and_Animation_Modules_Library\RGCordTransV15.py
   :language: python
   :start-after: self.DrawOption = {
   :end-before:  '''Available drawing options''' 