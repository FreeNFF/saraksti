file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()
print(data)

print("Faila nosaukums: ",file.name)


print("Simbolu skaits: ", len(data))
words = data.split()
count_words= len(words)
print("Vārdu skaits: ", count_words)

file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
lines = file.readlines()
line_count = len(lines)
print("Teksta līnijas kopā:", line_count)

file= open('2teksts.txt', encoding="utf-8")#nolasa teksta datni, utf-8 - valoda
data = file.read()

