import numpy as np

import matplotlib.pyplot as plt

# IO - read text
from pyinterpolate import read_txt
# Experimental variogram
from pyinterpolate import build_experimental_variogram
# Theoretical Variogram
from pyinterpolate import TheoreticalVariogram, build_theoretical_variogram
DATA = 'pl_dem_epsg2180.txt'
dem = read_txt(DATA)
# Look into a first few lines of data

print(dem[-5:, :])
# Create experimental semivariogram

step_radius = 500  # meters
max_range = 10000  # meters

experimental_variogram = build_experimental_variogram(input_array=dem, step_size=step_radius, max_range=max_range)
# What is a type of experimental variogram?

print(type(experimental_variogram))
print(experimental_variogram)
experimental_variogram.plot(plot_semivariance=True, plot_covariance=True, plot_variance=True)

