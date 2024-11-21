file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()
print(data)
print("--------------------------------------------------")

print("Faila nosaukums: ",file.name)
print("--------------------------------------------------")


print("Simbolu skaits: ", len(data))
words = data.split()
count_words= len(words)
print("Vārdu skaits: ", count_words)


file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
lines = file.readlines()
line_count = len(lines)
print("Teksta līnijas kopā:", line_count)
print("--------------------------------------------------")

file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read(10)
print("Pirmie desmit simboli: ",data)
print("--------------------------------------------------")

file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()
print("Pirmais simbols: ",data[0])
print("--------------------------------------------------")

file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()

print('Pēdējais simbols:',data[-1])
print("--------------------------------------------------")

def Pirma():
    file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
    line = file.readlines()
    print('Pirmā rindiņa: ', line[0])
Pirma()


