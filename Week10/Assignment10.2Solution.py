# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
#  second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that
# the autograder does not have support for the sorted() function.
# Desired output listed on Assignment10.2.py
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()
times = list()

for line in fh:
    if line.startswith('From '): # Notice the space after the from.  Will get more results if you have this.
        times.append(line.rstrip().split()[5])
        #print words
#print times

times = [c.split(":",1)[0] for c in times]

#print times

for time in times:
    #print time
    counts[time] = counts.get(time,0) + 1
#print counts

for (k,v) in sorted(counts.items()):
    print k,v