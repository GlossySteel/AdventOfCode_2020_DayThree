# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:39:33 2021

@author: Joseph Kharzo
"""

# Not sure what the key error is but the program works

import pandas as pd

df = pd.read_csv("Infinite_Forest.csv")

forest = df['Forest']

trees = 0

i = 1
j = 3

moreForest = forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest + forest

while i <= 323:
    print(moreForest[i][j])
    if moreForest[i][j] == '#':
        trees +=1
    print(trees)
    j+=3
    i+=1

print(trees)