def rec_sort(lista, element, cnt):

    if element == len(lista):
        return lista

    elif cnt == len(lista):
        return rec_sort(lista, element+1, 0)

    elif len(lista[element]) > len(lista[cnt]):
        temp = lista[element]
        lista[element] = lista[cnt]
        lista[cnt] = temp
        return rec_sort(lista, element, cnt)

    else:
        return rec_sort(lista, element, cnt+1)

lista = ["samo", "je", "ovo je dobro", "i", "neki-mali", "primjer", "opet"]
print(rec_sort(lista, 0, 0))

#Vaš zadatak je da realizirate rekurzivni algoritam sortiranja nekog niza stringova 
#prema njihovoj duljini. Za ovaj slučaj samo osigurajte sortiranje od najduljeg prema 
#najkraćem, a u pseudokodu navedite rješenje koje u sebi uključuje obje mogućnosti (od najkraćeg prema duljem i obrnuto).
