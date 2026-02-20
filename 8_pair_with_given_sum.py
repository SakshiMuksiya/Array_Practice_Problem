#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Find pair with the given sum
def pair_sum(arr,req_sum):
    pairs=[]
    for i in range(len(arr)//2):
        if abs(arr[i]-req_sum) in arr:
            pairs.append((arr[i],abs(arr[i]-req_sum)))
    return pairs
req_sum=int(input("\nEnter the sum : "))    
print(f"The pair of elements whose sum = {req_sum} is {pair_sum(arr,req_sum)} ")