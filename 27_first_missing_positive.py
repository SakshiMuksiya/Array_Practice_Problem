#Find first positive missing integer
miss_arr=[1,6,-3,5,3,7,4]
def first_pos_missing(arr):
    n=len(arr)
    for i in range(n):
        while 1<=arr[i]<=n and arr[i]!=arr[arr[i]-1]:
            temp=arr[i]
            arr[i]=arr[arr[i]-1]
            arr[temp-1]=temp
    for i in range(1,n+1):
        if i!=arr[i-1]:
            return i
    return i+1
print(f"\nThe first missing positive integer in the array {miss_arr} is {first_pos_missing(miss_arr)}")