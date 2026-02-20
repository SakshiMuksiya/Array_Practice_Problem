# Merge two sorted arrays into a sorted array
sort_arr1=[1,2,3,5,7,9]
sort_arr2=[0,2,4,5,6,8]
sorted_array=sorted(sort_arr1+sort_arr2)
print("\nThe sorted array after merging two sorted arrays ")
print(f"{sort_arr1} and {sort_arr2} is \n{sorted_array}")