saraksts=['gailis', 'cālis', 'vista']
print(saraksts)
print("Saraksta garmus ir ", len(saraksts))
print("--------------------------------------------------")

saraksts.append('pīle')
print(saraksts)
print("--------------------------------------------------")

saraksts.pop(1)
print(saraksts)
print("--------------------------------------------------")

saraksts1 = ['lasis', 'sams', 'siļķe', 'līdaka', 'tuncis']#saraksts
for i in reversed(range(0,5)):#cikls, kas izdrukā sarkstu otrādāk
    print(saraksts1[i])#izdruka
print("--------------------------------------------------")