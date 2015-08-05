d = dict()
d['csev'] = 2
d['cwen'] = 4
print d

for (k,v) in d.items():
    print k,v

tups = d.items()
print tups


for (k,v) in sorted(d.items()):
    print k,v

c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list()
print c
for k, v in c.items():
    tmp.append( (v,k) )

print tmp

tmp.sort(reverse=True)
print tmp