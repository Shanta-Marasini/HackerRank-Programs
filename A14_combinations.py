from itertools import combinations,combinations_with_replacement
print('Hello my world')

# ans = combinations([1,2,3,4],3)
# print(list(ans))

# wholeInp = input('').split(' ')
# S = wholeInp[0]
# S = list(S)
# S.sort()
# k = int(wholeInp[1])
#
# for i in range(1,k+1):
#     ans = combinations(S,i)
#     ansList = list(ans)
#
#
#     for x in ansList:
#         listX = list(x)
#         mainAns = ''.join(listX)
#         print(mainAns)

wholeInp = input('').split(' ')
S = wholeInp[0]
S = list(S)
S.sort()
k = int(wholeInp[1])


ans = combinations_with_replacement(S,k)
ansList = list(ans)


for x in ansList:
    listX = list(x)
    mainAns = ''.join(listX)
    print(mainAns)