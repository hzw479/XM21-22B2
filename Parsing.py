import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import tree
import ast
import matplotlib.pyplot as plt
import numpy as np
import itertools
from ast import literal_eval as make_tuple

file_name= 'RL/policies/e1a3g9'
"""
df=pd.read_csv("testcsv")
#print(len(df))
df= df.drop_duplicates().reset_index(drop=True)
#print(len(df))





y,x=df['Winner'], df['Pegs removed']
X=[]
for i in x:
    X.append(ast.literal_eval(i))

for i in range(len(X)):
    for j in range(len(X[i])):
        flatlist = sum(X[i][j], ())
        X[i][j]=int(''.join(map(str, flatlist)))

Xdf=pd.DataFrame(X).fillna(0)
X_train, X_test, y_train, y_test = train_test_split(Xdf, y, test_size=0.33, random_state=42)
#print(len(X_train), len(y_train))
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
tree.plot_tree(clf)


df=pd.read_csv("Mietestreadme")
temp=df['Winner']
list_of_smart_winners = []
for i in temp:
    list_of_smart_winners.append(i)
print(
    'dumb game: 1:', list_of_smart_winners.count(1),
    '2: ', list_of_smart_winners.count(2)
)

list_of_winners = []
_list_of_winners = []
f = open(file_name, "r")
fnew=f.readlines()
for i in fnew:
    list_of_winners.append(i[-4])
for i in list_of_winners:
    _list_of_winners.append(int(i))
print(
    'smart game: 1:', _list_of_winners.count(1),
    '2: ', _list_of_winners.count(2)
)
#f_list=fnew[0].split(',')
#listlist=[]
#for i in f_list:
#    try:
#        integer = int(i)
#        listlist.append(integer)
#    except:
#        continue
#print(
#    'smart game: 1:', listlist.count(1),
#    '2: ', listlist.count(2)
#)
"""
df=pd.read_csv("dict.csv", names=['Weight', 'Board'])

hej=df.loc[df['Weight'] >= 0.7]
print(hej)
hej.to_csv(r'mettecsv', index = False)

