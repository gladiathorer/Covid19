import pandas as pd

df = pd.read_csv('output.csv')

betegségSzámok = {}

össz = len(df["Sorszám"])

for sor in df["Alapbetegségek"]:
    for betegség in sor.split(', '):
        if betegség in betegségSzámok:
            betegségSzámok[betegség] = betegségSzámok[betegség] + 1
        else:
            betegségSzámok[betegség] = 1

rendezett = {k: v for k, v in sorted(betegségSzámok.items(), key=lambda item: item[1], reverse=True)} #megrendezem

for i in rendezett:
    if betegségSzámok[i] > 100:
        print("{} betegség {} alkalommal ({:.2f} százalék)".format(i, betegségSzámok[i], betegségSzámok[i]/össz))
'''
Jó ötlet, mondjuk ha megnézed az outputját, akkor látszik, hogy van benne egy két dolog amit fejleszteni lehetne, mondjuk regexel :)
'''
