#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#rotate array to left by k position
k=int(input("Enter the value of k: "))
def rotate_anticlockwise(arr,k):
    n=len(arr)
    def reversed(arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    if n==0:
        return
    else:
        k=k%n
        reversed(arr,0,k-1) #rotate the first k elements
        reversed(arr,k,n-1) #rotate the last k-1 elements
        reversed(arr,0,n-1) #rotate the array
    return arr
print(f"\nThe anti-clockwise rotated array is {rotate_anticlockwise(arr,k)}")
