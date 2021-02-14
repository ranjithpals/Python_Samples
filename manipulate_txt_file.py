import os
import csv
from collections import namedtuple
# Get TxT file path
# file_path = os.curdir+'/files/Covid19_india-201004-194827.csv'
file_path = os.path.join(os.getcwd(), 'files\StatewiseTestingDetails-201004-194827.csv')
print(file_path)

record = namedtuple('record', 'sno date state cured deaths confirmed')
# Fieldnames
# fieldnames = ['sno', 'date', 'state', 'cured', 'deaths', 'confirmed']
fieldnames = ['sno', 'date', 'state', 'total_sample', 'negative', 'positive']
# Read the txt file

with open(file_path, 'r') as f:
    # List to add the modified Records
    rec_lst = []
    for n, line in enumerate(csv.DictReader(f, fieldnames=fieldnames)):
        # Read the contents of each line
        sno = line[fieldnames[0]]
        line[fieldnames[0]] = n+1
        date = line[fieldnames[1]]
        state = line[fieldnames[2]]
        cured = line[fieldnames[3]]
        deaths = line[fieldnames[4]]
        confirmed = line[fieldnames[5]]
        # print(sno, date, state)
        # Modify the date format to YYYY-MM-DD
        if date:
            date_part = date.split('/')
            if date_part[2] == '20':
                date_part[2] = '2020'
            date_part[0] = date_part[0].rjust(2, '0')
            date_part[1] = date_part[1].rjust(2, '0')
            mod_date = (date_part[2], date_part[1], date_part[0])
            # Joining with '-' separator
            new_date = '-'.join(mod_date)
        # print(date)
        line['date'] = new_date
        # Add the dictionary to a List
        # print(line)
        rec_lst.append(line)

# new_file_path = os.curdir+'/files/Covid19_india.csv'
new_file_path = os.path.join(os.getcwd(), 'files\StatewiseTestingDetails.csv')

# Write the Output to a csv file using a DictWriter
with open(new_file_path, 'w', newline='') as out_f:
    write = csv.DictWriter(out_f, delimiter=',', fieldnames=fieldnames)
    # for line in rec_lst:
    #    print(line)
    write.writerows(rec_lst)



