from random import randint

def sumEven(lista, index):
    if index < 0:
        return 0
    else:
        if lista[index] % 2 == 0:
            return lista[index] + sumEven(lista, index - 1)
        else:
            return sumEven(lista, index - 1)


def genList(size):
    lista = []
    for i in range(size):
        lista.append(randint(0, size))
    return lista


lista = genList(10)
print(lista)
index = len(lista) - 1
print(sumEven(lista, index))
