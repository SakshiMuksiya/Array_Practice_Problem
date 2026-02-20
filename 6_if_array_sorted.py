#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Check if array is sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print("Is the array sorted? ",is_sorted(arr))