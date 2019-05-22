counts = dict()
names = ['cesv','cews','cesv','cesv','sff','cews']
for name in names :
    # if name not in counts :
    #     counts[name] = 1
    # else :
    #     counts[name] = counts[name] + 1
    counts[name] = counts.get(name, 0) + 1
print(counts)