print('hello Shiva baba my world')

str = 'AABCAAADA'
k = 3

n = len(str)
no = n//k
t = ['' for x in range(no)]
index = 0
for i in range(n):
    if i == (index + 1) * k:
        index += 1
    t[index] += str[i]


print(t)

for x in t:
    u = ''
    for y in x:
        if y not in u:
            u += y
    print(u)