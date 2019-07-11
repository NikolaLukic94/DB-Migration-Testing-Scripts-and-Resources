import csv

with open('FL_insurance_sample.csv', mode='r') as csv_file:
    d_reader = csv.DictReader(csv_file)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames
    headers_count = len(headers)

    print("Num of columns is",headers_count)