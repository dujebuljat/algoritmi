def get_all_of_lenth_n(lst, length=3):
    sub_lst = []
    for element in lst:
        if len(element) == length:
            sub_lst.append(element)
    if len(sub_lst) == 0:
        return "Nema elemenata te duljine...."
    else:
        return sub_lst
