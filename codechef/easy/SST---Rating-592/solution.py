# cook your dish here
# cook your dish here
t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    
    # Calculate company valuations
    val1 = A * 10
    val2 = B * 5
    
    if val1 > val2:
        print("FIRST")
    elif val2 > val1:
        print("SECOND")
    else:
        print("ANY")