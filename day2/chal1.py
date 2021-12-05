f = open("input.txt", 'r')
lines=f.readlines()
horizontal=0
depth=0
for line in lines:
    line=line.strip('\n')
    distance=int(line[-1])
    if line.startswith("forward"):
        horizontal+=distance
    if line.startswith("up"):
        depth-=distance
    if line.startswith("down"):
        depth+=distance
print(horizontal*depth)
f.close()