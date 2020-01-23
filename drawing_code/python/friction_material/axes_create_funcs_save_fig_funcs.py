# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
    
fig3 = plt.figure(3,figsize=(4, 4),dpi=100)
ax = plt.gca()

line1, = plt.plot([0,1],[0,0],'b')

plt.axis('equal')
plt.axis('off')
#fig3.savefig('case1b.pgf')#, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()
