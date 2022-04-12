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
ax = fig.add_axes([0.5,0.5,0.8,0.8])

#we very the (d) the distance between the source and the window between
#50-1200mm with known behavior for the increasing error with distance.
#we will measure this error with grey17 and white88 to compare.
stepsize=50
maxdist=1200
mindist=50
distrange=maxdist-mindist
d=[stepsize*n for n in range(1,int(distrange/stepsize)+2)]
derror=np.zeros_like(d)*0.01 # TEST FOR A REAL VALUE HERE.


#For each value of d we very angle the distance between the window and the secondary
#object
angle=[n*3 for n in range(30)]
angleerror=np.zeros_like(angle)+0.1 # TEST A REAL VALUE HERE.

# Plot the change in error for each curve as a function of distance angle.
# This way we can visualize a flat curve means no impact from the object.
# An positive trend means that the error increases with distance angle
# A negative trend mean that the error decreaseses with distance.
a=0.15
b=[0.2+0.15*n for n in range(len(d))]
y=np.zeros_like(angle)
yerrs=[err+0.1*1/random.randrange(1,10) for err in np.zeros_like(y)]

for i in range(len(d)):
        bi=b[i]
        for j in range(len(angle)):
                y[j]=a*angle[j]+bi
        if i % 6 == 0:
                ax.errorbar(angle,y,marker=None, xerr=angleerror, yerr=yerrs, linestyle='--', linewidth=1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
ax.tick_params(axis='y',which='major',direction='out',length=10,width=2,pad=15,labelsize=32)
ax.set_xticks([d for i,d in enumerate(angle) if i % 4 == 0])
ax.set_xticklabels([f'{d}°' for i,d in enumerate(angle) if i % 4 == 0])
ax.yaxis.set_major_locator(MultipleLocator(5.00))
ax.yaxis.set_minor_locator(MultipleLocator(1.00))
ax.yaxis.get_major_locator()
ax.yaxis.get_major_formatter()
ax.grid(True,which='major',axis='both',alpha=0.3)
ax.set_xlabel('Incidence Angle (φ)')
ax.set_ylabel('Change in Error: Δerr(d+ε) (mm)')
ax.set_title('Glass Object Detection Error')
ax.legend([f'd = {d}(mm)' for i,d in enumerate(d) if i % 6 == 0], fontsize=32, loc='upper left')

#plt.show()
plt.savefig("linearexample.pdf", bbox_inches='tight')
