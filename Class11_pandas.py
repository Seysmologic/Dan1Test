import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %matplotlib inline

sns.get_dataset_names()
df = sns.load_dataset('iris')

print(df.head())
print(df.shape)
print(df.head(n = 10))
print(df.tail())
print(df.columns)
print(df.index)
print(df.sample(n = 5))
print(df.info())
print(df.select_dtypes(include=['float64'])) # обрати потрібні типи данних
print(df.describe()) # basic statis df
print(df.isnull())
print(df.isnull().sum())
print(df['species'])
print(df['species'].values)
print(df['species'].value_counts())
print(df['species'].value_counts(normalize= True))
print(df['species'].hist())