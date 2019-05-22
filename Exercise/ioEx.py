fhand = open('test.txt')
print(fhand)

for line in fhand:
    if(line.startswith('So')):
        print(line.rstrip())

lines = open('test.txt')

# string1 = lines.read()
# print(string1)
# print(len(string1))