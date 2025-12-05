def find_max_joltage(seq):
    seq=str(seq)
    n=len(seq)

    if n<2:
        return 0
    
    max_num=0
    
    for i in range(n-1):
        digit1=int(seq[i])
        for j in range(i+1, n):
            digit2=int(seq[j])
            num=digit1*10+digit2
            if num> max_num:
                max_num=num
    return max_num

def find_max12(sequence):
    #seq=str(seq)
    n=len(seq)
    if n<12:
        return 0
    
    num=""
    window_start_index=0
    for k in range(12):
        window_end_index=n-(12-k)
        current_window=seq[window_start_index:window_end_index+1]
        max_char=max(current_window)
        num+=max_char

        window_start_index=seq.index(max_char, window_start_index)+1
    return num

if __name__=="__main__":
    try:
        with open("input.txt", "r") as f:
            sequences=f.read().split()
    except:
        print("Error: file not found")

    sum_max_j=0
    sum_max_12=0

    for seq in sequences:
        sum_max_j+= find_max_joltage(seq)
        sum_max_12+=int(find_max12(seq))

    print(sum_max_j)
    print(sum_max_12)
     

