f = open("input.txt", 'r')
lines=f.readlines()
horizontal=0
depth=0
aim=0
for line in lines:
    line=line.strip('\n')
    distance=int(line[-1])
    if line.startswith("forward"):
        horizontal+=distance
        depth+=aim*distance
    if line.startswith("up"):
        aim-=distance
    if line.startswith("down"):
        aim+=distance
print(horizontal*depth)
f.close()