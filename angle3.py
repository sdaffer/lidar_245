import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import random

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['axes.labelsize'] = 32
mpl.rcParams['axes.titlesize'] = 50
plt.rcParams['text.usetex'] = False

fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.2,0.2,0.6,0.6])

#we very the (d) the distance between the source and the window between
#50-1200mm with known behavior for the increasing error with distance.
#we will measure this error with grey17 and white88 to compare.

glass_distance=103.5
glass_distance_uncertainty=8.7
target_distance=236.5
target_distance_uncertainty=8.8
angle_error=3.5
glass_angle=np.array([0,5,10,15,20,30])
mean_distance=np.array([149.72,184.03,226.7,244.56,246.58,246.18])
std=np.array([1.72,1.94,1.68,1.91,1.78,1.90])
stderr=np.array([0.06,0.06,0.05,0.06,0.06,0.06])


yerr=std+stderr
xerr=np.ones_like(yerr)*angle_error

ax.errorbar(glass_angle,mean_distance,marker=None, xerr=xerr, yerr=yerr, ls='none', label='LiDaR Thick Glass')
ax.axhline(y=glass_distance, xmin=-5, xmax=65,color='orange', label='Glass Distance Measured')
ax.axhline(y=glass_distance+glass_distance_uncertainty, xmin=-5, xmax=65,color='orange',linestyle='--', label='Glass Distance Uncertainty')
ax.axhline(y=glass_distance-glass_distance_uncertainty, xmin=-5, xmax=65,color='orange',linestyle='--')

ax.axhline(y=target_distance, xmin=-5, xmax=65,color='red', label='Target Distance Measured')
ax.axhline(y=target_distance+target_distance_uncertainty, xmin=-5, xmax=65,color='red',linestyle='--', label='Target Distance Uncertainty')
ax.axhline(y=target_distance-target_distance_uncertainty, xmin=-5, xmax=65,color='red',linestyle='--')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
ax.tick_params(axis='y',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
xlabels=np.arange(0, 70,step=10)
ax.set_xticks(xlabels)
ax.set_xticklabels([f'{d}' for i,d in enumerate(xlabels)])
#ax.yaxis.set_major_locator(MultipleLocator(5.00))
#ax.yaxis.set_minor_locator(MultipleLocator(1.00))
#ax.yaxis.get_major_locator()
#ax.yaxis.get_major_formatter()
ax.grid(True,which='major',axis='both',alpha=0.3)
ax.set_ylabel('Mean Distance (mm)')
ax.set_xlabel('Window Angle (degrees)')
ax.set_title('Object Detection Error')
ax.legend(loc='center right', fontsize=20)
plt.show()
#plt.savefig("linearexample.pdf", bbox_inches='tight')
