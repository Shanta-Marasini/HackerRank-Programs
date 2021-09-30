print("Hello my world")

s = input('')
w = int(input(''))
lines = len(s)/w
rem = len(s)%w
if rem != 0:
    lines = len(s)//w + 1
else:
    lines = len(s)//w

start = 0
end = w
for num in range(lines):
    singleLine = ''
    for i in range(start,end):
        if i == len(s)-1:
            break
        singleLine += s[i]
    start = end
    end += w
    print(singleLine)