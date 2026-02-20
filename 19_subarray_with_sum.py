#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#find subarray with a given sum
given=int(input("Enter the sum for subarray: "))
def sum_subarray(arr,given):
    s,e=0,0
    curr_sum=0
    res=[]
    for i in range(len(arr)):
        curr_sum+=arr[i]
        if curr_sum>=given:
            e=i
            while curr_sum>given and s<e:
                curr_sum-=arr[s]
                s+=1
            if curr_sum==given:
                res.append(s+1)
                res.append(e+1)
                return res
    return [-1]
print(f"\nThe subarray with the given sum is {sum_subarray(arr,given)}")