def dial_logic(rotations):
    current_dial=50
    count=0
    for r in rotations:
        direction, nof_rotations=1 if r[0]=='R' else -1, int(r[1:])
       
        current_dial=(current_dial+direction*nof_rotations)%100

        if current_dial==0:
            count+=1

    return count

def dial_logic_clicks(rotations):
    current_dial=50
    print(f"Current dial: {current_dial}")
    count_clicks_0=0
    for r in rotations:
        direction, nof_rotations=r[0], int(r[1:])

        for _ in range(nof_rotations):
            current_dial+= 1 if direction=="R" else -1
            current_dial%=100
            if current_dial==0:
                count_clicks_0+=1
    return count_clicks_0
    

if __name__=="__main__":
    try:
        with open("input.txt", "r") as f:
            rotations = f.read().split()
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")

    password=dial_logic(rotations)
    password2=dial_logic_clicks(rotations)
    print(f"The password to the North Pole is: {password}")
    print("Wrong, try the method 0x434C49434B!")
    print(f"The password to the North Pole is: {password2}")

