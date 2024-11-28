alfabets = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]
vardi = {burt: None for burt in alfabets}#izveido sarakstu, kur atslēgas elemnts ir pirmais burts

def valid_input(word):
    return word[0].isupper() and word.isalpha()#pārbauda vai ir alfabētā un vai sākās ar uppercase

def add(word):
    #pārbauda vai ir pareizi ievadīts
    if not valid_input(word):
        print("Nederīga ievade! Lūdzu ievadiet vārdu vēlreiz.")
        return
