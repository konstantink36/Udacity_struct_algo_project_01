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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# list of all numbers that receive calls, + numbers that send texts, + numbers that receive texts
numbers = [x[1] for x in calls] + [x[0] for x in texts] + [x[1] for x in texts]
numbers_set = set(numbers)

tele = set()

# put number in list of telemarketers, if it makes calls but does not send texts,receive texts or receive calls.
for x in calls:
    if x[0] not in numbers_set:
        tele.add(x[0])

tele_list = list(tele)
tele_list.sort()

print("These numbers could be telemarketers: ")
for x in tele_list:
    print(x)
