print('Hello my world')

string = input()
string = string.upper()

kvScore = 0
scScore = 0
strLength = len(string)

for i in range(strLength):
    if string[i] in 'AEIOU':
        kvScore += (strLength - i)
    else:
        scScore += (strLength - i)

if kvScore > scScore:
    print('{} {}'.format('Kevin',kvScore))
elif scScore > kvScore:
    print('{} {}'.format('Stuart', scScore))
else:
    print('Draw')




