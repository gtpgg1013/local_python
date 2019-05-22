d = {'a':10, 'b':1, 'c':3}
a = d.items()
print(sorted(a,reverse=True))

print(sorted([(v,k) for (k,v) in a]))

lst = []
for key,val in d.items():
    newtupp = (val,key)
    lst.append(newtupp)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)
        