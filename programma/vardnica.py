from turtle import update


tulkojums = {'Suns':'Hund', 'Kaķis':'Katze', 'Papagailis':'Papagei'}#vārdnīca
print(tulkojums['Suns'])#izdrukā tulkojumu
print("--------------------------------------------------")
tulkojums['Zaķis']='Hase'#pievieno vārdnīcai
print(tulkojums)
print("--------------------------------------------------")

#saliktā vārdnīca
sekmes={'Janka':{'sem1':4, 'sem2':2}, 'Dimitrijs':{'sem1':5, 'sem2':6}, 'Zigis':{'sem1':7,'sem2':8}}
janka=sekmes['Janka']
print(janka)
print("--------------------------------------------------")
janka1 = janka['sem1']
print("Pirmajā semstrī ieguva: ",janka1)
print("--------------------------------------------------")
janka2 = janka['sem2']
print("Otrajā semsetrī ieguva: ",janka2)
print("--------------------------------------------------")
print('Skolēnu skaits: ', len(sekmes))#nosaka vārdnīcas garumu

#vārdnīcas papildīšana
gramata={'Nosaukums':'The Hunger Games', 'Autors':'Suzanne Collins'}
print(gramata)
print("--------------------------------------------------")
autjaunosana={'Gads':2008, 'Žanrs':'Romāns', 'Izdevniecība':'Scholastic Press'}
gramata.update(autjaunosana)
print(gramata)
print("--------------------------------------------------")

atzimes_skaidrojums={10:'izcili', 9:'teicami', 8:'ļoti labi', 7:'labi', 6:'gandrīz labi', 5:'viduvēji', 4:'gandrīz vāji', 3:'vāji', 2:'ļoti vāji', 1:'ļoti, ļoti vāji', 'nv':'normāls vērtējums'}

while True:
    try:
        ievade= int(input("Ievadiet skaitli no 1-10: "))
        if 1<= ievade <=10:
            break
        else:
            print('Ievadītais skaitlis nav atbilstošs nosacījumiem.')
    except ValueError:
        print("Ievadītajam skaitlim jābut veselam skaitlim.")

skaidrojums = atzimes_skaidrojums[ievade]
print("Vārdiskais skaidrojums atzīmei ir: ",skaidrojums) 