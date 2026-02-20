#Maximum sum subarray (Kanade's algorithm)
arr_sub=[1,2,3,4,5,-4,-5]
def maxSubarraySum(arr):
    n = len(arr)
    res=max_sum=arr[0]
    for i in range(1,n):
        max_sum=max(max_sum+arr[i],arr[i])
        res=max(res,max_sum)
    return res
print(f"\nThe maximum sum of the subarray {arr_sub} is {maxSubarraySum(arr_sub)}")