def sum_all_unique_elements(lst):
    unq = set(lst)
    print("Sorted unique elements: ")
    print(sorted(unq))
    sums = 0
    if len(unq) == 0:
        print("The input array/list is empty!")
    else:
        for element in unq:
            sums += element
        print("Sum is: ", sums)



