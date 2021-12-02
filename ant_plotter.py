#!/usr/bin/env python

import numpy as np
from ant_reader import read_antfile
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

antlocs = read_antfile()

antn = antlocs['ant_id']
antx = antlocs['x']
anty = antlocs['y']
antz = antlocs['z']

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(antx,anty,antz)

for i, txt in enumerate(antn):
    ax.text(antx[i], anty[i], antz[i], txt, zorder=1, size=8)
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_zlabel('z [m]')

plt.show() 
