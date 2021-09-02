import random

def liste(*liste):
    cnt = 0
    maks = 0
    for lista in liste:
        cnt += 1
        print(lista)
        for integer in range(len(lista)):
            if maks < lista[integer]:
                maks = lista[integer]
                indx = integer
    print()

    return maks, indx, cnt


lista1 = [23, 1, -100, 23, 44, 567, 10000, 0]
lista2 = [-2, 3, 50000, 89, 1000]
lista3 = [244, 456, 300, 3000, -100, 0, 6, 77, 88, 235000]
rezultat = liste(lista1, lista2, lista3)
print("INDP: ", rezultat[1])
print("MAX: ", rezultat[0])
print("IN ARRAY: ", rezultat[2])

#Napravite algoritam koji može primiti proizvoljni broj 
#nizova / lista cijelih brojeva te će pronaći maksimalnu 
#vrijednost od svih mogućih vrijednosti. Također, algoritam 
#treba dati podatak u kojem nizu je taj maksimum, te koja mu 
#je izvorna indeksna pozicija u tom nizu. Isto tako osigurajte 
#ispis svih promatranih nizova.
