f = open("input.txt", 'r')
lines=list(map(int, f))
count=0
for i in range(1,len(lines)):
    if lines[i]>lines[i-1]:
        count+=1
print(count)
f.close()