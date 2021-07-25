import csv
import os

def getDataLines(data, fields):
    data_lines = []
    for field in fields:
        data_lines.append(data[field])
    return data_lines


def read_csv_data(fileName):
    data = csv.reader(open(os.path.join(os.getcwd(), fileName), mode='r', encoding="utf8"))
    fields = data.__next__()
    fields.append('repeated')
    data_lines = []
    for row in data:
        items = dict(zip(fields, row))
        data_lines.append(items)
    return data_lines, fields

fileName = input("Enter CSV file name: ")
fieldOfTable = input("Enter field table: ")

csv_reader, fields = read_csv_data(fileName)

data_file = open('repeatedValues.csv', 'w')
csv_writer = csv.writer(data_file)
csv_writer.writerow(fields)
 
for row in csv_reader:
    cont = 0
    for insideRow in csv_reader:
        if row[fieldOfTable] == insideRow[fieldOfTable]:
            cont = cont + 1
            row['repeated'] = cont 
    if cont > 1: 
            csv_writer.writerow(getDataLines(row, fields))       

data_file.close()