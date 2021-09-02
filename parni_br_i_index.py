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
