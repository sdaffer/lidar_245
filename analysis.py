import numpy as np
import pandas as pd

angle=str(0)


filename='file.csv'
data = np.asarray(pd.read_csv(filename))

data = data[1:,1]
# data = data[1:]
data = np.asarray(data[1:], dtype=float)
mean=np.mean(data)
median=np.median(data)
std=np.std(data)
se=np.std(data) / np.sqrt(np.shape(data)[0])

print(data)

print("mean:",mean)
print("median:", median)
print("std:",std)
print("se:",se)
print("n: ", np.shape(data)[0])

pd.DataFrame(data).to_csv(angle + '_deg_' + '_precise_2.csv')