counts = dict()
names = ['Aaron', 'Ray', 'Paddy', 'Eric', 'Arleen', 'Aaron']
for name in names:
    counts[name] = counts.get(name,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print counts, bigword, bigcount