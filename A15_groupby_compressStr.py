from itertools import groupby
print('Hello my world')

# S = input('')
# listS = list(S)
# print(listS)
#
# for key, group in groupby(listS):
#     print((len(list(group)), int(key)))

creatures = [('Animal','Dog'),
             ('Animal','Cat'),
             ('plant','rose'),
             ('Animal','Tiger')]

for key,group in groupby(creatures,lambda x:x[0]):
    for values in group:
        value = values[1]
    print((key,value))