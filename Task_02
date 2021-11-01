"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
dictionary ={}

# compute total call duration for each number and store it in dictionary
for x in calls:
    if x[0] not in dictionary:
        dictionary[x[0]] = int(x[3])
    else:
        dictionary[x[0]] += int(x[3])
    if x[1] not in dictionary:
        dictionary[x[1]] = int(x[3])
    else:
        dictionary[x[1]] += int(x[3])

maxkey = (max(dictionary, key=dictionary.get))
maxval = dictionary.get(maxkey)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxkey, maxval))
