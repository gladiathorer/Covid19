import pandas as pd

def halottkem():
    mylist = [pd.read_html('https://koronavirus.gov.hu/elhunytak')[0]]
    for i in range(1,335):
        temp = pd.read_html('https://koronavirus.gov.hu/elhunytak?page={}'.format(i))[0]
        mylist.append(temp)
    finallist = pd.concat(mylist)
    finallist.to_csv('output.csv')

df = pd.read_csv('input.csv')
for i in range(len(df['Az új elhunytak száma naponta'])):
    print(df['Dátum'][i])