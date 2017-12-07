import json

with open("../fibo2.pl","r") as fp:
    data=fp.read()

dico={}
maListe=data.split("\n",4)
maListe.pop()
tmp=""

for i in range(len(maListe)):
    if i == 0:
        dico[maListe[i][2:]]=[]
        tmp=maListe[i][2:]
    if i != 0:
        dico[tmp].append(maListe[i][2:])

print dico

json.dump(dico,open("../Nuit/tmp.json","w"), indent=4)
