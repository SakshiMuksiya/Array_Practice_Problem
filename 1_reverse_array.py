#initial array
arr=[1,2,0,3,4,5,0,9,5,3,4,7,0]
print("\nInitial array",arr)

#reverse the array 
#First way
rev_arr1=[]
for i in range(len(arr)-1,-1,-1):
    rev_arr1.append(arr[i])
print("\nFirst Reversed array:", rev_arr1)

#Second way
rev_arr2=arr.copy()
start,end=0,len(arr)-1
while start<=end:
    rev_arr2[start],rev_arr2[end]=rev_arr2[end],rev_arr2[start]
    start+=1
    end-=1
print("Second Reversed array:",rev_arr2)