with open("input.txt", "r") as f:
    manifold= f.read().split('\n')

#convert to list of chars
tachyon_manifold=[list(line) for line in manifold]

count=0
splitters_indexes=[]

for index_line, line in enumerate(tachyon_manifold):
    for index, char in enumerate(line):
        if char=='S':
            if index_line+1<len(tachyon_manifold):
                    tachyon_manifold[index_line+1][index]= '|'
        if char=='^':
            splitters_indexes.append(index)
            if tachyon_manifold[index_line-1][index]== '|':
                count+=1
            if index - 1 >= 0:
                tachyon_manifold[index_line][index-1]= '|'
            if index + 1 < len(line):
                tachyon_manifold[index_line][index+1]= '|'
            if tachyon_manifold[index_line+1][index]=='.':
                tachyon_manifold[index_line+1][index-1]='|'
                tachyon_manifold[index_line+1][index+1]='|'
        if tachyon_manifold[index_line-1][index]=='|':
            if tachyon_manifold[index_line][index]!='^':
                tachyon_manifold[index_line][index]='|'
        

#convert back to string
tachyon_manifold=["".join(line) for line in tachyon_manifold]

timelines=[0]*(len(splitters_indexes))
timelines[0]=1 #for S

for i in range(1, len(splitters_indexes)):
    for j in range(i-1, -1, -1):
        if splitters_indexes[i]==splitters_indexes[j]:
            break
        if abs(splitters_indexes[j] - splitters_indexes[i]) == 1:  
            timelines[i] += timelines[j]

# for l in tachyon_manifold:
#     print(l)

print(count)
print(sum(timelines)+1)



        


