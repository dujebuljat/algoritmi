import csv


def read_data_from_csv(file_path):
    all_data = []
    with open(file_path, newline="") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        print(data)
        for row in data:
            print(row)
            all_data.append(row)
    return all_data


def create_map(data):
    map = {}
    for row in data:
        map[row[0]] = int(row[1].strip())
    return map


def submap_greater_than(map, threshold=350):
    grt = {}
    for key in map.keys():
        if map[key] > threshold:
            grt[key] = map[key]
    return grt


def read_data_from_file(file_path):
    content = []
    with open(file_path, "r") as file:
        for line in file:
            res = line.strip("\n").split(", ")
            content.append(res)
    return content




