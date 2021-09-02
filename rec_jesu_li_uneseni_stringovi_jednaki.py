def same_strings(string1, string2):
    lista1 = list(string1)
    lista2 = list(string2)
    if lista1 == lista2:
        print("stringovi su jednaki")
    else:
        print("stringovi nisu jednaki")


def stepByStep(string1, string2):
    lista1 = list(string1)
    lista2 = list(string2)
    if len(lista1) != len(lista2):
        print("nisu")
    else:
        for i in range(len(lista1)):
            if lista1[i] != lista2[i]:
                print("nisu")
                break
            else:
                if i == len(lista1) - 1 and lista1[i] == lista2[i]:
                    print("jesu")

int = "prvi string"
int2 = "drugi string"
int3 = "drugi string"
same_strings(int, int2)
same_strings(int2, int3)
stepByStep(int, int2)
stepByStep(int2, int3)
