print('Hello my world')

command = []
listt = []
n = int(input(''))
for i in range(n):
    com = input().split(' ')
    command.append(com)

print(command)

for com in command:
    if com[0] == 'insert':
        listt.insert(int(com[1]),int(com[2]))
    elif com[0] == 'print':
        print(listt)
    elif com[0] == 'remove':
        listt.remove(int(com[1]))
    elif com[0] == 'append':
        listt.append(int(com[1]))
    elif com[0] == 'sort':
        listt.sort()
    elif com[0] == 'pop':
        listt.pop()
    elif com[0] == 'reverse':
        listt.reverse()
