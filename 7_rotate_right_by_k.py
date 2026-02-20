#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Rotate array by k positions to the right
k=int(input("Enter the value of k: "))
def rotate_clockwise(arr,k):
    n=len(arr)
    if n==0:
        return 
    else:
        k=k%n
        arr[:n-k]=reversed(arr[:n-k]) # rotating first n-k elements
        arr[n-k:]=reversed(arr[n-k:])  # rotating last k elements
        arr[:]=reversed(arr)
        return arr
print(f"The clockwise rotated array by {k} positions is {rotate_clockwise(arr,k)} ")