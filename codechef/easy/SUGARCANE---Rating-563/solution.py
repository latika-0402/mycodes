# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    total=50*n
    print(int(total-(2*(0.2*total)+(0.3*total))))