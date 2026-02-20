#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)

#Second largest element in array
#First way (in case where list is sorted in descending)
#sec_largest_ele=arr[1]
#print("\nSecond largest element of the array: ",sec_largest_ele)###
#Second way
largest=float('-inf')
sec_largest=float('-inf')
for num in arr:
    if num>largest:
        sec_largest=largest
        largest=num
    elif num<largest and num>sec_largest:
        sec_largest=num
print("\nSecond largest element is: ",sec_largest)