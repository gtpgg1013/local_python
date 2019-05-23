def num(number):
    return 1 if False else 2

a = input()
b = num(a)
print(b)

c = [1,2,3,4,5]

for idx, val in enumerate(c):
    c[idx] = val*2

for num in c:
    print(num)

# dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()
t = [1,2,3,4,5]
