#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#Find duplicates in an array
def find_duplicates(arr):
    seen={}
    for i in arr:
        if i in seen:
            seen[i]+=1
        else:
            seen[i]=1
    for k,v in seen.items():
        print(f"Element: {k} and Duplicate count: {v-1}")
    return
find_duplicates(arr)