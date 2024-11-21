steks = [1,50, 99]#izveido steku
print(steks)
steks.append('(')
steks.append(')')
print(steks)
print(steks.pop())
print(steks.pop())
print(steks)
print('-------------------------------------------------------')


#izveido un izdēš elelemntu
import queue#biblotēkas pievienošana
steks=queue.LifoQueue()
steks.put('pirmais')
steks.put('otrais')
print(steks.queue)
print('izņemts',steks.get())
print('izņemts',steks.get())
print('-------------------------------------------------------')

#atgriezt steka elementu skaitu
steks=queue.LifoQueue()
steks.put('pirmais')
steks.put('otrais')
steks.put('trešais')
print(steks.queue)
print(steks.qsize())#elementu skaits
print('-------------------------------------------------------')
