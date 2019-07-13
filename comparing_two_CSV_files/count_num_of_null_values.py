import csv
import numpy as np
import pandas as pd

first = pd.read_csv("FL_insurance_sample.csv")
null_columns=first.columns[first.isnull().any()]
nu1 = first[null_columns].isnull().sum()
print("In first table:")
print(nu1)

#all null cols
#print(train[train.isnull().any(axis=1)][null_columns].head())

second = pd.read_csv("FL_insurance_sample.csv")
null_columns=second.columns[second.isnull().any()]
nu2 = second[null_columns].isnull().sum()
print("\n In second table:")
print(nu2)

if(nu1.equals(nu2)):
    print("\n Number or null values are matching")

