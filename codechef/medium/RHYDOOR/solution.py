# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    door_opens = 0
    streak = 0
    current_char = ''
        
    for char in s:
        if char == current_char:
                streak += 1
        else:
                current_char = char
                streak = 1
                
        if streak == 3:
                door_opens += 1
                streak = 0
                current_char = ''
                
    print(door_opens)