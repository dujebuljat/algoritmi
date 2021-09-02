from pckg_zad_5 import read_data_from_csv, create_map, submap_greater_than, read_data_from_file

content = read_data_from_file("scores.csv")
print(content)

# data = read_data_from_csv("scores.csv")
# print(data)
# mapa = create_map(data)
# print(mapa)
# grt = submap_greater_than(mapa)
# print("-------------------------------------------------------------------")
# print(grt)
# print(dict(sorted(grt.items(), key=lambda item: item[1], reverse=True)))
