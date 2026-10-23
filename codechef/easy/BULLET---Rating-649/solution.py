# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    
    # Check the remainder when divided by 3
    if x % 3 == 1:
        print("HUGE")
    elif x % 3 == 2:
        print("SMALL")
    else:
        print("NORMAL")