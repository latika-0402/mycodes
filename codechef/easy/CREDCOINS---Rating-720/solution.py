# cook your dish here
n=int(input())
arr=list(map(int,input().split()))
arr_even=0
arr_odd=0
for i in range(len(arr)):
        if arr[i]%2==0:
            arr_even+=1
        else:arr_odd+=1
if arr_even>arr_odd:print("READY FOR BATTLE")
else:print("NOT READY")