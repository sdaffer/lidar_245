from cmath import rect
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
# ax = fig.add_axes([0.2,0.2,0.8,0.8])
ax = fig.add_axes([0.2,0.2,0.6,0.6])
# ax = fig.add_axes([])
# ax = fig.add_axes([0.5,1,0.5,1])

#we very the (d) the distance between the source and the window between
#50-1200mm with known behavior for the increasing error with distance.
#we will measure this error with grey17 and white88 to compare.

# beam splitter w/ backdrop at 200mm 0 deg incidence
delta=1.016 # Correct mm distance
dist=np.array([50, 100, 150, 150])*delta
dstd=np.array([1.73, 1.80, 1.66, 1.86])*delta
dmean=np.array([23.21, 73.52, 133.88, 119.12])*delta
dstderr=np.array([0.06, 0.06, 0.05, 0.06])*delta
derr=abs(dist-dmean)
ax.errorbar(dmean,dstd,marker=None, xerr=derr, yerr=dstderr, ls='none', label='LiDaR Target')

# beam splitter w/0 backdrop 0 deg incidence
delta=1.016 # Correct mm distance
dist=np.array([50, 100, 150])*delta
dstd=np.array([1.96, 1.78, 1.83])*delta
dmean=np.array([17.15, 66.39, 119.12])*delta
dstderr=np.array([0.06, 0.06, 0.06])*delta
derr=abs(dist-dmean)
ax.errorbar(dmean,dstd,marker=None, xerr=derr, yerr=dstderr, ls='none', label='LiDaR No Target')


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
# ax.legend([f'd = {d}(mm)' for i,d in enumerate(d) if i % 6 == 0], fontsize=32, loc='upper left')
ax.legend(loc='center right', fontsize=20)
# plt.show()
plt.savefig("angletest.pdf", bbox_inches='tight')
