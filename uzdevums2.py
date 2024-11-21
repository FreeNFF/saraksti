naturali_skaitli = list(range(1,11))
print(naturali_skaitli)
print("--------------------------------------------------")

kavdrats = [x**3 for x in naturali_skaitli]
print(kavdrats)
print("--------------------------------------------------")

apvienots = naturali_skaitli + kavdrats
print(apvienots)
print("--------------------------------------------------")

mazakais = min(naturali_skaitli)
lielakais = max(naturali_skaitli)

print('Mazākais skaitlis sarakstā: ',mazakais)
print("Lielākais skaitlis no saraksta: ",lielakais)
print("--------------------------------------------------")

summa = sum(naturali_skaitli)
print("Saraksta summa: ", summa)
print("--------------------------------------------------")

saraksts1 = ['lasis', 'sams', 'siļķe', 'līdaka', 'tuncis']
print(saraksts1)
print("--------------------------------------------------")

garakais = max(saraksts1, key=len)#key uir arguments lai salīdzinātu elementu garumus
print("Garākais elements sarakstā: ",garakais)
print("--------------------------------------------------")

isakais = min(saraksts1, key=len)#key uir arguments lai salīdzinātu elementu garumus
print("Garākais elements sarakstā: ",isakais)
print("--------------------------------------------------")
