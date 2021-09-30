from itertools import permutations
print('Hello my world')

# ans = permutations([1,2,3,4],3)
# print(list(ans))

wholeInp = input('').split(' ')
S = wholeInp[0]
k = int(wholeInp[1])

ans = permutations(S,k)
ansList = list(ans)
ansList.sort()

for x in ansList:
    listX = list(x)
    mainAns = ''.join(listX)
    print(mainAns)