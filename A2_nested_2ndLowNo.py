print('Hello Shiva baba my world')

#2nd largest element in the lsit

mainList = [['Tina', 21],
            ['Harry', 20],
            ['Berry', 20],
            ['Harsh', 19],
            ['Akriti', 19]]

mainList.sort(key = lambda x: x[1],reverse = True)
print(mainList)
n = len(mainList)
result = []
for i in range(n-1,0,-1):
    if mainList[i][1] != mainList[i - 1][1]:
        result.append(mainList[i - 1][0])
        for j in range(i-1, 0, -1):
            if mainList[j][1] == mainList[j-1][1]:
                result.append(mainList[j - 1][0])
            else:
                break
        break

result.sort()
print('\n'.join(result))
