"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
import csv


def max_delta(file: str):
    with open(file, 'rt') as inf:
        data = [(float(row['ChangePerc']), row['Year']) for row in csv.DictReader(inf)]
        data.sort(reverse=True)
        list_1 = list(data[0])
        return(list_1[1])


print(max_delta("world_population.csv"))
