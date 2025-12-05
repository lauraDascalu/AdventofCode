with open("input.txt", "r") as f:
    content=f.read().strip()

ranges, ingredients= content.split('\n\n', 1)

fresh_count=0
fresh_ingredients=[]

for r in ranges.split('\n'):
    low, upper= r.split('-')
    for i in ingredients.split('\n'):
        if int(i) in range(int(low), int(upper)+1):
            if i not in fresh_ingredients:
                fresh_count+=1
                fresh_ingredients.append(i)


#part 2
ranges_list=[]
for r in ranges.split('\n'):
    ranges_list.append(tuple(map(int, r.split('-'))))

count=0

ranges_list.sort(key=lambda x:x[0])
merged_ranges=[]
current_low, current_upper = ranges_list[0]
for next_low, next_upper in ranges_list[1:]:
    if next_low <= current_upper + 1:
        current_upper = max(current_upper, next_upper)
    else:
        merged_ranges.append((current_low, current_upper))
        current_low, current_upper = next_low, next_upper
    
merged_ranges.append((current_low, current_upper))

count=sum(upper - low + 1 for low, upper in merged_ranges)

print(fresh_count)
print(count)

