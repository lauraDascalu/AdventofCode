def count_roll_adjacents(grid, r, c):
    nrows=len(grid)
    ncols=len(grid[0])

    roll_count=0

    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if dr==0 and dc==0:
                continue
            neighbour_r, neighbour_c= r+dr, c+dc
            if 0<=neighbour_r<nrows and 0 <=neighbour_c<ncols:
                if grid[neighbour_r][neighbour_c]=='@':
                    roll_count+=1
    return roll_count

if __name__=="__main__":
    with open("input.txt", "r") as f:
        grid=f.read().split()
    
    grid = [list(line) for line in grid if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    rolls_to_remove = 1

    count_removed=0

    while rolls_to_remove>0:
        rolls_to_remove=0
        to_remove_coords=[]
        for r in range(rows):
            for c in range(cols):
                adj_rolls=count_roll_adjacents(grid, r, c)
                if adj_rolls < 4:
                    if grid[r][c]=='@':
                        to_remove_coords.append((r,c))
                        rolls_to_remove+=1
        
        if rolls_to_remove>0:
            for r,c in to_remove_coords:
                grid[r][c]="."

        count_removed+=rolls_to_remove
    
    print(count_removed)





