print("___________________§§_________________________\n_____________§____§§§§________________________\n__§___§__________§§§§§§_________________§_____\n_________§§_____§§§§§§§§______________________\n_______________§§§§§§§§§§______§______________\n§___§_________§§§§§§§§§§§§_________§__________\n_________________§§§§§§_______________________\n__________§_____§§§§§§§§______________________\n_______________§§§§§§§§§§_____§_______________\n______________§§§§§§§§§§§§____________________\n_§_____§_____§§§§§§§§§§§§§§§__________________\n___________§§§§§§§§§§§§§§§§§§§______§____§____\n________§§§§§§§§§§§§§§§§§§§§§§§§______________\n__§___________§§§§§§§§§§§§____________________\n____________§§§§§§§§§§§§§§§§_____§____________\n_________§§§§§§§§§§§§§§§§§§§§§§_________§_____\n______§§§§§§§§§§§§§§§§§§§§§§§§§§§_____________\n___§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§______§___\n__§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§_______\n§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§_____\n________________§§§§§§§§______________________\n___§______§_____§§§§§§§§______________________")
print()
print("-----------------------------------------------------------------------------------------------")
print()
def egle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")

n =9
egle(n)