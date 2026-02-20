#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Find the leader element
def leader(arr):
    result=[]
    max_right=arr[-1]
    result.append(max_right)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>=max_right:
            max_right=arr[i]
            result.append(arr[i])
    result.reverse()
    return result
print(f"\nThe leader elements of array {arr} are {leader(arr)}")