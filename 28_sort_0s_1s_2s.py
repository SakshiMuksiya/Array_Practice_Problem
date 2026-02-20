#Sort an array of 0s, 1s and 2s
arr_012=[0,2,1,1,2,1,2,2,0,2,1,0,0,0]
def sort012(arr):
    n=len(arr)
    lo=0
    mid=0
    hi=n-1
    while mid<=hi:
        if arr[mid]==0:
            arr[lo],arr[mid]=arr[mid],arr[lo]
            lo+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[hi]=arr[hi],arr[mid]
            hi-=1
    return arr
print(f"\nThe sorted array of 0s, 1s and 2s is {sort012(arr_012)}")