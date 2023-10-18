Running Processes CSV Script

#creates imports
import os
import psutil
import csv

# Test psutil to see what it returns using print() and print(type())
     # print(list(psutil.Process().as_dict().keys()))

# Now we have the attributes and we learned that they are in a list.
# Looking up the values to the attribures, the follwoing attributes will give us the information we need to fill in our CSV file.# 'pid', 'name', 'exe', 'cpu_percent','memory_info'# psutil has a function called 'psutil.process_iter'. This function returns an iterator yielding a Process class instance for all running processes on the local machine.# This function also allows us to specify attributes, attrs=[], that we need for our output. We now have enough information to proceeed.
# Get a list of all running processes, defining an empty list
# Since the result of the 'psutil.process_iter' is a list we need to iterate thorugh it using a for loop
# # We need to create a variable to place the irritated data in and append the information to our empty list
# def makeCSV():
process = []
for proc in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):
    process_info = proc.info
    process.append(process_info)


     # Write the process information to a CSV file
with open('processInformation.csv', encoding='UTF8', mode='w', newline='') as csv_file:
    fieldnames = ['pid', 'name', 'exe', 'cpu_percent', 'memory_info']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for process_info in process:
        writer.writerow(process_info)
