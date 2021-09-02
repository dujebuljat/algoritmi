def rec(lista, index):
    if index < 0:
        return lista
    else:
        if lista[index] % 2 != 0:
            lista.remove(lista[index])
            return rec(lista, index - 1)
        else:
            return rec(lista, index - 1)

lista = [1,2,3,4,5,6,7,8,9]
print(rec(lista,len(lista)-1))
