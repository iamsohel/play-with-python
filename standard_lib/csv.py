import csv

with open("data.csv", "w") as file:
    writter = csv.writer(file)
    writter.writerow(['t_id', 'p_id', 'price'])
    writter.writerow(['1', '2', '3'])
    writter.writerow(['2', '2', '3'])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
