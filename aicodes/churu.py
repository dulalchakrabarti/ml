import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi

from windrose import WindroseAxes

#Open wind data from a Excel file

df = pd.read_excel('churu.xlsx')
#print(df.head)
df['WS10M_x'] = df['WS10M'] * np.sin(df['WD10M'] * pi / 180.0)
df['WS10M_y'] = df['WS10M'] * np.cos(df['WD10M'] * pi / 180.0)
fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
df.plot(kind='scatter', x='WS10M_x', y='WS10M_y', alpha=0.35, ax=ax)
plt.savefig('xy.jpg')
plt.show()
df['WS10M'].hist(figsize=(10,6))
plt.savefig('hist.jpg')
plt.show()
ax = WindroseAxes.from_ax()
ax.bar(df.WD10M, df.WS10M, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.savefig('windrose1.jpg')
plt.show()
ax = WindroseAxes.from_ax()
ax.box(df.WD10M, df.WS10M, bins=np.arange(0, 8, 1))
ax.set_legend()
plt.savefig('windrose2.jpg')
plt.show()
ax = WindroseAxes.from_ax()
ax.contourf(df.WD10M, df.WS10M, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.set_legend()
plt.savefig('contour1.jpg')
plt.show()
ax = WindroseAxes.from_ax()
ax.contour(df.WD10M, df.WS10M, bins=np.arange(0, 8, 1), cmap=cm.hot, lw=3)
ax.set_legend()
plt.savefig('contour2.jpg')
plt.show()

