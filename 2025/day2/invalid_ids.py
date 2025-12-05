def find_invalid_id(id):
    id=str(id)
    n=len(id)
    if n%2==0:
        if id[int(n/2):]==id[:int(n/2)]:
            return True
    return False

def find_invalid_id2(id):
    id=str(id)
    n=len(id)
    if n < 2:
        return False
    for i in range(1, n//2+1):
       if n%i ==0:
           invalid_id_found=id[:i]* (n//i)
           if invalid_id_found==id:
                return True
    return False  
    
if __name__=="__main__":
    try:
        with open("input.txt", "r") as f:
            ids=f.read().split(",")
    except FileNotFoundError:
        print("Error: file not found")

    sum=0
    sum2=0

    for id in ids:
        first_id, sec_id=id.split("-")
        start=int(first_id)
        end=int(sec_id)

        for i in range(start, end+1):
            if find_invalid_id(i) == True:
                sum += i
            if find_invalid_id2(i)==True:
                sum2+=i

    print(f"The sum of invalid ids: {sum}")
    print(f"The sum of invalid ids: {sum2}")

