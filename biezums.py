with open("Masinmacisanas.txt",'r', encoding='utf-8') as file:#nolasa teksta datni, utf-8 - valoda
    data= file.read()
print(data)

lines = data.split()
print(lines)

