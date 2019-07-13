import csv

with open('FL_insurance_sample.csv', mode='r') as csv_file:
    reader = csv.reader(csv_file)
    i = next(reader)
    i = sorted(i)
    print(i)


with open('FL_insurance_sample.csv', mode='r') as csv_second_file:
    second_reader = csv.reader(csv_second_file)
    s = next(second_reader)
    s = sorted(s)
    print(s)

if(i == s):
    print("\n Everything is matching")
else:
    d1 = {sub[0]: sub for sub in i}
    d2 = {sub[0]: sub for sub in s}
    print("The ones in first table only: ")
    print([d2[k] for k in d2.keys() - d1])
    print("The ones in 2nd table only: ")
    print([d1[k] for k in d1.keys() - d2])

