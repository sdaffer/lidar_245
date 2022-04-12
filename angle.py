import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import random

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['axes.labelsize'] = 32
mpl.rcParams['axes.titlesize'] = 50
plt.rcParams['text.usetex'] = False

fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.2,0.2,0.8,0.8])

#we very the (d) the distance between the source and the window between
#50-1200mm with known behavior for the increasing error with distance.
#we will measure this error with grey17 and white88 to compare.

glass_distance=103.5
glass_distance_uncertainty=8.7
target_distance=236.5
target_distance_uncertainty=8.8
angle_error=3.5
glass_angle=np.array([0,0,5,10,15,20,30,40,50,50,60])
mean_distance=np.array([92.01,90.35,112.21,172.61,240.10,244.83,245.09,244.25,243.55,243.91,242.42])
std=np.array([1.62,1.80,2.87,2.21,1.92,2.10,2.12,2.09,2.11,2.09,2.31])
stderr=np.array([0.05,0.06,0.09,0.07,0.06,0.07,0.07,0.07,0.07,0.07,0.07])


yerr=std+stderr
xerr=np.ones_like(yerr)*angle_error

ax.errorbar(glass_angle,mean_distance,marker=None, xerr=xerr, yerr=yerr, ls='none')
ax.axhline(y=glass_distance, xmin=-5, xmax=65,color='orange')
ax.axhline(y=glass_distance+glass_distance_uncertainty, xmin=-5, xmax=65,color='orange',linestyle='--')
ax.axhline(y=glass_distance-glass_distance_uncertainty, xmin=-5, xmax=65,color='orange',linestyle='--')

ax.axhline(y=target_distance, xmin=-5, xmax=65,color='red')
ax.axhline(y=target_distance+target_distance_uncertainty, xmin=-5, xmax=65,color='red',linestyle='--')
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
ax.legend([f'd = {d}(mm)' for i,d in enumerate(d) if i % 6 == 0], fontsize=32, loc='upper left')

plt.show()
#plt.savefig("linearexample.pdf", bbox_inches='tight')
