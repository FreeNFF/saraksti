alfabets = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]
vardi = {burt: None for burt in alfabets}#izveido sarakstu, kur atslēgas elemnts ir pirmais burts

def valid_input(word):
    return word[0].isupper() and word.isalpha()#pārbauda vai ir alfabētā un vai sākās ar uppercase

def add(word):
    #pārbauda vai ir pareizi ievadīts
    if not valid_input(word):
        print("Nederīga ievade!")
        return
    
    primais_burts= word[0].upper()

    if primais_burts in vardi:#ja nav tad pievieno
        if vardi[primais_burts] is None:
            vardi[primais_burts]=word
            print(f"Pievienoju vārdu {word} vietā {primais_burts}.")
        else:#ja ir aizņemts tad apmaina
            print(f"Vārds vietā {primais_burts} jau ir aizņemts. Apmainu vārdu {vardi[primais_burts]} ar {word}.")
            vardi[primais_burts]=word
    else:
        print("Nepareizs pirmais burts! Lūdzu ievadiet vēlreiz.")

def izvada_vardus():#izdrukā vārdus
    print("\nAlfabēta vārdi:")
    for burt, vards in vardi.items():
        if vards:
            print(f"{burt}: {vards}")
        else:
            print(f"{burt}: Nav vārda")

def all_done():#pārbauda vai viss ir aizpildīts
    return  all(vards is not None for vards in vardi.values())

def galvena():
    vārdi=['Ainaži', 'Saulkrasti', 'Dobele', 'Sigulda', 'Tukums', 'Liepāja', 'Talsi', 'Ludza', 'Cēsis', 'Gulbene', 'Ventspils', 'Vecumnieki', 'Engure', 'Ērgļi', 'Staicele', 'Kuldīga', 'Aizpute', 'Krāslava', 'Madona', 'Jūrmala', 'Rīga']

    jaut= "nekas"
    while jaut != "Stop":
        jaut = input("Ja vēlaties beigt tad ievadiet vārdu 'Stop', ja vēlaties turpināt ievadiet 'Start': ")
        if jaut== "Start":
            vardss= input("Ievadiet nosaukumu: ")
            if not valid_input(vardss):
                print("Nederīga ievade!")
            else:
                vārdi.append(vardss)

        else:
            pass

    for vards in vārdi:
        add(vards)
        izvada_vardus()

        if all_done():
            print("\n Alfabēts pilnībā aizpildīts.")
            break

galvena()