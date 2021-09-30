from collections import Counter
print('Hello my World')

# listt = [1,2,3,5,4,6,7,5,3,2]
# listtDict = Counter(listt)
# print(listtDict)
# print(listtDict.items())
# print(listtDict.keys())
# print(listtDict.values())

X = int(input(''))
shoeSize = input('').split(' ')
shoeSizeCount = dict(Counter(shoeSize))
customerSizeList = []
customerPriceList = []


N = int(input(''))
price = 0

for n in range(N):
    customer = input('').split(' ')
    customerSize = customer[0]
    customerPrice = int(customer[1])
    customerSizeList.append(customerSize)
    customerPriceList.append(customerPrice)

shoeNum = min(X,N)
for i in range(shoeNum):
    if customerSizeList[i] in shoeSizeCount.keys():
        if shoeSizeCount[customerSizeList[i]] > 0:
            shoeSizeCount[customerSizeList[i]] -=1
            price += customerPriceList[i]

print(price)

