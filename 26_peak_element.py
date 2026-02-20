#find peak element
peak_arr=[1,2,3,5,2]
def peak(arr):
    for i in range(0,len(arr)-1):
        if arr[i+1]>arr[i] and arr[i+1]>arr[i+2]:
            return arr[i+1]
print(f"\nThe peak element in the array {peak_arr} is {peak(peak_arr)}")