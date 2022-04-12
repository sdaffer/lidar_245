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

delta=1.016 # Correct mm distance
dist=np.array([50,100,100,200,200,300,300,400,500,600,700,800])*delta
dstd=np.array([1.583,1.78,1.78,1.75,1.70,2.58,2.61,4.87,6.99,7.50,7.59,7.22])*delta
dmean=np.array([43.42,99.12,99.88,202.8,201.68,310.6,305.03,469.64,659.90,662.91,903.68,909.9])*delta
dstderr=np.array([0.05,0.05,0.056,0.057,0.06,0.084,0.08,0.16,0.23,0.24,0.25,0.23])*delta
derr=abs(dist-dmean)

ax.errorbar(dmean,dstd,marker=None, xerr=derr, yerr=dstderr, ls='none')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
ax.tick_params(axis='y',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
#ax.set_xticks([d for i,d in enumerate(dmean) if i % 4 == 0])
#ax.set_xticklabels([f'{d}' for i,d in enumerate(dmean) if i % 2 == 0])
ax.yaxis.set_major_locator(MultipleLocator(5.00))
ax.yaxis.set_minor_locator(MultipleLocator(1.00))
ax.yaxis.get_major_locator()
ax.yaxis.get_major_formatter()
ax.grid(True,which='major',axis='both',alpha=0.3)
ax.set_xlabel('Mean Distance (mm)')
ax.set_ylabel('Standard Deviation')
ax.set_title('Object Detection Error')
#ax.legend([f'd = {d}(mm)' for i,d in enumerate(d) if i % 6 == 0], fontsize=32, loc='upper left')

plt.show()
#plt.savefig("linearexample.pdf", bbox_inches='tight')
