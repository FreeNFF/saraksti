import json

with open("3Jason.json", 'r', encoding="utf-8-sig") as file:
    data=json.load(file)
    print(data)
print("Datnes nosaukums ir: ", file.name)