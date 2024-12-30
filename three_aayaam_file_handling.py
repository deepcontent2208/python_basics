#---------------------------------------------------------------------
# File Handling - OPEN Statement
#---------------------------------------------------------------------
# ip_file = open('python_orders_file.csv', 'r')
# op_file = open('python_output_file.csv', 'w')
import csv

# while 1:
#     line = ip_file.readline()
#     if line:
#         print(line)
#     else:
#         break

# lines = ip_file.readlines()
# print(type(lines))
#
# for record in lines:
#     print(record.split(',')[0], record.split(',')[3], record.split(',')[5])
#     data = record.split(',')[0] + ',' + record.split(',')[3] + ',' + record.split(',')[5]+'\n'
#     op_file.write(data)
#
# ip_file.close()
# op_file.close()


#---------------------------------------------------------------------
# File Handling - WITH Statement
#---------------------------------------------------------------------
# with open('python_orders_file.csv','r') as input_file:
#     lines = input_file.readlines()
#     with open('python_orders_outfile.csv', 'w') as output_file:
#         for record in lines:
#             data=record
#             output_file.write(data)

#---------------------------------------------------------------------
# File Handling - CSV module
#---------------------------------------------------------------------
# with open('python_orders_file.csv','r') as input_file:
    # reader = csv.reader(input_file, delimiter=',',quotechar='"')
    # dict_reader = csv.DictReader(input_file, delimiter=',',quotechar='"')

    # for record in dict_reader:
    #     print(record)

#---------------------------------------------------------------------
# File Handling - JSON module
#---------------------------------------------------------------------
# import json
# with open('python_orders_file.json', 'r') as json_ip_file:
#     json_records = json_ip_file.readlines()
#     print(type(json_records))
#     # json_records = json.loads(json_records)
#     # print(type(json_records))
#     # for i in json_records:
#     #     i = json.loads(i)
#     i = json_records[0]
#     i = json.loads(i)
#     for records in i:
#         print(records)
