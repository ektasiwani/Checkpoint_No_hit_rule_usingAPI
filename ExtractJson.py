import json
import csv
import os

print("How many files you have:")
total_num = int(input())

for k in range(total_num):

    with open('/opt/tmp/jsonfile'+str(k+1)+'.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    rulebase = data['rulebase'][0]['rulebase']
    data_info = []

    for i in range(len(rulebase)):
        data_part = []
        source_array = []
        des_array = []
        ser_array = []
        action_array = []

        name = rulebase[i]['name']
        data_part.append(name)
        number = rulebase[i]['rule-number']
        data_part.append(number)
        source = rulebase[i]['source']

        for j in range(len(source)):
            source_array.append(rulebase[i]['source'][j]['name'])
        data_part.append(source_array)
        for j in range(len(rulebase[i]['destination'])):
            des_array.append(rulebase[i]['destination'][j]['name'])
        data_part.append(des_array)
        for j in range(len(rulebase[i]['service'])):
            ser_array.append(rulebase[i]['service'][j]['name'])
        data_part.append(ser_array)
        data_part.append(rulebase[i]['action']['name'])
        data_info.append(data_part)

    print(data_info)

    if os.path.isfile('outputfile.csv'):
        with open('outputfile.csv', 'a') as outcsv:
            #configure writer to write standard csv file
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            for item in data_info:
                #Write item to outcsv
                writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])

    else:
        with open('outputfile.csv', 'w+') as outcsv:
            writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['name', 'number', 'source', 'destination', 'service', 'action'])
            for item in data_info:
                #Write item to outcsv
                writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])
