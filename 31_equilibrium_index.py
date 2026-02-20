#Find equilibrium index
equi_arr=[1,2,3,0,3,3]
def equilibrium(arr):
    prefsum=0
    total=sum(arr)
    for i in range(len(arr)):
        suffsum = total-prefsum-arr[i]
        if suffsum == prefsum:
            return i
        prefsum+=arr[i]
    return -1
print(f"\nThe equilibrium index of array {equi_arr} is {equilibrium(equi_arr)}")