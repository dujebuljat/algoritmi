def stringFunction(string):
    listaString = list(string)
    originals = []
    duplicates = []
    for char in listaString:
        if char not in originals and char != " ":
            originals.append(char)
        else:
            duplicates.append(char)

    for char in originals:
        num = 1
        for duplicatesChar in duplicates:
            if duplicatesChar == char:
                num += 1
        print("itr-" + char + ": " + str(num))
    return True

inpt = input("Input: ")
stringFunction(inpt)
