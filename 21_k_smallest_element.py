#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#find kth smallest element
def kth_small_ele(arr):
    r=sorted(arr)
    return r[k-1]
k=int(input("\nEnter the value of k for the smallest element: "))
print(f"\nThe {k} smallest element in the array is {kth_small_ele(arr)}")