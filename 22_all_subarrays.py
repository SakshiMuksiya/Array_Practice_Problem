#find all subarrays
arr_sub=[1,2,3]
def all_subarrays(arr,start,end):
    if end==len(arr):
        return
    elif start>end:
        return all_subarrays(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return all_subarrays(arr,start+1,end)
all_subarrays(arr_sub,0,0)