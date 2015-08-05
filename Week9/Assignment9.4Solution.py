# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
#  messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
#  mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
#  loop to find the most prolific committer.
# Desired Output : cwen@iupui.edu 5
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()
words = list()
for line in fh:
    if line.startswith('From '): # Notice the space after the from.  Will get more results if you have this.
        words.append(line.rstrip().split()[1])
        #print words
#print words
for word in words:
    #print word
    counts[word] = counts.get(word,0) + 1
#print counts

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount