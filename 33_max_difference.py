#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Find maximum difference pair (j>i)
def max_diff(arr):
    return (min(arr), max(arr))
print(f"\nThe maximum difference pair in array {arr} is {max_diff(arr)}")