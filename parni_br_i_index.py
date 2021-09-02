import random

def parnibr():
    listabrojeva = []
    finalnalista = []


    N = int(input("Unesite željenu količinu brojeva: "))
    for i in range(N):
        listabrojeva.append(random.randint(1, 100))

    for j in listabrojeva:
        if j % 2 == 0:
            indeks = listabrojeva.index(j)
            finalnalista.append((j, indeks))
        elif j % 2 != 0:
            continue
    print(listabrojeva)
    #print(finalnalista)
    return finalnalista


rezultat = parnibr()
print(rezultat)

#Napravite algoritam koji u nizu cijelih brojeva 
#pronalazi sve parne brojeve i njihove indeksne 
#pozicije. U slučaju da nema parnih brojeva 
#algoritam daje praznu strukturu podataka i 
#pripadnu poruku. Dodatni zahtjev je da napravite 
#funkciju ili metodu (ovisno rješavate li u Pythonu 
#ili JAVI) koja slučajno generira polazni niz željene 
#duljine n. Pored konkretne implementacije trebate napisati 
#pseudokod vašeg rješenja. Testiranje izvršite za niz duljine 8 elemenata.
