import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(figsize=(18,10))
ax = fig.add_subplot(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
u=x; v=y; w=z
    
ax.quiver(x, y, z, u, v, w, length=0.2)
ax.set_title(r'Vector field $\vec{F} = x\vec{i}+y\vec{j}+z\vec{k}$')
fig.savefig('vectorfield3d.png')
plt.show()
