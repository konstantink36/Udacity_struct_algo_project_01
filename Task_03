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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A

prefix = set()

for x in calls:
#if caller is from bangalore and called number is fixed line, put area code of called number in list
    if x[0].startswith('(080)') and x[1].startswith('(0'):
        prefix.add((x[1].split(')')[0])[1:])
#if caller is from bangalore and called number is mobile number, put area code of called number in list
    elif x[0].startswith('(080)') and (x[1].startswith('7') or x[1].startswith('8') or x[1].startswith('9')):
        prefix.add(x[1][:4])
#if caller is from bangalore and called number is telemarketer, put area code of called number in list
    elif x[0].startswith('(080)') and x[1].startswith('140'):
        prefix.add(x[1][:3])

prefix_list = list(prefix)
prefix_list.sort()

print("The numbers called by people in Bangalore have codes:")
for x in prefix_list:
    print(x)

#Part B

# all calls from bangalore fixed line
allcalls = list()
for x in calls:
    if x[0].startswith('(080)'):
        allcalls.append(x[1])

# all calls from bangalore fixed line to bangalore fixed line
bcalls = list()
for x in calls:
    if x[0].startswith('(080)') and x[1].startswith('(080)'):
        bcalls.append(x[1])

perc = (((len(bcalls))/(len(allcalls)))*100)

print( format(perc, '.2f'), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
