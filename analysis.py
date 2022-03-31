import numpy as np
import pandas as pd

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

pd.DataFrame(data).to_csv(str(median) + '_glass_nopaper.csv')