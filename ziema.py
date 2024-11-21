
file= open('Ziema.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
print(file.read())
print('\n')
print('-------------------------------------------------------------')
file= open('Ziema.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
print("Pirmie 12 simboli: ",file.read(12))
print('-------------------------------------------------------------')
file= open('Ziema.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
letter = file.read()
print("Pēdējais simbols: ",letter[-1])
print('-------------------------------------------------------------')

words = 0#nosaka vārdu skaitu/ vienkārši pašam sākumam
with open('Ziema.txt', encoding="utf-8") as file:#atver failu

    data = file.read()#nolasa failu
    lines = data.split()#sadala failu vārdos
    words += len(lines)#Nosaka vārdu skaitu, izmantojot ciklu

print("Kopā vārdi:",words)#izdrukā vārdu skaitu
print('-------------------------------------------------------------')

file= open('Ziema.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
lines = file.readlines()#ar funkcija readlines sadala rindiņās
print("Teksts par līnijām:", lines)#izdrukā rindiņas daudzumu
print('-------------------------------------------------------------')
line_count = len(lines)#nolasa rindiņu skaitu
print("Teksta līnijas kopā:", line_count)#izdrukā rindiņas daudzumu
print('-------------------------------------------------------------')


with open('Ziema.txt', encoding="utf-8") as file:#atver failu/ nolasa failu

    data = file.read()#Nolasa failu
    lines1 = data.split()
    lines = data.split()[-1]#Sagrupē visu pa vārdiem, paņem pēdējo vārdu

print("Teksts pa vārdiem: ",lines1)
print('-------------------------------------------------------------')
print("Pēdējais vārds: ",lines)#izdrukā pēdējo vārdu
print('-------------------------------------------------------------')
