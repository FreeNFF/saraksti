from asyncio import ensure_future
import json

dati = {
    "persona":{
        "vards": "Arturiks",
        "vecums": 48,
        "pilseta": "Daugavpils",
        "hobijs": ["gamble","dzeršana"]

    },
    "uznemums":{
        "nosaukums": "Fenikss",
        "amats": "apsargs",
        "darbinieki": 15
    }
}

#izveidojam JSON datni, uzmantojot json.dumps()
json_datne = json.dumps(dati, ensure_ascii=False, indent=2)
#dati izmantoti tikai ASVII simboli, var saturēt tikai ASCII simbolus
print(json_datne)#izprintējam json datnis

with open("dati.json", "w", encoding="utf-8") as file:
    file.write(json_datne)