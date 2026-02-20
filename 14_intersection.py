#Intersection of two arrays
sort_arr1=[1,2,3,5,7,9]
sort_arr2=[0,2,4,5,6,8]
def intersection(arr1,arr2):
    sa=set(arr1)
    inter=[]
    for i in arr2:
        if i in sa and i not in inter:
            inter.append(i)
            sa.remove(i)
    return inter
print(f"\nThe intersection of two arrays \narray 1: {sort_arr1} and array 2: {sort_arr2} is")
print(f"{intersection(sort_arr1,sort_arr2)}")