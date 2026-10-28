# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    codes = input().split()
    
    start38_count = codes.count("START38")
    ltime108_count = codes.count("LTIME108")
    
    print(start38_count, ltime108_count)