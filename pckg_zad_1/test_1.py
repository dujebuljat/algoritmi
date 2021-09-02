from pckg_zad_1 import get_all_of_lenth_n

unos = input("Unesite neku rečenicu...\n")
print(unos)

lista = unos.strip().split()
print(lista)
rs = get_all_of_lenth_n(lista)
print("Rezultat:")
print(rs)
print("Sortirani ulaz:")
print(sorted(lista, reverse=True))

