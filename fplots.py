import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import random

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 50
plt.rcParams['text.usetex'] = False

fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0.5,0.5,0.8,0.8])

#we very the (d1) the distance between the source and the window between
#50-1200mm with known behavior for the increasing error with distance.
#we will measure this error with grey17 and white88 to compare.
stepsize=50
maxdist=1200
mindist=50
distrange=maxdist-mindist
d1=[stepsize*n for n in range(1,int(distrange/stepsize)+2)]
d1error=np.zeros_like(d1)*0.01 # TEST FOR A REAL VALUE HERE.


#For each value of d1 we very d2 the distance between the window and the secondary
#object
d2=[n*0.25 for n in range(20)]
d2error=np.zeros_like(d2)+0.1 # TEST A REAL VALUE HERE.

# Plot the change in error for each curve as a function of distance d2.
# This way we can visualize a flat curve means no impact from the object.
# An positive trend means that the error increases with distance d2
# A negative trend mean that the error decreaseses with distance.
a=1.7
c=0.3
b=[1.7+0.05*n for n in range(len(d1))]
y=np.zeros_like(d2)
yerrs=[err+0.1*1/random.randrange(1,10) for err in np.zeros_like(y)]

for i in range(len(d1)):
        bi=b[i]
        for j in range(len(d2)):
                y[j]=a*np.exp(-(d2[j]-bi)**2/(2*c**2))
        if i % 6 == 0:
                ax.errorbar(d2,y,marker=None, xerr=d2error, yerr=yerrs, linestyle='--', linewidth=1)
#p2=ax.plot(x2,delta2,marker='o',markersize=9,markerfacecolor='blue',markeredgecolor='black',
#        markeredgewidth=2,linestyle='-',linewidth=4,zorder=3,color='blue')

ax.spines['right'].set_visible(False)
#ax.spines['left'].set_visible(False)
#ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x',which='major',direction='out',length=10,width=2,pad=15,labelsize=20)
ax.tick_params(axis='y',which='major',direction='out',length=10,width=2,pad=15,labelsize=20)
ax.set_xticks([d for i,d in enumerate(d2) if i % 2 == 0])
ax.set_xticklabels([f'{d}' for i,d in enumerate(d2) if i % 2 == 0])
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.get_major_locator()
ax.yaxis.get_major_formatter()
ax.grid(True,which='major',axis='both',alpha=0.3)
ax.set_xlabel('Distance: d (mm)')
ax.set_ylabel('Change in Error: Δerr(d+ε) (mm)')
ax.set_title('Glass Object Detection Error')
ax.legend([f'd1 = {d}(mm)' for i,d in enumerate(d1) if i % 6 == 0], fontsize=20, loc='upper right')





#p2=ax.plot(x2,delta2,marker='o',markersize=9,markerfacecolor='blue',markeredgecolor='black',
#        markeredgewidth=2,linestyle='-',linewidth=4,zorder=3,color='blue')

plt.savefig("gaussianexample.pdf", bbox_inches='tight')
