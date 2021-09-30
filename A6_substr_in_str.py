#how to mutate a string
#1. use list constructor

string = 'GeeksforGeeks is for Geeks'
sub_string = 'Geeks'
lenSub = len(sub_string)

i = 0
count = 0
while i < len(string):
    newStr = ''
    if (len(string)-i) >= len(sub_string):
        for j in range(i,lenSub):
            newStr += string[j]
        lenSub += 1
        if sub_string in newStr:
            count += 1
    else:
        break
    i +=1

print(count)




