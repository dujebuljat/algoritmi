def rec_extract(lista, duljina, cnt):
    if cnt == len(lista):
        return lista
    elif len(lista[cnt]) != duljina:
        lista.remove(lista[cnt])
        return rec_extract(lista, duljina, cnt)
    else:
        return rec_extract(lista, duljina, cnt + 1)

lista = ['ovo', 'je', 'neki', 'string', 'ima', 'elemenata', 'više', 'od', 'tri']
print(lista)
print(rec_extract(lista, 3, 0))

#Rekurzivnim algoritmom iz niza sa proizvoljnim brojem stringova izvršite ekstrakciju 
#samo stringova željene duljine (npr. 3). Ispišite ulazni niz i dobiveni niz rekurzivnim 
#algoritmom. Napišite pseudokod algoritma koji bi vršio isti zadatak, a koji ne koristi princip rekurzije.
