import iris
import numpy as np

print(iris.__version__)
print(np.__version__)

import iris.plot as iplt
import iris.quickplot as qplt
import matplotlib.pyplot as plt

cube = iris.load_cube(iris.sample_data_path('A1B_north_america.nc'))
ts = cube[-1, 20, ...]
plt.subplot(2, 1, 1)
iplt.plot(ts)

plt.subplot(2, 1, 2)
qplt.plot(ts)

plt.subplots_adjust(hspace=0.5)
plt.show()
import cartopy.crs as ccrs

plt.figure(figsize=(12, 8))

plt.subplot(1, 2, 1)
qplt.contourf(cube[0, ...], 25)
ax = plt.gca()
ax.coastlines()

ax = plt.subplot(1, 2, 2, projection=ccrs.RotatedPole(100, 37))
qplt.contourf(cube[0, ...], 25)
ax.coastlines()

plt.show()

