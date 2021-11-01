"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

#list of all phone numbers sending/receiving texts and sending/receiving calls:
numbers = [x[0] for x in texts] + [x[1] for x in texts] + [x[0] for x in calls] + [x[1] for x in calls]

#list of unique numbers:
numbers_unique= set(numbers)

print("There are", len(numbers_unique) , "different telephone numbers in the records.")
