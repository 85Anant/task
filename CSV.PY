import csv
with open("STUDENT.CSV",mode="r") as file:
    csv_file = csv.reader(file)
    for lines in csv_file:
        print(lines)