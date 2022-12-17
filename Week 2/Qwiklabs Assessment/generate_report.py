#generate_report.py file begins with a line containing the #! character combination, which is commonly called hash bang or shebang, and continues with the path to
#the interpreter. If the kernel finds that the first two bytes are #! then it uses the rest of the line as an interpreter and passes the file as an argument.
#The goal of the script is to read the CSV file and generate a report with the total number of people in each department.

#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  with open(csv_file_location) as file:
    
    #passing a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible.
    #Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer 
    #separately, we group them together conveniently into a dialect object. 
    #Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    #DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into
    #a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as
    #the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.
    employee_file = csv.DictReader(file, dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
      employee_list.append(data)

    return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  
  #remove the redundant department and return a dictionary with the count of employees in each department
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
  f.close()

employee_list = read_employees('/home/student-01-bd68cae36195/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student-01-bd68cae36195/data/report.txt')
