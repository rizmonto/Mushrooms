from data_functions import*
from pprint import pprint
import numpy as np
import pandas as pd
import pylab as p

instance_filename = 'train.csv'
instances = np.array(load_instances(instance_filename))

#print type(instances[0::, 5])

#df = load_instances_panda(instance_filename)

df = load_instances_panda(instance_filename)

#print df.head(3)

#print df.dtypes

#print df.info()

#print df.describe()

#print df[df['Age'] > 60][['Sex', 'Pclass', 'Age', 'Survived']]

#print df[df['Age'].isnull()][['Sex', 'Pclass', 'Age', 'Survived']]

#for i in range (1, 4):
   # print i, len(df[(df['Sex'] == 'male') & (df['Pclass'] == i)])

#df['Age'].dropna().hist()
df['Age'].dropna().hist(bins=16, range=(0,80), alpha = .5)
p.show()