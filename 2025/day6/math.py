from math import prod

with open("input.txt") as f:
    *nums_lines, ops_line = f.read().split("\n")

problems=[]
for i,x in enumerate(ops_line):
    if op:= {'*': prod, '+': sum}.get(x):
        p=(i, op)
        problems.append(p)

indexes_start, ops=zip(*problems)

indexes_stop = [i-1  for i in indexes_start[1:]]
indexes_stop.append(len(max(*nums_lines)))

columns=[]
for start, stop in zip(list(indexes_start), list(indexes_stop)):
    nums= [int(line[start:stop]) for line in nums_lines]
    columns.append(nums)

#part1
results=[]
for col, op in zip(columns, ops):
    results.append(op(col))

#part2
new_columns=[]
for start, stop in zip(list(indexes_start), list(indexes_stop)):
    nums= [line[start:stop] for line in nums_lines]
    zipped = zip(*nums)
    new_nums = [int(''.join(c).strip()) for c in zipped]
    new_columns.append(new_nums)

results2=[]
for col, op in zip(new_columns, ops):
    results2.append(op(col))


print(sum(results))
print(sum(results2))





    