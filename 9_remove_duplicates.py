#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
# Remove duplicates from the array without changing the order
def remove_duplicates(arr):
    unique=[]
    for i in arr:
        if i not in unique:
            unique.append(i)
    return unique
print("\nThe array without duplicates is ", remove_duplicates(arr))