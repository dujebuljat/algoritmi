from pckg_zad_4 import checking_input_sentence


user_input = input("Enter something as a  simple sentence...\n")
lst = user_input.strip().split()
print(lst)
finale = checking_input_sentence(lst)
print("<<<<<<<<<<<<<<<<<< Finalno rješenje >>>>>>>>>>>>>>>>>>>>")
print(finale)
join_all = " ".join(finale)
print(join_all)
