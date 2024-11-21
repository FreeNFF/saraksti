D = {}
print(D)

saraksts = [['a',1],['b',2],['a',3],['a',4],['c',5],['c',1000]]

for i in range(len(saraksts)):
    #ja ir atslēga, tad pievieno vērtību
    if saraksts[i][0] in D:
        D[saraksts[i][0]].append(saraksts[i][1])

    #ja nav, tad to pievieno
    else:
        D[saraksts[i][0]] = []
        D[saraksts[i][0]].append(saraksts[i][1])

print(D)

