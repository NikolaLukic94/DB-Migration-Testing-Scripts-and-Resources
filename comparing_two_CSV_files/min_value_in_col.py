import csv

with open('FL_insurance_sample.csv', mode='r') as csv_file1:
    reader1 = csv.reader(csv_file1)
    next(reader1)
    answer1 = min(int(column[0].replace(',', '')) for column in reader1)#specify col #, starting with 0
    print(answer1)


with open('FL_insurance_sample.csv', mode='r') as csv_file2:
    reader2 = csv.reader(csv_file2)
    next(reader2)
    answer2 = min(int(column[0].replace(',', '')) for column in reader2)#specify col #, starting with 0
    print(answer2)

if(answer1 == answer2):
    print("\n Everything is matching")
else:
    print("Not matching")