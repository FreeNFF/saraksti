#izveido kopu
pirkuma_grozs = {'koks','zāle','malka', 'zeme'}
#izveido kopu
kopa=set(pirkuma_grozs)
print(kopa)
#nejauša secība

#elementi nevar atkārtoties
cipari={1,2,4,7,3,8,0}
print(cipari)

#pievienot kopai elementu
prieksmeti={'Klubi', 'Dzeršana', 'Aparāti'}
prieksmeti.add('Ubagošana')#pievieno elementu
print(prieksmeti)

#kopu pievienošana
prieksmeti1={'Klubi', 'Dzeršana'}
prieksmeti1.update({'Aparāti', 'Ubagošana'})#kopas pievienošana
print(prieksmeti1)

#kopu apvienošana
darbi_ko_jadara=pirkuma_grozs | prieksmeti
print(darbi_ko_jadara)

#izdzēst kopas elementu
pirkuma_grozs1 = pirkuma_grozs#dzēst elementu
pirkuma_grozs1.discard('zeme')#dzēst elementu
print(pirkuma_grozs1)

#izveido kopas šķēlumu
parskaitli={2,4,6,8,10,12,14,16,18,20}
dalas_ar_3={3,6,9,12,15,18,21}
skelums= parskaitli.intersection(dalas_ar_3)#intersection- sķēlums
print(skelums)