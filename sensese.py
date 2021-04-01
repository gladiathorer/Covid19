import numpy as np 
import matplotlib.pyplot
import time
import pandas as pd

bai = pd.read_csv('by_agegroups_input.csv')
print(bai.columns)
print(bai.head())

def to_list(string):
    return [int(s) for s in string.split() if s.isdigit()]

#print(bai['Halottak kora'].tolist()[0])

bai['hk'] = bai.apply(lambda x: to_list(x['Halottak kora']), axis = 1)
print(bai.columns, bai.head())
print(to_list((bai['hk'].tolist()[3])))

def scatter(list):
    unique = {}
    for v in list:
        unique.setdefault(v, [0]).append(0)
    print(unique)

print(type(bai['Halottak kora'].tolist()[0]))
#scatter(bai['Halottak kora'].tolist()[0])