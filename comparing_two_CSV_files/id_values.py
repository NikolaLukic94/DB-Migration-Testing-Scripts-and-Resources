import csv

with open('FL_insurance_sample.csv', mode='r') as csv_file1:
	reader1 = csv.DictReader(csv_file1)
	data1 = [row for row in reader1]
	column_data1 = []
	column_name1 = "policyID"
	for row in data1:
		column_data1.append(row[column_name1])

	column_data1 = sorted(column_data1)


with open('FL_insurance_sample.csv', mode='r') as csv_file2:
	reader2 = csv.DictReader(csv_file2)
	data2 = [row for row in reader2]
	column_data2 = []
	column_name2 = "policyID"
	for row in data2:
		column_data2.append(row[column_name2])

	column_data2 = sorted(column_data2)


if(column_data1 == column_data2):
    print("\n Everything is matching")
else:
    d1 = {sub[0]: sub for sub in column_data1}
    d2 = {sub[0]: sub for sub in column_data2}
    print("Difference: ")
    print([d2[k] for k in d2.keys() - d1])
    print([d1[k] for k in d1.keys() - d2])
