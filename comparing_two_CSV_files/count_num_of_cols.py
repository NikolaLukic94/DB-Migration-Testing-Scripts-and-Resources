import csv

with open('FL_insurance_sample.csv', mode='r') as csv_file:
    d_reader = csv.DictReader(csv_file)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames
    headers_count = len(headers)

    print("Num of columns is", headers_count)

with open('FL_insurance_sample.csv', mode='r') as csv_file2:
    d_reader2 = csv.DictReader(csv_file2)

    #get fieldnames from DictReader object and store in list
    headers2 = d_reader2.fieldnames
    headers_count2 = len(headers2)

    print("Num of columns is", headers_count2)

if(headers_count == headers_count2):
    print("\n Everything is matching")
else:
    d1 = {sub[0]: sub for sub in headers_count}
    d2 = {sub[0]: sub for sub in headers_count2}
    print("Difference: ")
    print([d2[k] for k in d2.keys() - d1])
    print([d1[k] for k in d1.keys() - d2])
