f = open("input.txt", 'r')
lines=list(map(int, f))
count=0
for i in range(3,len(lines)):
    sum1=lines[i]+lines[i-1]+lines[i-2]
    sum2=lines[i-1]+lines[i-2]+lines[i-3]
    if sum1>sum2:
        count+=1
print(count)
f.close()