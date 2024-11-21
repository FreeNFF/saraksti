#izveidot sarakstu
saraksts = ['burgers', 'kebabs', 'hotdogs']
print(saraksts)
#noteikt garumu
print("Saraksta garums = ",len(saraksts))
print("--------------------------------------------------")

#pielikt elementu saraksta beigās
saraksts.append('pica')
print(saraksts)
print("--------------------------------------------------")

#ievietot elementu pirms cita elementa ar indeksu
saraksts.insert(1, 'tortīlija')
print(saraksts)
print("--------------------------------------------------")

#mainīt sarakstu elementu secību uz pretējo
saraksts.reverse()
print(saraksts)
print("--------------------------------------------------")

#noņemt elementu
#saraksts.remove('hotdogs')#uzreiz elementu
saraksts.pop(1)#noņemt pēc indeksa, pēr kārtas skaitļa
print(saraksts)
print("--------------------------------------------------")

#nomainīt esošu elementu ar jaunu
saraksts[0] = 'pizza'
saraksts[1] = 'kebab'
saraksts[2] = 'tortilla'
saraksts[3] = 'burger'
print(saraksts)

saraksts = [1, 3, 8, 12]
print(type(saraksts), '\nx= ', saraksts)#izdrukā skaitļu rindu kā sarakstu

#divudomensiju masīvs
divdimensiju_masivs = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 24]]
print(divdimensiju_masivs)
print("desmiti - ",divdimensiju_masivs[1])