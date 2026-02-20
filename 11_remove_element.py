#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)
#remove given element from the array
element=int(input("Enter the element you want to remove from the array: "))
arr.remove(element)
print("\nThe array after removing the element: ",arr)