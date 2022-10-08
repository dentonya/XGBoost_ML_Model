import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.read_csv('Historical Product Demand.csv')
dt=df.head()
#print(dt)
y = df.describe().transpose()
#print(y)
s = df.shape
z = df.nunique()
#print(s)
#print(z)
t = df.tail(10)
print(t)