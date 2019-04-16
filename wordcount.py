print('Enter the line of Text')

line = 'the clown ran after the car and the car ran into the tent \
and the tent fell down on the clown and the car '

dddd = dict()
for word in line.split() :
    dddd[word] = dddd.get(word, 0) + 1

print(dddd)

for key in dddd :
    print('key :', key,', count :', dddd[key])

print(list(dddd))
print(dddd.keys())
print(dddd.values())
print(dddd.items())

for aaa, bbb in dddd.items() :
    print(aaa, bbb)