print("hello my world")

s = input('')      # raw_input for hacker rank
listt = s.split(' ')
row = int(listt[0])
column = int(listt[1])

identical_lines = (row - 1) // 2
das_len = (column - 3) // 2
dot_len = 3
d = '-'
s ='.|.'

print('1st way')

for i in range(identical_lines):
    print(d*das_len + (s * (i*2+1)) + d*das_len)
    das_len -= 3
    dot_len += 6

print('WELCOME'.center(column, d))

das_len +=3
dot_len -=6
for i in range(identical_lines,0,-1):
    print(d*das_len + (s * (i *2-1)) + d*das_len)
    das_len += 3
    dot_len -= 6

print('2nd way')

for i in range(1,row,2):
    print((s*i).center(column,'-'))

print('WELCOME'.center(column,'-'))

for i in range(row-2,-1,-2):
    print((s * i).center(column, '-'))

print('3rd way')

for i in range(0,row//2):
    print((s*(i*2+1)).center(column,'-'))

print('WELCOME'.center(column,'-'))

row2 = row//2
for i in range(row//2,0,-1):
    print((s * (i*2-1)).center(column, '-'))
