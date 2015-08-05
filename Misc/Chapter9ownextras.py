counts = dict()
print 'Enter a line of text'
line = raw_input('')

words = line.split()
#update if capital letters
print 'Words:', words

print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1

for key in counts:
    print key, counts[key]

#print list(words) - this will print out the keys only of a dictionary in a list
#print words.values() - this will print out the values from the words dictionary
#print words.items() - this will print out a list of tuples (pair matches)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count


emails = {}
If blah not in email
    append

ccc=dict()
ccc['csev'] = 1
ccc['csev'] = ccc['csev'] + 1

#probably better to do this.  Add emails to list then dictionary
counts = dict()
names = ['a','b','etc.']
for name in names:
    if name not in counts:
        counts[name] = 1
    else
        counts[name] = counts[name] + 1

counts = dict()
names = ['a','b','etc.']
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts