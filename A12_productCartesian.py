from itertools import product
print('Hello my world')

# ans = product([1,2,3],repeat=2)
# print(list(ans))
#
# ans1 = product([1,2,3],[1,2])
# print(list(ans1))
#
# a = [[1,2,3],[4,5]]
# ans3 = product(*a)
# print(list(ans3))
#
# b = [1,2,3]
# c = [4,5]
# d = [b,c]
# ans4 = product(b,c)
# print(tuple(ans4))

A = input('').split(' ')
B = input('').split(' ')
for i in range(len(A)):
    A[i]= int(A[i])
for i in range(len(B)):
    B[i]= int(B[i])
ans = product(A,B)
ansList = list(ans)
ansList.sort()
for x in ansList:
    print(x),


# print(mainAns)