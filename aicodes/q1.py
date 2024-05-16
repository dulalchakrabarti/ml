import plotly.figure_factory as ff
import numpy as np
#![newplot (33)|690x168](upload://i8AYByBc8UrYBgdY1QXejq9bACe.png)

x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x)*y
v = np.sin(x)*y

N = np.sqrt(u**2 + v**2)
#print(N)
u /= N
v /= N

fig = ff.create_quiver(x, y, u, v,scaleratio=0.1, scale=0.5)
fig.show()

