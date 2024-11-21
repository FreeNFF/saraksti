with open("Masinmacisanas.txt",'r', encoding='utf-8') as file:#nolasa teksta datni, utf-8 - valoda
    data= file.read()
print(data)

print("------------------------------------------------")

word_count={}
lines = data.split()
print(lines)
print("------------------------------------------------")

for word in lines:
    if len(word)>=4:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count = 1
print(word_count)