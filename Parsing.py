import pandas as pd


smart_csv= 'RL/policies/e1a3g9'
rand_csv = "ABM/random10k.csv"



df=pd.read_csv(rand_csv)
temp=df['Winner']
list_of_winners = []
for i in temp:
    list_of_winners.append(i)
print(
    'RANDOM GAME: \n Player 1 succes rate:', list_of_winners.count(1)*100/len(list_of_winners),'%',
    '\n Player 2 succes rate: ', list_of_winners.count(2)*100/len(list_of_winners),'%'
)

list_of_winners = []
_list_of_winners = []
f = open(smart_csv, "r")
fnew=f.readlines()
for i in fnew:
    list_of_winners.append(i[-4])
for i in list_of_winners:
    _list_of_winners.append(int(i))
print(
    'SMART GAME: \n Player 1 succes rate:', _list_of_winners.count(1)*100/len(_list_of_winners),'%',
    '\n Player 2 succes rate: ', _list_of_winners.count(2)*100/len(_list_of_winners),'%'
)

